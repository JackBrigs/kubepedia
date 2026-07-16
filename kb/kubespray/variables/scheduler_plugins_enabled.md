---
id: VARIABLE-SCHEDULER_PLUGINS_ENABLED
type: variable
title: scheduler_plugins_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - scheduler_plugins_enabled
tags:
  - scheduler-plugins
  - addons
sources:
  - type: code
    path: roles/kubernetes-apps/scheduler_plugins/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/scheduler_plugins/defaults/main.yml
    note: "Toggle for scheduler-plugins deployment, default false"
relations: []
---

# scheduler_plugins_enabled

## Summary
Boolean toggle that controls whether the scheduler-plugins addon is deployed. Default is `false`.

## Implementation
Defined in `roles/kubernetes-apps/scheduler_plugins/defaults/main.yml` as `scheduler_plugins_enabled: false`, and also declared in `roles/kubespray_defaults/defaults/main/main.yml` with the same default `false`. The default value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Present in Kubespray >=v2.29.0 <=v2.31.0. Related variables: `scheduler_plugins_controller_image_repo`, `scheduler_plugins_controller_image_tag`, `scheduler_plugins_version`.

## References
- roles/kubernetes-apps/scheduler_plugins/defaults/main.yml
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
