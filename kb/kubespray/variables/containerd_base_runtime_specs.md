---
id: VARIABLE-CONTAINERD_BASE_RUNTIME_SPECS
type: variable
title: containerd_base_runtime_specs
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_base_runtime_specs
tags:
  - containerd
  - runtime
sources:
  - type: code
    path: roles/container-engine/containerd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/defaults/main.yml
    note: "Map of base runtime spec files rendered for containerd"
relations: []
---

# containerd_base_runtime_specs

## Summary
Map of containerd base runtime spec files to generate on the host. By default
it defines a single `cri-base.json` produced by merging the default base
runtime spec with `containerd_default_base_runtime_spec_patch`.

## Implementation
Defined in `roles/container-engine/containerd/defaults/main.yml` as:

```yaml
containerd_base_runtime_specs:
  cri-base.json: "{{ containerd_default_base_runtime_spec | combine(containerd_default_base_runtime_spec_patch, recursive=1) }}"
```

This computed default is unchanged across v2.29.0, v2.29.1, v2.30.0, and
v2.31.0. Line: L43 (v2.29.x), L42 (v2.30.0/v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on
`containerd_default_base_runtime_spec` and
`containerd_default_base_runtime_spec_patch`.

## References
- roles/container-engine/containerd/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
