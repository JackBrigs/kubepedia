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
tags:
  - upgrade
  - breaking-change
  - cinder-csi
sources:
  - type: docs
    path: kubernetes/cloud-provider-openstack release notes — "breaking changes" / "action required" entries
    url: https://github.com/kubernetes/cloud-provider-openstack/releases
    note: "machine-extracted by scripts/upstream_issues.py, short and duplicate lines filtered out"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cinder-csi: declared breaking changes by release

## Summary

**6 behaviour changes** the project itself marked as breaking or action-required, across
5 releases from 1.18.0 to openstack-cloud-controller-manager-2.28.2. Read this before planning
an upgrade that crosses any of these versions: unlike defects, these are changes that work as
designed and still break a working configuration.

## Problem

An upgrade across a breaking change usually succeeds — the failure appears afterwards, in behaviour:
a setting silently ignored, a default flipped, an API version withdrawn.

## Context

### 1.18.0

- openstack-cloud-controller-manager: Support OpenStack Octavia by default as load balancer implementation. Action required. (#977, @lingxiankong)
- cinder-provisioner, manila-provisioner and cinder-flexvolume-plugin were removed from cloud-provider-openstack repository since release-1.18, use cinder-csi and manila-csi instead. Action required. (#991, @lingxiankong)

### 1.24.0

- [magnum-auto-healer] Remove Cinder V2 support. Action required. (#1769, @mnasiadka)

### openstack-cloud-controller-manager-2.26.5

- ACTION REQUIRED: Please note that you might have to delete the `cloud-controller-manager` service account in the `kube-system` namespace if it exists, as upgrading with helm would fail otherwise.

### openstack-cloud-controller-manager-2.27.6

- ACTION REQUIRED: Please note that you might have to delete the `cloud-controller-manager` service account in the `kube-system` namespace if it exists, as upgrading with helm would fail otherwise.

### openstack-cloud-controller-manager-2.28.2

- ACTION REQUIRED: Please note that you might have to delete the `cloud-controller-manager` service account in the `kube-system` namespace if it exists, as upgrading with helm would fail otherwise.

## Diagnostics

Compare the version in use against the list above:

```bash
kubectl get nodes -o wide          # runtime versions, for node components
helm list -A                       # chart-deployed components
```

## Known Issues

Entries are verbatim from upstream release notes and filtered mechanically: lines shorter than 45
characters and duplicates were dropped, because section headings and list fragments come through the
extractor as if they were entries. If a release you care about looks empty here, read its notes
upstream before concluding nothing changed.

## References

- Upstream releases of `kubernetes/cloud-provider-openstack`, read 2026-07-31 via `scripts/upstream_issues.py`;
  raw extraction in `reports/upstream/cinder-csi.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
