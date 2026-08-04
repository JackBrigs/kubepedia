#!/usr/bin/env python3
"""kubepedia code — поиск по исходникам компонента на точном теге.

Сильнейшее доказательство в этом проекте — тегнутый исходник: документация врёт,
заметки к релизам неполны, закрытый issue не доказывает исправления. Но до сих пор
код был доказательством и не был слоем: каждый разбор грепался руками, ответ уходил
в прозу, и следующий вопрос начинался с нуля.

Здесь код становится запрашиваемым — и, что важнее, **воспроизводимым**: каждая
находка выводится вместе с постоянной ссылкой на тот же тег, которую можно положить
в блок `sources:` документа KDS без ручной сборки URL.

Как это устроено. Клоны в `src-cache/` частичные (`--filter=blob:none`): содержимое
файлов не хранится, оно докачивается по требованию. Для `git show <файл>` этого
хватает, а `git grep` по тегу требует блобы всего дерева и падает на промисор-удалёнке
(проверено на kyverno: `could not fetch ... from promisor remote`). Поэтому тег
материализуется рабочим деревом один раз, и дальше по нему ходит обычный поиск по
файлам — 3–4 секунды на материализацию против десятков миллисекунд на запрос.

    kubepedia code webhookNameAndPath --component kyverno --tag v1.18.2
    kubepedia code 'MaxConnectionAge' --component cilium --kubespray v2.31.0
    kubepedia code 'denied the request' --component kubernetes --tag v1.34.7 --glob '*.go'
    kubepedia code --show kyverno:v1.18.2:pkg/config/config.go --lines 45-70
    kubepedia code --list
    kubepedia code --prune                 # снести материализованные деревья
"""
import argparse
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CACHE = os.path.join(ROOT, "src-cache")
TREES = os.path.join(CACHE, ".worktrees")

sys.path.insert(0, HERE)
from upstream_issues import REPOS  # компонент -> owner/repo  # noqa: E402


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


def repo_dir(comp):
    return os.path.join(CACHE, comp)


def slug(comp):
    """owner/repo для ссылок.

    Карта апстрима покрывает компоненты периметра, но в кэше лежат и репозитории вне
    её — например `enhancements`, из которого собран слой KEP. Для них владелец
    читается из самого клона, иначе инструмент их просто не видел бы, а карту
    пришлось бы держать в двух местах.
    """
    if comp in REPOS:
        return REPOS[comp]
    url = run(["git", "-C", repo_dir(comp), "config", "--get", "remote.origin.url"]).stdout.strip()
    m = re.search(r"[:/]([\w.-]+/[\w.-]+?)(?:\.git)?$", url)
    return m.group(1) if m else comp


def known():
    """Что можно спрашивать: карта апстрима плюс всё, что уже лежит в кэше."""
    local = {d for d in os.listdir(CACHE)
             if not d.startswith(".") and os.path.isdir(os.path.join(CACHE, d, ".git"))} \
        if os.path.isdir(CACHE) else set()
    return set(REPOS) | local


def ensure_clone(comp, quiet=False):
    """Частичный клон под компонент; создаётся при первом обращении."""
    path = repo_dir(comp)
    if os.path.isdir(os.path.join(path, ".git")):
        return path
    if comp not in REPOS:
        return None
    if not quiet:
        print(f"[..] {comp}: клона нет, забираю {REPOS[comp]} (частичный, без содержимого файлов)",
              file=sys.stderr)
    os.makedirs(CACHE, exist_ok=True)
    r = run(["git", "clone", "--quiet", "--filter=blob:none", "--no-checkout",
             f"https://github.com/{REPOS[comp]}.git", path])
    if r.returncode:
        print(f"[!!] {comp}: клонирование не удалось: {r.stderr.strip()[:200]}", file=sys.stderr)
        return None
    return path


def tags(comp):
    path = repo_dir(comp)
    if not os.path.isdir(path):
        return []
    return run(["git", "-C", path, "tag"]).stdout.split()


def resolve_tag(comp, want):
    """Версия -> реальное имя тега в этом репозитории.

    Проекты пишут теги по-разному: `v1.19.3` у большинства, голое `1.19.3` у части.
    Угадывать нельзя — несуществующий тег дал бы пустой результат, а пустой результат
    в этой задаче читается как «в коде такого нет», то есть как ложный ответ.
    """
    have = set(tags(comp))
    bare = want.lstrip("v")
    # форма с `v` идёт первой: часть проектов держит оба имени на одном коммите
    # (у cilium есть и `1.19.3`, и `v1.19.3`), а база везде цитирует форму с `v`
    for cand in (f"v{bare}", want, bare):
        if cand in have:
            return cand
    # не всё версионируется тегами: репозиторий KEP тегов не имеет вовсе и живёт
    # ветками. Имя ветки одинаково годится и для worktree, и для ссылки на GitHub —
    # но такая ссылка не постоянна, о чём предупреждаем на месте использования.
    if rev_of(comp, want):
        return want
    return None


