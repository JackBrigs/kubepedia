---
id: VARIABLE-CONTAINERD_DEBUG_FORMAT
type: variable
title: containerd_debug_format
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_debug_format
tags:
  - containerd
  - debug
sources:
  - type: code
    path: roles/container-engine/containerd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/defaults/main.yml
    note: "Defaults to an empty string"
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
---

# containerd_debug_format

## Summary
Output format for containerd debug logging, written into the `[debug]` section
of the containerd configuration. Default is an empty string `""`, leaving the
containerd default format in effect.

## Implementation
Defined in `roles/container-engine/containerd/defaults/main.yml` as:

```yaml
containerd_debug_format: ""
```

The default `""` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.
Line: L51 (v2.29.x), L50 (v2.30.0/v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Part of the containerd `[debug]` group with
`containerd_debug_address`, `containerd_debug_level`, `containerd_debug_uid`,
and `containerd_debug_gid`.

## References
- roles/container-engine/containerd/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
