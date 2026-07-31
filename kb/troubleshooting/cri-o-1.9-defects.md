---
id: TROUBLE-CRI_O_1_9_DEFECTS
type: troubleshooting
title: "cri-o 1.9: defects fixed in the 1.9 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.9.0 <1.10.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cri-o 1.9 known issues
  - cri-o 1.9 fixed in
  - is this cri-o bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cri-o
sources:
  - type: docs
    path: cri-o/cri-o release notes for the 1.9 line — bug-fix entries
    url: https://github.com/cri-o/cri-o/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cri-o 1.9: defects fixed in the 1.9 line

## Summary

**6 defects** the project fixed across **4 releases** of the 1.9 line, from 1.9.0 to
1.9.16. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.9.0

- container_exec: fix terminal true process json
- container_create: fix apparmor from container config

### 1.9.2

- sandbox: fix sandbox logPath when crio restarts

### 1.9.14

- server: fix race between container create and cadvisor asking for info

### 1.9.16

- Fix possible out of bounds access during log parsing
- container_create: fix race with sandbox being stopped


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.9.16**, the newest release recorded here for this line.

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