def rev_of(comp, name):
    """Git-ревизия под именем: тег, ветка удалённого или сам коммит."""
    for cand in (name, f"origin/{name}"):
        r = run(["git", "-C", repo_dir(comp), "rev-parse", "--verify", "--quiet", cand + "^{commit}"])
        if r.returncode == 0 and r.stdout.strip():
            return cand
    return None


def version_at(comp, kubespray_tag):
    """Версия компонента, которую Kubespray везёт на своём теге — через штатный лукап."""
    out = run([sys.executable, os.path.join(HERE, "versions_lookup.py"), comp,
               "--tags", kubespray_tag]).stdout
    for line in out.split("\n"):
        m = re.match(r"^(v\d+\.\d+\.\d+)\s+(\S+)", line)
        if m and m.group(1) == kubespray_tag and m.group(2) != "—":
            return m.group(2)
    return None


def worktree(comp, tag, quiet=False):
    """Материализованное дерево на теге; кэшируется между запусками."""
    path = os.path.join(TREES, comp, tag)
    if os.path.isdir(path) and os.listdir(path):
        return path
    repo = ensure_clone(comp, quiet)
    if not repo:
        return None
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not quiet:
        print(f"[..] {comp}@{tag}: материализую дерево (однократно)", file=sys.stderr)
    rev = rev_of(comp, tag) or tag
    if rev != tag and not quiet:
        print(f"[!!] {tag} — ветка, а не тег: ссылки на неё не постоянны, "
              f"для документа берите тег", file=sys.stderr)
    r = run(["git", "-C", repo, "worktree", "add", "--detach", path, rev])
    if r.returncode:
        print(f"[!!] {comp}@{tag}: не разложилось: {r.stderr.strip()[:200]}", file=sys.stderr)
        return None
    return path


def permalink(comp, tag, rel, line=None):
    url = f"https://github.com/{slug(comp)}/blob/{tag}/{rel}"
    return f"{url}#L{line}" if line else url


def grep_cmd(pattern, globs, ctx, target):
    """Команда поиска: ripgrep, если он есть в системе, иначе штатный grep.

    Опираться на ripgrep нельзя: на машине владельца `rg` — функция оболочки, а не
    бинарь, и вызов из Python падал с FileNotFoundError. Инструмент базы обязан
    работать на голой системе, поэтому запасной путь — POSIX grep, он есть и в macOS,
    и в Linux.
    """
    if shutil.which("rg"):
        cmd = ["rg", "--line-number", "--no-heading", "--color", "never",
               "--max-columns", "240"]
        for g in globs or []:
            cmd += ["--glob", g]
        if ctx:
            cmd += ["--context", str(ctx)]
        return cmd + [pattern, target]
    # -I пропускает двоичные файлы, -E даёт расширенные регулярные выражения
    cmd = ["grep", "-rnIE"]
    for g in globs or []:
        cmd += [f"--include={g}"]
    if ctx:
        cmd += ["-C", str(ctx)]
    return cmd + [pattern, target]


def search(comp, tag, pattern, globs, ctx, limit):
    wt = worktree(comp, tag)
    if not wt:
        return 1
    r = run(grep_cmd(pattern, globs, ctx, wt))
    if r.returncode == 2 and r.stderr.strip():
        print(f"[!!] поиск: {r.stderr.strip()[:200]}", file=sys.stderr)
        return 2
    lines = [x for x in r.stdout.split("\n") if x.strip()]
    if not lines:
        print(f"[--] {comp}@{tag}: совпадений нет "
              f"(это ответ «в коде такого нет» — тег существует и разложен)")
        return 1

    print(f"# {comp}@{tag} — {slug(comp)}\n")
    shown = 0
    for raw in lines:
        rel = raw[len(wt):].lstrip("/")
        m = re.match(r"^([^:]+):(\d+)[:-](.*)$", rel)
        if not m:
            print(f"  {rel}")
            continue
        if shown >= limit:
            print(f"\n… показаны первые {limit}; сузьте запрос или поднимите --limit")
            break
        f, ln, text = m.group(1), m.group(2), m.group(3)
        print(f"{f}:{ln}: {text.strip()[:240]}")
        print(f"    {permalink(comp, tag, f, ln)}")
        shown += 1
    return 0


def show(spec, lines_range):
    """Показать файл целиком или диапазон строк: comp:tag:path."""
    parts = spec.split(":", 2)
    if len(parts) != 3:
        print("[!!] нужен вид comp:tag:path", file=sys.stderr)
        return 2
    comp, want, rel = parts
    tag = resolve_tag(comp, want) or want
    wt = worktree(comp, tag)
    if not wt:
        return 1
    full = os.path.join(wt, rel)
    if not os.path.isfile(full):
        print(f"[!!] {rel} нет в {comp}@{tag}", file=sys.stderr)
        return 1
    with open(full, encoding="utf-8", errors="replace") as fh:
        body = fh.read().split("\n")
    lo, hi = 1, len(body)
    if lines_range:
        m = re.match(r"^(\d+)(?:-(\d+))?$", lines_range)
        if not m:
            print("[!!] --lines задаётся как 100 или 100-140", file=sys.stderr)
            return 2
        lo = int(m.group(1))
        hi = int(m.group(2) or m.group(1))
    print(f"# {comp}@{tag} — {rel}:{lo}-{min(hi, len(body))}")
    print(f"# {permalink(comp, tag, rel, lo)}\n")
    for i in range(lo, min(hi, len(body)) + 1):
        print(f"{i:6}  {body[i - 1]}")
    return 0


