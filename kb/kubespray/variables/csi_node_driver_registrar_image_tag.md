---
id: VARIABLE-CSI_NODE_DRIVER_REGISTRAR_IMAGE_TAG
type: variable
title: csi_node_driver_registrar_image_tag
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - csi_node_driver_registrar_image_tag
tags:
  - csi
  - download
  - image
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Image tag for the sig-storage csi-node-driver-registrar sidecar."
relations: []
---

# csi_node_driver_registrar_image_tag

## Summary
Sets the container image tag for the CSI node-driver-registrar sidecar. Default is `v2.4.0`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
csi_node_driver_registrar_image_tag: "v2.4.0"
```

The value `v2.4.0` is unchanged across v2.29.0-v2.31.0.

## Compatibility
Present across Kubespray v2.29.0-v2.31.0. Paired with `csi_node_driver_registrar_image_repo`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
