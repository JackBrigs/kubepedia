---
id: TROUBLE-CRI_O_1_14_DEFECTS
type: troubleshooting
title: "cri-o 1.14: defects fixed in the 1.14 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.14.0 <1.15.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cri-o 1.14 known issues
  - cri-o 1.14 fixed in
  - is this cri-o bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cri-o
sources:
  - type: docs
    path: cri-o/cri-o release notes for the 1.14 line — bug-fix entries
    url: https://github.com/cri-o/cri-o/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cri-o 1.14: defects fixed in the 1.14 line

## Summary

**13 defects** the project fixed across **7 releases** of the 1.14 line, from 1.14.0 to
1.14.12. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.14.0

- Fix segfault for invalid paths in GetDiskUsageStats()
- container_create: fix race with sandbox being stopped
- container_server: fix a segfault when the sandbox is not found
- container: fix potential segfault on setup failure
- Usernamespaces: Fix permissions on runDirPath and BundlePath

### 1.14.1

- Fix possible out of bounds access during log parsing
- sandbox: fix segfault with manage_network_ns_lifecycle

### 1.14.4

- Fix runtime panic when having concurrent writes to runtime impl map

### 1.14.5

- Fix up machine os content version and cri-o version in spec

### 1.14.10

- Fix parse of memory.limit_in_bytes on 32-bit machines
- Fix container image used for integration tests

### 1.14.11

- Update vendor code for cni and ocicni and libpod, fix build errors

### 1.14.12

- Fix integration tests by adjusting image digest


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.14.12**, the newest release recorded here for this line.

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
