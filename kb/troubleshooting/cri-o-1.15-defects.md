---
id: TROUBLE-CRI_O_1_15_DEFECTS
type: troubleshooting
title: "cri-o 1.15: defects fixed in the 1.15 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.15.0 <1.16.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cri-o 1.15 known issues
  - cri-o 1.15 fixed in
  - is this cri-o bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cri-o
sources:
  - type: docs
    path: cri-o/cri-o release notes for the 1.15 line — bug-fix entries
    url: https://github.com/cri-o/cri-o/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cri-o 1.15: defects fixed in the 1.15 line

## Summary

**38 defects** the project fixed across **5 releases** of the 1.15 line, from 1.15.0 to
1.15.4. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.15.0

- Fix `hack/openpgp_tag.sh` on older distributions
- Fix broken link to `policy.json(5)` in `README.md`
- Fix mentioned distributions within the setup tutorial
- Fix oci segfault when cgroup cannot be configured
- Fix possible out of bounds access during log parsing
- Fix possible runtime panic when netns is `nil`
- Fix possible runtime panic when netns is not set up
- Fix runtime panic when having concurrent writes to runtime impl map
- 14bce4555 Fix mockGetRef, and deal with all of the fallout
- b52bd78c8 Fix e2e*features*\* selinux denials
- a7cf5b5a2 Fix Vagrantfile vendor inconsistency
- 0f446aeaf Fix mentioned distributions in README.md
- 1b70e6533 Fix mentioned distributions within the setup tutorial
- fd81c3e82 Fix errcheck lint for network namespace creation
- 1951bda01 Fix runtime panic when having concurrent writes to runtime impl map
- 59f8db7e8 Fix build issues on 32-bit architectures
- 65925cc39 Fix possible runtime panic on store shutdown
- 44864aaf2 Add gocritic paramTypeCombine linter and fixes
- e672d4a95 Add gocritic builtinShadow linter and fixes
- c1e9670e0 Add gocritic importShadow linter and fixes
- a5295f178 Add gocritic wrapperFunc linter and fixes
- ea9e2474a Add gocritic unnamedResult linter and fix issues
- b73bc4632 Add gocritic sloppyReassign linter and fixes
- cd2981c27 Add gocritic appendCombine linter and fixes
- 3407a25ff Add gocritic appendAssign linter and fixes
- 4a64aba22 Add nakedret linter and related fixes
- a8fe9e09b Fix kubernetes import paths for cri-api
- c2e70adc5 fixes assumption that socklen_t is always an unsigned long
- dd9192469 Fix hack/openpgp_tag.sh on older distributions
- e6daef18c fix broken link to policy.json(5) in readme
- e12380508 oci: fix segfault when cgroup cannot be configured
- 61f8a5c41 Fix possible out of bounds access during log parsing

### 1.15.1

- 964699128 Fix container image used for integration tests
- e2bc98748 Fix parse of memory.limit_in_bytes on 32-bit machines

### 1.15.2

- 799d7e328 crio-wipe: Fix int compare in lib.bash

### 1.15.3

- b44db9645 Fix integration tests by adjusting image digest

### 1.15.4

- cf9047092 test: update image digest to fix test
- 685ec07bb fix selinux label on volume mount directory creation


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.15.4**, the newest release recorded here for this line.

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
