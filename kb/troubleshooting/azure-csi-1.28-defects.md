---
id: TROUBLE-AZURE_CSI_1_28_DEFECTS
type: troubleshooting
title: "azure-csi 1.28: defects fixed in the 1.28 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.28.0 <1.29.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - azure-csi 1.28 known issues
  - azure-csi 1.28 fixed in
  - is this azure-csi bug already fixed
tags:
  - troubleshooting
  - upgrade
  - azure-csi
sources:
  - type: docs
    path: kubernetes-sigs/azuredisk-csi-driver release notes for the 1.28 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/azuredisk-csi-driver/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# azure-csi 1.28: defects fixed in the 1.28 line

## Summary

**39 defects** the project fixed across **13 releases** of the 1.28 line, from 1.28.0 to
1.28.12. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.28.0

- tes: fix golint action failure by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1748
- fix: detach disk failure when there is throttling by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1755
- fix: PremiumV2_LRS caching mode issue by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1790
- fix: add securityContext.seccompProfile for driver controller by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1805
- fix: make sure the VolumeSnapshots v1 CRDs exist before starting by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1851

### 1.28.1

- [release-1.28] fix: missing log when IMDS is not available on windows node by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1888
- [release-1.28] fix: PerformancePlus setting issue by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1895

### 1.28.2

- [release-1.28] fix: cloned volume could not be recognized on Windows node when source volume is mounted on the same node by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1914

### 1.28.3

- [release-1.28] fix: remove cross region snapshot copy 5s delay by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1941
- [release-1.28] fix: use env var in powershell cmdlet by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1942

### 1.28.4

- [release-1.28] fix: increase snapshot timeout to 20min by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1983
- [release-1.28] fix: Ultra and PremiumV2 disk snapshot delay issue by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1984
- [release-1.28] fix: allow resizing to min required size for performance plus disks by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1987
- [release-1.28] fix: ensure Kubernets conformant format for location by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1989
- [release-1.28] doc: fix code spelling errors by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1997
- [release-1.28] fix: upgrade mount-utils lib by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1993
- [release-1.28] test: fix verify-helm-chart failure by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2003

### 1.28.5

- [release-1.28]chore: fix google.golang.org/grpc GHSA-m425-mq94-257g by @cvvz in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2030

### 1.28.6

- [release-1.28] test: fix multi-zone test failure on capz multi-zone cluster by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2100
- [release-1.28] fix: improve disk attach/detach error message by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2097
- [release-1.28] test: fix windows volume cloning test failure by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2110

### 1.28.7

- [release-1.28] test: fix goveralls by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2182
- [release-1.28] fix: cache GetVolumeStats on Windows node by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2276

### 1.28.8

- [release-1.28] fix: print error logs in NodeGetVolumeStats by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2281
- [release-1.28] fix: refine GetFreeSpace call on Windows by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2291
- [release-1.28] fix: liveness probe failure when hostNetwork not enabled in controller by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2319
- [release-1.28] test: fix stdlib CVE due to golang v1.22.2 by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2329

### 1.28.9

- [release-1.28] test: fix codespell error by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2348
- [release 1.28] fix shield guard on csi controller and node by @umagnus in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2360
- [release-1.28] fix: panic on Windows node when getFreeSpace failed on volume path by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2369

### 1.28.10

- [release-1.28] test: fix trivy action failure by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2392
- [release-1.28] fix: GHSA-xr7q-jx4m-x55m by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2403
- [release-1.28] fix: increase azuredisk container memory limits as 600Mi by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2425

### 1.28.11

- [release-1.28] fix: create snapshot failure in edge zone by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2454
- [release-1.28] fix: resize failure when cloning a volume with bigger size on Windows by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2506
- [release-1.28] cleanup: upgrade golint version and fix golint errors by @umagnus in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2507
- [release-1.28] fix: increase liveness-probe timeout on Windows node by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2515
- [release-1.28] fix golint and disable staticcheck by @umagnus in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2522

### 1.28.12

- [release-1.28] test: fix trivy action by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2598


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.28.12**, the newest release recorded here for this line.

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
