---
id: VARIABLE-CONTAINERD_PACKAGE_INFO
type: variable
title: containerd_package_info
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_package_info
tags:
  - containerd
  - packages
sources:
  - type: code
    path: roles/container-engine/docker/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/docker/defaults/main.yml
    note: "Package descriptor consumed by the docker role; default has an empty pkgs list"
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
---

# containerd_package_info

## Summary
Package descriptor (a `pkgs` mapping) used by the docker container-engine role when installing containerd alongside Docker. The default declares an empty `pkgs` list, to be populated per-distribution.

## Implementation
Defined in `roles/container-engine/docker/defaults/main.yml`:

```yaml
containerd_package_info:
  pkgs:
```

`pkgs` has no inline entries in the default; the empty mapping is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. This variable lives in the `docker` role's defaults (used when Docker is the container manager), distinct from the standalone `containerd` role.

## References
- roles/container-engine/docker/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
