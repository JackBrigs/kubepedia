---
id: VARIABLE-CONTAINERD_REGISTRY_AUTH
type: variable
title: containerd_registry_auth
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_registry_auth
tags:
  - containerd
  - registry
sources:
  - type: code
    path: roles/container-engine/containerd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/defaults/main.yml
    note: "List of per-registry authentication entries; default empty list"
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
---

# containerd_registry_auth

## Summary
Holds per-registry authentication entries (registry + credentials) for containerd. Default is an empty list `[]`, i.e. no registry auth configured.

## Implementation
Defined in `roles/container-engine/containerd/defaults/main.yml`:

```yaml
containerd_registry_auth: []
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Applies only when the container runtime is containerd. Related variable: `containerd_registries_mirrors`.

## References
- roles/container-engine/containerd/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
