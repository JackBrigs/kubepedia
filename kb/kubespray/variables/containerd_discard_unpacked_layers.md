---
id: VARIABLE-CONTAINERD_DISCARD_UNPACKED_LAYERS
type: variable
title: containerd_discard_unpacked_layers
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_discard_unpacked_layers
tags:
  - containerd
  - images
sources:
  - type: code
    path: roles/container-engine/containerd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/defaults/main.yml
    note: "Discards unpacked image layers to save disk space; default true"
relations: []
---

# containerd_discard_unpacked_layers

## Summary
Controls whether containerd discards unpacked image layers to save disk space (applies to containerd < 2.1). Default is `true`.

## Implementation
Defined in `roles/container-engine/containerd/defaults/main.yml`, with an inline comment noting it is only for containerd < 2.1:

```yaml
containerd_discard_unpacked_layers: true
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Affects the containerd CRI image pull configuration.

## References
- roles/container-engine/containerd/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
