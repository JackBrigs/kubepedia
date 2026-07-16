---
id: VARIABLE-CONTAINERD_ADDITIONAL_RUNTIMES
type: variable
title: containerd_additional_runtimes
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_additional_runtimes
tags:
  - containerd
  - runtime
sources:
  - type: code
    path: roles/container-engine/containerd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/defaults/main.yml
    note: "Defaults to an empty list []"
relations: []
---

# containerd_additional_runtimes

## Summary
List of additional containerd runtimes to configure (beyond the default runc),
for example Kata Containers or gVisor. Default is an empty list `[]`, so no
extra runtimes are configured unless the user supplies entries.

## Implementation
Defined in `roles/container-engine/containerd/defaults/main.yml` as:

```yaml
containerd_additional_runtimes: []
```

The default `[]` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.
The commented example above the definition changed shape between v2.29.x and
v2.30.0/v2.31.0 (the example runtime options were updated), but the default
value itself is unchanged. Line: L23 (v2.29.x), L22 (v2.30.0/v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Each entry typically specifies `name`,
`type`, and runtime options rendered into the containerd config.

## References
- roles/container-engine/containerd/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
