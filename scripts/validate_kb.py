#!/usr/bin/env python3
"""
Валидатор консистентности базы знаний Kubespray Encyclopedia.

Инвариант (см. CLAUDE.md, раздел 11): источник истины о СОСТАВЕ базы —
файловая система (versions/, diffs/, troubleshooting/, reports/).
INDEX.md и README-MOC — производный навигационный слой. При расхождении
приоритет у ФС; расхождение = дефект индекса, который этот скрипт ловит.

Использование:
    python3 scripts/validate_kb.py [path/to/knowledge-base]

Код возврата: 0 — все жёсткие проверки пройдены; 1 — есть расхождения.
Полные проверки (счётчики, метадата) требуют PyYAML; при его отсутствии
они пропускаются с предупреждением, остальные проверки выполняются.
"""
import os
import re
import sys
import glob

try:
    import yaml
    HAVE_YAML = True
except Exception:
    HAVE_YAML = False


def find_kb():
    if len(sys.argv) > 1:
        return os.path.abspath(sys.argv[1])
    here = os.path.dirname(os.path.realpath(__file__))
    repo = os.path.dirname(here)
    return os.path.join(repo, "knowledge-base")


class Report:
    def __init__(self):
        self.hard_fail = 0
        self.warns = 0

    def check(self, name, ok, details=""):
        mark = "PASS" if ok else "FAIL"
        if not ok:
            self.hard_fail += 1
        print(f"[{mark}] {name}")
        if details:
            for line in details.splitlines():
                print(f"       {line}")

    def warn(self, name, details=""):
        self.warns += 1
        print(f"[WARN] {name}")
        if details:
            for line in details.splitlines():
                print(f"       {line}")

    def ok(self, name, details=""):
        print(f"[PASS] {name}")
        if details:
            for line in details.splitlines():
                print(f"       {line}")


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def frontmatter(text):
    """Вернуть dict простых ключей верхнего уровня из YAML-frontmatter (--- ... ---)."""
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    fm = {}
    block = m.group(1) if m else text[:2000]
    for line in block.splitlines():
        km = re.match(r"^([a-z_]+):\s*(.+?)\s*$", line)
        if km:
            fm[km.group(1)] = km.group(2).strip().strip("'\"")
    return fm


def yaml_list_len(path, key):
    """Длина списка под ключом key; учитывает frontmatter-документы и голый YAML."""
    docs = list(yaml.safe_load_all(read(path)))
    for d in docs:
        if isinstance(d, dict) and isinstance(d.get(key), list):
            return len(d[key])
    return 0