def source_block(comp, tag, rel, note):
    """Готовый блок sources: для документа KDS — чтобы не собирать URL руками."""
    print("sources:")
    print("  - type: code")
    print(f"    path: {rel}")
    print(f"    url: {permalink(comp, tag, rel)}")
    print(f'    note: "{note or "verified against the tagged source"}"')
    return 0


def listing():
    cached, missing = [], []
    for comp in sorted(known()):
        if os.path.isdir(os.path.join(repo_dir(comp), ".git")):
            n = len(tags(comp))
            wts = os.path.join(TREES, comp)
            mat = len(os.listdir(wts)) if os.path.isdir(wts) else 0
            cached.append(f"  {comp:24} тегов {n:5}   разложено деревьев: {mat}")
        else:
            missing.append(comp)
    print(f"в кэше ({len(cached)}):")
    print("\n".join(cached))
    print(f"\nбудут склонированы при первом обращении ({len(missing)}):")
    print("  " + ", ".join(missing))
    return 0


def prune():
    if not os.path.isdir(TREES):
        print("материализованных деревьев нет")
        return 0
    n = 0
    for comp in sorted(os.listdir(TREES)):
        repo = repo_dir(comp)
        for tag in sorted(os.listdir(os.path.join(TREES, comp))):
            run(["git", "-C", repo, "worktree", "remove", "--force",
                 os.path.join(TREES, comp, tag)])
            n += 1
        run(["git", "-C", repo, "worktree", "prune"])
    print(f"снесено деревьев: {n} (объекты остаются в клоне — повторная материализация "
          f"уже не пойдёт в сеть)")
    return 0


def main():
    ap = argparse.ArgumentParser(
        description="Поиск по исходникам компонента на точном теге, с постоянными ссылками")
    ap.add_argument("pattern", nargs="?", help="регулярное выражение для поиска")
    ap.add_argument("--component", "-c", help="компонент из карты апстрима")
    ap.add_argument("--tag", "-t", help="тег компонента, например v1.18.2")
    ap.add_argument("--kubespray", "-k", metavar="TAG",
                    help="взять версию компонента, которую везёт этот тег Kubespray")
    ap.add_argument("--glob", "-g", action="append", help="фильтр путей, можно повторять")
    ap.add_argument("--context", "-C", type=int, default=0, help="строк контекста")
    ap.add_argument("--limit", type=int, default=40, help="максимум совпадений в выводе")
    ap.add_argument("--show", metavar="COMP:TAG:PATH", help="показать файл на теге")
    ap.add_argument("--lines", help="диапазон строк для --show: 100 или 100-140")
    ap.add_argument("--source", metavar="COMP:TAG:PATH", help="готовый блок sources: для KDS")
    ap.add_argument("--note", help="текст note в блоке --source")
    ap.add_argument("--list", action="store_true", help="что есть в кэше")
    ap.add_argument("--prune", action="store_true", help="снести материализованные деревья")
    args = ap.parse_args()

    if args.list:
        return listing()
    if args.prune:
        return prune()
    if args.show:
        return show(args.show, args.lines)
    if args.source:
        parts = args.source.split(":", 2)
        if len(parts) != 3:
            ap.error("--source задаётся как comp:tag:path")
        comp, want, rel = parts
        return source_block(comp, resolve_tag(comp, want) or want, rel, args.note)

    if not args.pattern or not args.component:
        ap.error("нужны образец поиска и --component (либо --show/--source/--list)")
    comp = args.component
    if comp not in known():
        near = [c for c in known() if comp in c or c in comp]
        ap.error(f"неизвестный компонент '{comp}'"
                 + (f"; возможно: {', '.join(near)}" if near else "; посмотрите --list"))

    want = args.tag
    if args.kubespray:
        want = version_at(comp, args.kubespray)
        if not want:
            print(f"[!!] {comp} на теге Kubespray {args.kubespray} не разрешается — "
                  f"задайте --tag явно", file=sys.stderr)
            return 1
        print(f"[ok] Kubespray {args.kubespray} везёт {comp} {want}", file=sys.stderr)
    if not want:
        ap.error("нужен --tag или --kubespray")

    if not ensure_clone(comp):
        return 1
    tag = resolve_tag(comp, want)
    if not tag:
        sample = ", ".join(sorted(tags(comp))[-5:])
        print(f"[!!] тега под версию {want} в {comp} нет. Последние теги: {sample}",
              file=sys.stderr)
        return 1
    return search(comp, tag, args.pattern, args.glob, args.context, args.limit)


if __name__ == "__main__":
    sys.exit(main())
