---
id: VARIABLE-DOCKER_PLUGINS
type: variable
title: docker_plugins
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - docker_plugins
tags:
  - docker
  - plugins
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "List of docker plugins to install; default [] (empty)"
relations:
  - type: see_also
    target: VARIABLE-CONTAINER_MANAGER
---

# docker_plugins

## Summary
List of Docker plugins to install using `docker plugin install --grant-all-permissions`. Empty by default, so no plugins are installed. Consumed by the `container-engine/docker` role (`roles/container-engine/docker/tasks/main.yml`).

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
## A list of plugins to install using 'docker plugin install --grant-all-permissions'
## Empty by default so no plugins will be installed.
docker_plugins: []
```

Value is unchanged (`[]`) across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Relevant only when `container_manager == 'docker'`. Consumed by `roles/container-engine/docker/tasks/main.yml`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
