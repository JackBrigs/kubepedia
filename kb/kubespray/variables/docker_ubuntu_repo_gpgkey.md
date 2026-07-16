---
id: VARIABLE-DOCKER_UBUNTU_REPO_GPGKEY
type: variable
title: docker_ubuntu_repo_gpgkey
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - docker_ubuntu_repo_gpgkey
tags:
  - docker
  - repository
  - ubuntu
sources:
  - type: code
    path: roles/container-engine/docker/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/docker/defaults/main.yml
    note: "Ubuntu docker-ce apt repo GPG key URL"
relations: []
---

# docker_ubuntu_repo_gpgkey

## Summary
URL of the GPG key for the Ubuntu Docker CE apt repository. Referenced by the Ubuntu `docker_repo_key_info` override.

## Implementation
Defined in `roles/container-engine/docker/defaults/main.yml`:

```yaml
docker_ubuntu_repo_gpgkey: 'https://download.docker.com/linux/ubuntu/gpg'
```

Value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. Consumed as `docker_repo_key_info.url` in `roles/container-engine/docker/vars/ubuntu.yml`.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Relevant on Ubuntu hosts when `container_manager == 'docker'`. Related: `docker_ubuntu_repo_base_url`, `docker_ubuntu_repo_repokey`, `docker_repo_key_info`.

## References
- roles/container-engine/docker/defaults/main.yml
- roles/container-engine/docker/vars/ubuntu.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
