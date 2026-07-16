---
id: VARIABLE-DOCKER_DNS_OPTIONS
type: variable
title: docker_dns_options
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - docker_dns_options
tags:
  - docker
  - dns
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "List of resolver options for the Docker daemon DNS configuration"
relations:
  - type: see_also
    target: VARIABLE-CONTAINER_MANAGER
---

# docker_dns_options

## Summary
List of resolver options applied to the Docker daemon DNS configuration. Defaults to `ndots:{{ ndots }}`, `timeout:2`, and `attempts:2`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

```yaml
docker_dns_options:
- ndots:{{ ndots }}
- timeout:2
- attempts:2
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on `ndots`; applies to the Docker container engine DNS setup.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
