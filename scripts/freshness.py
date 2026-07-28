#!/usr/bin/env python3
"""kubepedia feed — freshness / drift monitor. Answers "has upstream moved past the KB?"

Two kinds of staleness, the "freshness treadmill" the KB lives on:
  1. **New Kubespray tags** upstream beyond the KB's ceiling (need RELEASE/UPGRADE docs).
  2. **Aging `verified_at`** — date-sensitive facts (especially the per-component CVE
     matrices) drift as new CVEs land; flag docs older than a threshold.

    kubepedia feed                    # report; exit 1 if behind/stale (for a nightly CI job)
    kubepedia feed --stale-days 120   # staleness threshold (default 180)
    kubepedia feed --no-remote        # skip the network ls-remote; use the local checkout

New Kubespray tags are read from the upstream remote (`git ls-remote`), falling back to
the local `kubespray-src` checkout when the network is unavailable.
"""
import argparse
import json
import urllib.request
import datetime
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KB = os.path.join(ROOT, "kb")
IDS = os.path.join(ROOT, "index", "ids.txt")
KUBESPRAY_URL = "https://github.com/kubernetes-sigs/kubespray.git"
LOCAL_SRC = os.path.join(ROOT, "kubespray-src")


def vt(s):
    return tuple(int(x) for x in re.findall(r"\d+", s))


def kb_release_tags():
    tags = []
    with open(IDS) as f:
        for line in f:
            m = re.match(r"^RELEASE-V([0-9_]+)$", line.strip())
            if m:
                tags.append("v" + m.group(1).replace("_", "."))
    return sorted(set(tags), key=vt)


def upstream_tags(use_remote):
    if use_remote:
        try:
            p = subprocess.run(["git", "ls-remote", "--tags", "--refs", KUBESPRAY_URL],
                               capture_output=True, text=True, timeout=30)
            tags = re.findall(r"refs/tags/(v\d+\.\d+\.\d+)", p.stdout)
            if tags:
                return sorted(set(tags), key=vt), "remote"
        except (OSError, subprocess.TimeoutExpired):
            pass
    if os.path.isdir(os.path.join(LOCAL_SRC, ".git")):
        p = subprocess.run(["git", "-C", LOCAL_SRC, "tag", "-l", "v*"],
                           capture_output=True, text=True)
        tags = re.findall(r"(v\d+\.\d+\.\d+)", p.stdout)
        return sorted(set(tags), key=vt), "local (kubespray-src)"
    return [], "unavailable"


def verified_ages(today):
    """[(age_days, date, relpath)] for every doc with a verified_at, + the CVE-matrix subset."""
    p = subprocess.run(["grep", "-rlE", r'^verified_at:', KB], capture_output=True, text=True)
    rows = []
    cve = []
    for path in p.stdout.splitlines():
        try:
            head = open(path).read(2000)
        except OSError:
            continue
        m = re.search(r'verified_at:\s*"?(\d{4}-\d{2}-\d{2})"?', head)
        if not m:
            continue
        try:
            d = datetime.date.fromisoformat(m.group(1))
        except ValueError:
            continue
        age = (today - d).days
        rel = os.path.relpath(path, ROOT)
        rows.append((age, m.group(1), rel))
        if path.endswith("-known-cves.md") or "KNOWN_CVES" in head[:400]:
            cve.append((age, m.group(1), rel))
    return sorted(rows, reverse=True), sorted(cve, reverse=True)


UPSTREAM_REPO = "kubernetes-sigs/kubespray"
JOURNAL = os.path.join(ROOT, "reports", "UPSTREAM-WATCH.md")


def merged_prs(since, limit=100):
    """Влитые PR апстрима начиная с даты `since` (YYYY-MM-DD).

    Возрождает то, что раньше велось руками в ежевечернем отчёте базы 0.1.0:
    что изменилось в Kubespray с прошлой проверки. Триаж остаётся за человеком —
    инструмент показывает список, а не решает, что важно.
    """
    url = (f"https://api.github.com/repos/{UPSTREAM_REPO}/pulls"
           f"?state=closed&sort=updated&direction=desc&per_page={min(limit, 100)}")
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json",
                                               "User-Agent": "kubepedia-freshness"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.load(r)
    except Exception as exc:                     # noqa: BLE001 — сеть не должна ронять отчёт
        return None, str(exc)
    out = []
    for pr in data:
        m = pr.get("merged_at")
        if not m or m[:10] < since:
            continue
        out.append({"n": pr["number"], "date": m[:10], "title": pr["title"],
                    "url": pr["html_url"]})
    return sorted(out, key=lambda x: x["date"], reverse=True), None


def last_journal_date(default_since):
    """Дата последней записи в журнале — отсюда считается «что нового»."""
    if not os.path.exists(JOURNAL):
        return default_since
    dates = re.findall(r"^## (\d{4}-\d{2}-\d{2})", open(JOURNAL, encoding="utf-8").read(), re.M)
    return max(dates) if dates else default_since


