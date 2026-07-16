---
id: COMPONENT-LOCAL_VOLUME_PROVISIONER
type: component
title: local-volume-provisioner
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: "2.5.0"
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - local-volume-provisioner
tags:
  - storage
  - provisioner
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "local_volume_provisioner_version / local_volume_provisioner_image_repo / local_volume_provisioner_image_tag"
relations: []
---

# local-volume-provisioner

## Summary
local-volume-provisioner is the Kubernetes sig-storage Local Volume Static Provisioner. It discovers pre-provisioned local disks/directories on nodes and exposes them as PersistentVolumes using local storage. In Kubespray it is an opt-in storage add-on: the enable flag `local_volume_provisioner_enabled` defaults to `false`, so it is not deployed unless explicitly enabled. Across all indexed tags (v2.29.0 through v2.31.0) the pinned version is `2.5.0`.

## Context
This document covers Kubespray tags v2.29.0, v2.29.1, v2.30.0, and v2.31.0. local-volume-provisioner is disabled by default (`local_volume_provisioner_enabled: false`). When enabled, the preinstall role creates the required local volume directories (`roles/kubernetes/preinstall/tasks/0050-create_directories.yml`) and the `external_provisioner` app role deploys the provisioner. It depends on local disks/mount points being present on the nodes; it does not dynamically create backing storage, it only publishes existing local paths as PVs.

## Implementation
The version is defined in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
local_volume_provisioner_version: "2.5.0"
local_volume_provisioner_image_repo: "{{ kube_image_repo }}/sig-storage/local-volume-provisioner"
local_volume_provisioner_image_tag: "v{{ local_volume_provisioner_version }}"
```

The image tag is derived by prefixing `v` to the version. The version is identical in every indexed tag:

| Tag | local_volume_provisioner_version |
|-----|----------------------------------|
| v2.29.0 | 2.5.0 |
| v2.29.1 | 2.5.0 |
| v2.30.0 | 2.5.0 |
| v2.31.0 | 2.5.0 |

Image repo (v2.31.0): `{{ kube_image_repo }}/sig-storage/local-volume-provisioner`; image tag `v2.5.0`.

## Configuration
- Enable flag: `local_volume_provisioner_enabled` — default `false` (`roles/kubespray_defaults/defaults/main/main.yml`; also set `false` in `inventory/sample/group_vars/k8s_cluster/addons.yml`).
- Version var: `local_volume_provisioner_version` — default `2.5.0`.
- Image repo: `local_volume_provisioner_image_repo` — `{{ kube_image_repo }}/sig-storage/local-volume-provisioner`.
- Image tag: `local_volume_provisioner_image_tag` — `v{{ local_volume_provisioner_version }}`.

## Compatibility
The pinned version is `2.5.0` for all four indexed tags (no change between v2.29.0 and v2.31.0). Applicable to the Kubernetes versions shipped by those Kubespray tags (approximately Kubernetes 1.31–1.35). Suitable for clusters that expose pre-provisioned local disks as PersistentVolumes.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
