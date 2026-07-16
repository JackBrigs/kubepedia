---
id: VARIABLE-DOCKER_CONTAINERD_VERSION
type: variable
title: docker_containerd_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: "1.6.32"
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - docker_containerd_version
tags:
  - docker
  - containerd
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "containerd version installed with the Docker container engine, default 1.6.32"
relations:
  - type: see_also
    target: VARIABLE-CONTAINER_MANAGER
---

# docker_containerd_version

## Summary
Version of containerd installed alongside the Docker container engine (Docker's bundled containerd, distinct from the standalone containerd runtime). Defaults to `1.6.32`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
docker_containerd_version: 1.6.32
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies when the Docker container engine is selected.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
