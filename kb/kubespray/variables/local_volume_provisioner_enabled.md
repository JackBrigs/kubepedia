---
id: VARIABLE-LOCAL_VOLUME_PROVISIONER_ENABLED
type: variable
title: local_volume_provisioner_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - local_volume_provisioner_enabled
tags:
  - storage
  - addons
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Defines default local_volume_provisioner_enabled: false"
relations: []
---

# local_volume_provisioner_enabled

## Summary
Toggles deployment of the Local Volume Provisioner addon (sig-storage local-volume-provisioner). Default is `false`, so the addon is not installed unless explicitly enabled.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as `local_volume_provisioner_enabled: false`. Mirrored (also `false`) in the sample inventory `inventory/sample/group_vars/k8s_cluster/addons.yml`. Value is unchanged across v2.29.0–v2.31.0 (only line numbers shift: main.yml 448 → 449 → 457; addons.yml line 36 → 32).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Related variables: `local_volume_provisioner_storage_classes`, `local_volume_provisioner_image_repo`, `local_volume_provisioner_version`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- inventory/sample/group_vars/k8s_cluster/addons.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
