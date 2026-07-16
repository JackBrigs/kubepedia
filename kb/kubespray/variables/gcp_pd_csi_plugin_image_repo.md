---
id: VARIABLE-GCP_PD_CSI_PLUGIN_IMAGE_REPO
type: variable
title: gcp_pd_csi_plugin_image_repo
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - gcp_pd_csi_plugin_image_repo
tags:
  - gcp
  - csi
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Container image repository for the GCP PD CSI driver plugin."
relations: []
---

# gcp_pd_csi_plugin_image_repo

## Summary
Image repository path for the GCP Persistent Disk CSI driver plugin image. It is derived from `kube_image_repo` and points to the cloud-provider-gcp driver image.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as `gcp_pd_csi_plugin_image_repo: "{{ kube_image_repo }}/cloud-provider-gcp/gcp-compute-persistent-disk-csi-driver"`. The computed expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on `kube_image_repo`. Related variables: `gcp_pd_csi_plugin_image_tag`, `gcp_pd_csi_plugin_version`, `gcp_pd_csi_enabled`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
