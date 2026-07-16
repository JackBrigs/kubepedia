---
id: VARIABLE-DOCKER_IMAGE_INFO_COMMAND
type: variable
title: docker_image_info_command
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - docker_image_info_command
tags:
  - docker
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Shell command used to list locally present Docker images with their tags and digests"
relations: []
---

# docker_image_info_command

## Summary
Shell command used to enumerate Docker images already present on a node, emitting each image's RepoTags and RepoDigests. Used by the download role to decide which images still need pulling when the container engine is Docker.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`. The command runs `{{ docker_bin_dir }}/docker images -q` and pipes IDs into `docker inspect` with a Go template that joins `.RepoTags` and `.RepoDigests`:

```yaml
docker_image_info_command: "{{ docker_bin_dir }}/docker images -q | xargs -i {{ docker_bin_dir }}/docker inspect -f '{{ if .RepoTags }}{{ join .RepoTags "," }}{{ end }}{{ if .RepoDigests }},{{ join .RepoDigests "," }}{{ end }}' {} | tr '\n' ','"
```

(In the source the inner `{{ }}` are escaped via `{% raw %}` / literal delimiters.) The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on `docker_bin_dir`; applies to the Docker container engine.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
