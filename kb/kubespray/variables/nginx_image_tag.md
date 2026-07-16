---
id: VARIABLE-NGINX_IMAGE_TAG
type: variable
title: nginx_image_tag
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - nginx_image_tag
tags:
  - nginx
  - download
  - image
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Image tag for the nginx load-balancer container"
relations: []
---

# nginx_image_tag

## Summary
Container image tag for the nginx image used by the local API-server load balancer. The value changes across tags: `1.28.0-alpine` through v2.30.0, bumped to `1.28.2-alpine` in v2.31.0.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`. The value differs between tags:

| Tag | nginx_image_tag |
|-----|-----------------|
| v2.29.0 | 1.28.0-alpine |
| v2.29.1 | 1.28.0-alpine |
| v2.30.0 | 1.28.0-alpine |
| v2.31.0 | 1.28.2-alpine |

## Compatibility
Kubespray range: `>=v2.29.0 <=v2.31.0`. Paired with `nginx_image_repo`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
