---
id: VARIABLE-DOCKER_FEDORA_REPO_GPGKEY
type: variable
title: docker_fedora_repo_gpgkey
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - docker_fedora_repo_gpgkey
tags:
  - docker
  - repository
  - fedora
sources:
  - type: code
    path: roles/container-engine/docker/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/docker/defaults/main.yml
    note: "URL of the Docker Fedora repository GPG key; default https://download.docker.com/linux/fedora/gpg"
relations:
  - type: see_also
    target: VARIABLE-CONTAINER_MANAGER
---

# docker_fedora_repo_gpgkey

## Summary
URL of the GPG key used to verify the Docker repository on Fedora hosts. Defaults to `https://download.docker.com/linux/fedora/gpg`.

## Implementation
Defined in `roles/container-engine/docker/defaults/main.yml`:

```yaml
docker_fedora_repo_gpgkey: 'https://download.docker.com/linux/fedora/gpg'
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies on Fedora when Docker is the selected container engine. Related: `docker_fedora_repo_base_url`.

## References
- roles/container-engine/docker/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
