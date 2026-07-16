---
id: VARIABLE-CSI_NODE_DRIVER_REGISTRAR_IMAGE_REPO
type: variable
title: csi_node_driver_registrar_image_repo
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - csi_node_driver_registrar_image_repo
tags:
  - csi
  - download
  - image
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Image repository for the sig-storage csi-node-driver-registrar sidecar."
relations: []
---

# csi_node_driver_registrar_image_repo

## Summary
Sets the container image repository for the CSI node-driver-registrar sidecar. Default is a computed expression `{{ kube_image_repo }}/sig-storage/csi-node-driver-registrar`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
csi_node_driver_registrar_image_repo: "{{ kube_image_repo }}/sig-storage/csi-node-driver-registrar"
```

The value (the same computed expression) is unchanged across v2.29.0-v2.31.0.

## Compatibility
Present across Kubespray v2.29.0-v2.31.0. Derives from `kube_image_repo`. Paired with `csi_node_driver_registrar_image_tag`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
