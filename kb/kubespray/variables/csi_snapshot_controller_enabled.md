---
id: VARIABLE-CSI_SNAPSHOT_CONTROLLER_ENABLED
type: variable
title: csi_snapshot_controller_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - csi_snapshot_controller_enabled
tags:
  - csi
  - snapshot
  - toggle
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Boolean toggle for deploying the CSI snapshot controller; default false."
relations: []
---

# csi_snapshot_controller_enabled

## Summary
Boolean toggle that controls whether the CSI snapshot controller is deployed. Default is `false`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

```yaml
csi_snapshot_controller_enabled: false
```

The value `false` is unchanged across v2.29.0-v2.31.0.

## Compatibility
Present across Kubespray v2.29.0-v2.31.0. Related to the CSI snapshotter image variables (`csi_snapshotter_image_repo`, `csi_snapshotter_image_tag`).

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
