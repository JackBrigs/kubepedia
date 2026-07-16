---
id: VARIABLE-NGINX_CONFIG_DIR
type: variable
title: nginx_config_dir
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - nginx_config_dir
tags:
  - nginx
  - loadbalancer
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Directory holding the nginx configuration for the localhost load balancer"
relations: []
---

# nginx_config_dir

## Summary
Filesystem directory where the nginx configuration is written for the local API-server load balancer. Default: `/etc/nginx`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
nginx_config_dir: "/etc/nginx"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line number shifts to 102 in v2.30.0, back to 101 in v2.31.0, but value is identical).

## Compatibility
Kubespray range: `>=v2.29.0 <=v2.31.0`. Relevant to the localhost/nginx load-balancer configuration.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
