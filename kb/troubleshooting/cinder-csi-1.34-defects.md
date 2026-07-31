---
id: TROUBLE-CINDER_CSI_1_34_DEFECTS
type: troubleshooting
title: "cinder-csi 1.34: defects fixed in the 1.34 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.34.0 <1.35.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cinder-csi 1.34 known issues
  - cinder-csi 1.34 fixed in
  - is this cinder-csi bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cinder-csi
sources:
  - type: docs
    path: kubernetes/cloud-provider-openstack release notes for the 1.34 line — bug-fix entries
    url: https://github.com/kubernetes/cloud-provider-openstack/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cinder-csi 1.34: defects fixed in the 1.34 line

## Summary

**5 defects** the project fixed across **2 releases** of the 1.34 line, from 1.34.0 to
1.34.1. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.34.0

- fix error for build-local-images by @archerwu9425 in https://github.com/kubernetes/cloud-provider-openstack/pull/2916
- [occm] fix lbaas logs by @kayrus in https://github.com/kubernetes/cloud-provider-openstack/pull/2870
- [Barbican][KMS] Fix clouds.yaml authentication by @modzilla99 in https://github.com/kubernetes/cloud-provider-openstack/pull/2896
- doc: fix typo in keystone sync example by @winiciusallan in https://github.com/kubernetes/cloud-provider-openstack/pull/3003

### 1.34.1

- [release-1.34] fix bump scripts by @k8s-infra-cherrypick-robot in https://github.com/kubernetes/cloud-provider-openstack/pull/3014


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.34.1**, the newest release recorded here for this line.

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
