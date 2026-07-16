---
id: VARIABLE-REGISTRY_IMAGE_REPO
type: variable
title: registry_image_repo
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - registry_image_repo
tags:
  - registry
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Image repository path for the in-cluster registry container"
relations: []
---

# registry_image_repo

## Summary
Image repository path for the container image used by the in-cluster registry addon. Defaults to `{{ docker_image_repo }}/library/registry`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
registry_image_repo: "{{ docker_image_repo }}/library/registry"
```

Unchanged across v2.29.0-v2.31.0 (line 298 in v2.29.0, line 295 in v2.31.0).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Derives from `docker_image_repo`; used together with `registry_image_tag` when `registry_enabled` is true.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
