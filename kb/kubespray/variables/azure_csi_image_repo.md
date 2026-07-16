---
id: VARIABLE-AZURE_CSI_IMAGE_REPO
type: variable
title: azure_csi_image_repo
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - azure_csi_image_repo
tags:
  - csi
  - azure
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Default azure_csi_image_repo: \"mcr.microsoft.com/oss/kubernetes-csi\""
relations: []
---

# azure_csi_image_repo

## Summary
Container image registry/repository for the Azure Disk CSI sidecar images (attacher, provisioner, resizer, livenessprobe, node-registrar). Default is `mcr.microsoft.com/oss/kubernetes-csi`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
azure_csi_image_repo: "mcr.microsoft.com/oss/kubernetes-csi"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Combined with the `azure_csi_*_image_tag` variables to build the sidecar image references. Distinct from `azure_csi_plugin_image_repo` (the driver plugin itself).

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
