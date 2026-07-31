---
id: TROUBLE-CRI_O_1_13_DEFECTS
type: troubleshooting
title: "cri-o 1.13: defects fixed in the 1.13 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.13.0 <1.14.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cri-o 1.13 known issues
  - cri-o 1.13 fixed in
  - is this cri-o bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cri-o
sources:
  - type: docs
    path: cri-o/cri-o release notes for the 1.13 line — bug-fix entries
    url: https://github.com/cri-o/cri-o/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cri-o 1.13: defects fixed in the 1.13 line

## Summary

**18 defects** the project fixed across **6 releases** of the 1.13 line, from 1.13.0 to
1.13.10. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.13.0

- 5a4c3be91 container_create: fix RunAsGroup logic
- 9c7f9ad79 Merge pull request #1910 from runcom/fix-kata
- 4da359e4c vendor: revendor c/storage to fix a devicemapper bug
- 4a360891e Merge pull request #1909 from isimluk/fix-overflow
- ced618faa vendor: update storage for a panic fix
- 542feb760 Merge pull request #1884 from runcom/fix-dev
- c2a8afd5c container_create: fix dev mounts and remove nodev from /dev mounts
- 845f1c142 docs: fix links for policy.json, registries.conf
- 8a64c99a8 conmon: fix case when symlink == max UNIX socket path
- 6edbe3f79 fix containerd-release moved to release-tool

### 1.13.1

- ede97e6c Merge pull request #1960 from giuseppe/fix-another-segfault-1.13
- 094402d3 container_server: fix a segfault when the sandbox is not found

### 1.13.4

- 03eff1c0 container_create: fix race with sandbox being stopped

### 1.13.5

- ac05e1b4 Merge pull request #2186 from openSUSE/release-1.13-oob-log-fix
- 645a8144 Fix possible out of bounds access during log parsing

### 1.13.6

- 47f02d2e Merge pull request #2216 from giuseppe/fix-fd-leak

### 1.13.10

- 807e3e3cb Fix parse of memory.limit_in_bytes on 32-bit machines
- 82d6ddec8 Fix integration tests for CNI update


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.13.10**, the newest release recorded here for this line.

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
