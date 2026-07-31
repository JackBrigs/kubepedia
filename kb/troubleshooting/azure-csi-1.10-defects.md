---
id: TROUBLE-AZURE_CSI_1_10_DEFECTS
type: troubleshooting
title: "azure-csi 1.10: defects fixed in the 1.10 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.10.0 <1.11.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - azure-csi 1.10 known issues
  - azure-csi 1.10 fixed in
  - is this azure-csi bug already fixed
tags:
  - troubleshooting
  - upgrade
  - azure-csi
sources:
  - type: docs
    path: kubernetes-sigs/azuredisk-csi-driver release notes for the 1.10 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/azuredisk-csi-driver/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# azure-csi 1.10: defects fixed in the 1.10 line

## Summary

**9 defects** the project fixed across **1 releases** of the 1.10 line, from 1.10.0 to
1.10.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.10.0

- fix: arm64 image build by @mainred in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1048
- fix: install updated packages to fix CVE issues by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1055
- fix: missing static PV data in VolumeAttachments by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1062
- fix: increase registrar container cpu limit by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1065
- fix: snapshot throttling issue by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1066
- fix: increase registrar probe timeout value on Windows by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1068
- fix: upgrade azure lib to fix panic issue on node driver by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1081
- fix: update v1.9.0 chart file by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1103
- fix: detach disk should return error when throttled by @andyzhangx in https://github.com/kubernetes-sigs/azuredisk-csi-driver/pull/1105


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.10.0**, the newest release recorded here for this line.

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
