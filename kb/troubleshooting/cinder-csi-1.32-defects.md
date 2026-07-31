---
id: TROUBLE-CINDER_CSI_1_32_DEFECTS
type: troubleshooting
title: "cinder-csi 1.32: defects fixed in the 1.32 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.32.0 <1.33.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cinder-csi 1.32 known issues
  - cinder-csi 1.32 fixed in
  - is this cinder-csi bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cinder-csi
sources:
  - type: docs
    path: kubernetes/cloud-provider-openstack release notes for the 1.32 line — bug-fix entries
    url: https://github.com/kubernetes/cloud-provider-openstack/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cinder-csi 1.32: defects fixed in the 1.32 line

## Summary

**11 defects** the project fixed across **2 releases** of the 1.32 line, from 1.32.0 to
1.32.1. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.32.0

- fix instructions by @zetaab in https://github.com/kubernetes/cloud-provider-openstack/pull/2642
- fix helm chart builds by @zetaab in https://github.com/kubernetes/cloud-provider-openstack/pull/2643
- [cinder-csi-plugin] fix global config requirement for node-service by @kayrus in https://github.com/kubernetes/cloud-provider-openstack/pull/2678
- Fix CSI tests by @kayrus in https://github.com/kubernetes/cloud-provider-openstack/pull/2712
- [occm] fix ovn security groups by @zetaab in https://github.com/kubernetes/cloud-provider-openstack/pull/2705
- [tests] bump devstack branch to stable/2023.2, fix python issues by @kayrus in https://github.com/kubernetes/cloud-provider-openstack/pull/2716
- Fix warnings reported while building container images by @Niharika0306 in https://github.com/kubernetes/cloud-provider-openstack/pull/2701
- [occm] fix node internal/external IP order by @kayrus in https://github.com/kubernetes/cloud-provider-openstack/pull/2719
- fix helm chart versions by @zetaab in https://github.com/kubernetes/cloud-provider-openstack/pull/2761

### 1.32.1

- [release-1.32] [Barbican][KMS] Fix clouds.yaml authentication by @k8s-infra-cherrypick-robot in https://github.com/kubernetes/cloud-provider-openstack/pull/2928
- [release-1.32] [occm] fix lbaas logs by @k8s-infra-cherrypick-robot in https://github.com/kubernetes/cloud-provider-openstack/pull/2924


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.32.1**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `kubernetes/cloud-provider-openstack`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/cinder-csi.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
