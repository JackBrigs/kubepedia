---
id: VARIABLE-SCHEDULER_PLUGINS_CONTROLLER_IMAGE_TAG
type: variable
title: scheduler_plugins_controller_image_tag
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - scheduler_plugins_controller_image_tag
tags:
  - scheduler-plugins
  - image
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Image tag for the scheduler-plugins controller"
relations: []
---

# scheduler_plugins_controller_image_tag

## Summary
Container image tag for the scheduler-plugins controller. Derived from `scheduler_plugins_version` prefixed with `v`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:
`scheduler_plugins_controller_image_tag: "v{{ scheduler_plugins_version }}"`.
The computed expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0; the concrete tag depends on `scheduler_plugins_version` in each tag.

## Compatibility
Present in Kubespray >=v2.29.0 <=v2.31.0. Depends on `scheduler_plugins_version`; related to `scheduler_plugins_controller_image_repo` and `scheduler_plugins_enabled`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
