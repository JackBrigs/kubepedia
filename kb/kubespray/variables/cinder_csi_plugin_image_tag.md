---
id: VARIABLE-CINDER_CSI_PLUGIN_IMAGE_TAG
type: variable
title: cinder_csi_plugin_image_tag
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cinder_csi_plugin_image_tag
tags:
  - cinder
  - csi
  - image
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Container image tag for the Cinder CSI plugin"
relations: []
---

# cinder_csi_plugin_image_tag

## Summary
Container image tag for the OpenStack Cinder CSI plugin. Computed as `v` prefixed to `cinder_csi_plugin_version`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
cinder_csi_plugin_image_tag: "v{{ cinder_csi_plugin_version }}"
```

This computed expression is unchanged across v2.29.0-v2.31.0 (line 348 in v2.29.0, 350 in v2.29.1, 351 in v2.30.0, 338 in v2.31.0). With the default `cinder_csi_plugin_version` of `1.30.0`, the resulting tag is `v1.30.0`.

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Depends on `cinder_csi_plugin_version`. Paired with `cinder_csi_plugin_image_repo`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
