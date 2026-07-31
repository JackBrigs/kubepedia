#!/usr/bin/env python3
"""kubepedia defects — документы «исправленные дефекты» по линиям поддержки.

Парный к `gen_breaking_docs.py`. Тот берёт из добытого проблемного слоя ломающие
изменения, этот — исправления дефектов, то есть основную массу: пятнадцать с
лишним тысяч строк по всем компонентам.

Почему по минорным линиям, а не по компоненту целиком: у containerd за всю историю
2610 исправлений, единым списком это нечитаемо и бесполезно. Линия поддержки —
естественная единица: внутри неё апгрейд дёшев, и вопрос «а это уже чинили?»
задают именно в её границах.

Документ отвечает на один вопрос: несёт ли моя версия этот дефект. Если версия
меньше той, под которой стоит запись, — несёт.

    kubepedia defects --all
    kubepedia defects --component containerd
    kubepedia defects --all --dry-run
"""
import argparse
import collections
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "reports", "upstream")
KB = os.path.join(ROOT, "kb", "troubleshooting")
MIN_ENTRIES = 5           # ниже этого документ не окупает себя как отдельная запись
MIN_LEN = 45
MARK = "machine-extracted by scripts/upstream_issues.py"

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from upstream_issues import REPOS  # noqa: E402


def slug(text):
    return re.sub(r"[^A-Z0-9]+", "_", text.upper()).strip("_")


def vkey(v):
    n = [int(x) for x in re.findall(r"\d+", v)[:3]]
    return n + [0] * (3 - len(n))


def clean(items):
    out, seen = [], set()
    for raw in items:
        parts = re.split(r"(?i)\bAction required\b", raw) if re.search(r"(?i)action required", raw) else [raw]
        for part in parts:
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
id: TROUBLE-{sid}_{lid}_DEFECTS
type: troubleshooting
title: "{comp} {line}: defects fixed in the {line} line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">={line}.0 <{nextline}.0"
verified_at: "{today}"
confidence: verified
aliases:
  - {comp} {line} known issues
  - {comp} {line} fixed in
  - is this {comp} bug already fixed
tags:
  - troubleshooting
  - upgrade
  - {comp}
sources:
  - type: docs
    path: {repo} release notes for the {line} line — bug-fix entries
    url: https://github.com/{repo}/releases
    note: "{MARK}; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# {comp} {line}: defects fixed in the {line} line

## Summary

**{total} defects** the project fixed across **{nrel} releases** of the {line} line, from {first} to
{last}. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

{body}

## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **{last}**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than {minlen} characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `{repo}`, extracted {today} by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/{comp}.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
"""


def build(comp, today):
    path = os.path.join(RAW, f"{comp}.json")
    if not os.path.exists(path):
        return []
    with open(path) as f:
        data = json.load(f)
    per = collections.defaultdict(dict)
    for ver, secs in data.items():
        m = re.match(r"v?(\d+\.\d+)", ver)
        if not m:
            continue
        items = clean(secs.get("bug fixes", []))
        if items:
            per[m.group(1)][ver] = items
    out = []
    for line, rels in per.items():
        total = sum(len(v) for v in rels.values())
        if total < MIN_ENTRIES:
            continue
        vers = sorted(rels, key=vkey)
        body = []
        for v in vers:
            body.append(f"### {v.lstrip('v')}\n")
            body += [f"- {x}" for x in rels[v]]
            body.append("")
        major, minor = line.split(".")[:2]
        out.append({
            "comp": comp, "sid": slug(comp), "line": line, "lid": slug(line),
            "nextline": f"{major}.{int(minor) + 1}",
            "repo": REPOS.get(comp, "?"), "total": total, "nrel": len(rels),
            "first": vers[0].lstrip("v"), "last": vers[-1].lstrip("v"),
            "body": "\n".join(body), "today": today, "minlen": MIN_LEN, "MARK": MARK,
        })
    return out


def main():
    ap = argparse.ArgumentParser(description="Документы об исправленных дефектах по линиям")
    ap.add_argument("--component", action="append")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--today", default="2026-07-31")
    args = ap.parse_args()

    comps = args.component or (sorted(
        os.path.basename(p)[:-5] for p in os.listdir(RAW) if p.endswith(".json")) if args.all else [])
    if not comps:
        ap.error("нужен --component или --all")

    made = total = 0
    for comp in comps:
        for d in build(comp, args.today):
            out = os.path.join(KB, f"{comp}-{d['line']}-defects.md")
            # у компонента может быть разобранный руками документ по той же линии
            # под своим именем — машинный дубль тогда не нужен
            hand = os.path.join(KB, f"{comp}-{d['line']}-known-issues.md")
            if os.path.exists(hand) and not args.force:
                print(f"     {comp} {d['line']}: есть рукописный разбор линии, пропускаю")
                continue
            if os.path.exists(out) and MARK not in open(out, encoding="utf-8").read() and not args.force:
                print(f"     {comp} {d['line']}: рукописный документ, пропускаю")
                continue
            made += 1
            total += d["total"]
            if not args.dry_run:
                with open(out, "w", encoding="utf-8") as f:
                    f.write(DOC.format(**d))
        print(f"[ok] {comp:24} линий с документами: "
              f"{len([1 for _ in build(comp, args.today)])}")
    print(f"\nдокументов: {made}, записей в них: {total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
