---
id: VARIABLE-SCHEDULER_PLUGINS_CONTROLLER_IMAGE_REPO
type: variable
title: scheduler_plugins_controller_image_repo
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - scheduler_plugins_controller_image_repo
tags:
  - scheduler-plugins
  - image
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Image repository for the scheduler-plugins controller"
relations: []
---

# scheduler_plugins_controller_image_repo

## Summary
Container image repository for the scheduler-plugins controller. Derived from `kube_image_repo` with the `scheduler-plugins/controller` path appended.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:
`scheduler_plugins_controller_image_repo: "{{ kube_image_repo }}/scheduler-plugins/controller"`.
The computed expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Present in Kubespray >=v2.29.0 <=v2.31.0. Depends on `kube_image_repo`; related to `scheduler_plugins_controller_image_tag` and `scheduler_plugins_enabled`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
