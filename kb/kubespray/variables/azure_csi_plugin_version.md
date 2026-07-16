---
id: VARIABLE-AZURE_CSI_PLUGIN_VERSION
type: variable
title: azure_csi_plugin_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - azure_csi_plugin_version
tags:
  - csi
  - azure
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Default azure_csi_plugin_version: \"1.10.0\""
relations: []
---

# azure_csi_plugin_version

## Summary
Version of the Azure Disk CSI driver plugin deployed by Kubespray. Default is `1.10.0`. It also feeds `azure_csi_plugin_image_tag` via `"v{{ azure_csi_plugin_version }}"`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
azure_csi_plugin_version: "1.10.0"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Consumed by `azure_csi_plugin_image_tag`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
