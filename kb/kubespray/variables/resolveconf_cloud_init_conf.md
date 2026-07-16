---
id: VARIABLE-RESOLVECONF_CLOUD_INIT_CONF
type: variable
title: resolveconf_cloud_init_conf
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - resolveconf_cloud_init_conf
tags:
  - dns
  - preinstall
sources:
  - type: code
    path: roles/kubernetes/preinstall/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/preinstall/defaults/main.yml
    note: "Path of the cloud-init resolvconf file managed by preinstall; default /etc/resolveconf_cloud_init.conf"
relations: []
---

# resolveconf_cloud_init_conf

## Summary
Filesystem path of the cloud-init resolvconf configuration file that the preinstall role manages when configuring host DNS. Defaults to `/etc/resolveconf_cloud_init.conf`.

## Implementation
Defined in `roles/kubernetes/preinstall/defaults/main.yml` at line 29:

```yaml
resolveconf_cloud_init_conf: /etc/resolveconf_cloud_init.conf
```

Unchanged across v2.29.0-v2.31.0 (line 29 in all four tags).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Used by the preinstall DNS configuration tasks; related to `resolvconf_mode`.

## References
- roles/kubernetes/preinstall/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
