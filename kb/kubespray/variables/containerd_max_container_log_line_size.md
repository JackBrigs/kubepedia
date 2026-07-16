---
id: VARIABLE-CONTAINERD_MAX_CONTAINER_LOG_LINE_SIZE
type: variable
title: containerd_max_container_log_line_size
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_max_container_log_line_size
tags:
  - containerd
  - logging
sources:
  - type: code
    path: roles/container-engine/containerd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/defaults/main.yml
    note: "Max container log line size passed to the containerd CRI plugin; default 16384"
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
---

# containerd_max_container_log_line_size

## Summary
Sets the maximum size (in bytes) of a single container log line for the containerd CRI plugin. Lines longer than this are split. Default is `16384`.

## Implementation
Defined in `roles/container-engine/containerd/defaults/main.yml`:

```yaml
containerd_max_container_log_line_size: 16384
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Applies only when the container runtime is containerd; consumed while rendering the containerd CRI configuration.

## References
- roles/container-engine/containerd/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
