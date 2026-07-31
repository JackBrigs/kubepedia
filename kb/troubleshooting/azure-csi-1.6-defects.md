---
id: TROUBLE-AZURE_CSI_1_6_DEFECTS
type: troubleshooting
title: "azure-csi 1.6: defects fixed in the 1.6 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.6.0 <1.7.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - azure-csi 1.6 known issues
  - azure-csi 1.6 fixed in
  - is this azure-csi bug already fixed
tags:
  - troubleshooting
  - upgrade
  - azure-csi
sources:
  - type: docs
    path: kubernetes-sigs/azuredisk-csi-driver release notes for the 1.6 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/azuredisk-csi-driver/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# azure-csi 1.6: defects fixed in the 1.6 line

## Summary

**7 defects** the project fixed across **1 releases** of the 1.6 line, from 1.6.0 to
1.6.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.6.0

- fix: Remove gen-skus-map by @jsafrane in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/961
- fix: disable networkAccessPolicy on Azure Stack Cloud by @songjiaxun in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/960
- fix: driver register issue on Windows node by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/970
- fix: remove kubelet-registration-probe on Linux by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/972
- fix: set default userAgent issue by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/973
- fix: disable disk related rate limit by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/979
- fix: ignore GetDisk throttling in DeleteDisk by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/980


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.6.0**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `kubernetes-sigs/azuredisk-csi-driver`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/azure-csi.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
