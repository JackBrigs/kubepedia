---
id: VARIABLE-CONTAINERD_LIMIT_MEM_LOCK
type: variable
title: containerd_limit_mem_lock
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_limit_mem_lock
tags:
  - containerd
  - systemd
sources:
  - type: code
    path: roles/container-engine/containerd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/defaults/main.yml
    note: "Sets LimitMEMLOCK for the containerd systemd unit; default \"infinity\""
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
---

# containerd_limit_mem_lock

## Summary
Controls the `LimitMEMLOCK` resource limit applied to the containerd systemd service unit (maximum locked-in-memory address space). Default is `"infinity"`.

## Implementation
Defined in `roles/container-engine/containerd/defaults/main.yml`:

```yaml
containerd_limit_mem_lock: "infinity"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Applies only when the container runtime is containerd. Related systemd-limit variables: `containerd_limit_core`, `containerd_limit_proc_num`, `containerd_limit_open_file_num`.

## References
- roles/container-engine/containerd/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
