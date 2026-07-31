---
id: TROUBLE-AZURE_CSI_1_33_DEFECTS
type: troubleshooting
title: "azure-csi 1.33: defects fixed in the 1.33 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.33.0 <1.34.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - azure-csi 1.33 known issues
  - azure-csi 1.33 fixed in
  - is this azure-csi bug already fixed
tags:
  - troubleshooting
  - upgrade
  - azure-csi
sources:
  - type: docs
    path: kubernetes-sigs/azuredisk-csi-driver release notes for the 1.33 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/azuredisk-csi-driver/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# azure-csi 1.33: defects fixed in the 1.33 line

## Summary

**37 defects** the project fixed across **9 releases** of the 1.33 line, from 1.33.0 to
1.33.10. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.33.0

- fix: avoid duplicate ssl mounts on Fedora node in AzureStack environment by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2922
- fix: avoid get disk call in disk creation by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2934
- fix: reduce get disk calls in disk attach/detach on VMSS by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2941
- fix: merge OTEL metrics with legacy registerer by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2949
- fix: increase TaintRemovalInitialDelay as 30s by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2977
- fix: detach disk should have more priority than attach disk on the same node by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2992
- fix: panic for GetZoneByNodeName on Azure Stack by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3017
- fix: remove unnecessary get vmss call during disk attach by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3022
- fix: decrease poller delay in AzureClient as 5s by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3034
- fix: incorrect disk num discovery on Windows 2019 node by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3038
- fix: disk detach failure on AzureStack Hub by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3047
- fix: vpa install and uninstall script by @umagnus in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3058
- fix: adjust the batch size as per the number of disks allowed by @nearora-msft in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3039
- fix: bump mount-utils to fix volume resizing failure when there are nfs unresponsive volumes by @gnufied in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3071
- fix: vmss flex node naming parsing issue by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3091

### 1.33.2

- [release-1.33] fix: make disk and snapshot uri regex case insensitive everywhere by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3151
- [release-1.33] fix: xfs mount failure on Azure Linux 3.0 node by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3175
- [release-1.33] fix: helm chart index on release-1.33 by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3185

### 1.33.3

- [release-1.33] fix: batching implementation should allow for an early exit for disks already processed in the batch by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3211
- [release-1.33] test: fix TestConcurrentDetachDisk ut failure on Windows by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3231

### 1.33.5

- [release-1.33] test: fix helm install by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3299
- [release-1.33] fix: China cloud endpoints by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3305
- [release-1.33] fix: ZRS disk should support 4 zones by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3310
- [release-1.33] fix: detach call should not use the full context deadline by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3334

### 1.33.6

- [release-1.33] test: fix govet error by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3359
- [release-1.33] fix: validating Block Device Size Before Resizing FileSystem by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3361
- [release-1.33] fix: disable enable-minimum-retry-after by default by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3362
- [release-1.33] test: fix sanity test failure by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3367
- [release-1.33] Revert "fix: disable enable-minimum-retry-after by default" by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3371
- [release-1.33] fix: reconcile loop to watch migrations if earlier submission had failed by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3384
- [release-1.33] fix: create volume failure when requested pvc size is smaller than snapshot disk size by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3395

### 1.33.7

- [release-1.33] fix: disk creation failure in AzureStack env by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3429

### 1.33.8

- [release-1.33] fix: ASH static provision segmentation fault by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3452
- [release-1.33] fix: let nodeExpandVolume retried if block device size is taking time to reflect in host by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3474

### 1.33.9

- [release-1.33] fix: Correct CSI-Provisioner permissions for VAC by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3496
- [release-1.33] test: fix trivy action failure by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3577

### 1.33.10

- fix: correct local uninstall command in v1.33.x install docs by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3594


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.33.10**, the newest release recorded here for this line.

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
