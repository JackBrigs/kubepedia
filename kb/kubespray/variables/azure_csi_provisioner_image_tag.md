---
id: VARIABLE-AZURE_CSI_PROVISIONER_IMAGE_TAG
type: variable
title: azure_csi_provisioner_image_tag
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - azure_csi_provisioner_image_tag
tags:
  - csi
  - azure
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Default azure_csi_provisioner_image_tag: \"v2.2.2\""
relations: []
---

# azure_csi_provisioner_image_tag

## Summary
Image tag for the csi-provisioner sidecar used by the Azure Disk CSI driver. Default is `v2.2.2`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
azure_csi_provisioner_image_tag: "v2.2.2"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Combined with `azure_csi_image_repo`. Applies when Azure Disk CSI is enabled (`azure_csi_enabled`).

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
