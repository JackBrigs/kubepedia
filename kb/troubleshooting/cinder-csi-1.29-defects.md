---
id: TROUBLE-CINDER_CSI_1_29_DEFECTS
type: troubleshooting
title: "cinder-csi 1.29: defects fixed in the 1.29 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.29.0 <1.30.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cinder-csi 1.29 known issues
  - cinder-csi 1.29 fixed in
  - is this cinder-csi bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cinder-csi
sources:
  - type: docs
    path: kubernetes/cloud-provider-openstack release notes for the 1.29 line — bug-fix entries
    url: https://github.com/kubernetes/cloud-provider-openstack/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cinder-csi 1.29: defects fixed in the 1.29 line

## Summary

**7 defects** the project fixed across **1 releases** of the 1.29 line, from 1.29.0 to
1.29.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.29.0

- [occm] Make sure we don't mask LB tests failures and fix what was failing by @dulek in https://github.com/kubernetes/cloud-provider-openstack/pull/2360
- [occm] fix: octavia tlsContainerRef validation for barbican secrets by @Nuckal777 in https://github.com/kubernetes/cloud-provider-openstack/pull/2456
- [occm] update doc to fix typos and better description `router-id` by @jeffyjf in https://github.com/kubernetes/cloud-provider-openstack/pull/2479
- [cinder-csi-plugin] Fix dmesg binary in the container image by @kayrus in https://github.com/kubernetes/cloud-provider-openstack/pull/2495
- Fix some typos by @jeffyjf in https://github.com/kubernetes/cloud-provider-openstack/pull/2488
- [fix] Added call to WaitGroup's Done method in csi package by @meetmorrowsolonmars in https://github.com/kubernetes/cloud-provider-openstack/pull/2511
- [occm] Fix panic on failure to get loadbalancer status by @pierreprinetti in https://github.com/kubernetes/cloud-provider-openstack/pull/2512


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.29.0**, the newest release recorded here for this line.

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
