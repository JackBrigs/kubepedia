---
id: VARIABLE-SYSTEM_CPU_RESERVED
type: variable
title: system_cpu_reserved
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - system_cpu_reserved
tags:
  - kubelet
  - resources
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "CPU amount reserved for system daemons via kubelet system-reserved; default 500m"
relations: []
---

# system_cpu_reserved

## Summary
Amount of CPU reserved for system daemons (OS-level, non-Kubernetes processes)
through the kubelet `system-reserved` configuration. Default is `500m`.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml`:

```yaml
system_cpu_reserved: "500m"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Part of the kubelet system-reserved settings,
alongside `system_memory_reserved` and `system_ephemeral_storage_reserved`.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
