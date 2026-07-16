---
id: VARIABLE-ETCD_CONFIG_DIR
type: variable
title: etcd_config_dir
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_config_dir
tags:
  - etcd
  - paths
sources:
  - type: code
    path: roles/etcd_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd_defaults/defaults/main.yml
    note: "Base etcd config/ssl directory; default /etc/ssl/etcd"
relations:
  - type: see_also
    target: COMPONENT-ETCD
---

# etcd_config_dir

## Summary
Base directory for etcd configuration and TLS material. Default is `/etc/ssl/etcd`. It is the base for `etcd_cert_dir` (`{{ etcd_config_dir }}/ssl`).

## Implementation
Defined in `roles/etcd_defaults/defaults/main.yml:19` as `etcd_config_dir: /etc/ssl/etcd`. Also defined in `roles/kubespray_defaults/defaults/main/main.yml` with the same value (line 716 in v2.29.0/v2.29.1, 719 in v2.30.0, 738 in v2.31.0). The default `/etc/ssl/etcd` is **unchanged across v2.29.0-v2.31.0**.

## Compatibility
Kubespray v2.29.0-v2.31.0. Consumed by `etcd_cert_dir`. Related: `etcd_data_dir`.

## References
- roles/etcd_defaults/defaults/main.yml
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
