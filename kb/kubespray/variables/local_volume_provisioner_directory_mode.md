---
id: VARIABLE-LOCAL_VOLUME_PROVISIONER_DIRECTORY_MODE
type: variable
title: local_volume_provisioner_directory_mode
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - local_volume_provisioner_directory_mode
tags:
  - storage
  - addons
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Defines local_volume_provisioner_directory_mode with default 0700"
relations: []
---

# local_volume_provisioner_directory_mode

## Summary
Filesystem permission mode applied to directories managed by the local volume provisioner addon. Default is `0700`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
local_volume_provisioner_directory_mode: "0700"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Part of the local volume provisioner addon configuration.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
