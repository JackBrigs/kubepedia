---
id: VARIABLE-NVIDIA_GPU_DEVICE_PLUGIN_CONTAINER
type: variable
title: nvidia_gpu_device_plugin_container
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - nvidia_gpu_device_plugin_container
tags:
  - kubernetes-apps
  - container-engine-accelerator
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/container_engine_accelerator/nvidia_gpu/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/container_engine_accelerator/nvidia_gpu/defaults/main.yml
    note: "default: registry.k8s.io/nvidia-gpu-device-plugin@sha256:0842734032018be107f…"
relations: []
---
<!-- generated: variable-stub -->

# nvidia_gpu_device_plugin_container

## Summary

Kubespray variable `nvidia_gpu_device_plugin_container` — default `registry.k8s.io/nvidia-gpu-device-plugin@sha256:0842734032018be107f…`. Defined in `roles/kubernetes-apps/container_engine_accelerator/nvidia_gpu/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/container_engine_accelerator/nvidia_gpu/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
nvidia_gpu_device_plugin_container: registry.k8s.io/nvidia-gpu-device-plugin@sha256:0842734032018be107f…
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/container_engine_accelerator/nvidia_gpu/defaults/main.yml` (Kubespray `v2.31.0`).
