---
id: VARIABLE-NVIDIA_DRIVER_INSTALL_SUPPORTED
type: variable
title: nvidia_driver_install_supported
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - nvidia_driver_install_supported
tags:
  - kubernetes-apps
  - container-engine-accelerator
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/container_engine_accelerator/nvidia_gpu/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/container_engine_accelerator/nvidia_gpu/defaults/main.yml
    note: "default: false"
relations: []
---
<!-- generated: variable-stub -->

# nvidia_driver_install_supported

## Summary

Kubespray variable `nvidia_driver_install_supported` — default `false`. Defined in `roles/kubernetes-apps/container_engine_accelerator/nvidia_gpu/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/container_engine_accelerator/nvidia_gpu/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
nvidia_driver_install_supported: false
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/container_engine_accelerator/nvidia_gpu/defaults/main.yml` (Kubespray `v2.31.0`).
