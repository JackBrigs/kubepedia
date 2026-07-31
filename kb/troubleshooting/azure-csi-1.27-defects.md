---
id: TROUBLE-AZURE_CSI_1_27_DEFECTS
type: troubleshooting
title: "azure-csi 1.27: defects fixed in the 1.27 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.27.0 <1.28.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - azure-csi 1.27 known issues
  - azure-csi 1.27 fixed in
  - is this azure-csi bug already fixed
tags:
  - troubleshooting
  - upgrade
  - azure-csi
sources:
  - type: docs
    path: kubernetes-sigs/azuredisk-csi-driver release notes for the 1.27 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/azuredisk-csi-driver/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# azure-csi 1.27: defects fixed in the 1.27 line

## Summary

**8 defects** the project fixed across **2 releases** of the 1.27 line, from 1.27.0 to
1.27.1. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.27.0

- fix: switch base image to fix CVEs by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1704
- fix: incorrect driver version in CSIDriver by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1707
- fix: buildx issue with provenance disabled by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1720
- fix: increase csi-attacher worker-threads num by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1719
- fix: second expand volume failure on Ubuntu 22.04 by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1728

### 1.27.1

- [release-1.27] tes: fix golint action failure by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1778
- [release-1.27] fix: detach disk failure when there is throttling by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1782
- [release-1.27] fix: PremiumV2_LRS caching mode issue by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1795


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.27.1**, the newest release recorded here for this line.

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
