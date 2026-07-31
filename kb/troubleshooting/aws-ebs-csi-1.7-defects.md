---
id: TROUBLE-AWS_EBS_CSI_1_7_DEFECTS
type: troubleshooting
title: "aws-ebs-csi 1.7: defects fixed in the 1.7 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.7.0 <1.8.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - aws-ebs-csi 1.7 known issues
  - aws-ebs-csi 1.7 fixed in
  - is this aws-ebs-csi bug already fixed
tags:
  - troubleshooting
  - upgrade
  - aws-ebs-csi
sources:
  - type: docs
    path: kubernetes-sigs/aws-ebs-csi-driver release notes for the 1.7 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/aws-ebs-csi-driver/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# aws-ebs-csi 1.7: defects fixed in the 1.7 line

## Summary

**6 defects** the project fixed across **1 releases** of the 1.7 line, from 1.7.0 to
1.7.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.7.0

- Set handle-volume-inuse-error to false which fixes csi-resizer getting OOMKilled ([#1280](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/1280), [@stijndehaes](https://github.com/stijndehaes))
- Fix unable to create CSI snapshot-EBS csi driver ([#1257](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/1257), [@torredil](https://github.com/torredil))
- Temporarily fix CI ([#1240](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/1240), [@torredil](https://github.com/torredil))
- Fix IOPS parameter bug when no volume type is defined ([#1236](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/1236), [@torredil](https://github.com/torredil))
- Add quotes around the extra-tags argument in chart template ([#1198](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/1198), [@Kaezon](https://github.com/Kaezon))
- Avoid git tag conflicts when vendoring hack/e2e in other repos (efs/fsx) ([#1270](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/1270), [@wongma7](https://github.com/wongma7))


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.7.0**, the newest release recorded here for this line.

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
