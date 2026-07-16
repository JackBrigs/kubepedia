---
id: VARIABLE-DOCKER_INSECURE_REGISTRIES
type: variable
title: docker_insecure_registries
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - docker_insecure_registries
tags:
  - docker
  - registry
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "List of insecure registries for the Docker daemon; default empty list"
relations:
  - type: see_also
    target: VARIABLE-CONTAINER_MANAGER
---

# docker_insecure_registries

## Summary
List of registries the Docker daemon may access over plain HTTP or with untrusted TLS. Defaults to an empty list (none).

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
docker_insecure_registries: []
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies when Docker is the selected container engine. Analogous to `crio_insecure_registries` for CRI-O.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