def main():
    ap = argparse.ArgumentParser(description="Kubepedia freshness / drift monitor")
    ap.add_argument("--stale-days", type=int, default=180)
    ap.add_argument("--no-remote", action="store_true", help="skip network; use local checkout")
    ap.add_argument("--upstream", action="store_true",
                    help="добавить раздел «что влито в апстрим с прошлой проверки»")
    ap.add_argument("--since", help="считать изменения апстрима с этой даты (YYYY-MM-DD)")
    ap.add_argument("--journal", action="store_true",
                    help="дописать отчёт в reports/UPSTREAM-WATCH.md")
    ap.add_argument("--today", help="reference date YYYY-MM-DD (default: system today)")
    ap.add_argument("--lang", choices=["ru", "en"], default="ru")
    args = ap.parse_args()
    ru = args.lang == "ru"
    today = datetime.date.fromisoformat(args.today) if args.today else datetime.date.today()

    kb_tags = kb_release_tags()
    ceiling = kb_tags[-1] if kb_tags else "v0.0.0"
    up, src = upstream_tags(not args.no_remote)
    behind = [t for t in up if vt(t) > vt(ceiling)]

    ages, cve = verified_ages(today)
    stale = [r for r in ages if r[0] > args.stale_days]

    out = [f"# {'Свежесть базы' if ru else 'KB freshness'} — {today}\n"]
    out.append(f"{'Потолок базы' if ru else 'KB ceiling'}: **{ceiling}**  "
               f"({'источник апстрим-тегов' if ru else 'upstream source'}: {src})")

    out.append(f"\n## {'Новые теги Kubespray за потолком' if ru else 'New Kubespray tags beyond ceiling'}\n")
    if behind:
        out.append("❌ " + (f"апстрим ушёл вперёд — нужны RELEASE/UPGRADE доки для:" if ru
                            else "upstream is ahead — need RELEASE/UPGRADE docs for:"))
        out += [f"  - **{t}**" for t in behind]
    elif src == "unavailable":
        out.append("⚪ " + ("не удалось получить апстрим-теги" if ru else "couldn't read upstream tags"))
    else:
        out.append("✅ " + (f"база на потолке апстрима ({ceiling})" if ru
                            else f"KB is at the upstream ceiling ({ceiling})"))

    if args.upstream or args.journal:
        since = args.since or last_journal_date(str(today - datetime.timedelta(days=7)))
        prs, err = merged_prs(since)
        out.append(f"\n## {'Влито в апстрим с ' if ru else 'Merged upstream since '}{since}\n")
        if err:
            out.append(("⚪ не удалось получить список PR: " if ru else "⚪ could not fetch PRs: ") + err)
        elif not prs:
            out.append("✅ " + ("новых влитых PR нет" if ru else "no new merged PRs"))
        else:
            out.append(("Триаж за человеком: смотреть те, что трогают роли и плейбуки — "
                        "они меняют поведение на нодах." if ru else
                        "Human triage: the ones touching roles/playbooks change node behaviour."))
            for pr in prs:
                out.append(f"- `{pr['date']}` [#{pr['n']}]({pr['url']}) {pr['title']}")

    out.append(f"\n## {'Устаревание (verified_at)' if ru else 'Staleness (verified_at)'}\n")
    out.append((f"Порог: {args.stale_days} дн. Просрочено: **{len(stale)}** из {len(ages)} доков."
                if ru else
                f"Threshold: {args.stale_days}d. Stale: **{len(stale)}** of {len(ages)} docs."))
    if cve:
        oldest_cve = cve[0]
        out.append((f"CVE-матрицы ({len(cve)}) — самая старая: `{oldest_cve[2]}` "
                    f"({oldest_cve[1]}, {oldest_cve[0]} дн. назад). CVE date-sensitive — "
                    f"пере-свип: `python3 scripts/cve_sweep.py`." if ru else
                    f"CVE matrices ({len(cve)}) — oldest: `{oldest_cve[2]}` "
                    f"({oldest_cve[1]}, {oldest_cve[0]}d old). Re-sweep: `python3 scripts/cve_sweep.py`."))
    if stale[:8]:
        out.append(("\nСамые старые доки:" if ru else "\nOldest docs:"))
        out += [f"  - {age} дн — `{rel}` ({date})" for age, date, rel in stale[:8]]

    behind_or_stale = bool(behind) or bool(stale)
    out.append(f"\n## {'Вердикт' if ru else 'Verdict'}\n")
    out.append(("❌ база отстаёт / устарела — см. выше." if (behind_or_stale and ru)
                else "✅ база свежа." if ru
                else "❌ KB is behind / stale — see above." if behind_or_stale
                else "✅ KB is fresh."))
    report = "\n".join(out) + "\n"
    sys.stdout.write(report)

    if args.journal:
        # запись дописывается сверху: свежая проверка первой, история остаётся историей
        head = ("# Наблюдение за апстримом\n\n"
                "Дневник проверок: что появилось в Kubespray с прошлого раза и в каком "
                "состоянии база. Дописывается `kubepedia feed --journal`; дата последней "
                "записи служит точкой отсчёта для следующей.\n\n"
                "Преемник ручного «ежевечернего отчёта» базы 0.1.0 "
                "(`knowledge-base/reports/nightly/`), заглохшего 2026-07-15.\n")
        # внутренние заголовки отчёта уходят на уровень ниже даты
        entry = re.sub(r"^## ", "### ", report, flags=re.M)
        entry = re.sub(r"^# (Свежесть базы|KB freshness) — ", "## ", entry, flags=re.M)
        prev = ""
        if os.path.exists(JOURNAL):
            body = open(JOURNAL, encoding="utf-8").read().split("\n## ", 1)
            prev = ("\n## " + body[1]) if len(body) > 1 else ""
        os.makedirs(os.path.dirname(JOURNAL), exist_ok=True)
        with open(JOURNAL, "w", encoding="utf-8") as f:
            f.write(head + "\n" + entry + prev)
        sys.stderr.write(f"[feed] запись добавлена в {os.path.relpath(JOURNAL, ROOT)}\n")

    return 1 if behind_or_stale else 0


if __name__ == "__main__":
    main()
