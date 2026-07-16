---
id: VARIABLE-HAPROXY_IMAGE_TAG
type: variable
title: haproxy_image_tag
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - haproxy_image_tag
tags:
  - haproxy
  - loadbalancer
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "HAProxy image tag; 3.2.4-alpine up to v2.30.0, 3.2.13-alpine in v2.31.0"
relations: []
---

# haproxy_image_tag

## Summary
Image tag (version) of the HAProxy container used for the local API-server load balancer. The value changed between tags, bumping the pinned HAProxy 3.2 patch release in v2.31.0.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`. The value differs between tags:

| Tag | Value |
|-----|-------|
| v2.29.0 | `3.2.4-alpine` |
| v2.29.1 | `3.2.4-alpine` |
| v2.30.0 | `3.2.4-alpine` |
| v2.31.0 | `3.2.13-alpine` |

## Compatibility
Kubespray v2.29.0-v2.31.0. Related: `haproxy_image_repo`, `haproxy_config_dir`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
