---
id: CONCEPT-CSI_LAYER
type: concept
title: "CSI storage layer in Kubespray (sidecars, snapshot controller, drivers)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - CSI
  - csi sidecars
  - external-provisioner attacher snapshotter resizer
  - snapshot controller
  - csi drivers kubespray
  - VolumeSnapshotClass
tags:
  - csi
  - storage
  - components
  - upgrade
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    lines: "317-327"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "CSI sidecar image tags (tag v2.31.0)"
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "csi_snapshot_controller_enabled; *_csi_enabled driver flags (tag v2.31.0)"
relations:
  - type: see_also
    target: COMPONENT-SNAPSHOT_CONTROLLER
  - type: see_also
    target: CONCEPT-COMPONENT_VERSION_SELECTION
  - type: see_also
    target: COMPONENT-CINDER_CSI
---

# CSI storage layer in Kubespray (sidecars, snapshot controller, drivers)

## Summary

Kubespray's CSI story has three parts: the **shared CSI sidecar images** (used by every
driver), the cluster-wide **snapshot controller**, and the **per-provider CSI drivers**.
All are opt-in. Note that `v2.31.0` carries **major** sidecar bumps versus `v2.29.0`
(external-attacher `v3 → v4`, external-snapshotter `v5 → v6`), which matters when
upgrading storage.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`. All drivers/snapshotting are **off by
  default**.
- Sidecars are shared container images that each CSI driver's controller/node pods embed.

## Implementation

### Shared CSI sidecars (v2.31.0 image tags)

| Sidecar | v2.31.0 | v2.29.0 | note |
|---------|---------|---------|------|
| external-attacher | `v4.4.2` | `v3.3.0` | **major bump v3→v4** |
| external-provisioner | `v3.6.2` | `v3.0.0` | |
| external-snapshotter | `v6.3.2` | `v5.0.0` | **major bump v5→v6** |
| external-resizer | `v1.9.2` | `v1.3.0` | |
| node-driver-registrar | `v2.4.0` | (same line) | |
| livenessprobe | `v2.11.0` | `v2.5.0` | |

These move as **fixed literal pins** (change only on a Kubespray bump —
[[CONCEPT-COMPONENT_VERSION_SELECTION]]).

### Snapshot controller

- `csi_snapshot_controller_enabled: false` — deploys the cluster-wide **snapshot
  controller** and the `VolumeSnapshot`/`VolumeSnapshotClass`/`VolumeSnapshotContent`
  CRDs ([[COMPONENT-SNAPSHOT_CONTROLLER]]). Required for CSI volume snapshots regardless
  of driver.

### Per-provider CSI drivers (enable flags)

- `cinder_csi_enabled` (OpenStack — [[COMPONENT-CINDER_CSI]]), `aws_ebs_csi_enabled`,
  `azure_csi_enabled`, `gcp_pd_csi_enabled`, `vsphere_csi_enabled`.
- Node-local storage without a cloud: local-path-provisioner and
  local-volume-provisioner (separate add-ons).

## Compatibility

- **Upgrade impact:** the `v2.29.0 → v2.31.0` sidecar jumps (attacher v3→v4, snapshotter
  v5→v6) can change CRD API expectations and RBAC — after upgrading, verify
  `VolumeSnapshotClass`/`VolumeSnapshot` objects and driver deployments reconcile cleanly.
- Snapshotting requires **both** the snapshot controller (cluster-wide, one instance) and
  a snapshot-capable driver; enabling only the driver won't give you snapshots.
- CSI sidecar and Kubernetes version have their own compatibility matrices upstream;
  Kubespray pins tested combinations per tag — prefer the bundled versions over ad-hoc
  overrides.

## References

- CSI sidecar tags (download.yml:317-327) and driver flags (main.yml) at tag `v2.31.0`;
  v2.29.0 values via `git show`. Snapshot controller: [[COMPONENT-SNAPSHOT_CONTROLLER]];
  version mechanism: [[CONCEPT-COMPONENT_VERSION_SELECTION]].
