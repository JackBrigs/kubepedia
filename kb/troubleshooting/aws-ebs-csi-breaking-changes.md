---
id: TROUBLE-AWS_EBS_CSI_BREAKING_CHANGES
type: troubleshooting
title: "aws-ebs-csi: declared breaking changes by release"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.2.0 <=1.38.1"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - aws-ebs-csi breaking changes
  - aws-ebs-csi upgrade broke
  - aws-ebs-csi action required upgrade
  - what breaks upgrading aws-ebs-csi
tags:
  - upgrade
  - breaking-change
  - aws-ebs-csi
sources:
  - type: docs
    path: kubernetes-sigs/aws-ebs-csi-driver release notes — entries marked breaking / action required
    url: https://github.com/kubernetes-sigs/aws-ebs-csi-driver/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# aws-ebs-csi: declared breaking changes by release

## Summary

**5 behaviour changes** the project itself marked as breaking or action-required, across
4 releases from 0.2.0 to 1.38.1. These are not defects: they work as designed and still break
a configuration that worked yesterday. An upgrade crossing any of them needs a decision, not just a
rollout.

## Problem

The upgrade itself usually succeeds. The damage shows up afterwards — a setting silently ignored, a
default flipped, an API version withdrawn, a variable that must now be set explicitly.

## Context

### 0.2.0

- Upgrade the Kubernetes cluster to 1.13+ before deploying the driver. Since CSI 1.0 is only supported starting from Kubernetes 1.13

### 0.4.0

- Update Kubernetes cluster to 1.14+ before installing the driver, since the released driver manifest assumes 1.14+ cluster
- storageclass parameter's `fstype` key is deprecated in favor of `csi.storage.k8s.io/fstype` key. Please update the key in you stroage parameters

### 1.33.0

- The AZ topology key `CreateVolume` returns has changed from `topology.ebs.csi.aws.com/zone` to `topology.kubernetes.io/zone`. Volumes created on `v1.33.0` or any future version will be incompatible with versions before `v1.28.0`. No other customer-facing impact is expected unless you directly depend on the topology label. For more information and the reasoning behind this change, see [issue #729](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/issues/729#issuecomment-1942026577)

### 1.38.1

- Changed time units from microseconds to seconds for all counters


## Diagnostics

```bash
# which version is actually deployed
kubectl get nodes -o wide
helm list -A
```

Cross the list above against the range you are moving through, not only the target version.

## Known Issues

Entries are verbatim from upstream release notes and filtered mechanically: lines shorter than
45 characters and duplicates are dropped, because section headings and list fragments reach the
extractor looking like entries. If a release you care about appears empty here, read its notes
upstream before concluding that nothing changed.

## References

- Upstream releases of `kubernetes-sigs/aws-ebs-csi-driver`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/aws-ebs-csi.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
