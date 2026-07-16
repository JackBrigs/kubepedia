---
id: VARIABLE-DOCKER_REMOVE_PACKAGES_APT
type: variable
title: docker_remove_packages_apt
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - docker_remove_packages_apt
tags:
  - docker
  - apt
sources:
  - type: code
    path: roles/container-engine/docker/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/docker/defaults/main.yml
    note: "Old apt docker packages removed before install; default list of 3 packages"
relations: []
---

# docker_remove_packages_apt

## Summary
List of old/conflicting Docker apt package names removed on Debian-family hosts before installing Docker CE. Used by `roles/container-engine/docker/tasks/pre-upgrade.yml`.

## Implementation
Defined in `roles/container-engine/docker/defaults/main.yml`:

```yaml
docker_remove_packages_apt:
  - docker
  - docker-engine
  - docker.io
```

Value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies to apt-based distros when `container_manager == 'docker'`. Related: `docker_remove_packages_yum`.

## References
- roles/container-engine/docker/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
