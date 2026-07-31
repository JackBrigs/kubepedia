---
id: TROUBLE-AWS_EBS_CSI_1_22_DEFECTS
type: troubleshooting
title: "aws-ebs-csi 1.22: defects fixed in the 1.22 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.22.0 <1.23.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - aws-ebs-csi 1.22 known issues
  - aws-ebs-csi 1.22 fixed in
  - is this aws-ebs-csi bug already fixed
tags:
  - troubleshooting
  - upgrade
  - aws-ebs-csi
sources:
  - type: docs
    path: kubernetes-sigs/aws-ebs-csi-driver release notes for the 1.22 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/aws-ebs-csi-driver/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# aws-ebs-csi 1.22: defects fixed in the 1.22 line

## Summary

**5 defects** the project fixed across **2 releases** of the 1.22 line, from 1.22.0 to
1.22.1. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.22.0

- Correct volume limits for i4i instance types ([#1699](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/1699), [@talnevo](https://github.com/talnevo))
- Use SSM to get latest stable AMI for EC2 nodes ([#1689](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/1689), [@torredil](https://github.com/torredil))
- Add `i4i.large` to volume limits config ([#1715](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/1715), [@torredil](https://github.com/torredil))

### 1.22.1

- Cherry-pick from v1.23.1: Do not call ModifyVolume if the volume is already in the desired state ([#1741](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/1741), [@ConnorJC3](https://github.com/ConnorJC3))
- Upgrade volume-modifier-for-k8s sidecar to 0.1.3 for Leader election conflict with csi-resizer bug fix ([#14](https://github.com/awslabs/volume-modifier-for-k8s/pull/14), [@torredil](https://github.com/torredil))


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.22.1**, the newest release recorded here for this line.

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
