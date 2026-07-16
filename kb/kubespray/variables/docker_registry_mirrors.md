---
id: VARIABLE-DOCKER_REGISTRY_MIRRORS
type: variable
title: docker_registry_mirrors
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - docker_registry_mirrors
tags:
  - docker
  - registry
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "List of additional registry mirrors; default [] (empty)"
relations: []
---

# docker_registry_mirrors

## Summary
A list of additional registry mirrors (for example, a China registry mirror) passed to the Docker daemon. Empty by default. Rendered into the daemon config by `roles/container-engine/docker/templates/docker-options.conf.j2`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
## A list of additional registry mirrors, for example China registry mirror. Empty by default.
# docker_registry_mirrors:
#   - https://registry.docker-cn.com
#   - https://mirror.aliyuncs.com
docker_registry_mirrors: []
```

Value is unchanged (`[]`) across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Relevant only when `container_manager == 'docker'`. Consumed by `roles/container-engine/docker/templates/docker-options.conf.j2`. Related: `docker_insecure_registries`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
