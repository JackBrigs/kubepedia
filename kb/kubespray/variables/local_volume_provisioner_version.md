---
id: VARIABLE-LOCAL_VOLUME_PROVISIONER_VERSION
type: variable
title: local_volume_provisioner_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - local_volume_provisioner_version
tags:
  - storage
  - version
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Defines the local-volume-provisioner version (2.5.0)"
relations: []
---

# local_volume_provisioner_version

## Summary
Version of the sig-storage Local Volume Provisioner deployed by Kubespray. Default is `2.5.0`. It feeds the image tag (`v{{ local_volume_provisioner_version }}`).

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as `local_volume_provisioner_version: "2.5.0"`. The value is unchanged across v2.29.0–v2.31.0 (only line numbers shift: 303 → 305 → 306 → 300).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Consumed by `local_volume_provisioner_image_tag`. Related variables: `local_volume_provisioner_image_repo`, `local_volume_provisioner_enabled`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
