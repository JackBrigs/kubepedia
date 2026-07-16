---
id: VARIABLE-DOCKER_DEBIAN_REPO_GPGKEY
type: variable
title: docker_debian_repo_gpgkey
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - docker_debian_repo_gpgkey
tags:
  - docker
  - repository
  - debian
sources:
  - type: code
    path: roles/container-engine/docker/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/docker/defaults/main.yml
    note: "URL of the Docker Debian repository GPG key; default https://download.docker.com/linux/debian/gpg"
relations: []
---

# docker_debian_repo_gpgkey

## Summary
URL of the GPG key used to verify the Docker APT repository on Debian hosts. Defaults to `https://download.docker.com/linux/debian/gpg`.

## Implementation
Defined in `roles/container-engine/docker/defaults/main.yml`:

```yaml
docker_debian_repo_gpgkey: 'https://download.docker.com/linux/debian/gpg'
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies on Debian when Docker is the selected container engine. Related: `docker_debian_repo_base_url`, `docker_debian_repo_repokey`.

## References
- roles/container-engine/docker/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
