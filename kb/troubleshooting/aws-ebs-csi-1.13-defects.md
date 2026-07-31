---
id: TROUBLE-AWS_EBS_CSI_1_13_DEFECTS
type: troubleshooting
title: "aws-ebs-csi 1.13: defects fixed in the 1.13 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.13.0 <1.14.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - aws-ebs-csi 1.13 known issues
  - aws-ebs-csi 1.13 fixed in
  - is this aws-ebs-csi bug already fixed
tags:
  - troubleshooting
  - upgrade
  - aws-ebs-csi
sources:
  - type: docs
    path: kubernetes-sigs/aws-ebs-csi-driver release notes for the 1.13 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/aws-ebs-csi-driver/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# aws-ebs-csi 1.13: defects fixed in the 1.13 line

## Summary

**5 defects** the project fixed across **1 releases** of the 1.13 line, from 1.13.0 to
1.13.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.13.0

- Add version information from tag to GCR build ([#1426](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/1426), [@ConnorJC3](https://github.com/ConnorJC3))
- `pkg/driver/controller.go` uses ToLower ([#1429](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/1429), [@yevhenvolchenko](https://github.com/yevhenvolchenko))
- Increase cloudbuild timeout ([#1430](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/1430), [@torredil](https://github.com/torredil))
- Use `PULL_BASE_REF` for `VERSION` instead of `GIT_TAG` for GCR builds ([#1439](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/1439), [@ConnorJC3](https://github.com/ConnorJC3))
- Grab version via tag directly from git ([#1441](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/1441), [@ConnorJC3](https://github.com/ConnorJC3))


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.13.0**, the newest release recorded here for this line.

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
