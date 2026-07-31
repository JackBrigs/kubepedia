---
id: TROUBLE-CINDER_CSI_1_31_DEFECTS
type: troubleshooting
title: "cinder-csi 1.31: defects fixed in the 1.31 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.31.0 <1.32.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cinder-csi 1.31 known issues
  - cinder-csi 1.31 fixed in
  - is this cinder-csi bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cinder-csi
sources:
  - type: docs
    path: kubernetes/cloud-provider-openstack release notes for the 1.31 line — bug-fix entries
    url: https://github.com/kubernetes/cloud-provider-openstack/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cinder-csi 1.31: defects fixed in the 1.31 line

## Summary

**6 defects** the project fixed across **3 releases** of the 1.31 line, from 1.31.0 to
1.31.4. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.31.0

- [occm] fix e2e tests by @zetaab in https://github.com/kubernetes/cloud-provider-openstack/pull/2636
- [occm] Fix: Set instanceID to get subnet for loadbalancer. by @ovstuckrad in https://github.com/kubernetes/cloud-provider-openstack/pull/2639

### 1.31.2

- [release-1.31] [cinder-csi-plugin] fix global config requirement for node-service by @k8s-infra-cherrypick-robot in https://github.com/kubernetes/cloud-provider-openstack/pull/2683
- [release-1.31] [occm] fix ovn security groups by @k8s-infra-cherrypick-robot in https://github.com/kubernetes/cloud-provider-openstack/pull/2713

### 1.31.4

- [release-1.31] [Barbican][KMS] Fix clouds.yaml authentication by @k8s-infra-cherrypick-robot in https://github.com/kubernetes/cloud-provider-openstack/pull/2926
- [release-1.31] [occm] fix lbaas logs by @k8s-infra-cherrypick-robot in https://github.com/kubernetes/cloud-provider-openstack/pull/2925


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.31.4**, the newest release recorded here for this line.

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
