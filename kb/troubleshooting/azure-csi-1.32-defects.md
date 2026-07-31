---
id: TROUBLE-AZURE_CSI_1_32_DEFECTS
type: troubleshooting
title: "azure-csi 1.32: defects fixed in the 1.32 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.32.0 <1.33.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - azure-csi 1.32 known issues
  - azure-csi 1.32 fixed in
  - is this azure-csi bug already fixed
tags:
  - troubleshooting
  - upgrade
  - azure-csi
sources:
  - type: docs
    path: kubernetes-sigs/azuredisk-csi-driver release notes for the 1.32 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/azuredisk-csi-driver/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# azure-csi 1.32: defects fixed in the 1.32 line

## Summary

**68 defects** the project fixed across **11 releases** of the 1.32 line, from 1.32.0 to
1.32.12. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.32.0

- fix: add CriticalAddonsOnly toleration into controller pod by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2560
- fix: support attach operations after premiumV2 disk migration by @landreasyan in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2569
- fix: vm-type is not overriding as expected by @umagnus in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2578
- test: fix trivy action by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2594
- fix: support old api version for Azure Stack Hub by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2617
- fix: add serial format limit to fix OOM issue when formatting a few disks in parallel in csi-azuredisk-node by @umagnus in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2616
- fix: tagValueDelimiter parameter mismatch by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2624
- fix: avoid duplicate ssl mounts on Redhat in AzureStack environment by @gulywwx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2663
- fix: avoid duplicate ssl mounts on Redhat in AzureStack in chart config by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2668
- fix: increase snapshot container memory limit by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2677
- fix: update max data disk count table with v6 VM sku by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2682
- fix: support disk discovery on Windows Gen2 and v6 VM sku by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2671
- fix: unmount volume issue on Windows node by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2691
- chore: update cloud provider lib with UserAgent fix by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2689
- test: fix building latest-windows-hp tag by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2698
- fix: revert to go1.22 windows filesystem stdlib behavior by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2692
- fix: allow more powershell command running at same time on Windows node by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2699
- fix: increase azuredisk memory limit on node by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2705
- fix: resize is required after snapshot restore/volume clone on Windows by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2733
- fix: ModifyVolume interface parameter check by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2739
- fix: runOnControlPlane chart config by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2742
- feat: add noformat option to fix fsck stuck issue on Linux node by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2751
- test: fix external e2e test failure by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2758
- fix: increase provisioner, resizer, snapshotter retry-interval-max by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2763
- feat: add directmount option to fix fsck stuck issue on Linux node by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2766
- fix: get disk stuck issue by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2783
- test: fix pv deletion timeout by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2796
- fix: wrong node matching when detaching dangling disk by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2812
- Revert "fix: wrong node matching when detaching dangling disk" by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2815
- fix: remove duplicated imagePullSecrets deployment config by @adriananeci in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2819
- doc: fix chart README doc by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2829
- fix: set get disk timeout as 15s and make it configurable by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2857
- fix: issue #2858 incorrect controller.affinity property processing by @olegch in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2859
- fix: obsolete vmss cache issue after disk is resized successfully by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2865
- fix: disable batch attach when hitting MaximumDataDisksExceeded error by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2883
- fix: ignore GetDisk timeout during disk attach by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2894
- fix: incorrect cloud provider setting in sovereign cloud by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2911
- fix: merge mutable parameters for disk creation to support ModifyVolume changes by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2913
- fix: Merge mutable parameters for disk creation by @antoine-gaillard in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2910
- fix: storageEndpoint issue in sovereign cloud by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2916

### 1.32.1

- [release-1.32] fix: avoid duplicate ssl mounts on Fedora node in AzureStack environment by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2927
- [release-1.32] fix: avoid get disk call in disk creation by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2935
- [release-1.32] fix: reduce get disk calls in disk attach/detach on VMSS by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2942
- [release-1.32] fix: merge OTEL metrics with legacy registerer by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2951

### 1.32.2

- [release-1.32] fix: increase TaintRemovalInitialDelay as 30s by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2978
- [release-1.32] fix: detach disk should have more priority than attach disk on the same node by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2993

### 1.32.3

- [release-1.32] fix: panic for GetZoneByNodeName on Azure Stack by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3018
- [release-1.32] fix: remove unnecessary get vmss call during disk attach by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3024
- [release-1.32] fix: decrease poller delay in AzureClient as 5s by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3035

### 1.32.4

- [release-1.32] fix: incorrect disk num discovery on Windows 2019 node by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3040

### 1.32.5

- [release-1.32] fix: disk detach failure on AzureStack Hub by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3048
- [release-1.32] doc: fix snapshot crd illegal characters by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3066
- [release-1.32] fix: adjust the batch size as per the number of disks allowed by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3073

### 1.32.6

- [release-1.32] fix: vmss flex node naming parsing issue by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3095

### 1.32.8

- [release-1.32] fix: make disk and snapshot uri regex case insensitive everywhere by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3152
- [release-1.32] fix: xfs mount failure on Azure Linux 3.0 node by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3176
- [release-1.32] fix: helm chart index on release-1.32 by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3186

### 1.32.9

- [release-1.32] fix: batching implementation should allow for an early exit for disks already processed in the batch by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3212

### 1.32.11

- [release-1.32] test: fix helm install by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3300
- [release-1.32] fix: China cloud endpoints by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3306
- [release-1.32] fix: ZRS disk should support 4 zones by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3311
- [release-1.32] fix: detach call should not use the full context deadline by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3335

### 1.32.12

- [release-1.32] test: fix govet error by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3360
- [release-1.32] fix: disable enable-minimum-retry-after by default by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3363
- [release-1.32] test: fix sanity test failure by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3368
- [release-1.32] Revert "fix: disable enable-minimum-retry-after by default" by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3372
- [release-1.32] fix: ASH static provision segmentation fault by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3453
- [release-1.32] fix: create volume failure when requested pvc size is smaller than snapshot disk size by @priyansh17 in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/3401


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.32.12**, the newest release recorded here for this line.

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
