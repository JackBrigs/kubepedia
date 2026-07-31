---
id: TROUBLE-AWS_EBS_CSI_1_0_DEFECTS
type: troubleshooting
title: "aws-ebs-csi 1.0: defects fixed in the 1.0 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.0.0 <1.1.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - aws-ebs-csi 1.0 known issues
  - aws-ebs-csi 1.0 fixed in
  - is this aws-ebs-csi bug already fixed
tags:
  - troubleshooting
  - upgrade
  - aws-ebs-csi
sources:
  - type: docs
    path: kubernetes-sigs/aws-ebs-csi-driver release notes for the 1.0 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/aws-ebs-csi-driver/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# aws-ebs-csi 1.0: defects fixed in the 1.0 line

## Summary

**6 defects** the project fixed across **1 releases** of the 1.0 line, from 1.0.0 to
1.0.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.0.0

- Resize filesystem when restore a snapshot to larger size volume ([#753](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/753), [@AndyXiangLi](https://github.com/AndyXiangLi))
- handling describe instances consistency issue ([#801](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/801), [@vdhanan](https://github.com/vdhanan))
- Cap IOPS when calculating from iopsPerGB ([#809](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/809), [@jsafrane](https://github.com/jsafrane))
- Fix broken gomocks ([#843](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/843), [@wongma7](https://github.com/wongma7))
- Fix missing import ([#849](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/849), [@wongma7](https://github.com/wongma7))
- instance metadata issue fix ([#855](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/855), [@vdhanan](https://github.com/vdhanan))


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.0.0**, the newest release recorded here for this line.

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
