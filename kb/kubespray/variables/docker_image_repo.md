---
id: VARIABLE-DOCKER_IMAGE_REPO
type: variable
title: docker_image_repo
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - docker_image_repo
tags:
  - docker
  - registry
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Registry hostname for Docker Hub images; default docker.io"
relations: []
---

# docker_image_repo

## Summary
Registry hostname used as the base for Docker Hub-hosted images referenced by Kubespray. Defaults to `docker.io`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
docker_image_repo: "docker.io"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Used to compose image references; sits alongside `gcr_image_repo`, `kube_image_repo`, and `quay_image_repo`. Override to point Docker Hub images at a mirror.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
