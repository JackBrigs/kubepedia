---
id: VARIABLE-CINDER_CSI_PLUGIN_VERSION
type: variable
title: cinder_csi_plugin_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: "1.30.0"
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cinder_csi_plugin_version
tags:
  - cinder
  - csi
  - version
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Pinned version of the Cinder CSI plugin, default 1.30.0"
relations: []
---

# cinder_csi_plugin_version

## Summary
Pinned version string of the OpenStack Cinder CSI plugin. Default value is `1.30.0`. Drives the plugin's image tag.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
cinder_csi_plugin_version: "1.30.0"
```

The value `1.30.0` is unchanged across v2.29.0-v2.31.0 (line 346 in v2.29.0, 348 in v2.29.1, 349 in v2.30.0, 336 in v2.31.0).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Consumed by `cinder_csi_plugin_image_tag` (`v{{ cinder_csi_plugin_version }}`).

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
