---
id: TROUBLE-AWS_EBS_CSI_1_2_DEFECTS
type: troubleshooting
title: "aws-ebs-csi 1.2: defects fixed in the 1.2 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.2.0 <1.3.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - aws-ebs-csi 1.2 known issues
  - aws-ebs-csi 1.2 fixed in
  - is this aws-ebs-csi bug already fixed
tags:
  - troubleshooting
  - upgrade
  - aws-ebs-csi
sources:
  - type: docs
    path: kubernetes-sigs/aws-ebs-csi-driver release notes for the 1.2 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/aws-ebs-csi-driver/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# aws-ebs-csi 1.2: defects fixed in the 1.2 line

## Summary

**5 defects** the project fixed across **2 releases** of the 1.2 line, from 1.2.0 to
1.2.1. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.2.0

- Default extra-create-metadata true so that volumes get created with pvc/pv tags ([#937](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/937), [@wongma7](https://github.com/wongma7))
- Default controller.extra-create-metadata true so that volumes get created with pvc/pv tags ([#941](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/941), [@wongma7](https://github.com/wongma7))
- Fix podLabels case in Helm chart ([#925](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/925), [@eytanhanig](https://github.com/eytanhanig))
- Download fixed version of eksctl to avoid bugs ([#967](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/967), [@wongma7](https://github.com/wongma7))

### 1.2.1

- Fix mount idempotency ([#1019](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/1019), [@nirmalaagash](https://github.com/nirmalaagash))


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.2.1**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `kubernetes-sigs/aws-ebs-csi-driver`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/aws-ebs-csi.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
