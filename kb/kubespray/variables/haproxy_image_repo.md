---
id: VARIABLE-HAPROXY_IMAGE_REPO
type: variable
title: haproxy_image_repo
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - haproxy_image_repo
tags:
  - haproxy
  - loadbalancer
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Container image repository for HAProxy; derived from docker_image_repo"
relations: []
---

# haproxy_image_repo

## Summary
Container image repository for the HAProxy image used by the local API-server load balancer. Computed from `docker_image_repo` as `{{ docker_image_repo }}/library/haproxy`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
haproxy_image_repo: "{{ docker_image_repo }}/library/haproxy"
```

The computed expression is unchanged across v2.29.0-v2.31.0.

## Compatibility
Kubespray v2.29.0-v2.31.0. Related: `haproxy_image_tag`, `docker_image_repo`, `haproxy_config_dir`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
