---
id: VARIABLE-LOCAL_VOLUME_PROVISIONER_IMAGE_REPO
type: variable
title: local_volume_provisioner_image_repo
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - local_volume_provisioner_image_repo
tags:
  - storage
  - image
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Defines the container image repository for local-volume-provisioner"
relations: []
---

# local_volume_provisioner_image_repo

## Summary
Container image repository for the Local Volume Provisioner. Default is the computed expression `{{ kube_image_repo }}/sig-storage/local-volume-provisioner`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as `local_volume_provisioner_image_repo: "{{ kube_image_repo }}/sig-storage/local-volume-provisioner"`. The expression is unchanged across v2.29.0–v2.31.0 (only line numbers shift: 304 → 306 → 307 → 301).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Derives from `kube_image_repo`. Related variables: `local_volume_provisioner_image_tag`, `local_volume_provisioner_version`, `local_volume_provisioner_enabled`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
