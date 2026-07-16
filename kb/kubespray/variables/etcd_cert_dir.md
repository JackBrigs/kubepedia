---
id: VARIABLE-ETCD_CERT_DIR
type: variable
title: etcd_cert_dir
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_cert_dir
tags:
  - etcd
  - certificates
  - paths
sources:
  - type: code
    path: roles/etcd_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd_defaults/defaults/main.yml
    note: "Directory holding etcd TLS certificates; default {{ etcd_config_dir }}/ssl"
relations:
  - type: see_also
    target: COMPONENT-ETCD
---

# etcd_cert_dir

## Summary
Directory where etcd TLS certificates are stored. Default is the computed expression `{{ etcd_config_dir }}/ssl`, which resolves to `/etc/ssl/etcd/ssl`.

## Implementation
Defined in `roles/etcd_defaults/defaults/main.yml:20` as `etcd_cert_dir: "{{ etcd_config_dir }}/ssl"`. Also defined in `roles/kubespray_defaults/defaults/main/main.yml` with the same expression (line 718 in v2.29.0/v2.29.1, 721 in v2.30.0, 740 in v2.31.0). The expression is **unchanged across v2.29.0-v2.31.0**.

## Compatibility
Kubespray v2.29.0-v2.31.0. Derived from `etcd_config_dir`. Related: `etcd_cert_group`, `etcd_cert_alt_names`.

## References
- roles/etcd_defaults/defaults/main.yml
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
