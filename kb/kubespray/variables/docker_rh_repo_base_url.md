---
id: VARIABLE-DOCKER_RH_REPO_BASE_URL
type: variable
title: docker_rh_repo_base_url
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - docker_rh_repo_base_url
tags:
  - docker
  - repository
  - rhel
sources:
  - type: code
    path: roles/container-engine/docker/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/docker/defaults/main.yml
    note: "CentOS/RedHat docker-ce repo base URL used by rh_docker.repo template"
relations:
  - type: see_also
    target: VARIABLE-CONTAINER_MANAGER
---

# docker_rh_repo_base_url

## Summary
Base URL of the CentOS/RHEL Docker CE yum repository. Rendered into `roles/container-engine/docker/templates/rh_docker.repo.j2`.

## Implementation
Defined in `roles/container-engine/docker/defaults/main.yml`:

```yaml
docker_rh_repo_base_url: 'https://download.docker.com/linux/rhel/{{ ansible_distribution_major_version }}/$basearch/stable'
```

The default is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. Kylin overrides it in `roles/container-engine/docker/vars/kylin.yml` to `'https://download.docker.com/linux/centos/8/$basearch/stable'` (also unchanged across the four tags).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Relevant on RHEL-family hosts when `container_manager == 'docker'`. Related: `docker_rh_repo_gpgkey`.

## References
- roles/container-engine/docker/defaults/main.yml
- roles/container-engine/docker/vars/kylin.yml, roles/container-engine/docker/templates/rh_docker.repo.j2
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
