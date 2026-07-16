---
id: VARIABLE-CONTAINERD_BASE_RUNTIME_SPEC_RLIMIT_NOFILE
type: variable
title: containerd_base_runtime_spec_rlimit_nofile
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_base_runtime_spec_rlimit_nofile
tags:
  - containerd
  - runtime
sources:
  - type: code
    path: roles/container-engine/containerd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/defaults/main.yml
    note: "Defaults to 65535"
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
---

# containerd_base_runtime_spec_rlimit_nofile

## Summary
Sets the `RLIMIT_NOFILE` (max open files) hard and soft limit applied to
containers through the containerd base runtime spec patch. Default is `65535`.

## Implementation
Defined in `roles/container-engine/containerd/defaults/main.yml` as:

```yaml
containerd_base_runtime_spec_rlimit_nofile: 65535
```

The default `65535` is unchanged across v2.29.0, v2.29.1, v2.30.0, and
v2.31.0. It is referenced by `containerd_default_base_runtime_spec_patch` for
both the hard and soft `RLIMIT_NOFILE` values. Line: L30 (v2.29.x),
L29 (v2.30.0/v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Consumed by
`containerd_default_base_runtime_spec_patch`, which feeds into
`containerd_base_runtime_specs`.

## References
- roles/container-engine/containerd/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
