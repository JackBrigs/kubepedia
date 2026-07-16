---
id: VARIABLE-METRICS_SERVER_ENABLED
type: variable
title: metrics_server_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - metrics_server_enabled
tags:
  - addons
  - metrics-server
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Role default metrics_server_enabled: false"
relations: []
---

# metrics_server_enabled

## Summary
Toggles deployment of the Kubernetes Metrics Server addon. Default is `false` (disabled), so Metrics Server is not installed unless the user opts in.

## Implementation
Defined as a role default in `roles/kubespray_defaults/defaults/main/main.yml` with value `metrics_server_enabled: false`. It is also exposed to users in the sample inventory `inventory/sample/group_vars/k8s_cluster/addons.yml` with the same value `false`. The default is unchanged across v2.29.0-v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Enabling it activates the related `metrics_server_*` image/version variables (`metrics_server_image_repo`, `metrics_server_image_tag`, `metrics_server_version`).

## References
- roles/kubespray_defaults/defaults/main/main.yml
- inventory/sample/group_vars/k8s_cluster/addons.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
