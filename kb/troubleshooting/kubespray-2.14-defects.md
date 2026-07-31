---
id: TROUBLE-KUBESPRAY_2_14_DEFECTS
type: troubleshooting
title: "kubespray 2.14: defects fixed in the 2.14 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.14.0 <2.15.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kubespray 2.14 known issues
  - kubespray 2.14 fixed in
  - is this kubespray bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kubespray
sources:
  - type: docs
    path: kubernetes-sigs/kubespray release notes for the 2.14 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/kubespray/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kubespray 2.14: defects fixed in the 2.14 line

## Summary

**5 defects** the project fixed across **3 releases** of the 2.14 line, from 2.14.0 to
2.14.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.14.0

- [CRI-O] Fix kubelet cgroup driver detection (#6331)
- Fix resolv.conf configuration for Fedora CoreOS (#6138)
- Multiples fixes for proxy and no_proxy variables (#6112 #6431 #6558)

### 2.14.1

- fix kubelet_flexvolumes_plugins_dir undefined (#6670)

### 2.14.2

- Fix cinder & external_openstack cacert deployment (#6832)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.14.2**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `kubernetes-sigs/kubespray`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/kubespray.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
