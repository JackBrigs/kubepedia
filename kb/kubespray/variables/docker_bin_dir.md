---
id: VARIABLE-DOCKER_BIN_DIR
type: variable
title: docker_bin_dir
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - docker_bin_dir
tags:
  - docker
  - container-runtime
sources:
  - type: code
    path: roles/container-engine/docker/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/docker/defaults/main.yml
    note: "Directory holding the docker binary, default /usr/bin"
relations:
  - type: see_also
    target: VARIABLE-CONTAINER_MANAGER
---

# docker_bin_dir

## Summary
Filesystem directory that contains the `docker` binary, used to build Docker command paths. Defaults to `/usr/bin`.

## Implementation
Defined in `roles/container-engine/docker/defaults/main.yml` as `docker_bin_dir: "/usr/bin"`. The same default is also set in `roles/kubespray_defaults/defaults/main/main.yml` (`docker_bin_dir: /usr/bin`) and mirrored in `inventory/sample/group_vars/all/docker.yml`. The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Consumed by Docker command construction and by `docker_image_info_command`.

## References
- roles/container-engine/docker/defaults/main.yml
- roles/kubespray_defaults/defaults/main/main.yml
- inventory/sample/group_vars/all/docker.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
