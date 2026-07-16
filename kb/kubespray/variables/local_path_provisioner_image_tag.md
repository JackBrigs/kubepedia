---
id: VARIABLE-LOCAL_PATH_PROVISIONER_IMAGE_TAG
type: variable
title: local_path_provisioner_image_tag
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - local_path_provisioner_image_tag
tags:
  - storage
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Computes local_path_provisioner_image_tag from local_path_provisioner_version"
relations: []
---

# local_path_provisioner_image_tag

## Summary
Container image tag for the local-path-provisioner addon. Computed from `local_path_provisioner_version` as `v{{ local_path_provisioner_version }}`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
local_path_provisioner_image_tag: "v{{ local_path_provisioner_version }}"
```

The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Depends on `local_path_provisioner_version`; paired with `local_path_provisioner_image_repo`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
