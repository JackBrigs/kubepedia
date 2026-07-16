---
id: VARIABLE-DOCKER_PACKAGE_INFO
type: variable
title: docker_package_info
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - docker_package_info
tags:
  - docker
  - packages
sources:
  - type: code
    path: roles/container-engine/docker/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/docker/defaults/main.yml
    note: "Structure describing Docker packages to install; empty base default, overridden per-distro in vars/"
relations:
  - type: see_also
    target: VARIABLE-CONTAINER_MANAGER
---

# docker_package_info

## Summary
Data structure listing the Docker packages to install (and, per distro, the package manager). The base default carries an empty `pkgs` list; concrete values are supplied by OS-specific `vars/` files.

## Implementation
Defined as an empty base default in `roles/container-engine/docker/defaults/main.yml`:

```yaml
docker_package_info:
  pkgs:
```

It is overridden per distribution in `roles/container-engine/docker/vars/*.yml` (e.g. `ubuntu.yml`, `debian.yml`, `fedora.yml`, `redhat.yml`, `amazon.yml`, `suse.yml`, `clearlinux.yml`, `kylin.yml`, `uniontech.yml`), where `pkgs` is filled from the versioned package variables. Example from `vars/ubuntu.yml`:

```yaml
docker_package_info:
  pkgs:
    - "{{ containerd_versioned_pkg[docker_containerd_version | string] }}"
    - "{{ docker_cli_versioned_pkg[docker_cli_version | string] }}"
    - "{{ docker_versioned_pkg[docker_version | string] }}"
```

The base default and the per-distro override structure are unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies when Docker is the selected container engine. Effective value depends on the target OS.

## References
- roles/container-engine/docker/defaults/main.yml
- roles/container-engine/docker/vars/ubuntu.yml (and other vars/*.yml per distro)
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
