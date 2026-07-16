---
id: VARIABLE-ETCD_CERT_GROUP
type: variable
title: etcd_cert_group
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_cert_group
tags:
  - etcd
  - certificates
  - permissions
sources:
  - type: code
    path: roles/etcd_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd_defaults/defaults/main.yml
    note: "Group owner for etcd certificate files; default root"
relations:
  - type: see_also
    target: COMPONENT-ETCD
---

# etcd_cert_group

## Summary
Group ownership applied to etcd certificate files. Default is `root`.

## Implementation
Defined in `roles/etcd_defaults/defaults/main.yml` as `etcd_cert_group: root` (line 22 in v2.29.0/v2.29.1, line 21 in v2.30.0/v2.31.0). The default `root` is **unchanged across v2.29.0-v2.31.0**; only the line number shifted.

## Compatibility
Kubespray v2.29.0-v2.31.0. Related: `etcd_cert_dir`, `etcd_config_dir`.

## References
- roles/etcd_defaults/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
