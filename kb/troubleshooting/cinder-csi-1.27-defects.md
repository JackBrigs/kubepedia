---
id: TROUBLE-CINDER_CSI_1_27_DEFECTS
type: troubleshooting
title: "cinder-csi 1.27: defects fixed in the 1.27 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.27.0 <1.28.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cinder-csi 1.27 known issues
  - cinder-csi 1.27 fixed in
  - is this cinder-csi bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cinder-csi
sources:
  - type: docs
    path: kubernetes/cloud-provider-openstack release notes for the 1.27 line — bug-fix entries
    url: https://github.com/kubernetes/cloud-provider-openstack/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cinder-csi 1.27: defects fixed in the 1.27 line

## Summary

**7 defects** the project fixed across **2 releases** of the 1.27 line, from 1.27.0 to
1.27.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.27.0

- fix test gate by @zetaab in https://github.com/kubernetes/cloud-provider-openstack/pull/2100
- cinder csi: fix double snapshots package import by @kayrus in https://github.com/kubernetes/cloud-provider-openstack/pull/2135
- [all] Fix cloudbuild by @mdbooth in https://github.com/kubernetes/cloud-provider-openstack/pull/2145
- [all] Fix substitution of _SHORT_TAG in cloudbuild by @mdbooth in https://github.com/kubernetes/cloud-provider-openstack/pull/2146

### 1.27.2

- [occm]: fix blackhole route atomic delete logic (1.27 cherry-pick) by @kayrus in https://github.com/kubernetes/cloud-provider-openstack/pull/2260
- [release-1.27] fix gate by @k8s-infra-cherrypick-robot in https://github.com/kubernetes/cloud-provider-openstack/pull/2311
- [release-1.27] [cinder-csi-plugin]: fix pagination, avoid unnecessary memory allocation, add more logs by @k8s-infra-cherrypick-robot in https://github.com/kubernetes/cloud-provider-openstack/pull/2310


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.27.2**, the newest release recorded here for this line.

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
