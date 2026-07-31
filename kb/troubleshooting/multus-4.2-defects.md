---
id: TROUBLE-MULTUS_4_2_DEFECTS
type: troubleshooting
title: "multus 4.2: defects fixed in the 4.2 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=4.2.0 <4.3.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - multus 4.2 known issues
  - multus 4.2 fixed in
  - is this multus bug already fixed
tags:
  - troubleshooting
  - upgrade
  - multus
sources:
  - type: docs
    path: k8snetworkplumbingwg/multus-cni release notes for the 4.2 line — bug-fix entries
    url: https://github.com/k8snetworkplumbingwg/multus-cni/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# multus 4.2: defects fixed in the 4.2 line

## Summary

**5 defects** the project fixed across **3 releases** of the 4.2 line, from 4.2.0 to
4.2.4. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 4.2.0

- Updated network-attachment-definition-client to v1.7.6 (thanks @Brian-McM! for the fix)
- (And there's fixes for e2e config and runtimeConfig API versions)

### 4.2.3

- Fix node reboot issue by using install_multus bin to update cni file by @Untersander in https://github.com/k8snetworkplumbingwg/multus-cni/pull/1445

### 4.2.4

- Adds support for CNI STATUS + other fixes for CNI Spec 1.1.0 by @trozet in https://github.com/k8snetworkplumbingwg/multus-cni/pull/1470
- Fix typo: cilium spelling by @linuzctl in https://github.com/k8snetworkplumbingwg/multus-cni/pull/1465


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **4.2.4**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `k8snetworkplumbingwg/multus-cni`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/multus.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
