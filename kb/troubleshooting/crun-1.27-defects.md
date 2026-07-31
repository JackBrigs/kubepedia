---
id: TROUBLE-CRUN_1_27_DEFECTS
type: troubleshooting
title: "crun 1.27: defects fixed in the 1.27 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.27.0 <1.28.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - crun 1.27 known issues
  - crun 1.27 fixed in
  - is this crun bug already fixed
tags:
  - troubleshooting
  - upgrade
  - crun
sources:
  - type: docs
    path: containers/crun release notes for the 1.27 line — bug-fix entries
    url: https://github.com/containers/crun/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# crun 1.27: defects fixed in the 1.27 line

## Summary

**9 defects** the project fixed across **2 releases** of the 1.27 line, from 1.27 to
1.27.1. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.27

- container: fix createRuntime hooks not receiving bundle path
- cgroup: fix read_pids_cgroup skipping child cgroups
- utils: fix memory leak and missing cache in libcrun_initialize_apparmor()
- container: fix CPU busy loop when output pipe is blocked
- numerous fixes for error handling, errno usage, and resource leaks

### 1.27.1

- linux: fix bind mount propagation regression. Mounts hot-plugged after container start (e.g. USB drives) were invisible or owned by nobody inside the container because propagation peer groups were destroyed
- utils: fix AppArmor profile inside a user namespace
- cgroup: fix recursive cgroup cleanup failure that could cause EBADF errors when deleting containers with sub-cgroups
- libcrun: fix "unlink /dev/console: Read-only file system" error when running containers with --read-only


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.27.1**, the newest release recorded here for this line.

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
