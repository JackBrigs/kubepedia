---
id: TROUBLE-CRI_O_1_10_DEFECTS
type: troubleshooting
title: "cri-o 1.10: defects fixed in the 1.10 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.10.0 <1.11.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cri-o 1.10 known issues
  - cri-o 1.10 fixed in
  - is this cri-o bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cri-o
sources:
  - type: docs
    path: cri-o/cri-o release notes for the 1.10 line — bug-fix entries
    url: https://github.com/cri-o/cri-o/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cri-o 1.10: defects fixed in the 1.10 line

## Summary

**8 defects** the project fixed across **3 releases** of the 1.10 line, from 1.10.0 to
1.10.4. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.10.0

- container_exec: Fix terminal setting for exec
- Cleanup two comments that a previous patch fixed
- factor common code out of ListImages, fix some missing locking
- Fix create container failure due to wrong image reference
- vendor: bump runtime-tools to fix caps drop handling
- sandbox: fix sandbox logPath when crio restarts

### 1.10.1

- Fix handling of /dev/shm mounting inside of containers

### 1.10.4

- server: fix race between container create and cadvisor asking for info


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.10.4**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `cri-o/cri-o`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/cri-o.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
