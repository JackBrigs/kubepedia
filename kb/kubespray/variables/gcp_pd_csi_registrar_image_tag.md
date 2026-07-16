---
id: VARIABLE-GCP_PD_CSI_REGISTRAR_IMAGE_TAG
type: variable
title: gcp_pd_csi_registrar_image_tag
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - gcp_pd_csi_registrar_image_tag
tags:
  - gcp
  - csi
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Image tag for the GCP PD CSI node-driver-registrar sidecar, default v1.2.0-gke.0."
relations: []
---

# gcp_pd_csi_registrar_image_tag

## Summary
Image tag for the GCP Persistent Disk CSI node-driver-registrar sidecar image pulled from `gcp_pd_csi_image_repo`. Default is `v1.2.0-gke.0`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as `gcp_pd_csi_registrar_image_tag: "v1.2.0-gke.0"`. The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variables: `gcp_pd_csi_image_repo`, `gcp_pd_csi_attacher_image_tag`, `gcp_pd_csi_provisioner_image_tag`, `gcp_pd_csi_driver_image_tag`, `gcp_pd_csi_enabled`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
