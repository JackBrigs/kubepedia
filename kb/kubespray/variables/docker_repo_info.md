---
id: VARIABLE-DOCKER_REPO_INFO
type: variable
title: docker_repo_info
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - docker_repo_info
tags:
  - docker
  - repository
sources:
  - type: code
    path: roles/container-engine/docker/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/docker/defaults/main.yml
    note: "Docker package repo definition; default has empty repos, overridden per-distro"
relations: []
---

# docker_repo_info

## Summary
Describes the Docker CE package repository (list of repo entries) added on the host before installing Docker. The role default is an empty mapping; distribution-specific `vars/*.yml` files fill in the actual `repos` list.

## Implementation
Default in `roles/container-engine/docker/defaults/main.yml` (empty):

```yaml
docker_repo_info:
  repos:
```

Overridden per distro, e.g. `roles/container-engine/docker/vars/ubuntu.yml`:

```yaml
docker_repo_info:
  repos:
    - >
      deb [arch={{ host_architecture }}] {{ docker_ubuntu_repo_base_url }}
      {{ ansible_distribution_release | lower }}
      stable
```

`vars/debian.yml` provides an analogous block. Both the default and the debian/ubuntu overrides are unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Relevant when `container_manager == 'docker'`. Related: `docker_repo_key_info`, `docker_ubuntu_repo_base_url`, `docker_debian_repo_base_url`.

## References
- roles/container-engine/docker/defaults/main.yml
- roles/container-engine/docker/vars/ubuntu.yml, roles/container-engine/docker/vars/debian.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
