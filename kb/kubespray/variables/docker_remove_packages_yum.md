---
id: VARIABLE-DOCKER_REMOVE_PACKAGES_YUM
type: variable
title: docker_remove_packages_yum
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - docker_remove_packages_yum
tags:
  - docker
  - yum
sources:
  - type: code
    path: roles/container-engine/docker/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/docker/defaults/main.yml
    note: "Old yum docker packages removed before install; default list of 11 packages"
relations:
  - type: see_also
    target: VARIABLE-CONTAINER_MANAGER
---

# docker_remove_packages_yum

## Summary
List of old/conflicting Docker yum package names removed on RHEL-family hosts before installing Docker CE. Used by `roles/container-engine/docker/tasks/pre-upgrade.yml`.

## Implementation
Defined in `roles/container-engine/docker/defaults/main.yml`:

```yaml
docker_remove_packages_yum:
  - docker
  - docker-common
  - docker-engine
  - docker-selinux.noarch
  - docker-client
  - docker-client-latest
  - docker-latest
  - docker-latest-logrotate
  - docker-logrotate
  - docker-engine-selinux.noarch
```

Value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies to yum/dnf-based distros when `container_manager == 'docker'`. Related: `docker_remove_packages_apt`, `podman_remove_packages_yum`.

## References
- roles/container-engine/docker/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
