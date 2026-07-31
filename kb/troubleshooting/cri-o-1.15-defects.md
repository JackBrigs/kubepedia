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

**19 defects** the project fixed across **4 releases** of the 1.15 line, from 1.15.0 to
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
- Fix mockGetRef, and deal with all of the fallout
- Fix errcheck lint for network namespace creation
- Add gocritic paramTypeCombine linter and fixes
- Add gocritic unnamedResult linter and fix issues
- fixes assumption that socklen_t is always an unsigned long
- Fix hack/openpgp_tag.sh on older distributions
- oci: fix segfault when cgroup cannot be configured

### 1.15.1

- Fix container image used for integration tests
- Fix parse of memory.limit_in_bytes on 32-bit machines

### 1.15.3

- Fix integration tests by adjusting image digest

### 1.15.4

- fix selinux label on volume mount directory creation


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
