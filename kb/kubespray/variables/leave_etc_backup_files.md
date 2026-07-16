---
id: VARIABLE-LEAVE_ETC_BACKUP_FILES
type: variable
title: leave_etc_backup_files
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - leave_etc_backup_files
tags:
  - preinstall
  - backup
sources:
  - type: code
    path: roles/kubernetes/preinstall/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/preinstall/defaults/main.yml
    note: "Defines leave_etc_backup_files with default true"
relations: []
---

# leave_etc_backup_files

## Summary
Controls whether backup copies of files modified in `/etc` (created by preinstall tasks) are kept on the nodes. Default is `true`, so backup files are left in place.

## Implementation
Defined in `roles/kubernetes/preinstall/defaults/main.yml`:

```yaml
leave_etc_backup_files: true
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. No known constraints. Belongs to the `kubernetes/preinstall` role.

## References
- roles/kubernetes/preinstall/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
