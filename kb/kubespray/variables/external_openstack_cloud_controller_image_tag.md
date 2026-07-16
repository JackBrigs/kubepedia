---
id: VARIABLE-EXTERNAL_OPENSTACK_CLOUD_CONTROLLER_IMAGE_TAG
type: variable
title: external_openstack_cloud_controller_image_tag
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - external_openstack_cloud_controller_image_tag
tags:
  - openstack
  - cloud-controller
  - image-tag
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Defines the image tag of the OpenStack cloud controller manager (v1.32.0 through v2.30.0, v1.35.0 in v2.31.0)"
relations: []
---

# external_openstack_cloud_controller_image_tag

## Summary
Sets the container image tag for the OpenStack external cloud controller manager. The value changes between tags: `v1.32.0` up to v2.30.0, then `v1.35.0` in v2.31.0.

## Implementation
Defined in two places with identical values per tag: `roles/kubespray_defaults/defaults/main/download.yml` and `roles/kubernetes-apps/external_cloud_controller/openstack/defaults/main.yml`.

| Tag | Value |
|-----|-------|
| v2.29.0 | `v1.32.0` |
| v2.29.1 | `v1.32.0` |
| v2.30.0 | `v1.32.0` |
| v2.31.0 | `v1.35.0` |

## Compatibility
Kubespray v2.29.0–v2.31.0. Used only when the external OpenStack cloud controller is deployed. Related: `external_openstack_cloud_controller_image_repo`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- roles/kubernetes-apps/external_cloud_controller/openstack/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
