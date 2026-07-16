---
id: VARIABLE-AZURE_CSI_SNAPSHOTTER_IMAGE_TAG
type: variable
title: azure_csi_snapshotter_image_tag
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - azure_csi_snapshotter_image_tag
tags:
  - azure
  - csi
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Image tag for the Azure CSI external-snapshotter sidecar; default v3.0.3"
relations: []
---

# azure_csi_snapshotter_image_tag

## Summary
Sets the container image tag for the external-snapshotter sidecar used by the Azure CSI driver. Default value is `v3.0.3`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
azure_csi_snapshotter_image_tag: "v3.0.3"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Available in Kubespray `>=v2.29.0 <=v2.31.0`. Relevant only when the Azure CSI driver is deployed; related to the other `azure_csi_*_image_tag` and `azure_csi_plugin_*` download variables.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
