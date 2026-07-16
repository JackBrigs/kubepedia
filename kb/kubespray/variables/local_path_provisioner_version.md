---
id: VARIABLE-LOCAL_PATH_PROVISIONER_VERSION
type: variable
title: local_path_provisioner_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: "0.0.32"
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - local_path_provisioner_version
tags:
  - storage
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Defines local_path_provisioner_version with default 0.0.32"
relations: []
---

# local_path_provisioner_version

## Summary
Version of the Rancher local-path-provisioner addon that Kubespray deploys. Default is `0.0.32`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
local_path_provisioner_version: "0.0.32"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Feeds `local_path_provisioner_image_tag` (`v{{ local_path_provisioner_version }}`).

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
