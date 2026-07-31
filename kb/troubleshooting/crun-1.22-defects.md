---
id: TROUBLE-CRUN_1_22_DEFECTS
type: troubleshooting
title: "crun 1.22: defects fixed in the 1.22 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.22.0 <1.23.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - crun 1.22 known issues
  - crun 1.22 fixed in
  - is this crun bug already fixed
tags:
  - troubleshooting
  - upgrade
  - crun
sources:
  - type: docs
    path: containers/crun release notes for the 1.22 line — bug-fix entries
    url: https://github.com/containers/crun/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# crun 1.22: defects fixed in the 1.22 line

## Summary

**6 defects** the project fixed across **1 releases** of the 1.22 line, from 1.22 to
1.22. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.22

- criu: fix checkpoint and restore for containers that have a bind mount where the destination is a symbolic link
- cgroup: fix incorrect setting of cpu.max when the OCI quota is -1
- fix a regression that caused issues when dealing with paths that do not exist and openat2 is not available
- fix an issue where the file descriptor for the rootfs would become stale if the rootfs was replaced by a mount
- fix a potential crash in krun by checking if library handles exist before being unloaded
- cgroup: fix a regression on WSL when running with cgroup v1


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.22**, the newest release recorded here for this line.

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
