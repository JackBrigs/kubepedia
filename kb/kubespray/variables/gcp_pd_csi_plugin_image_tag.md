---
id: VARIABLE-GCP_PD_CSI_PLUGIN_IMAGE_TAG
type: variable
title: gcp_pd_csi_plugin_image_tag
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - gcp_pd_csi_plugin_image_tag
tags:
  - gcp
  - csi
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Image tag for the GCP PD CSI driver plugin, derived from the plugin version."
relations: []
---

# gcp_pd_csi_plugin_image_tag

## Summary
Container image tag for the GCP Persistent Disk CSI driver plugin. It is computed from `gcp_pd_csi_plugin_version` by prefixing a `v`, e.g. `v1.9.2`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as `gcp_pd_csi_plugin_image_tag: "v{{ gcp_pd_csi_plugin_version }}"`. The computed expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0; with the default `gcp_pd_csi_plugin_version: "1.9.2"` it resolves to `v1.9.2`.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on `gcp_pd_csi_plugin_version`. Related variables: `gcp_pd_csi_plugin_image_repo`, `gcp_pd_csi_enabled`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
