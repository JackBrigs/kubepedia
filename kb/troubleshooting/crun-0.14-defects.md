---
id: TROUBLE-CRUN_0_14_DEFECTS
type: troubleshooting
title: "crun 0.14: defects fixed in the 0.14 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.14.0 <0.15.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - crun 0.14 known issues
  - crun 0.14 fixed in
  - is this crun bug already fixed
tags:
  - troubleshooting
  - upgrade
  - crun
sources:
  - type: docs
    path: containers/crun release notes for the 0.14 line — bug-fix entries
    url: https://github.com/containers/crun/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# crun 0.14: defects fixed in the 0.14 line

## Summary

**7 defects** the project fixed across **2 releases** of the 0.14 line, from 0.14 to
0.14.1. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.14

- linux: fix an issue where the basename for $NOTIFY_SOCKET is different than /notify
- cgroup: fix an issue on CentOS 7.8 when using net_cls and net_prio
- cgroup, v2: fix crun update with both --memory -1 --memory-swap -1
- linux: fix double close on the same file descriptor
- linux: fix path lookups for relative paths containing '/'

### 0.14.1

- fix a regression in crun-0.14 where openat2(2) would fail when bind mounting a symlink
- various small fixes to allow running regression tests outside of source tree


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.14.1**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `containers/crun`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/crun.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
