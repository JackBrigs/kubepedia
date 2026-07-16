---
id: VARIABLE-REGISTRY_VERSION
type: variable
title: registry_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - registry_version
tags:
  - registry
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Version of the registry container image; default 2.8.1"
relations: []
---

# registry_version

## Summary
Version string of the container-registry image used by the in-cluster registry addon. Defaults to `2.8.1`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
registry_version: "2.8.1"
```

Unchanged across v2.29.0-v2.31.0 (line 297 in v2.29.0, line 294 in v2.31.0).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Consumed by `registry_image_tag`; effective only when `registry_enabled` is true.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
