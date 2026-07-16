---
id: VARIABLE-DOCKER_REPO_KEY_INFO
type: variable
title: docker_repo_key_info
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - docker_repo_key_info
tags:
  - docker
  - repository
sources:
  - type: code
    path: roles/container-engine/docker/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/docker/defaults/main.yml
    note: "Docker repo GPG key definition; default has empty repo_keys, overridden per-distro"
relations: []
---

# docker_repo_key_info

## Summary
Describes the GPG signing key(s) for the Docker CE package repository. The role default is an empty mapping; distribution-specific `vars/*.yml` files supply the key URL and fingerprint.

## Implementation
Default in `roles/container-engine/docker/defaults/main.yml` (empty):

```yaml
docker_repo_key_info:
  repo_keys:
```

Overridden per distro, e.g. `roles/container-engine/docker/vars/ubuntu.yml`:

```yaml
docker_repo_key_info:
  url: '{{ docker_ubuntu_repo_gpgkey }}'
  repo_keys:
    - '{{ docker_ubuntu_repo_repokey }}'
```

`vars/debian.yml` provides an analogous block using the debian repo key vars. Both the default and the debian/ubuntu overrides are unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Relevant when `container_manager == 'docker'`. Related: `docker_repo_info`, `docker_ubuntu_repo_gpgkey`, `docker_ubuntu_repo_repokey`.

## References
- roles/container-engine/docker/defaults/main.yml
- roles/container-engine/docker/vars/ubuntu.yml, roles/container-engine/docker/vars/debian.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
