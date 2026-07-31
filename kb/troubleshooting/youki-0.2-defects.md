---
id: TROUBLE-YOUKI_0_2_DEFECTS
type: troubleshooting
title: "youki 0.2: defects fixed in the 0.2 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.2.0 <0.3.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - youki 0.2 known issues
  - youki 0.2 fixed in
  - is this youki bug already fixed
tags:
  - troubleshooting
  - upgrade
  - youki
sources:
  - type: docs
    path: youki-dev/youki release notes for the 0.2 line — bug-fix entries
    url: https://github.com/youki-dev/youki/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# youki 0.2: defects fixed in the 0.2 line

## Summary

**11 defects** the project fixed across **1 releases** of the 0.2 line, from 0.2.0 to
0.2.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.2.0

- [Trivial] exclude the oci-runtime-test from the typos by @yihuaf in https://github.com/containers/youki/pull/2133
- disable musl test for now by @yihuaf in https://github.com/containers/youki/pull/2150
- Fix musl test function not parametered correctly by @yihuaf in https://github.com/containers/youki/pull/2158
- Rust 1.71.0 by @utam0k in https://github.com/containers/youki/pull/2167
- Make container_args clone-able by @yihuaf in https://github.com/containers/youki/pull/2193
- Fix podman tests to properly run by @YJDoc2 in https://github.com/containers/youki/pull/2233
- Named all GitHub Actions workflows by @utam0k in https://github.com/containers/youki/pull/2256
- Include Breaking Changes section in the release note by @utam0k in https://github.com/containers/youki/pull/2265
- Extend wait time for auto-merge by @utam0k in https://github.com/containers/youki/pull/2278
- Switch codespace from gitpod by @utam0k in https://github.com/containers/youki/pull/2306
- Rust 1.72 by @utam0k in https://github.com/containers/youki/pull/2323


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.2.0**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `youki-dev/youki`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/youki.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
