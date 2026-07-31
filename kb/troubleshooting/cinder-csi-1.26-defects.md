---
id: TROUBLE-CINDER_CSI_1_26_DEFECTS
type: troubleshooting
title: "cinder-csi 1.26: defects fixed in the 1.26 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.26.0 <1.27.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cinder-csi 1.26 known issues
  - cinder-csi 1.26 fixed in
  - is this cinder-csi bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cinder-csi
sources:
  - type: docs
    path: kubernetes/cloud-provider-openstack release notes for the 1.26 line — bug-fix entries
    url: https://github.com/kubernetes/cloud-provider-openstack/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cinder-csi 1.26: defects fixed in the 1.26 line

## Summary

**7 defects** the project fixed across **4 releases** of the 1.26 line, from 1.26.0 to
1.26.4. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.26.0

- [occm] Fix panic when setting fake proxy protocol LB hostname by @mtneug in https://github.com/kubernetes/cloud-provider-openstack/pull/2005
- fix cinder and manila CI issue by @jichenjc in https://github.com/kubernetes/cloud-provider-openstack/pull/2020
- Fix gate: CI of cinder CSI failure by @jichenjc in https://github.com/kubernetes/cloud-provider-openstack/pull/2027
- fix: remove leftover from bundled snapshot controller by @zifeo in https://github.com/kubernetes/cloud-provider-openstack/pull/2050

### 1.26.1

- Automated cherry pick of #2100: fix testgate by @zetaab in https://github.com/kubernetes/cloud-provider-openstack/pull/2101

### 1.26.3

- [occm]: fix blackhole route atomic delete logic (1.26 cherry-pick) by @kayrus in https://github.com/kubernetes/cloud-provider-openstack/pull/2259

### 1.26.4

- [cinder-csi-plugin] Fixed pagination issue in Cinder CSI ListVolumes and ListSnapshots calls (cherry-pick) by @kayrus in #2296


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.26.4**, the newest release recorded here for this line.

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
