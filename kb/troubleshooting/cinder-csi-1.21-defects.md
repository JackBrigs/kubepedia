---
id: TROUBLE-CINDER_CSI_1_21_DEFECTS
type: troubleshooting
title: "cinder-csi 1.21: defects fixed in the 1.21 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.21.0 <1.22.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cinder-csi 1.21 known issues
  - cinder-csi 1.21 fixed in
  - is this cinder-csi bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cinder-csi
sources:
  - type: docs
    path: kubernetes/cloud-provider-openstack release notes for the 1.21 line — bug-fix entries
    url: https://github.com/kubernetes/cloud-provider-openstack/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cinder-csi 1.21: defects fixed in the 1.21 line

## Summary

**6 defects** the project fixed across **1 releases** of the 1.21 line, from 1.21.0 to
1.21.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.21.0

- [openstack-cloud-controller-manager] Fixed the broken header issue when accessing the load balancer service with PROXY protocol enabled from within the cluster. (#1449, @lingxiankong)
- [cinder-csi-plugin] Fixed the issue where the file system size stays the same when expanding the volume. (#1434, @Fedosin)
- [cinder-csi-plugin] Fixed the issue that the ephemeral inline volume is yet available when attaching to the node. (#1429, @ramineni)
- [manila-csi-plugin] Fixed a leak causing high memory consumption (#1473, @gman0)
- [octavia-ingress-controller] Fixed the issue that pools and l7 policies are removed no matter how the Ingress is changed. (#1418, @lingxiankong)
- [magnum-auto-healer] Fixed an issue that k8s master node repair failed when the node is boot from volume. (#1447, @openstacker)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.21.0**, the newest release recorded here for this line.

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
