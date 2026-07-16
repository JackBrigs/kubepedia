---
id: VARIABLE-GCP_PD_CSI_IMAGE_REPO
type: variable
title: gcp_pd_csi_image_repo
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - gcp_pd_csi_image_repo
tags:
  - gcp
  - csi
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Registry hosting the GCP PD CSI sidecar images, default gke.gcr.io."
relations: []
---

# gcp_pd_csi_image_repo

## Summary
Container registry that hosts the GCP Persistent Disk CSI sidecar images (attacher, provisioner, resizer, registrar, driver). Default is `gke.gcr.io`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as `gcp_pd_csi_image_repo: "gke.gcr.io"`. The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variables: `gcp_pd_csi_driver_image_tag`, `gcp_pd_csi_attacher_image_tag`, `gcp_pd_csi_provisioner_image_tag`, `gcp_pd_csi_registrar_image_tag`, `gcp_pd_csi_enabled`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
