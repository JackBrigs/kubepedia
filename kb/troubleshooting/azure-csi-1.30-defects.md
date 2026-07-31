---
id: TROUBLE-AZURE_CSI_1_30_DEFECTS
type: troubleshooting
title: "azure-csi 1.30: defects fixed in the 1.30 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.30.0 <1.31.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - azure-csi 1.30 known issues
  - azure-csi 1.30 fixed in
  - is this azure-csi bug already fixed
tags:
  - troubleshooting
  - upgrade
  - azure-csi
sources:
  - type: docs
    path: kubernetes-sigs/azuredisk-csi-driver release notes for the 1.30 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/azuredisk-csi-driver/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# azure-csi 1.30: defects fixed in the 1.30 line

## Summary

**75 defects** the project fixed across **12 releases** of the 1.30 line, from 1.30.0 to
1.30.12. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.30.0

- fix: Ultra and PremiumV2 disk snapshot delay issue by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1953
- fix: increase snapshot timeout to 20min by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1979
- fix: allow resizing to min required size for performance plus disks by @RomanBednar in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1950
- fix: ensure Kubernets conformant format for location by @daniel-weisse in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1981
- cleanup: fix k8s.io/endpointslice dependency by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2014
- fix: v1.29.1.1-windows-hp image by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2060
- fix: improve disk attach/detach error message by @umagnus in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2093
- fix: avoid disk lun collision issue in edge case by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2089
- Chores:bump dependencies to fix cve by @MartinForReal in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2132

### 1.30.1

- [release-1.30] fix: ensure azure cloud config could be loaded from secret by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2204
- [release-1.30] fix: enable check-disk-lun-collision during disk attach by default by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2210
- [release-1.30] fix: use force detach as backoff when disk detach failed by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2216
- [release-1.30] fix: copy volume error in cross zone scenario by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2225
- [release-1.30] fix: Workload identity is not working. by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2236
- [release-1.30] fix: refine check disk lun collision logic by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2240
- [release-1.30] fix: allow special char in tag value by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2247
- [release-1.30] fix: enable http with track2 sdk by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2252
- [release-1.30] fix: vendor get zone panic fix by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2256
- [release-1.30] fix: stop attaching disk when get disk lun failed by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2262
- [release-1.30] fix: revert http-endpoint change on windows daemonset by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2266
- [release-1.30] fix: possible dead loop in GetVolumeStats on Windows by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2270
- [release-1.30] fix: cache GetVolumeStats on Windows node by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2274
- [release-1.30] fix: print error logs in NodeGetVolumeStats by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2282

### 1.30.2

- [release-1.30] fix: refine GetFreeSpace call on Windows by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2289
- [release-1.30] fix: use alternative driver name in used lun check by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2299
- [release-1.30] fix: liveness probe failure when hostNetwork not enabled in controller by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2317
- [release-1.30] test: fix stdlib CVE due to golang v1.22.2 by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2327
- [release-1.30] test: fix codespell error by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2346
- [release 1.30] fix shield guard on csi controller and node by @umagnus in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2363
- [release-1.30] fix: panic on Windows node when getFreeSpace failed on volume path by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2367
- [release-1.30] fix: add ReservedDataDiskSlotNum copy from DriverOptions to Driver struct by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2385
- [release-1.30] test: fix trivy action failure by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2390
- [release-1.30] fix: GHSA-xr7q-jx4m-x55m by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2401
- [release-1.30] fix: managed identity token refresh issue by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2405

### 1.30.3

- [release-1.30] fix: increase azuredisk container memory limits as 600Mi by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2423
- [release-1.30] fix: add pv patch permission with HonorPVReclaimPolicy enabled by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2440

### 1.30.4

- [release-1.30] fix: create snapshot failure in edge zone by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2451
- [release-1.30] fix: only enable removeNotReadyTaint on driver node daemonset by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2459
- [release-1.30] fix: checkDiskLun throttling issue by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2468
- [release-1.30] fix: upgrade csi-provisioner to v5.0.2 to fix pv deletion stuck issue by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2474

### 1.30.5

- [release-1.30] cleanup: upgrade golint version and fix golint errors by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2489
- [release-1.30] fix: resize failure when cloning a volume with bigger size on Windows by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2504
- [release-1.30] fix: increase liveness-probe timeout on Windows node by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2513
- [release-1.30] fix: upgrade node-driver-registrar to fix register timeout issue by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2511
- [release-1.30] fix: liveness probe failure when hostNetwork not enabled on linux node by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2525

### 1.30.6

- [release-1.30] fix: add CriticalAddonsOnly toleration into controller pod by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2566
- [release-1.30] fix: support attach operations after premiumV2 disk migration by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2572
- [release-1.30] fix: vm-type is not overriding as expected by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2581
- [release-1.30] test: fix trivy action by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2596
- [release-1.30] fix: add serial format limit to fix OOM issue when formatting a few disks in parallel in csi-azuredisk-node by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2623
- [release-1.30] fix: tagValueDelimiter parameter mismatch by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2627

### 1.30.7

- [release-1.30] fix: avoid duplicate ssl mounts on Redhat in AzureStack environment by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2666
- [release-1.30] fix: increase snapshot container memory limit by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2680
- [release-1.30] fix: update max data disk count table with v6 VM sku by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2684
- [release-1.30] fix: unmount volume issue on Windows node by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2695
- [release-1.30] fix: revert to go1.22 windows filesystem stdlib behavior by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2701
- [release-1.30] fix: allow more powershell command running at same time on Windows node by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2704
- [release-1.30] fix: increase azuredisk memory limit on node by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2707
- [release-1.30] fix: runOnControlPlane chart config by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2744
- [release-1.30] fix: resize is required after snapshot restore/volume clone on Windows by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2754
- [release-1.30] test: fix external e2e test failure by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2761
- [release-1.30] feat: add noformat option to fix fsck stuck issue on Linux node by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2756
- [release-1.30] fix: increase provisioner, resizer, snapshotter retry-interval-max by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2765
- [release-1.30] feat: add directmount option to fix fsck stuck issue on Linux node by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2769
- [release-1.30] fix: get disk stuck issue by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2785
- [release-1.30] test: fix pv deletion timeout by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2798

### 1.30.8

- [release-1.30] fix: remove duplicated imagePullSecrets deployment config by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2822
- [release-1.30] fix: set get disk timeout as 15s and make it configurable by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2863
- [release-1.30] fix: incorrect affinity chart config by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2867
- [release-1.30] fix: disable batch attach when hitting MaximumDataDisksExceeded error by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2890
- [release-1.30] fix: ignore GetDisk timeout during disk attach by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2896

### 1.30.10

- [release-1.30] fix: avoid duplicate ssl mounts on Fedora node in AzureStack environment by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2929
- [release-1.30] fix: avoid get disk call in disk creation by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2939

### 1.30.11

- [release-1.30] fix: detach disk should have more priority than attach disk on the same node by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2995

### 1.30.12

- [release-1.30] fix: adjust the batch size as per the number of disks allowed by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3077


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.30.12**, the newest release recorded here for this line.

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
