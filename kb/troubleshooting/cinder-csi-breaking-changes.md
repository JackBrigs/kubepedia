---
id: TROUBLE-CINDER_CSI_BREAKING_CHANGES
type: troubleshooting
title: "cinder-csi: declared breaking changes by release"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.18.0 <=openstack-cloud-controller-manager-2.28.2"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cinder-csi breaking changes
  - cinder-csi upgrade broke
  - cinder-csi action required upgrade
  - what breaks upgrading cinder-csi
tags:
  - upgrade
  - breaking-change
  - cinder-csi
sources:
  - type: docs
    path: kubernetes/cloud-provider-openstack release notes — entries marked breaking / action required
    url: https://github.com/kubernetes/cloud-provider-openstack/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cinder-csi: declared breaking changes by release

## Summary

**6 behaviour changes** the project itself marked as breaking or action-required, across
5 releases from 1.18.0 to openstack-cloud-controller-manager-2.28.2. These are not defects: they work as designed and still break
a configuration that worked yesterday. An upgrade crossing any of them needs a decision, not just a
rollout.

## Problem

The upgrade itself usually succeeds. The damage shows up afterwards — a setting silently ignored, a
default flipped, an API version withdrawn, a variable that must now be set explicitly.

## Context

### 1.18.0

- openstack-cloud-controller-manager: Support OpenStack Octavia by default as load balancer implementation
- cinder-provisioner, manila-provisioner and cinder-flexvolume-plugin were removed from cloud-provider-openstack repository since release-1.18, use cinder-csi and manila-csi instead

### 1.24.0

- [magnum-auto-healer] Remove Cinder V2 support

### openstack-cloud-controller-manager-2.26.5

- Please note that you might have to delete the `cloud-controller-manager` service account in the `kube-system` namespace if it exists, as upgrading with helm would fail otherwise

### openstack-cloud-controller-manager-2.27.6

- Please note that you might have to delete the `cloud-controller-manager` service account in the `kube-system` namespace if it exists, as upgrading with helm would fail otherwise

### openstack-cloud-controller-manager-2.28.2

- Please note that you might have to delete the `cloud-controller-manager` service account in the `kube-system` namespace if it exists, as upgrading with helm would fail otherwise


## Diagnostics

```bash
# which version is actually deployed
kubectl get nodes -o wide
helm list -A
```

Cross the list above against the range you are moving through, not only the target version.

## Known Issues

Entries are verbatim from upstream release notes and filtered mechanically: lines shorter than
45 characters and duplicates are dropped, because section headings and list fragments reach the
extractor looking like entries. If a release you care about appears empty here, read its notes
upstream before concluding that nothing changed.

## References

- Upstream releases of `kubernetes/cloud-provider-openstack`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/cinder-csi.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
