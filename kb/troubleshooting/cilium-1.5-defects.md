---
id: TROUBLE-CILIUM_1_5_DEFECTS
type: troubleshooting
title: "cilium 1.5: defects fixed in the 1.5 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.5.0 <1.6.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cilium 1.5 known issues
  - cilium 1.5 fixed in
  - is this cilium bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cilium
sources:
  - type: docs
    path: cilium/cilium release notes for the 1.5 line — bug-fix entries
    url: https://github.com/cilium/cilium/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cilium 1.5: defects fixed in the 1.5 line

## Summary

**9 defects** the project fixed across **3 releases** of the 1.5 line, from 1.5.0 to
1.5.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.5.0

- Added non-conformant LRO terminal states `Cancelled` and `Completed`
- Credentials now preserve MSAL headers e.g. X-Client-Sku
- #78: Fix unchecked error in example code (thanks @ravron)
- #70: Fix the handling of pre-releases and the 0.0.0 release edge case
- #97: Fixed copyright file for proper display on GitHub
- #107: Fix handling prerelease when sorting alphanum and num
- #109: Fixed where Validate sometimes returns wrong message on error

### 1.5.1

- `InteractiveBrowserCredential` handles `AdditionallyAllowedTenants` correctly

### 1.5.2

- `ManagedIdentityCredential` now specifies resource IDs correctly for Azure Container Instances


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.5.2**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `cilium/cilium`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/cilium.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
