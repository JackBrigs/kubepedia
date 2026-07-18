---
id: VARIABLE-KATA_CONTAINERS_QEMU_DEBUG
type: variable
title: kata_containers_qemu_debug
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - kata_containers_qemu_debug
tags:
  - container-engine
  - kata-containers
  - variable
sources:
  - type: code
    path: roles/container-engine/kata-containers/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/kata-containers/defaults/main.yml
    note: "default: false"
relations: []
---
<!-- generated: variable-stub -->

# kata_containers_qemu_debug

## Summary

Kubespray variable `kata_containers_qemu_debug` — default `false`. Defined in `roles/container-engine/kata-containers/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/container-engine/kata-containers/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
kata_containers_qemu_debug: false
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/container-engine/kata-containers/defaults/main.yml` (Kubespray `v2.31.0`).
