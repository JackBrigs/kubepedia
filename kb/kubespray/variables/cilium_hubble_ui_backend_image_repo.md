---
id: VARIABLE-CILIUM_HUBBLE_UI_BACKEND_IMAGE_REPO
type: variable
title: cilium_hubble_ui_backend_image_repo
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_hubble_ui_backend_image_repo
tags:
  - cilium
  - hubble
  - images
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Defines the container image repository for the Hubble UI backend; default {{ quay_image_repo }}/cilium/hubble-ui-backend"
relations: []
---

# cilium_hubble_ui_backend_image_repo

## Summary
Sets the container image repository for the Cilium Hubble UI backend component. Default: `{{ quay_image_repo }}/cilium/hubble-ui-backend` (resolves to a quay.io path). Used only when Hubble UI is enabled.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
cilium_hubble_ui_backend_image_repo: "{{ quay_image_repo }}/cilium/hubble-ui-backend"
```

The value is consumed in `roles/network_plugin/cilium/templates/values.yaml.j2` (`hubble.ui.backend.image.repository`). Unchanged across v2.29.0-v2.31.0 (only the line number in `download.yml` shifts between tags).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variables: `cilium_hubble_ui_backend_image_tag`, `cilium_hubble_ui_image_repo`, `cilium_hubble_ui_image_tag`, `cilium_enable_hubble`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- roles/network_plugin/cilium/templates/values.yaml.j2
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
