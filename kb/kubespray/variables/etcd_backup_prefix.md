---
id: VARIABLE-ETCD_BACKUP_PREFIX
type: variable
title: etcd_backup_prefix
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_backup_prefix
tags:
  - etcd
  - backup
sources:
  - type: code
    path: roles/etcd_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd_defaults/defaults/main.yml
    note: "Base directory prefix for etcd backups; default /var/backups"
relations: []
---

# etcd_backup_prefix

## Summary
The base directory prefix under which etcd snapshot backups are stored on etcd nodes. Default is `/var/backups`.

## Implementation
Defined in `roles/etcd_defaults/defaults/main.yml`:
```yaml
etcd_backup_prefix: "/var/backups"
```
The default value `/var/backups` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 12 in all four tags).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related to `etcd_backup_retention_count`.

## References
- roles/etcd_defaults/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
