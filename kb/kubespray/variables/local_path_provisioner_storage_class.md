---
id: VARIABLE-LOCAL_PATH_PROVISIONER_STORAGE_CLASS
type: variable
title: local_path_provisioner_storage_class
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - local_path_provisioner_storage_class
tags:
  - kubernetes-apps
  - external-provisioner
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/external_provisioner/local_path_provisioner/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/external_provisioner/local_path_provisioner/defaults/main.yml
    note: "default: local-path"
relations: []
---
<!-- generated: variable-stub -->

# local_path_provisioner_storage_class

## Summary

Kubespray variable `local_path_provisioner_storage_class` — default `local-path`. Defined in `roles/kubernetes-apps/external_provisioner/local_path_provisioner/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/external_provisioner/local_path_provisioner/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
local_path_provisioner_storage_class: local-path
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/external_provisioner/local_path_provisioner/defaults/main.yml` (Kubespray `v2.31.0`).
