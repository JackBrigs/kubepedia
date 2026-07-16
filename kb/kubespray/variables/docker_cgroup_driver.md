---
id: VARIABLE-DOCKER_CGROUP_DRIVER
type: variable
title: docker_cgroup_driver
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - docker_cgroup_driver
tags:
  - docker
  - container-runtime
sources:
  - type: code
    path: roles/container-engine/docker/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/docker/defaults/main.yml
    note: "Defines docker_cgroup_driver with default systemd"
relations: []
---

# docker_cgroup_driver

## Summary
Cgroup driver configured for the Docker daemon. Default is `systemd`, matching the kubelet's default cgroup driver.

## Implementation
Defined in `roles/container-engine/docker/defaults/main.yml` (line 17 in all four tags):

```yaml
docker_cgroup_driver: systemd
```

The default value `systemd` is unchanged across v2.29.0, v2.29.1, v2.30.0 and v2.31.0.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Only relevant when `container_manager` is `docker`; the Docker container engine is deprecated upstream but still selectable in this range.

## References
- roles/container-engine/docker/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