def main():
    kb = find_kb()
    if not os.path.isdir(kb):
        print(f"knowledge-base не найдена: {kb}")
        return 2
    os.chdir(kb)
    r = Report()
    print(f"knowledge-base: {kb}")
    print(f"PyYAML: {'да' if HAVE_YAML else 'НЕТ (проверка счётчиков №4 пропущена)'}")
    print("-" * 60)

    index = read("INDEX.md") if os.path.exists("INDEX.md") else ""
    ts_readme = read("troubleshooting/README.md") if os.path.exists("troubleshooting/README.md") else ""

    # --- 1. Версии: ФС <-> INDEX ---
    fs_versions = sorted(
        os.path.basename(p) for p in glob.glob("versions/v*") if os.path.isdir(p)
    )
    idx_versions = set(re.findall(r"versions/(v\d+\.\d+\.\d+)/", index))
    missing = [v for v in fs_versions if v not in idx_versions]
    phantom = [v for v in idx_versions if v not in fs_versions]
    r.check(
        "1. Версии: каждая versions/*/ упомянута в INDEX и наоборот",
        not missing and not phantom,
        (f"нет в INDEX: {missing}\n" if missing else "")
        + (f"фантом в INDEX (нет папки): {phantom}" if phantom else ""),
    )

    # --- 2. Diffs: ФС <-> INDEX ---
    fs_diffs = sorted(
        os.path.basename(p)[:-3] for p in glob.glob("diffs/v*__*.md")
    )
    idx_diffs = set(re.findall(r"diffs/(v[\d.]+__v[\d.]+)", index))
    d_missing = [d for d in fs_diffs if d not in idx_diffs]
    d_phantom = [d for d in idx_diffs if d not in fs_diffs]
    r.check(
        "2. Diffs: каждый diffs/*.md слинкован в INDEX и наоборот",
        not d_missing and not d_phantom,
        (f"нет в INDEX: {d_missing}\n" if d_missing else "")
        + (f"фантом в INDEX: {d_phantom}" if d_phantom else ""),
    )

    # --- 3. Troubleshooting: число файлов совпадает с заявленным ---
    fs_ts = len(glob.glob("troubleshooting/issues/*.md"))
    declared = set()
    for txt in (index, ts_readme):
        for line in txt.splitlines():
            if re.search(r"troubleshoot|записи", line, re.I):
                declared.update(int(n) for n in re.findall(r"\b(\d{1,4})\b", line))
    if not declared:
        r.warn("3. Troubleshooting: число записей нигде не заявлено", f"на диске: {fs_ts}")
    else:
        r.check(
            "3. Troubleshooting: число файлов совпадает с заявленным в INDEX/README",
            fs_ts in declared,
            f"на диске: {fs_ts}; заявленные рядом со словом troubleshooting/записи: {sorted(declared)}",
        )

    # --- 4. Статистика INDEX: пересчёт из YAML ---
    if HAVE_YAML:
        rows = re.findall(
            r"^\|\s*(v\d+\.\d+\.\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|",
            index, re.M,
        )
        if not rows:
            r.warn("4. Статистика: таблица со счётчиками в INDEX не найдена")
        else:
            bad = []
            for v, vars_i, inv_i, tags_i in rows:
                vd = f"versions/{v}"
                real_vars = sum(
                    yaml_list_len(p, "variables")
                    for p in glob.glob(f"{vd}/variables/*.yaml")
                )
                real_inv = sum(
                    yaml_list_len(p, "variables")
                    for p in glob.glob(f"{vd}/inventory/*.yaml")
                )
                tpath = f"{vd}/ansible-tags.yaml"
                real_tags = yaml_list_len(tpath, "tags") if os.path.exists(tpath) else 0
                for label, declared_n, real_n in (
                    ("переменные", int(vars_i), real_vars),
                    ("inventory", int(inv_i), real_inv),
                    ("ansible-теги", int(tags_i), real_tags),
                ):
                    if declared_n != real_n:
                        bad.append(f"{v} {label}: INDEX={declared_n} факт={real_n}")
            r.check(
                "4. Статистика INDEX: счётчики совпадают с пересчётом из YAML",
                not bad,
                "\n".join(bad),
            )
    else:
        r.warn("4. Статистика: пропущено (нет PyYAML)")

    # --- 5. Wiki-ссылки резолвятся ---
    notes = set()
    for f in glob.glob("**/*.md", recursive=True):
        notes.add(f[:-3])
    for f in glob.glob("**/*.yaml", recursive=True):
        notes.add(f[:-5])
    linkre = re.compile(r"\[\[(.+?)\]\]")
    broken = []
    for f in glob.glob("**/*.md", recursive=True):
        for mt in linkre.finditer(read(f)):
            tgt = re.split(r"\\?\|", mt.group(1))[0].split("#")[0].strip().rstrip("\\").strip()
            if not tgt:
                continue
            base = os.path.basename(tgt)
            if tgt in notes or any(
                n == tgt or n.endswith("/" + tgt) or os.path.basename(n) == base
                for n in notes
            ):
                continue
            broken.append(f"{f}: [[{tgt}]]")
    r.check(
        "5. Wiki-ссылки: все резолвятся",
        not broken,
        "\n".join(broken[:30]) + (f"\n... ещё {len(broken)-30}" if len(broken) > 30 else ""),
    )

    # --- 6. Смешение версий: frontmatter kubespray_version == папка ---
    mix = []
    for f in glob.glob("versions/*/**/*", recursive=True):
        if not (f.endswith(".md") or f.endswith(".yaml")):
            continue
        m = re.match(r"versions/(v\d+\.\d+\.\d+)/", f)
        if not m:
            continue
        vdir = m.group(1)
        fm = frontmatter(read(f))
        kv = fm.get("kubespray_version")
        if kv and kv not in (vdir, "unknown"):
            mix.append(f"{f}: frontmatter {kv} != папка {vdir}")
    r.check("6. Смешение версий: kubespray_version совпадает с папкой", not mix, "\n".join(mix))

    # --- 7. Метадата (раздел 8): kubespray_version + git_commit у YAML срезов ---
    meta_bad = []
    for f in glob.glob("versions/*/**/*.yaml", recursive=True):
        fm = frontmatter(read(f))
        miss = [k for k in ("kubespray_version", "git_commit") if k not in fm]
        if miss:
            meta_bad.append(f"{f}: нет {miss}")
    r.check(
        "7. Метадата: у каждого YAML среза есть kubespray_version и git_commit",
        not meta_bad,
        "\n".join(meta_bad[:30]),
    )

    print("-" * 60)
    print(f"Итог: жёстких расхождений {r.hard_fail}, предупреждений {r.warns}")
    return 1 if r.hard_fail else 0


if __name__ == "__main__":
    sys.exit(main())
