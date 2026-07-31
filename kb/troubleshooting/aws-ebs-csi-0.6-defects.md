---
id: TROUBLE-AWS_EBS_CSI_0_6_DEFECTS
type: troubleshooting
title: "aws-ebs-csi 0.6: defects fixed in the 0.6 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.6.0 <0.7.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - aws-ebs-csi 0.6 known issues
  - aws-ebs-csi 0.6 fixed in
  - is this aws-ebs-csi bug already fixed
tags:
  - troubleshooting
  - upgrade
  - aws-ebs-csi
sources:
  - type: docs
    path: kubernetes-sigs/aws-ebs-csi-driver release notes for the 0.6 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/aws-ebs-csi-driver/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# aws-ebs-csi 0.6: defects fixed in the 0.6 line

## Summary

**5 defects** the project fixed across **1 releases** of the 0.6 line, from 0.6.0 to
0.6.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.6.0

- Adding amd64 as nodeSelector to avoid arm64 archtectures (#471) ([#472](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/472), [@hugoprudente](https://github.com/hugoprudente))
- Fix e2e test ([#468](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/468), [@leakingtapan](https://github.com/leakingtapan))
- Correct golint warning ([#478](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/478), [@gliptak](https://github.com/gliptak))
- Fix migration test ([#500](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/500), [@leakingtapan](https://github.com/leakingtapan))
- Fixed resizing docs to refer the right path to example spec ([#504](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/504), [@amuraru](https://github.com/amuraru))


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.6.0**, the newest release recorded here for this line.

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
