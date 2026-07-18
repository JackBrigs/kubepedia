---
id: VARIABLE-REGISTRY_DISK_SIZE
type: variable
title: registry_disk_size
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - registry_disk_size
tags:
  - kubernetes-apps
  - registry
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/registry/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/registry/defaults/main.yml
    note: "default: 10Gi"
relations: []
---
<!-- generated: variable-stub -->

# registry_disk_size

## Summary

Kubespray variable `registry_disk_size` — default `10Gi`. Defined in `roles/kubernetes-apps/registry/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/registry/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
registry_disk_size: 10Gi
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/registry/defaults/main.yml` (Kubespray `v2.31.0`).
