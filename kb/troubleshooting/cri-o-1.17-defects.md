---
id: TROUBLE-CRI_O_1_17_DEFECTS
type: troubleshooting
title: "cri-o 1.17: defects fixed in the 1.17 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.17.0 <1.18.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cri-o 1.17 known issues
  - cri-o 1.17 fixed in
  - is this cri-o bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cri-o
sources:
  - type: docs
    path: cri-o/cri-o release notes for the 1.17 line — bug-fix entries
    url: https://github.com/cri-o/cri-o/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cri-o 1.17: defects fixed in the 1.17 line

## Summary

**19 defects** the project fixed across **4 releases** of the 1.17 line, from 1.17.0 to
1.17.5. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.17.0

- 6fcac310d Fix reload behavior for unqualified search registries
- 46167cbec Fix possible segmentation fault in namespace removal
- eab842efc Fix pinns path mismatch for install and uninstall
- c3ac2e539 Fix possible segmentation fault in error handling
- fc2595923 fix the git commit variable in Makefile in case git doesn't exist
- fc5f63499 Fix possible branch condition evaluates to a garbage value
- 2911d495c Fix fish shell completion for new default conmon system.slice
- 29e2328bc Fix default storage driver for completions validation
- 6025578f1 Update golangci lint and apply fixes
- bcc4e1729 fix selinux label on volume mount directory creation
- 829123115 Fix invalid log_dir position in crio.conf
- 05f04b9ac Fix possible segmentation fault on restore when runtime_type changes

### 1.17.2

- f2d3397f4 stats: fix stats when systemd cgroups are used

### 1.17.3

- [`a967feba5`](https://github.com/cri-o/cri-o/commit/a967feba5d3dc3331e511136527df7b593688331) Merge pull request [#3533](https://github.com/cri-o/cri-o/pull/3533) from rhafer/fix-3511-1.17
- [`2a90d7520`](https://github.com/cri-o/cri-o/commit/2a90d752006cb3bf0cd5f623ca9a9348b085a7f4) Merge pull request [#3530](https://github.com/cri-o/cri-o/pull/3530) from haircommander/fix-netns-dir-1.17

### 1.17.5

- 1e5cec409 Revert "Fix potentially unclosed file in runtimeVM#CreateContainer"
- 04dd575a1 internal/oci/runtime_vm: fix resizePty signature
- 78009728b Fix potentially unclosed file in runtimeVM#CreateContainer
- 694daca8f test: update image digest to fix test


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.17.5**, the newest release recorded here for this line.

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
