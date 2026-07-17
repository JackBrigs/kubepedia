---
id: COMPONENT-GCP_PD_CSI
type: component
title: gcp-pd-csi
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: "1.9.2"
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - gcp-pd-csi
tags:
  - csi
  - gcp
  - storage
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "gcp_pd_csi_plugin_version / gcp_pd_csi_plugin_image_repo / gcp_pd_csi_plugin_image_tag"
relations:
  - type: see_also
    target: CONCEPT-CSI_LAYER
---

# gcp-pd-csi

## Summary
gcp-pd-csi is the Google Cloud Platform Persistent Disk CSI (Container Storage Interface) driver, which lets Kubernetes provision and attach GCP Persistent Disks as persistent volumes. In Kubespray it is an opt-in cloud-storage integration: the enable flag `gcp_pd_csi_enabled` defaults to `false`, so it is not deployed unless explicitly enabled. Across all indexed tags (v2.29.0 through v2.31.0) the pinned driver version is `1.9.2`.

## Context
This document covers Kubespray tags v2.29.0, v2.29.1, v2.30.0, and v2.31.0. gcp-pd-csi is disabled by default (`gcp_pd_csi_enabled: false`) and is intended for clusters running on Google Cloud. When enabled it provisions GCP Persistent Disk-backed storage; it therefore depends on a GCP environment and appropriate credentials.

## Implementation
The version is defined in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
gcp_pd_csi_plugin_version: "1.9.2"
gcp_pd_csi_plugin_image_repo: "{{ kube_image_repo }}/cloud-provider-gcp/gcp-compute-persistent-disk-csi-driver"
gcp_pd_csi_plugin_image_tag: "v{{ gcp_pd_csi_plugin_version }}"
```

The image tag is derived by prefixing `v` to the version. The version is identical in every indexed tag:

| Tag | gcp_pd_csi_plugin_version |
|-----|---------------------------|
| v2.29.0 | 1.9.2 |
| v2.29.1 | 1.9.2 |
| v2.30.0 | 1.9.2 |
| v2.31.0 | 1.9.2 |

Image repo (v2.31.0): `{{ kube_image_repo }}/cloud-provider-gcp/gcp-compute-persistent-disk-csi-driver`; image tag `v1.9.2`.

## Configuration
- Enable flag: `gcp_pd_csi_enabled` — default `false` (`roles/kubespray_defaults/defaults/main/main.yml`).
- Version var: `gcp_pd_csi_plugin_version` — default `1.9.2`.
- Image repo: `gcp_pd_csi_plugin_image_repo` — `{{ kube_image_repo }}/cloud-provider-gcp/gcp-compute-persistent-disk-csi-driver`.
- Image tag: `gcp_pd_csi_plugin_image_tag` — `v{{ gcp_pd_csi_plugin_version }}`.

## Compatibility
The pinned version is `1.9.2` for all four indexed tags (no change between v2.29.0 and v2.31.0). Applicable to the Kubernetes versions shipped by those Kubespray tags (approximately Kubernetes 1.31–1.35). Only relevant on GCP-based clusters.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
