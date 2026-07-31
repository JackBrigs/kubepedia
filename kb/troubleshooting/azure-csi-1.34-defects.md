---
id: TROUBLE-AZURE_CSI_1_34_DEFECTS
type: troubleshooting
title: "azure-csi 1.34: defects fixed in the 1.34 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.34.0 <1.35.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - azure-csi 1.34 known issues
  - azure-csi 1.34 fixed in
  - is this azure-csi bug already fixed
tags:
  - troubleshooting
  - upgrade
  - azure-csi
sources:
  - type: docs
    path: kubernetes-sigs/azuredisk-csi-driver release notes for the 1.34 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/azuredisk-csi-driver/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# azure-csi 1.34: defects fixed in the 1.34 line

## Summary

**27 defects** the project fixed across **5 releases** of the 1.34 line, from 1.34.0 to
1.34.4. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.34.0

- cleanup: fix helm chart index file by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3147
- fix: make disk and snapshot uri regex case insensitive everywhere by @landreasyan in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3149
- fix(doc): fixing typo in the doc by @pawanpraka1 in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3148
- fix: xfs mount failure on Azure Linux 3.0 node by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3160
- fix: typo in the required permissions by @jsafrane in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3181
- fix: batching implementation should allow for an early exit for disks already processed in the batch by @landreasyan in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3205
- fix: allow `.` in Azure tags by @kalexmills in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3277
- fix: China cloud endpoints by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3303
- fix: ZRS disk should support 4 zones by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3309
- fix: detach call should not use the full context deadline and should leave an active context for force detach on timeout by @landreasyan in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3294
- fix: validating Block Device Size Before Resizing FileSystem by @landreasyan in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3355
- fix: disable enable-minimum-retry-after by default by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3358
- fix: reconcile loop to watch migrations if earlier submission had failed by @hasethuraman in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3344
- fix: create volume failure when requested pvc size is smaller than snapshot disk size by @priyansh17 in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3379
- fix: disk creation failure in AzureStack env by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3428
- fix: ASH static provision segmentation fault by @Phaow in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3449

### 1.34.1

- [release-1.34] fix: let nodeExpandVolume retried if block device size is taking time to reflect in host by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3476
- [release-1.34] fix: handling dangling detaches in a better way by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3481

### 1.34.2

- [release-1.34] fix: Correct CSI-Provisioner permissions for VAC by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3495
- [release-1.34] fix: replace os.ReadDir with fs.ReadDir(1) to avoid extra memory usage by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3500

### 1.34.3

- [release-1.34] fix: trigger migration within few mins by batching the volumes or imp… by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3535
- [release-1.34] fix: incorrect node attached on waitingForDetached call by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3547
- [release-1.34] fix: increase checkDiskLun throttle threshold from 1s to 10s by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3566
- [release-1.34] fix: skip ManagedBy polling after successful VMSS detach by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3568
- [release-1.34] test: fix trivy action failure by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3576

### 1.34.4

- [release-1.34] fix: helm chart index by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3592
- [release-1.34] fix: wrong NVMe disk LUN mapping on Windows D4ads_v7 SKU VM by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3636


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.34.4**, the newest release recorded here for this line.

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
