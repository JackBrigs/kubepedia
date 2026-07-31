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

**31 defects** the project fixed across **6 releases** of the 1.10 line, from 1.10.0 to
1.10.5. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.10.0

- e00b07dc8 container_exec: Fix terminal setting for exec
- 04b325868 Cleanup two comments that a previous patch fixed
- ae956715b factor common code out of ListImages, fix some missing locking
- e35204c5e Fix create container failure due to wrong image reference
- 0b87fe448 Merge pull request #1367 from runcom/fix-selinuxopt
- 7f82f9bbe Makefile: fix SELINUXOPT generation
- 534143053 Merge pull request #1358 from runcom/master-netns-fix
- ada416b4e Makefile: Fix install.* prerequisites
- ea90be40c Merge pull request #1337 from nalind/fix-runasuser-cache
- 731083936 Merge pull request #1321 from runcom/bump-runtime-tools-cap-fix
- c718f15d4 vendor: bump runtime-tools to fix caps drop handling
- ebb88f9a6 Merge pull request #1306 from runcom/fix-log-path-restore
- a0157078a sandbox: fix sandbox logPath when crio restarts
- 28997fe4c Merge pull request #1304 from runcom/fix-ami-build
- 3c859c0d6 contrib: test: fix runc build on AMIs
- a50f352eb Update tutorial.md to fix a few minor errors
- 41aaf4e3d Merge pull request #1250 from giuseppe/fix-tmpdir-files
- ebc249cad Merge pull request #1214 from runcom/fix-1.10-vendor

### 1.10.1

- eaee119f Fix handling of /dev/shm mounting inside of containers
- abf5dd92 test: Fix race condition in ctr.bats

### 1.10.2

- 07ac5d36c Merge pull request #1607 from giuseppe/fix-reload-log-1.10
- 040d5282b Merge pull request #1541 from runcom/status-fix-1.10

### 1.10.3

- b15d3ed4 Merge pull request #1613 from runcom/create-fixes-1.10

### 1.10.4

- c432dabf network: Fix manage NetworkNS lifecycle
- 0291f8b7 Merge pull request #1628 from runcom/selinux-relabel-fixes-1.10
- 18ea4bdf sandbox_run: fix selinux relabel sharing
- 60aca683 container_create: more selinux relabel fixes
- 011fa7bd Merge pull request #1616 from runcom/fix-race-cadvisor-create
- 4cafb570 Merge pull request #1620 from runcom/fix-selinux-relabeling
- 70795f75 server: fix race between container create and cadvisor asking for info

### 1.10.5

- e0dd8a3d Merge pull request #1657 from chavafg/topic/fix-rc-1.10


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.10.5**, the newest release recorded here for this line.

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
