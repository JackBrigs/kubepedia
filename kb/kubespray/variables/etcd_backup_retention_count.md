---
id: VARIABLE-ETCD_BACKUP_RETENTION_COUNT
type: variable
title: etcd_backup_retention_count
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_backup_retention_count
tags:
  - etcd
  - backup
sources:
  - type: code
    path: roles/etcd_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd_defaults/defaults/main.yml
    note: "Number of etcd backups to retain; default -1 (keep all)"
relations:
  - type: see_also
    target: COMPONENT-ETCD
---

# etcd_backup_retention_count

## Summary
The number of etcd snapshot backups to retain. The default `-1` disables pruning, so all backups are kept.

## Implementation
Defined in `roles/etcd_defaults/defaults/main.yml`:
```yaml
etcd_backup_retention_count: -1
```
The default value `-1` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 16 in all four tags).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related to `etcd_backup_prefix`.

## References
- roles/etcd_defaults/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
