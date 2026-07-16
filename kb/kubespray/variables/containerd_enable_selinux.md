---
id: VARIABLE-CONTAINERD_ENABLE_SELINUX
type: variable
title: containerd_enable_selinux
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_enable_selinux
tags:
  - containerd
  - security
sources:
  - type: code
    path: roles/container-engine/containerd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/defaults/main.yml
    note: "Enables SELinux support in the containerd CRI plugin; default false"
relations: []
---

# containerd_enable_selinux

## Summary
Controls whether SELinux support is enabled in the containerd CRI plugin configuration. Default is `false`.

## Implementation
Defined in `roles/container-engine/containerd/defaults/main.yml`:

```yaml
containerd_enable_selinux: false
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Related security toggles: `containerd_disable_apparmor`.

## References
- roles/container-engine/containerd/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
