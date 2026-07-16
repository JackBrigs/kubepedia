---
id: VARIABLE-DOCKER_DEBIAN_REPO_BASE_URL
type: variable
title: docker_debian_repo_base_url
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - docker_debian_repo_base_url
tags:
  - docker
  - repository
  - debian
sources:
  - type: code
    path: roles/container-engine/docker/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/docker/defaults/main.yml
    note: "Base URL of the Docker APT repository for Debian; default https://download.docker.com/linux/debian"
relations: []
---

# docker_debian_repo_base_url

## Summary
Base URL of the upstream Docker APT repository used on Debian hosts when installing the Docker container engine. Defaults to `https://download.docker.com/linux/debian`.

## Implementation
Defined in `roles/container-engine/docker/defaults/main.yml`:

```yaml
docker_debian_repo_base_url: "https://download.docker.com/linux/debian"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies on Debian when Docker is the selected container engine. Related: `docker_debian_repo_gpgkey`, `docker_debian_repo_repokey`.

## References
- roles/container-engine/docker/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
