---
id: VARIABLE-DOCKER_VERSION
type: variable
title: docker_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - docker_version
tags:
  - docker
  - container-runtime
sources:
  - type: code
    path: roles/container-engine/docker/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/docker/defaults/main.yml
    note: "Docker CE version installed by the docker role; default '28.3'"
relations:
  - type: see_also
    target: VARIABLE-CONTAINER_MANAGER
---

# docker_version

## Summary
Sets the Docker CE version installed by the `container-engine/docker` role (used together with `docker_cli_version`, which defaults to `{{ docker_version }}`). Default is `'28.3'`. Per-distribution `vars/*.yml` files map this value to the actual `docker_versioned_pkg` package string, but the version selector itself lives in the role defaults.

## Implementation
Defined in `roles/container-engine/docker/defaults/main.yml`:

```yaml
docker_version: '28.3'
docker_cli_version: "{{ docker_version }}"
```

Value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies only when `container_manager == 'docker'`. Related: `docker_cli_version`, `docker_versioned_pkg` (per-distro `roles/container-engine/docker/vars/*.yml`).

## References
- roles/container-engine/docker/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
