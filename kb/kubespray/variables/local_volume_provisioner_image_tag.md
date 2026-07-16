---
id: VARIABLE-LOCAL_VOLUME_PROVISIONER_IMAGE_TAG
type: variable
title: local_volume_provisioner_image_tag
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - local_volume_provisioner_image_tag
tags:
  - storage
  - image
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Defines the container image tag for local-volume-provisioner"
relations: []
---

# local_volume_provisioner_image_tag

## Summary
Container image tag for the Local Volume Provisioner. Default is the computed expression `v{{ local_volume_provisioner_version }}`, which resolves to `v2.5.0`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as `local_volume_provisioner_image_tag: "v{{ local_volume_provisioner_version }}"`. The expression is unchanged across v2.29.0–v2.31.0 (only line numbers shift: 305 → 307 → 308 → 302). Since `local_volume_provisioner_version` is `2.5.0` in all four tags, this resolves to `v2.5.0`.

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Derives from `local_volume_provisioner_version`. Related variables: `local_volume_provisioner_image_repo`, `local_volume_provisioner_enabled`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
