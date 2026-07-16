---
id: VARIABLE-CONTAINERD_DEFAULT_RUNTIME
type: variable
title: containerd_default_runtime
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_default_runtime
tags:
  - containerd
  - runtime
sources:
  - type: code
    path: roles/container-engine/containerd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/defaults/main.yml
    note: "Defines the default containerd CRI runtime; default \"runc\""
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
---

# containerd_default_runtime

## Summary
Sets the name of the default runtime used by the containerd CRI plugin. Default is `"runc"`.

## Implementation
Defined in `roles/container-engine/containerd/defaults/main.yml`:

```yaml
containerd_default_runtime: "runc"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Selects among configured containerd runtimes (e.g. `containerd_runc_runtime`, `containerd_additional_runtimes`).

## References
- roles/container-engine/containerd/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
