#!/usr/bin/env python3
"""Generate source-grounded VARIABLE-* stub docs for Kubespray variables that don't
have a KDS doc yet — so links to per-variable docs resolve everywhere.

Each stub is derived from the Kubespray source (never fabricated): the real default
value, the defining defaults file, and the version envelope computed from which tags
actually contain the variable. Existing hand-written VARIABLE docs are left untouched.

    python scripts/gen_variable_stubs.py            # write stubs, then regenerate index
    python scripts/gen_variable_stubs.py --dry-run  # just report the counts
"""
import argparse
import json
import os
import re
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "kubespray-src")
OUTDIR = os.path.join(ROOT, "kb", "kubespray", "variables")
IDS = os.path.join(ROOT, "index", "ids.txt")
TAGS = ["v2.27.0", "v2.27.1", "v2.28.0", "v2.28.1",
        "v2.29.0", "v2.29.1", "v2.30.0", "v2.31.0"]
TODAY = "2026-07-18"
ID_RE = re.compile(r"^[A-Z0-9]+(_[A-Z0-9]+)*$")   # id slug (single underscores only)


def defaults_at(tag):
    """{var: (path, raw_value)} for every top-level key in a defaults file at `tag`."""
    out = subprocess.run(
        ["git", "-C", SRC, "grep", "-nE", "^[a-z][a-z0-9_]*:", tag, "--", "roles/"],
        capture_output=True, text=True).stdout
    defs = {}
    for ln in out.splitlines():
        parts = ln.split(":", 3)
        if len(parts) < 4:
            continue
        _tag, path, _lno, rest = parts
        if "/defaults/" not in path:
            continue
        kv = rest.split(":", 1)
        key = kv[0].strip()
        val = kv[1].strip() if len(kv) > 1 else ""
        if key and key not in defs:
            defs[key] = (path, val)
    return defs


def topical_tags(path):
    """Derive a couple of topical tags from the role path."""
    segs = [s for s in path.split("/")
            if s not in ("roles", "defaults", "main") and not s.endswith((".yml", ".yaml"))]
    tags = []
    for s in segs[:2]:
        t = s.replace("_", "-").lower()
        if t and t not in tags:
            tags.append(t)
    tags.append("variable")
    return tags


def value_display(val):
    if not val or val in ("|", ">", "|-", ">-"):
        return "(structured / block value — see source)"
    v = val.strip().strip('"').strip("'")
    v = v.replace('"', "'").replace("\\", "/")   # keep it safe inside a YAML "..." note
    if len(v) > 70:
        v = v[:67] + "…"
    return v or "(empty)"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    per_tag = {t: defaults_at(t) for t in TAGS}
    allvars = set().union(*[set(m) for m in per_tag.values()])
    existing = set()
    with open(IDS) as f:
        for line in f:
            if line.startswith("VARIABLE-"):
                existing.add(line.strip()[len("VARIABLE-"):])

    written, skipped_id, skipped_have = 0, 0, 0
    for name in sorted(allvars):
        slug = name.upper()
        if not ID_RE.match(slug):
            skipped_id += 1
            continue
        if slug in existing:
            skipped_have += 1
            continue
        present = [t for t in TAGS if name in per_tag[t]]
        if not present:
            continue
        lo, hi = present[0], present[-1]
        path, raw = per_tag[hi][name]
        val = value_display(raw)
        tags = topical_tags(path)
        url = f"https://github.com/kubernetes-sigs/kubespray/blob/{hi}/{path}"
        removed = "" if hi == TAGS[-1] else (
            f" **Removed after `{hi}`** (absent in later tags of the range).")
        body = f"""---
id: VARIABLE-{slug}
type: variable
title: {name}
status: active
kubespray_version: ">={lo} <={hi}"
kubernetes_version: null
component_version: null
verified_at: "{TODAY}"
confidence: verified
aliases:
  - {name}
tags:
{chr(10).join(f"  - {t}" for t in tags)}
sources:
  - type: code
    path: {path}
    url: {url}
    note: "default: {val}"
relations: []
---
<!-- generated: variable-stub -->

# {name}

## Summary

Kubespray variable `{name}` — default `{val}`. Defined in `{path}`. Present in Kubespray
`{lo}`–`{hi}` of the indexed range.{removed} (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `{path}` (Kubespray `{hi}`):

```yaml
{name}: {val}
```

## Compatibility

Present in the Kubespray tags `{lo}`–`{hi}`.{removed} Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `{path}` (Kubespray `{hi}`).
"""
        if not args.dry_run:
            with open(os.path.join(OUTDIR, f"{name}.md"), "w") as fh:
                fh.write(body)
        written += 1

    print(f"union vars: {len(allvars)}  existing VARIABLE docs: {len(existing)}")
    print(f"would write: {written}  skipped (invalid id): {skipped_id}  "
          f"skipped (already documented): {skipped_have}")
    if not args.dry_run:
        print("stubs written to", OUTDIR)


if __name__ == "__main__":
    main()
