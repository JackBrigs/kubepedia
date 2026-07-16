---
id: VARIABLE-CONTAINERD_EXTRA_RUNTIME_ARGS
type: variable
title: containerd_extra_runtime_args
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_extra_runtime_args
tags:
  - containerd
  - runtime
sources:
  - type: code
    path: roles/container-engine/containerd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/defaults/main.yml
    note: "Extra options injected into the containerd CRI runtime plugin section; default empty dict"
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
---

# containerd_extra_runtime_args

## Summary
Holds extra runtime configuration options injected into the containerd CRI runtime plugin section (`[plugins."io.containerd.cri.v1.runtime"]`), for options not explicitly supported by Kubespray's variables. Default is an empty mapping.

## Implementation
Defined in `roles/container-engine/containerd/defaults/main.yml`:

```yaml
containerd_extra_runtime_args: {}
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Related: `containerd_extra_args`.

## References
- roles/container-engine/containerd/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
