---
id: TROUBLE-AZURE_CSI_1_26_DEFECTS
type: troubleshooting
title: "azure-csi 1.26: defects fixed in the 1.26 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.26.0 <1.27.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - azure-csi 1.26 known issues
  - azure-csi 1.26 fixed in
  - is this azure-csi bug already fixed
tags:
  - troubleshooting
  - upgrade
  - azure-csi
sources:
  - type: docs
    path: kubernetes-sigs/azuredisk-csi-driver release notes for the 1.26 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/azuredisk-csi-driver/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# azure-csi 1.26: defects fixed in the 1.26 line

## Summary

**23 defects** the project fixed across **7 releases** of the 1.26 line, from 1.26.0 to
1.26.9. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.26.0

- fix: volume metrics on Windows csi-proxy v1beta by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1622
- fix: add disk lun check in VMSSFlex AttachDisk to avoid race condition by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1632
- fix: race condition in VMSS cache update by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1639
- fix: Add missing machine in SKU listings by @sboulkour in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1641
- Add requirements.txt with fixed versions to use in pip install by @mauriciopoppe in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1652
- fix e2e: disable podSecurity by @cvvz in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1668
- Revert "fix e2e: disable podSecurity" by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1669
- fix: set ForceAttemptHTTP2 as false to increase ARM throttling limit by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1676

### 1.26.1

- fix: update rather than replace existing cache entry by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1686

### 1.26.2

- fix: panic when allow-empty-cloud-config is set by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1699

### 1.26.3

- [release-1.26] fix: buildx issue with provenance disabled by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1745
- [release-1.26] fix: second expand volume failure on Ubuntu 22.04 by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1743
- [release-1.26] tes: fix golint action failure by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1749
- [release-1.26] fix: detach disk failure when there is throttling by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1758
- [release-1.26] fix: PremiumV2_LRS caching mode issue by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1794

### 1.26.4

- [release-1.26] test: fix external e2e test failure by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1812
- [release-1.26] fix: switch base image to fix CVEs by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1811
- [release-1.26] test: fix snapshot test failure by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1834

### 1.26.7

- [release-1.26] fix: ensure Kubernets conformant format for location by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1990
- [release-1.26] test: fix verify-helm-chart failure by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2005
- [release-1.26] doc: fix code spelling errors by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2006

### 1.26.9

- [release-1.26] test: fix multi-zone test failure on capz multi-zone cluster by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2102
- [release-1.26] fix: improve disk attach/detach error message by @umagnus in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/2104


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.26.9**, the newest release recorded here for this line.

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
