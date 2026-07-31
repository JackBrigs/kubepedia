---
id: TROUBLE-AWS_EBS_CSI_1_3_DEFECTS
type: troubleshooting
title: "aws-ebs-csi 1.3: defects fixed in the 1.3 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.3.0 <1.4.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - aws-ebs-csi 1.3 known issues
  - aws-ebs-csi 1.3 fixed in
  - is this aws-ebs-csi bug already fixed
tags:
  - troubleshooting
  - upgrade
  - aws-ebs-csi
sources:
  - type: docs
    path: kubernetes-sigs/aws-ebs-csi-driver release notes for the 1.3 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/aws-ebs-csi-driver/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# aws-ebs-csi 1.3: defects fixed in the 1.3 line

## Summary

**6 defects** the project fixed across **1 releases** of the 1.3 line, from 1.3.0 to
1.3.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.3.0

- Fix windows build IsCorruptedMnt not implemented ([#1047](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/1047), [@wongma7](https://github.com/wongma7))
- Hash volume name to get client token ([#1041](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/1041), [@vdhanan](https://github.com/vdhanan))
- Include ClusterRole and ClusterRoleBinding for csi-node ([#1021](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/1021), [@groodt](https://github.com/groodt))
- Fix gcr prow builld failing because docker missing --os-version ([#1020](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/1020), [@wongma7](https://github.com/wongma7))
- Fix gcr prow build failing because of IMAGE variable collision ([#1017](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/1017), [@wongma7](https://github.com/wongma7))
- Fix github build failing because of wrong docker hub registry name ([#1016](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/1016), [@wongma7](https://github.com/wongma7))


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.3.0**, the newest release recorded here for this line.

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
