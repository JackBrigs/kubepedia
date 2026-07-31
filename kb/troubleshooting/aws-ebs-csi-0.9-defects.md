---
id: TROUBLE-AWS_EBS_CSI_0_9_DEFECTS
type: troubleshooting
title: "aws-ebs-csi 0.9: defects fixed in the 0.9 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.9.0 <0.10.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - aws-ebs-csi 0.9 known issues
  - aws-ebs-csi 0.9 fixed in
  - is this aws-ebs-csi bug already fixed
tags:
  - troubleshooting
  - upgrade
  - aws-ebs-csi
sources:
  - type: docs
    path: kubernetes-sigs/aws-ebs-csi-driver release notes for the 0.9 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/aws-ebs-csi-driver/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# aws-ebs-csi 0.9: defects fixed in the 0.9 line

## Summary

**5 defects** the project fixed across **2 releases** of the 0.9 line, from 0.9.0 to
0.9.1. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.9.0

- Fix outdated ecr login command ([#680](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/680), [@wongma7](https://github.com/wongma7))
- Fix overlays not being updated for gcr migration ([#649](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/649), [@wongma7](https://github.com/wongma7))
- (Try to) fix cloudbuild ([#659](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/659), [@wongma7](https://github.com/wongma7))
- Fix stray argument in cloudbuild.yaml ([#661](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/661), [@wongma7](https://github.com/wongma7))

### 0.9.1

- delete leaked volume if driver don't know the volume status ([#771](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/771), [@AndyXiangLi](https://github.com/AndyXiangLi))


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.9.1**, the newest release recorded here for this line.

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
