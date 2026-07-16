---
id: VARIABLE-CONTAINERD_DEFAULT_BASE_RUNTIME_SPEC_PATCH
type: variable
title: containerd_default_base_runtime_spec_patch
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_default_base_runtime_spec_patch
tags:
  - containerd
  - runtime
sources:
  - type: code
    path: roles/container-engine/containerd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/defaults/main.yml
    note: "Patch merged into the default base runtime spec; sets RLIMIT_NOFILE"
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
---

# containerd_default_base_runtime_spec_patch

## Summary
Patch merged (recursively) into containerd's default base runtime spec. By
default it sets the process `RLIMIT_NOFILE` hard and soft limits from
`containerd_base_runtime_spec_rlimit_nofile`.

## Implementation
Defined in `roles/container-engine/containerd/defaults/main.yml` as:

```yaml
containerd_default_base_runtime_spec_patch:
  process:
    rlimits:
      - type: RLIMIT_NOFILE
        hard: "{{ containerd_base_runtime_spec_rlimit_nofile }}"
        soft: "{{ containerd_base_runtime_spec_rlimit_nofile }}"
```

This default is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.
Line: L32 (v2.29.x), L31 (v2.30.0/v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Consumes
`containerd_base_runtime_spec_rlimit_nofile` and is combined into
`containerd_base_runtime_specs` (`cri-base.json`).

## References
- roles/container-engine/containerd/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
