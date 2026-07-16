---
id: VARIABLE-LOCAL_VOLUME_PROVISIONER_STORAGE_CLASSES
type: variable
title: local_volume_provisioner_storage_classes
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - local_volume_provisioner_storage_classes
tags:
  - storage
  - addons
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Defines the default storage-class map for local-volume-provisioner"
relations: []
---

# local_volume_provisioner_storage_classes

## Summary
Defines the storage classes managed by the Local Volume Provisioner as a YAML block-scalar string (later cast to a Python dict). Default declares a single `local-storage` class using `/mnt/disks` for host and mount dirs, `Filesystem` volume mode, and `ext4` fs type.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` (and identically in the role default `roles/kubernetes-apps/external_provisioner/local_volume_provisioner/defaults/main.yml`, both line 12). The default value is:

```
{
  "{{ local_volume_provisioner_storage_class | default('local-storage') }}": {
    "host_dir": "{{ local_volume_provisioner_base_dir | default('/mnt/disks') }}",
    "mount_dir": "{{ local_volume_provisioner_mount_dir | default('/mnt/disks') }}",
    "volume_mode": "Filesystem",
    "fs_type": "ext4"
  }
}
```

Unchanged across v2.29.0–v2.31.0 (main.yml line 612 → 613 → 632; role default stays at line 12).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Uses helper variables `local_volume_provisioner_storage_class`, `local_volume_provisioner_base_dir`, `local_volume_provisioner_mount_dir`. Related variable: `local_volume_provisioner_enabled`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- roles/kubernetes-apps/external_provisioner/local_volume_provisioner/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
