---
id: TROUBLE-AZURE_CSI_1_31_DEFECTS
type: troubleshooting
title: "azure-csi 1.31: defects fixed in the 1.31 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.31.0 <1.32.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - azure-csi 1.31 known issues
  - azure-csi 1.31 fixed in
  - is this azure-csi bug already fixed
tags:
  - troubleshooting
  - upgrade
  - azure-csi
sources:
  - type: docs
    path: kubernetes-sigs/azuredisk-csi-driver release notes for the 1.31 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/azuredisk-csi-driver/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# azure-csi 1.31: defects fixed in the 1.31 line

## Summary

**83 defects** the project fixed across **13 releases** of the 1.31 line, from 1.31.0 to
1.31.12. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.31.0

- fix: ensure azure cloud config could be loaded from secret by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2202
- fix: enable check-disk-lun-collision during disk attach by default by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2208
- fix: use force detach as backoff when disk detach failed by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2211
- fix: copy volume error in cross zone scenario by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2223
- fix: Workload identity is not working. by @cvvz in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2233
- fix: refine check disk lun collision logic by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2239
- fix: allow special char in tag value by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2246
- fix: vendor get zone panic fix by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2249
- fix: stop attaching disk when get disk lun failed by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2260
- fix: possible dead loop in GetVolumeStats on Windows by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2267
- fix: cache GetVolumeStats on Windows node by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2273
- fix: print error logs in NodeGetVolumeStats by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2279
- fix: refine GetFreeSpace call on Windows by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2287
- fix: use alternative driver name in used lun check by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2298
- fix: liveness probe failure when hostNetwork not enabled in controller by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2315
- fix: broken chart index by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2316
- fix: shield guard issues on node by @umagnus in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2358
- fix: shield guard issues by @umagnus in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2354
- fix: panic on Windows node when getFreeSpace failed on volume path by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2366
- fix: shield guard issue on windows node hostprocess initContainer by @umagnus in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2364
- fix: add ReservedDataDiskSlotNum copy from DriverOptions to Driver struct by @ClementLachaussee in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2384
- fix: reservedDataDiskSlotNum chart setting in v1.29.7 by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2399
- fix: GHSA-xr7q-jx4m-x55m by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2400
- fix: managed identity token refresh issue by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2404
- fix: increase azuredisk container memory limits as 600Mi by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2422
- fix: add pv patch permission with HonorPVReclaimPolicy enabled by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2439
- fix: create snapshot failure in edge zone by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2450
- fix: only enable removeNotReadyTaint on driver node daemonset by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2456
- fix: checkDiskLun throttling issue by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2461
- fix: upgrade csi-provisioner to v5.0.2 to fix pv deletion stuck issue by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2472
- fix: upgrade csi-provisioner to v5.0.2 to fix pv deletion stuck issue on v1.30.3, v1.29.8 charts by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2476
- cleanup: upgrade golint version and fix golint errors by @Zhupku in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2487
- fix: increase liveness-probe timeout on Windows node by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2488
- fix: resize failure when cloning a volume with bigger size on Windows by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2503
- fix: upgrade node-driver-registrar to fix register timeout issue by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2510
- fix: liveness probe failure when hostNetwork not enabled on linux node by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2521

### 1.31.1

- [release-1.31] fix: add CriticalAddonsOnly toleration into controller pod by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2565
- [release-1.31] fix: support attach operations after premiumV2 disk migration by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2571
- [release-1.31] fix: vm-type is not overriding as expected by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2580
- [release-1.31] test: fix trivy action by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2595
- [release-1.31] fix: support old api version for Azure Stack Hub by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2621
- [release-1.31] fix: add serial format limit to fix OOM issue when formatting a few disks in parallel in csi-azuredisk-node by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2622
- [release-1.31] fix: tagValueDelimiter parameter mismatch by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2626

### 1.31.2

- [release-1.31] fix: avoid duplicate ssl mounts on Redhat in AzureStack environment by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2665
- [release-1.31] fix: increase snapshot container memory limit by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2678
- [release-1.31] fix: update max data disk count table with v6 VM sku by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2683
- [release-1.31] fix: support disk discovery on Windows Gen2 and v6 VM sku by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2686
- [release-1.31] fix: unmount volume issue on Windows node by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2693
- [release-1.31] fix: revert to go1.22 windows filesystem stdlib behavior by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2700
- [release-1.31] fix: allow more powershell command running at same time on Windows node by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2703
- [release-1.31] fix: increase azuredisk memory limit on node by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2706
- [release-1.31] fix: resize is required after snapshot restore/volume clone on Windows by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2734
- [release-1.31] fix: ModifyVolume interface parameter check by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2741
- [release-1.31] fix: runOnControlPlane chart config by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2743
- [release-1.31] test: fix external e2e test failure by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2759
- [release-1.31] feat: add noformat option to fix fsck stuck issue by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2755
- [release-1.31] fix: increase provisioner, resizer, snapshotter retry-interval-max by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2764
- [release-1.31] feat: add directmount option to fix fsck stuck issue on Linux node by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2768
- [release-1.31] fix: get disk stuck issue by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2784
- [release-1.31] test: fix pv deletion timeout by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2797

### 1.31.3

- [release-1.31] fix: remove duplicated imagePullSecrets deployment config by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2821
- [release-1.31] fix: upgrade azure cloud provider lib to fix AzureStack env setting issue on AKS by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2831

### 1.31.4

- [release-1.31] fix: set get disk timeout as 15s and make it configurable by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2861
- [release-1.31] fix: incorrect affinity chart config by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2866
- [release-1.31] fix: obsolete vmss cache issue after disk is resized successfully by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2870
- [release-1.31] fix: disable batch attach when hitting MaximumDataDisksExceeded error by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2889
- [release-1.31] fix: ignore GetDisk timeout during disk attach by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2895

### 1.31.5

- [release-1.31] chore: upgrade Azure cloud provider lib to fix azclient timeout setting issue by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2904
- [release-1.31] fix: merge mutable parameters for disk creation to support ModifyVolume changes by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2914
- [release-1.31] fix: storageEndpoint issue in sovereign cloud by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2917

### 1.31.6

- [release-1.31] fix: avoid duplicate ssl mounts on Fedora node in AzureStack environment by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2928
- [release-1.31] fix: avoid get disk call in disk creation by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2938
- [release-1.31] fix: reduce get disk calls in disk attach/detach on VMSS by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2943

### 1.31.7

- [release-1.31] fix: increase TaintRemovalInitialDelay as 30s by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2981
- [release-1.31] fix: detach disk should have more priority than attach disk on the same node by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2994

### 1.31.8

- [release-1.31] fix: incorrect disk num discovery on Windows 2019 node by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3041

### 1.31.9

- [release-1.31] fix: adjust the batch size as per the number of disks allowed by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3075

### 1.31.10

- [release-1.31] fix: vmss flex node naming parsing issue by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3096

### 1.31.11

- [release-1.31] test: fix golint errors by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3139
- [release-1.31] fix: xfs mount failure on Azure Linux 3.0 node by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3177
- [release-1.31] chore: fix helm chart index on release-1.31 by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3187

### 1.31.12

- [release-1.31] test: fix helm install by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3301
- [release-1.31] fix: ZRS disk should support 4 zones by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3312


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.31.12**, the newest release recorded here for this line.

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
