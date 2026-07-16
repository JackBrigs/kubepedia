---
id: VARIABLE-GCP_PD_CSI_ENABLED
type: variable
title: gcp_pd_csi_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - gcp_pd_csi_enabled
tags:
  - gcp
  - csi
  - storage
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Toggle for deploying the GCP Persistent Disk CSI driver, default false."
relations: []
---

# gcp_pd_csi_enabled

## Summary
Boolean toggle that controls whether Kubespray deploys the GCP Persistent Disk CSI driver. Default is `false` (the driver is not installed unless explicitly enabled).

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as `gcp_pd_csi_enabled: false`. The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. It is also shown commented out in `inventory/sample/group_vars/all/gcp.yml` as `# gcp_pd_csi_enabled: true`.

## Compatibility
Kubespray v2.29.0 through v2.31.0. When set to `true`, the GCP PD CSI image and sidecar variables apply. Related variables: `gcp_pd_csi_plugin_version`, `gcp_pd_csi_image_repo`, `gcp_pd_csi_driver_image_tag`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- inventory/sample/group_vars/all/gcp.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
