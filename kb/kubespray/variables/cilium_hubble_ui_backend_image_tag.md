---
id: VARIABLE-CILIUM_HUBBLE_UI_BACKEND_IMAGE_TAG
type: variable
title: cilium_hubble_ui_backend_image_tag
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_hubble_ui_backend_image_tag
tags:
  - cilium
  - hubble
  - images
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Defines the image tag for the Hubble UI backend; default v0.13.3"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_hubble_ui_backend_image_tag

## Summary
Sets the container image tag for the Cilium Hubble UI backend component. Default: `v0.13.3`. Used only when Hubble UI is enabled.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
cilium_hubble_ui_backend_image_tag: "v0.13.3"
```

The value is consumed in `roles/network_plugin/cilium/templates/values.yaml.j2` (`hubble.ui.backend.image.tag`). The default `v0.13.3` is unchanged across v2.29.0-v2.31.0 (only the line number in `download.yml` shifts between tags).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variables: `cilium_hubble_ui_backend_image_repo`, `cilium_hubble_ui_image_repo`, `cilium_hubble_ui_image_tag`, `cilium_enable_hubble`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- roles/network_plugin/cilium/templates/values.yaml.j2
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
