---
id: VARIABLE-ETCD_DATA_DIR
type: variable
title: etcd_data_dir
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_data_dir
tags:
  - etcd
  - paths
  - storage
sources:
  - type: code
    path: roles/etcd_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd_defaults/defaults/main.yml
    note: "etcd data directory; default /var/lib/etcd"
relations: []
---

# etcd_data_dir

## Summary
Filesystem directory where etcd stores its data. Default is `/var/lib/etcd`.

## Implementation
Defined in `roles/etcd_defaults/defaults/main.yml:13` as `etcd_data_dir: "/var/lib/etcd"`. The same value `/var/lib/etcd` also appears in `roles/adduser/defaults/main.yml:4`, `roles/kubespray_defaults/defaults/main/main.yml` (line 110 in v2.29.0/v2.29.1/v2.31.0, line 111 in v2.30.0), and the sample inventory `inventory/sample/group_vars/all/etcd.yml:3`. The default `/var/lib/etcd` is **unchanged across v2.29.0-v2.31.0**.

## Compatibility
Kubespray v2.29.0-v2.31.0. Related: `etcd_config_dir`, `etcd_cert_dir`. Exposed for override in the sample inventory.

## References
- roles/etcd_defaults/defaults/main.yml
- roles/kubespray_defaults/defaults/main/main.yml
- roles/adduser/defaults/main.yml
- inventory/sample/group_vars/all/etcd.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
