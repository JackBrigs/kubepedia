---
id: VARIABLE-HAPROXY_CONFIG_DIR
type: variable
title: haproxy_config_dir
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - haproxy_config_dir
tags:
  - haproxy
  - loadbalancer
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Directory holding the HAProxy configuration; default /etc/haproxy"
relations: []
---

# haproxy_config_dir

## Summary
Path to the directory where Kubespray writes the HAProxy configuration for the local API-server load balancer. Default is `/etc/haproxy`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

```yaml
haproxy_config_dir: "/etc/haproxy"
```

The value is unchanged across v2.29.0-v2.31.0 (line ~104-105 depending on tag).

## Compatibility
Kubespray v2.29.0-v2.31.0. Related: `haproxy_image_repo`, `haproxy_image_tag`, `loadbalancer_apiserver_type`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
