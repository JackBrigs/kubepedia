---
id: VARIABLE-CONTAINERD_EXTRA_ARGS
type: variable
title: containerd_extra_args
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_extra_args
tags:
  - containerd
  - config
sources:
  - type: code
    path: roles/container-engine/containerd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/defaults/main.yml
    note: "Extra config appended literally to containerd config.toml; default empty string"
relations: []
---

# containerd_extra_args

## Summary
Holds extra configuration to be put literally into `{{ containerd_cfg_dir }}/config.toml`. Default is an empty string.

## Implementation
Defined in `roles/container-engine/containerd/defaults/main.yml`, with an inline comment "Extra config to be put in {{ containerd_cfg_dir }}/config.toml literally":

```yaml
containerd_extra_args: ''
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Related: `containerd_extra_runtime_args`, `containerd_cfg_dir`.

## References
- roles/container-engine/containerd/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
