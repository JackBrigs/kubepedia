---
id: VARIABLE-EXPAND_PERSISTENT_VOLUMES
type: variable
title: expand_persistent_volumes
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - expand_persistent_volumes
tags:
  - storage
  - csi
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Global flag to allow expansion of persistent volumes; default false"
relations: []
---

# expand_persistent_volumes

## Summary
Global flag controlling whether persistent volume expansion is enabled (used when configuring storage classes). Default is `false`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as `expand_persistent_volumes: false` (line 461 in v2.29.0/v2.29.1, line 462 in v2.30.0, line 469 in v2.31.0). The value `false` is unchanged across v2.29.0-v2.31.0; only the line number shifted. Note: `roles/kubernetes-apps/persistent_volumes/upcloud-csi/defaults/main.yml` contains a separate, nested `expand_persistent_volumes: true` inside upcloud-csi storage-class definitions, which is a distinct per-storage-class setting, not this global default.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
