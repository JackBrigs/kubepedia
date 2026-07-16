---
id: VARIABLE-PODMAN_REMOVE_PACKAGES_YUM
type: variable
title: podman_remove_packages_yum
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - podman_remove_packages_yum
tags:
  - container-engine
  - docker
sources:
  - type: code
    path: roles/container-engine/docker/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/docker/defaults/main.yml
    note: "List of yum/dnf packages removed when installing Docker (default: podman)"
relations: []
---

# podman_remove_packages_yum

## Summary
List of RPM (yum/dnf) packages that the Docker role removes before/while installing Docker, to avoid conflicts. Defaults to a single entry: `podman`.

## Implementation
Defined in `roles/container-engine/docker/defaults/main.yml` (line 38):

```yaml
podman_remove_packages_yum:
  - podman
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0 (unchanged). Applies on yum/dnf (RHEL-family) hosts when the Docker container engine is selected. Related: `docker_remove_packages_apt`.

## References
- roles/container-engine/docker/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
