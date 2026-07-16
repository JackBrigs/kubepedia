---
id: VARIABLE-GCP_PD_CSI_PLUGIN_VERSION
type: variable
title: gcp_pd_csi_plugin_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - gcp_pd_csi_plugin_version
tags:
  - gcp
  - csi
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Pins the GCP Persistent Disk CSI driver version, default 1.9.2."
relations: []
---

# gcp_pd_csi_plugin_version

## Summary
Version of the GCP Persistent Disk CSI driver plugin that Kubespray deploys. Default is `1.9.2`. It feeds the derived image tag `gcp_pd_csi_plugin_image_tag` (`v{{ gcp_pd_csi_plugin_version }}`).

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as `gcp_pd_csi_plugin_version: "1.9.2"`. The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variables: `gcp_pd_csi_plugin_image_tag`, `gcp_pd_csi_plugin_image_repo`, `gcp_pd_csi_enabled`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
