---
id: VARIABLE-CONTAINERD_LIMIT_CORE
type: variable
title: containerd_limit_core
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_limit_core
tags:
  - containerd
  - systemd
sources:
  - type: code
    path: roles/container-engine/containerd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/defaults/main.yml
    note: "Sets LimitCORE for the containerd systemd unit; default \"infinity\""
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
---

# containerd_limit_core

## Summary
Controls the `LimitCORE` resource limit applied to the containerd systemd service unit (maximum size of a core dump). Default is `"infinity"`.

## Implementation
Defined in `roles/container-engine/containerd/defaults/main.yml`:

```yaml
containerd_limit_core: "infinity"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Applies only when the container runtime is containerd. Related systemd-limit variables: `containerd_limit_proc_num`, `containerd_limit_open_file_num`, `containerd_limit_mem_lock`.

## References
- roles/container-engine/containerd/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
