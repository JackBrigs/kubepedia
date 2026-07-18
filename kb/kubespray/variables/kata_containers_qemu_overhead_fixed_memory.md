---
id: VARIABLE-KATA_CONTAINERS_QEMU_OVERHEAD_FIXED_MEMORY
type: variable
title: kata_containers_qemu_overhead_fixed_memory
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - kata_containers_qemu_overhead_fixed_memory
tags:
  - kubernetes-apps
  - container-runtimes
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/container_runtimes/kata_containers/defaults/main.yaml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/container_runtimes/kata_containers/defaults/main.yaml
    note: "default: 160Mi"
relations: []
---
<!-- generated: variable-stub -->

# kata_containers_qemu_overhead_fixed_memory

## Summary

Kubespray variable `kata_containers_qemu_overhead_fixed_memory` — default `160Mi`. Defined in `roles/kubernetes-apps/container_runtimes/kata_containers/defaults/main.yaml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/container_runtimes/kata_containers/defaults/main.yaml` (Kubespray `v2.31.0`):

```yaml
kata_containers_qemu_overhead_fixed_memory: 160Mi
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/container_runtimes/kata_containers/defaults/main.yaml` (Kubespray `v2.31.0`).
