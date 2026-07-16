---
id: COMPONENT-LOCAL_PATH_PROVISIONER
type: component
title: local-path-provisioner
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: "0.0.32"
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - local-path-provisioner
tags:
  - storage
  - provisioner
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "local_path_provisioner_version / local_path_provisioner_image_repo / local_path_provisioner_image_tag"
relations: []
---

# local-path-provisioner

## Summary
local-path-provisioner is the Rancher Local Path Provisioner, a dynamic storage provisioner that creates PersistentVolumes backed by directories on local node disk. In Kubespray it is an opt-in storage add-on: the enable flag `local_path_provisioner_enabled` defaults to `false`, so it is not deployed unless explicitly enabled. Across all indexed tags (v2.29.0 through v2.31.0) the pinned version is `0.0.32`.

## Context
This document covers Kubespray tags v2.29.0, v2.29.1, v2.30.0, and v2.31.0. local-path-provisioner is disabled by default (`local_path_provisioner_enabled: false`). When enabled it provisions PersistentVolumes from local node storage, which makes it a lightweight option for single-node or bare-metal clusters without an external storage backend. It depends on writable local paths on the nodes.

## Implementation
The version is defined in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
local_path_provisioner_version: "0.0.32"
local_path_provisioner_image_repo: "{{ docker_image_repo }}/rancher/local-path-provisioner"
local_path_provisioner_image_tag: "v{{ local_path_provisioner_version }}"
```

The image tag is derived by prefixing `v` to the version. The version is identical in every indexed tag:

| Tag | local_path_provisioner_version |
|-----|--------------------------------|
| v2.29.0 | 0.0.32 |
| v2.29.1 | 0.0.32 |
| v2.30.0 | 0.0.32 |
| v2.31.0 | 0.0.32 |

Image repo (v2.31.0): `{{ docker_image_repo }}/rancher/local-path-provisioner`; image tag `v0.0.32`.

## Configuration
- Enable flag: `local_path_provisioner_enabled` — default `false` (`roles/kubespray_defaults/defaults/main/main.yml`).
- Version var: `local_path_provisioner_version` — default `0.0.32`.
- Image repo: `local_path_provisioner_image_repo` — `{{ docker_image_repo }}/rancher/local-path-provisioner`.
- Image tag: `local_path_provisioner_image_tag` — `v{{ local_path_provisioner_version }}`.

## Compatibility
The pinned version is `0.0.32` for all four indexed tags (no change between v2.29.0 and v2.31.0). Applicable to the Kubernetes versions shipped by those Kubespray tags (approximately Kubernetes 1.31–1.35). Suitable for clusters that need node-local dynamic provisioning.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
