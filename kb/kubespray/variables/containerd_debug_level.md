---
id: VARIABLE-CONTAINERD_DEBUG_LEVEL
type: variable
title: containerd_debug_level
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_debug_level
tags:
  - containerd
  - debug
sources:
  - type: code
    path: roles/container-engine/containerd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/defaults/main.yml
    note: "Defaults to \"info\""
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
---

# containerd_debug_level

## Summary
Log level for containerd, written into the `[debug]` section of the containerd
configuration. Default is `"info"`.

## Implementation
Defined in `roles/container-engine/containerd/defaults/main.yml` as:

```yaml
containerd_debug_level: "info"
```

The default `"info"` is unchanged across v2.29.0, v2.29.1, v2.30.0, and
v2.31.0. Line: L50 (v2.29.x), L49 (v2.30.0/v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Part of the containerd `[debug]` group with
`containerd_debug_address`, `containerd_debug_format`, `containerd_debug_uid`,
and `containerd_debug_gid`.

## References
- roles/container-engine/containerd/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
