#!/usr/bin/env python3
"""kubepedia breaking — документы «ломающие изменения» из добытого проблемного слоя.

Из трёх срезов, которые собирает `upstream_issues.py`, знанием базы становится один —
объявленные апстримом несовместимые изменения. Причина проста: дефекты исчисляются
тысячами и стареют вместе с версией, а ломающее изменение живёт вечно и отвечает на
единственный вопрос, который задают перед апгрейдом — «что у меня отвалится».

Документ пишется по компоненту, содержимое дословное. Отсев механический и описан
в самом документе: короткие строки и повторы — это заголовки и обрывки списков,
которые извлекатель принимает за записи.

    kubepedia breaking --all          # по всем, у кого набралось от трёх записей
    kubepedia breaking --component etcd
    kubepedia breaking --all --dry-run
"""
import argparse
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "reports", "upstream")
KB = os.path.join(ROOT, "kb", "troubleshooting")
MIN_ENTRIES = 3
MIN_LEN = 45
MARK = "machine-extracted by scripts/upstream_issues.py"

# компонент -> хвост стабильного идентификатора и репозиторий для ссылки
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from upstream_issues import REPOS  # noqa: E402


def slug(comp):
    return re.sub(r"[^A-Z0-9]+", "_", comp.upper()).strip("_")


def vkey(v):
    n = [int(x) for x in re.findall(r"\d+", v)[:3]]
    return n + [0] * (3 - len(n))


def clean(items):
    """Отсев мусора и разрезание слипшихся записей."""
    out, seen = [], set()
    for raw in items:
        # kubespray клеит несколько пунктов подряд через маркер «Action required»
        parts = re.split(r"(?i)\bAction required\b", raw)
        for part in (parts if len(parts) > 1 else [raw]):
            t = re.sub(r"\s*\(\[?#?\d+\]\(https?://[^\)]+\)\)?\s*$", "", part).strip()
            t = re.sub(r"\s+", " ", t).strip(" .;:")
            if len(t) < MIN_LEN:
                continue
            k = t.lower()[:80]
            if k in seen:
                continue
            seen.add(k)
            out.append(t)
    return out


DOC = """---
id: TROUBLE-{sid}_BREAKING_CHANGES
type: troubleshooting
title: "{comp}: declared breaking changes by release"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">={first} <={last}"
verified_at: "{today}"
confidence: verified
aliases:
  - {comp} breaking changes
  - {comp} upgrade broke
  - {comp} action required upgrade
  - what breaks upgrading {comp}
tags:
  - upgrade
  - breaking-change
  - {comp}
sources:
  - type: docs
    path: {repo} release notes — entries marked breaking / action required
    url: https://github.com/{repo}/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# {comp}: declared breaking changes by release

## Summary

**{total} behaviour changes** the project itself marked as breaking or action-required, across
{nrel} releases from {first} to {last}. These are not defects: they work as designed and still break
a configuration that worked yesterday. An upgrade crossing any of them needs a decision, not just a
rollout.

## Problem

The upgrade itself usually succeeds. The damage shows up afterwards — a setting silently ignored, a
default flipped, an API version withdrawn, a variable that must now be set explicitly.

## Context

{body}

## Diagnostics

```bash
# which version is actually deployed
kubectl get nodes -o wide
helm list -A
```

Cross the list above against the range you are moving through, not only the target version.

## Known Issues

Entries are verbatim from upstream release notes and filtered mechanically: lines shorter than
{minlen} characters and duplicates are dropped, because section headings and list fragments reach the
extractor looking like entries. If a release you care about appears empty here, read its notes
upstream before concluding that nothing changed.

## References

- Upstream releases of `{repo}`, extracted {today} by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/{comp}.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
"""


def build(comp, today):
    path = os.path.join(RAW, f"{comp}.json")
    if not os.path.exists(path):
        return None
    with open(path) as f:
        data = json.load(f)
    per = {v: clean(s.get("breaking changes", [])) for v, s in data.items()}
    per = {v: i for v, i in per.items() if i}
    total = sum(len(i) for i in per.values())
    if total < MIN_ENTRIES:
        return None
    vers = sorted(per, key=vkey)
    body = []
    for v in vers:
        body.append(f"### {v}\n")
        body += [f"- {x}" for x in per[v]]
        body.append("")
    return {
        "comp": comp, "sid": slug(comp), "repo": REPOS.get(comp, "?"),
        "total": total, "nrel": len(per),
        "first": vers[0].lstrip("v"), "last": vers[-1].lstrip("v"),
        "body": "\n".join(body), "today": today, "minlen": MIN_LEN,
    }


def main():
    ap = argparse.ArgumentParser(description="Документы о ломающих изменениях")
    ap.add_argument("--component", action="append")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true", help="перезаписать в том числе рукописные документы")
    ap.add_argument("--today", default="2026-07-31")
    args = ap.parse_args()

    comps = args.component or (sorted(
        os.path.basename(p)[:-5] for p in os.listdir(RAW) if p.endswith(".json")) if args.all else [])
    if not comps:
        ap.error("нужен --component или --all")

    made = 0
    for comp in comps:
        d = build(comp, args.today)
        if not d:
            print(f"[--] {comp:24} записей меньше {MIN_ENTRIES}")
            continue
        made += 1
        print(f"[ok] {comp:24} {d['total']:4} записей в {d['nrel']:3} релизах")
        if args.dry_run:
            continue
        out = os.path.join(KB, f"{comp}-breaking-changes.md")
        # рукописный документ богаче машинного: в нём разбор, а не только перечень.
        # Такой не трогаем — он не несёт метку генератора.
        if os.path.exists(out) and MARK not in open(out, encoding="utf-8").read() and not args.force:
            print(f"     {comp}: на месте рукописный документ, пропускаю (--force перезапишет)")
            made -= 1
            continue
        with open(out, "w", encoding="utf-8") as f:
            f.write(DOC.format(**d))
    print(f"\nдокументов: {made}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
