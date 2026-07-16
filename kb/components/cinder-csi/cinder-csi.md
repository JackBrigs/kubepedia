---
id: COMPONENT-CINDER_CSI
type: component
title: cinder-csi
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: "1.30.0"
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cinder-csi
tags:
  - csi
  - openstack
  - storage
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "cinder_csi_plugin_version / cinder_csi_plugin_image_repo / cinder_csi_plugin_image_tag"
relations: []
---

# cinder-csi

## Summary
cinder-csi is the OpenStack Cinder CSI (Container Storage Interface) driver, which lets Kubernetes provision and attach OpenStack Cinder block-storage volumes as persistent volumes. In Kubespray it is an opt-in cloud-storage integration: the enable flag `cinder_csi_enabled` defaults to `false`, so it is not deployed unless explicitly enabled. Across all indexed tags (v2.29.0 through v2.31.0) the pinned driver version is `1.30.0`.

## Context
This document covers Kubespray tags v2.29.0, v2.29.1, v2.30.0, and v2.31.0. cinder-csi is disabled by default (`cinder_csi_enabled: false`) and is intended for clusters running on OpenStack. When enabled it provisions Cinder-backed storage; it therefore depends on a reachable OpenStack cloud environment and appropriate credentials.

## Implementation
The version is defined in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
cinder_csi_plugin_version: "1.30.0"
cinder_csi_plugin_image_repo: "{{ kube_image_repo }}/provider-os/cinder-csi-plugin"
cinder_csi_plugin_image_tag: "v{{ cinder_csi_plugin_version }}"
```

The image tag is derived by prefixing `v` to the version. The version is identical in every indexed tag:

| Tag | cinder_csi_plugin_version |
|-----|---------------------------|
| v2.29.0 | 1.30.0 |
| v2.29.1 | 1.30.0 |
| v2.30.0 | 1.30.0 |
| v2.31.0 | 1.30.0 |

Image repo (v2.31.0): `{{ kube_image_repo }}/provider-os/cinder-csi-plugin`; image tag `v1.30.0`.

## Configuration
- Enable flag: `cinder_csi_enabled` — default `false` (`roles/kubespray_defaults/defaults/main/main.yml`).
- Version var: `cinder_csi_plugin_version` — default `1.30.0`.
- Image repo: `cinder_csi_plugin_image_repo` — `{{ kube_image_repo }}/provider-os/cinder-csi-plugin`.
- Image tag: `cinder_csi_plugin_image_tag` — `v{{ cinder_csi_plugin_version }}`.

## Compatibility
The pinned version is `1.30.0` for all four indexed tags (no change between v2.29.0 and v2.31.0). Applicable to the Kubernetes versions shipped by those Kubespray tags (approximately Kubernetes 1.31–1.35). Only relevant on OpenStack-based clusters.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
