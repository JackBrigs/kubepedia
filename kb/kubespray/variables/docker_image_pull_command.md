---
id: VARIABLE-DOCKER_IMAGE_PULL_COMMAND
type: variable
title: docker_image_pull_command
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - docker_image_pull_command
tags:
  - docker
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Command used to pull images with Docker; default {{ docker_bin_dir }}/docker pull"
relations: []
---

# docker_image_pull_command

## Summary
Command Kubespray uses to pull container images when Docker is the container engine. Built from `docker_bin_dir` plus `docker pull`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
docker_image_pull_command: "{{ docker_bin_dir }}/docker pull"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies when Docker is the selected container engine. Related: `docker_bin_dir`, `docker_image_info_command`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
