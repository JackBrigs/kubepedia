---
id: TROUBLE-CINDER_CSI_1_25_DEFECTS
type: troubleshooting
title: "cinder-csi 1.25: defects fixed in the 1.25 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.25.0 <1.26.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cinder-csi 1.25 known issues
  - cinder-csi 1.25 fixed in
  - is this cinder-csi bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cinder-csi
sources:
  - type: docs
    path: kubernetes/cloud-provider-openstack release notes for the 1.25 line — bug-fix entries
    url: https://github.com/kubernetes/cloud-provider-openstack/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cinder-csi 1.25: defects fixed in the 1.25 line

## Summary

**12 defects** the project fixed across **4 releases** of the 1.25 line, from 1.25.0 to
1.25.6. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.25.0

- occm: Fix LoadBalancer deletion when the underlying LoadBalancer does not exist by @ialidzhikov in https://github.com/kubernetes/cloud-provider-openstack/pull/1913
- occm: Fix not found checks for LoadBalancers do not cover all possible cases by @bd3lage in https://github.com/kubernetes/cloud-provider-openstack/pull/1942
- fix gate issue by @jichenjc in https://github.com/kubernetes/cloud-provider-openstack/pull/1959
- [manila-csi-plugin] Fix constraints configuration for application cred by @mtneug in https://github.com/kubernetes/cloud-provider-openstack/pull/1957
- [occm] Fix Naming of listener, pools and monitors during Creation by @shaardie in https://github.com/kubernetes/cloud-provider-openstack/pull/1966
- fix: Add region to providerID magic string by @sergelogvinov in https://github.com/kubernetes/cloud-provider-openstack/pull/1970
- [occm] Fix minor Inconsistency in `getMemberSubnetID` by @shaardie in https://github.com/kubernetes/cloud-provider-openstack/pull/1978
- [manila-csi-plugin] Fix fake csi and manila clients for sanity-csi test by @gman0 in https://github.com/kubernetes/cloud-provider-openstack/pull/1987

### 1.25.2

- Automated cherry pick of #2005: Fix panic when setting fake proxy protocol LB hostname by @zetaab in https://github.com/kubernetes/cloud-provider-openstack/pull/2012

### 1.25.4

- [occm] cherrypick: LB - Fix floating ip subnet detection and ipv6 handling by @chrigl in https://github.com/kubernetes/cloud-provider-openstack/pull/2022
- Automated cherry pick of #2100: fix testgate by @zetaab in https://github.com/kubernetes/cloud-provider-openstack/pull/2102

### 1.25.6

- [occm]: fix blackhole route atomic delete logic (1.25 cherry-pick) by @kayrus in https://github.com/kubernetes/cloud-provider-openstack/pull/2258


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.25.6**, the newest release recorded here for this line.

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
