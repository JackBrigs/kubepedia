---
id: TROUBLE-AWS_EBS_CSI_1_30_DEFECTS
type: troubleshooting
title: "aws-ebs-csi 1.30: defects fixed in the 1.30 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.30.0 <1.31.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - aws-ebs-csi 1.30 known issues
  - aws-ebs-csi 1.30 fixed in
  - is this aws-ebs-csi bug already fixed
tags:
  - troubleshooting
  - upgrade
  - aws-ebs-csi
sources:
  - type: docs
    path: kubernetes-sigs/aws-ebs-csi-driver release notes for the 1.30 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/aws-ebs-csi-driver/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# aws-ebs-csi 1.30: defects fixed in the 1.30 line

## Summary

**6 defects** the project fixed across **1 releases** of the 1.30 line, from 1.30.0 to
1.30.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.30.0

- Remove DeleteDisk call in CreateDisk path ([#2009](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/2009), [@ConnorJC3](https://github.com/ConnorJC3))
- Consolidate request handling in RecordRequestsMiddleware ([#2013](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/2013), [@torredil](https://github.com/torredil))
- Run taint removal only if Kubernetes API is available ([#2015](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/2015), [@torredil](https://github.com/torredil))
- Fix CVE G0-2024-2687 by bumping go and /x/net dependencies ([#1996](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/1996), [@AndrewSirenko](https://github.com/AndrewSirenko))
- Fix relationship between node service and mounter interface ([#1997](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/1997), [@torredil](https://github.com/torredil))
- Fix DeleteSnapshot error message ([#2000](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/2000), [@AndrewSirenko](https://github.com/AndrewSirenko))


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.30.0**, the newest release recorded here for this line.

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
