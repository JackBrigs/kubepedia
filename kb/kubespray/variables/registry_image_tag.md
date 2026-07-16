---
id: VARIABLE-REGISTRY_IMAGE_TAG
type: variable
title: registry_image_tag
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - registry_image_tag
tags:
  - registry
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Image tag for the in-cluster registry container, derived from registry_version"
relations: []
---

# registry_image_tag

## Summary
Image tag for the container image used by the in-cluster registry addon. Defaults to the value of `registry_version`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
registry_image_tag: "{{ registry_version }}"
```

Unchanged across v2.29.0-v2.31.0 (line 299 in v2.29.0, line 296 in v2.31.0).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Derives from `registry_version` (default `2.8.1`); paired with `registry_image_repo` when `registry_enabled` is true.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
