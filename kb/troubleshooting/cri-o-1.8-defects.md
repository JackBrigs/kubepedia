---
id: TROUBLE-CRI_O_1_8_DEFECTS
type: troubleshooting
title: "cri-o 1.8: defects fixed in the 1.8 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.8.0 <1.9.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cri-o 1.8 known issues
  - cri-o 1.8 fixed in
  - is this cri-o bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cri-o
sources:
  - type: docs
    path: cri-o/cri-o release notes for the 1.8 line — bug-fix entries
    url: https://github.com/cri-o/cri-o/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cri-o 1.8: defects fixed in the 1.8 line

## Summary

**5 defects** the project fixed across **3 releases** of the 1.8 line, from 1.8.0 to
1.8.4. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.8.0

- Fix a copy/paste error in libpod initializers
- fix host pid handling for containers and share uts ns
- oci: fixes to properly handle container stop action

### 1.8.3

- container_create: fix apparmor from container config

### 1.8.4

- container_exec: fix terminal true process json


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.8.4**, the newest release recorded here for this line.

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
