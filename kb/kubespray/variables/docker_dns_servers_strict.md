---
id: VARIABLE-DOCKER_DNS_SERVERS_STRICT
type: variable
title: docker_dns_servers_strict
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - docker_dns_servers_strict
tags:
  - docker
  - dns
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Whether Docker DNS server configuration is treated strictly, default false"
relations: []
---

# docker_dns_servers_strict

## Summary
Controls whether the Docker DNS server configuration is enforced strictly. Defaults to `false`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

```yaml
docker_dns_servers_strict: false
```

The same default is mirrored in `inventory/sample/group_vars/all/docker.yml`. The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies to the Docker container engine DNS setup.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- inventory/sample/group_vars/all/docker.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
