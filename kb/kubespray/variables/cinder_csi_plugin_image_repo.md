---
id: VARIABLE-CINDER_CSI_PLUGIN_IMAGE_REPO
type: variable
title: cinder_csi_plugin_image_repo
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cinder_csi_plugin_image_repo
tags:
  - cinder
  - csi
  - image
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Container image repository for the Cinder CSI plugin"
relations: []
---

# cinder_csi_plugin_image_repo

## Summary
Container image repository path for the OpenStack Cinder CSI plugin. Derived from `kube_image_repo` with the `/provider-os/cinder-csi-plugin` suffix.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
cinder_csi_plugin_image_repo: "{{ kube_image_repo }}/provider-os/cinder-csi-plugin"
```

This computed expression is unchanged across v2.29.0-v2.31.0 (line 347 in v2.29.0, 349 in v2.29.1, 350 in v2.30.0, 337 in v2.31.0).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Depends on `kube_image_repo`. Paired with `cinder_csi_plugin_image_tag` and `cinder_csi_plugin_version`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
