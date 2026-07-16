---
id: COMPONENT-SNAPSHOT_CONTROLLER
type: component
title: snapshot-controller
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: "v7.0.2"
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - snapshot-controller
tags:
  - storage
  - csi
  - snapshots
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "snapshot_controller_supported_versions / snapshot_controller_image_repo / snapshot_controller_image_tag"
relations: []
---

# snapshot-controller

## Summary
snapshot-controller is the Kubernetes sig-storage CSI Snapshot Controller. It watches VolumeSnapshot and VolumeSnapshotContent objects and drives the snapshot lifecycle for CSI drivers that support volume snapshots. In Kubespray it is an opt-in add-on: the enable flag `csi_snapshot_controller_enabled` defaults to `false`, so it is not deployed unless explicitly enabled (it is also implicitly required by some CSI drivers such as Cinder CSI). Across all indexed tags (v2.29.0 through v2.31.0) the resolved image version is `v7.0.2`.

## Context
This document covers Kubespray tags v2.29.0, v2.29.1, v2.30.0, and v2.31.0. The snapshot-controller is disabled by default (`csi_snapshot_controller_enabled: false`). It is deployed by the `kubernetes-apps/snapshots/snapshot-controller` role, gated in `roles/kubernetes-apps/snapshots/meta/main.yml` on `cinder_csi_enabled or csi_snapshot_controller_enabled`. It runs in the `snapshot_controller_namespace` (default `kube-system`) with `snapshot_controller_replicas` (default `1`). It depends on the cluster having the VolumeSnapshot CRDs and a CSI driver that supports snapshots.

## Implementation
The version is not a plain literal; it is resolved from a per-Kubernetes-version table keyed by `kube_major_version` in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
snapshot_controller_supported_versions:
  '1.35': "v7.0.2"
  '1.34': "v7.0.2"
  '1.33': "v7.0.2"
snapshot_controller_image_repo: "{{ kube_image_repo }}/sig-storage/snapshot-controller"
snapshot_controller_image_tag: "{{ snapshot_controller_supported_versions[kube_major_version] }}"
```

The table keys shift with the Kubernetes versions each tag ships, but every entry maps to `v7.0.2`, so the resolved image tag is `v7.0.2` regardless of which supported Kubernetes minor is in use. The resolved version is identical in every indexed tag:

| Tag | supported k8s keys | resolved snapshot-controller version |
|-----|--------------------|--------------------------------------|
| v2.29.0 | 1.31, 1.32, 1.33 | v7.0.2 |
| v2.29.1 | 1.31, 1.32, 1.33 | v7.0.2 |
| v2.30.0 | 1.32, 1.33, 1.34 | v7.0.2 |
| v2.31.0 | 1.33, 1.34, 1.35 | v7.0.2 |

Image repo (v2.31.0): `{{ kube_image_repo }}/sig-storage/snapshot-controller`; image tag `v7.0.2`.

## Configuration
- Enable flag: `csi_snapshot_controller_enabled` — default `false` (`roles/kubespray_defaults/defaults/main/main.yml`; commented example in `inventory/sample/group_vars/k8s_cluster/addons.yml`).
- Version source: `snapshot_controller_supported_versions[kube_major_version]` — resolves to `v7.0.2` for all supported Kubernetes minors.
- Image repo: `snapshot_controller_image_repo` — `{{ kube_image_repo }}/sig-storage/snapshot-controller`.
- Image tag: `snapshot_controller_image_tag` — `{{ snapshot_controller_supported_versions[kube_major_version] }}`.
- Namespace: `snapshot_controller_namespace` — default `kube-system`.
- Replicas: `snapshot_controller_replicas` — default `1` (leader election enabled only when replicas > 1).

## Compatibility
The resolved version is `v7.0.2` for all four indexed tags (no change between v2.29.0 and v2.31.0). The supported-versions table advances its Kubernetes keys per tag (1.31–1.33 in v2.29.x up to 1.33–1.35 in v2.31.0), covering approximately Kubernetes 1.31–1.35. Suitable for clusters using CSI drivers that support volume snapshots.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
