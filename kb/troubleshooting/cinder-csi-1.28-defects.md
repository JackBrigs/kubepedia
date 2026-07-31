---
id: TROUBLE-CINDER_CSI_1_28_DEFECTS
type: troubleshooting
title: "cinder-csi 1.28: defects fixed in the 1.28 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.28.0 <1.29.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cinder-csi 1.28 known issues
  - cinder-csi 1.28 fixed in
  - is this cinder-csi bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cinder-csi
sources:
  - type: docs
    path: kubernetes/cloud-provider-openstack release notes for the 1.28 line — bug-fix entries
    url: https://github.com/kubernetes/cloud-provider-openstack/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cinder-csi 1.28: defects fixed in the 1.28 line

## Summary

**13 defects** the project fixed across **2 releases** of the 1.28 line, from 1.28.0 to
1.28.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.28.0

- [manila-csi-plugin]fix manila sanity test by @jichenjc in https://github.com/kubernetes/cloud-provider-openstack/pull/2226
- [occm] fix daemonset annotations by @simonostendorf in https://github.com/kubernetes/cloud-provider-openstack/pull/2237
- [occm]: fix blackhole route atomic delete logic by @kayrus in https://github.com/kubernetes/cloud-provider-openstack/pull/2257
- Fix CSI spec versions by @kayrus in https://github.com/kubernetes/cloud-provider-openstack/pull/2254
- manila-csi: Fix image tag in e2e test scripts by @gouthampacha in https://github.com/kubernetes/cloud-provider-openstack/pull/2244
- [occm] Fixed the typo in the load balancing section in the README by @armagankaratosun in https://github.com/kubernetes/cloud-provider-openstack/pull/2232
- fix gate by @jichenjc in https://github.com/kubernetes/cloud-provider-openstack/pull/2283
- fixed Grammatical mistakes in barbican-kms-plugin by @Vikash-8090-Yadav in https://github.com/kubernetes/cloud-provider-openstack/pull/2289
- [cinder-csi-plugin]: fix pagination, avoid unnecessary memory allocation, add more logs by @kayrus in https://github.com/kubernetes/cloud-provider-openstack/pull/2296
- [occm] Fix protocol case mismatch (tcp vs TCP) by @dulek in https://github.com/kubernetes/cloud-provider-openstack/pull/2320
- [magnum-auto-healer] Fix Worker Nodes stuck in Ready,SchedulingDisabled status after repair by reboot by @pawcykca in https://github.com/kubernetes/cloud-provider-openstack/pull/2279

### 1.28.2

- [release-1.28] [occm] fix: octavia tlsContainerRef validation for barbican secrets by @k8s-infra-cherrypick-robot in https://github.com/kubernetes/cloud-provider-openstack/pull/2458
- [release-1.28] [occm] Make sure we don't mask LB tests failures and fix what was failing by @dulek in https://github.com/kubernetes/cloud-provider-openstack/pull/2537


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.28.2**, the newest release recorded here for this line.

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
