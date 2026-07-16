---
id: VARIABLE-CONTAINERD_USE_SYSTEMD_CGROUP
type: variable
title: containerd_use_systemd_cgroup
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_use_systemd_cgroup
tags:
  - containerd
  - cgroup
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Enables the systemd cgroup driver for the containerd runc runtime; default true"
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
---

# containerd_use_systemd_cgroup

## Summary
Boolean toggle that makes containerd's runc runtime use the systemd cgroup driver (`SystemdCgroup = true`). Default: `true`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
containerd_use_systemd_cgroup: true
```

The default value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only line numbers shift between tags).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies only when containerd is the container runtime. Should stay aligned with the kubelet cgroup driver.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
