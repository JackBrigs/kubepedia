---
id: TROUBLE-CRUN_1_4_DEFECTS
type: troubleshooting
title: "crun 1.4: defects fixed in the 1.4 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.4.0 <1.5.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - crun 1.4 known issues
  - crun 1.4 fixed in
  - is this crun bug already fixed
tags:
  - troubleshooting
  - upgrade
  - crun
sources:
  - type: docs
    path: containers/crun release notes for the 1.4 line — bug-fix entries
    url: https://github.com/containers/crun/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# crun 1.4: defects fixed in the 1.4 line

## Summary

**7 defects** the project fixed across **4 releases** of the 1.4 line, from 1.4.1 to
1.4.5. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.4.1

- Fix check for an invalid path. crun was performing the wrong check to validate a path, causing spurious failures at runtime
- Fix regression when joining a container that has explicit paths for the namespaces
- Fix build issues when configured with --enable-shared
- Fix build on systems where OPEN_TREE_CLOEXEC is not defined

### 1.4.2

- Fix running with a read-only /dev. The /dev/console file is created before re-mounting /dev as read-only

### 1.4.4

- Resolve symlinks in bind mounts when creating a user namespace

### 1.4.5

- exec: fix double free when using --apparmor and --process-label


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.4.5**, the newest release recorded here for this line.

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
