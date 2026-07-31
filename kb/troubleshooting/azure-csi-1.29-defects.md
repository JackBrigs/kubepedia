---
id: TROUBLE-AZURE_CSI_1_29_DEFECTS
type: troubleshooting
title: "azure-csi 1.29: defects fixed in the 1.29 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.29.0 <1.30.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - azure-csi 1.29 known issues
  - azure-csi 1.29 fixed in
  - is this azure-csi bug already fixed
tags:
  - troubleshooting
  - upgrade
  - azure-csi
sources:
  - type: docs
    path: kubernetes-sigs/azuredisk-csi-driver release notes for the 1.29 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/azuredisk-csi-driver/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# azure-csi 1.29: defects fixed in the 1.29 line

## Summary

**64 defects** the project fixed across **14 releases** of the 1.29 line, from 1.29.0 to
1.29.13. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.29.0

- fix: missing log when IMDS is not available on windows node by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1885
- fix: PerformancePlus setting issue by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1894
- fix: cloned volume could not be recognized on Windows node when source volume is mounted on the same node by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1909
- fix: remove cross region snapshot copy 5s delay by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1938
- fix: use env var in powershell cmdlet by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1939

### 1.29.1

- [release-1.29] fix: Ultra and PremiumV2 disk snapshot delay issue by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1980
- [release-1.29] fix: increase snapshot timeout to 20min by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1982
- [release-1.29] fix: allow resizing to min required size for performance plus disks by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1986
- [release-1.29] fix: ensure Kubernets conformant format for location by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1988
- [release-1.29] doc: fix code spelling errors by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1996
- [release-1.29] test: fix verify-helm-chart failure by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2002

### 1.29.2

- [release-1.29]chore: fix google.golang.org/grpc GHSA-m425-mq94-257g by @cvvz in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2029
- [release-1.29] fix: v1.29.1.1-windows-hp image by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2061

### 1.29.3

- [release-1.29] test: fix multi-zone test failure on capz multi-zone cluster by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2099
- [release-1.29] fix: improve disk attach/detach error message by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2096
- [release-1.29] test: fix windows volume cloning test failure by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2109
- [release-1.29] fix: avoid disk lun collision issue in edge case by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2117

### 1.29.4

- cleanup: fix k8s.io/endpointslice dependency by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2167
- [release-1.29] test: fix goveralls by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2181
- [release-1.29] fix: ensure azure cloud config could be loaded from secret by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2205
- [release-1.29] fix: Workload identity is not working. by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2237
- [release-1.29] fix: enable check-disk-lun-collision during disk attach by default by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2241
- [release-1.29] fix: refine check disk lun collision logic by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2242

### 1.29.5

- [release-1.29] fix: allow special char in tag value by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2248
- [release-1.29] fix: stop attaching disk when get disk lun failed by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2263
- [release-1.29] fix: possible dead loop in GetVolumeStats on Windows by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2271
- [release-1.29] fix: cache GetVolumeStats on Windows node by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2275
- [release-1.29] fix: print error logs in NodeGetVolumeStats by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2280

### 1.29.6

- [release-1.29] fix: refine GetFreeSpace call on Windows by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2290
- [release-1.29] fix: use alternative driver name in used lun check by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2300
- [release-1.29] fix: liveness probe failure when hostNetwork not enabled in controller by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2318
- [release-1.29] test: fix stdlib CVE due to golang v1.22.2 by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2328

### 1.29.7

- [release-1.29] test: fix codespell error by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2347
- [release 1.29] fix shield guard on csi controller and node by @umagnus in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2362
- [release-1.29] fix: panic on Windows node when getFreeSpace failed on volume path by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2368

### 1.29.8

- [release-1.29] test: fix trivy action failure by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2391
- [release-1.29] fix: GHSA-xr7q-jx4m-x55m by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2402
- [release-1.29] fix: increase azuredisk container memory limits as 600Mi by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2424
- [release-1.29] fix: add pv patch permission with HonorPVReclaimPolicy enabled by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2441

### 1.29.9

- [release-1.29] fix: create snapshot failure in edge zone by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2453
- [release-1.29] fix: checkDiskLun throttling issue by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2469
- [release-1.30] fix: upgrade csi-provisioner to v5.0.2 to fix pv deletion stuck issue by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2475

### 1.29.10

- [release-1.29] fix: resize failure when cloning a volume with bigger size on Windows by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2505
- [release-1.29] cleanup: upgrade golint version and fix golint errors by @umagnus in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2508
- [release-1.29] fix: upgrade node-driver-registrar to fix register timeout issue by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2512
- [release-1.29] fix: increase liveness-probe timeout on Windows node by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2514
- [release-1.29] fix golint and disable staticcheck by @umagnus in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2523
- [release-1.29] fix: liveness probe failure when hostNetwork not enabled on linux node by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2526

### 1.29.11

- [release-1.29] fix: add CriticalAddonsOnly toleration into controller pod by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2567
- [release-1.29] test: fix trivy action by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2597
- [release-1.29] fix: tagValueDelimiter parameter mismatch by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2628

### 1.29.12

- [release-1.29] fix: avoid duplicate ssl mounts on Redhat in AzureStack environment by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2667
- [release-1.29] fix: increase snapshot container memory limit by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2681
- [release-1.29] fix: update max data disk count table with v6 VM sku by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2685
- [release-1.29] fix: unmount volume issue on Windows node by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2696
- [release-1.29] fix: revert to go1.22 windows filesystem stdlib behavior by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2702
- [release-1.29] fix: increase azuredisk memory limit on node by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2708
- [release-1.29] fix: allow more powershell command running at same time on Windows node by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2711
- [release-1.29] test: fix external e2e test failure by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2760
- [release-1.29] feat: add noformat option to fix fsck stuck issue on Linux node by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2757
- [release-1.29] feat: add directmount option to fix fsck stuck issue on Linux node by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2770
- [release-1.29] fix: get disk stuck issue by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2786
- [release-1.29] test: fix pv deletion timeout by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2799

### 1.29.13

- [release-1.29] fix: remove duplicated imagePullSecrets deployment config by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2823


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.29.13**, the newest release recorded here for this line.

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
