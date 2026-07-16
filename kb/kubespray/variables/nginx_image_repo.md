---
id: VARIABLE-NGINX_IMAGE_REPO
type: variable
title: nginx_image_repo
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - nginx_image_repo
tags:
  - nginx
  - download
  - image
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Image repository for the nginx load-balancer container"
relations: []
---

# nginx_image_repo

## Summary
Container image repository for the nginx image used by the local API-server load balancer. Default: `{{ docker_image_repo }}/library/nginx`.

## Implementation
The authoritative default is defined in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
nginx_image_repo: "{{ docker_image_repo }}/library/nginx"
```

This value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. Note: `docs/developers/ci-setup.md` and `tests/common_vars.yml` override it to `{{ quay_image_repo }}/kubespray/nginx` for CI purposes only; the role default above is the source of truth.

## Compatibility
Kubespray range: `>=v2.29.0 <=v2.31.0`. Depends on `docker_image_repo`. Paired with `nginx_image_tag`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
