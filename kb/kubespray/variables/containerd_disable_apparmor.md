---
id: VARIABLE-CONTAINERD_DISABLE_APPARMOR
type: variable
title: containerd_disable_apparmor
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_disable_apparmor
tags:
  - containerd
  - security
sources:
  - type: code
    path: roles/container-engine/containerd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/defaults/main.yml
    note: "Disables AppArmor in containerd CRI config; default false"
relations: []
---

# containerd_disable_apparmor

## Summary
Controls whether AppArmor is disabled in the containerd CRI plugin configuration. Default is `false` (AppArmor not disabled).

## Implementation
Defined in `roles/container-engine/containerd/defaults/main.yml`:

```yaml
containerd_disable_apparmor: false
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Related security toggles: `containerd_enable_selinux`.

## References
- roles/container-engine/containerd/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
