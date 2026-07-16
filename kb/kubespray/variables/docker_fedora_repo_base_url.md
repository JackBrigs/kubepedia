---
id: VARIABLE-DOCKER_FEDORA_REPO_BASE_URL
type: variable
title: docker_fedora_repo_base_url
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - docker_fedora_repo_base_url
tags:
  - docker
  - repository
  - fedora
sources:
  - type: code
    path: roles/container-engine/docker/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/docker/defaults/main.yml
    note: "Base URL of the Docker yum/dnf repository for Fedora"
relations:
  - type: see_also
    target: VARIABLE-CONTAINER_MANAGER
---

# docker_fedora_repo_base_url

## Summary
Base URL of the upstream Docker repository used on Fedora hosts when installing the Docker container engine. Interpolates the distribution major version and `$basearch`.

## Implementation
Defined in `roles/container-engine/docker/defaults/main.yml`:

```yaml
docker_fedora_repo_base_url: 'https://download.docker.com/linux/fedora/{{ ansible_distribution_major_version }}/$basearch/stable'
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies on Fedora when Docker is the selected container engine. Related: `docker_fedora_repo_gpgkey`.

## References
- roles/container-engine/docker/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
