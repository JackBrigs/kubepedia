---
id: VARIABLE-METRICS_SERVER_IMAGE_REPO
type: variable
title: metrics_server_image_repo
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - metrics_server_image_repo
tags:
  - addons
  - metrics-server
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Computed Metrics Server image repository path"
relations:
  - type: see_also
    target: COMPONENT-METRICS_SERVER
---

# metrics_server_image_repo

## Summary
Container image repository for the Metrics Server addon. Computed from `kube_image_repo`, defaulting to `{{ kube_image_repo }}/metrics-server/metrics-server`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as `metrics_server_image_repo: "{{ kube_image_repo }}/metrics-server/metrics-server"`. The expression is unchanged across v2.29.0-v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on `kube_image_repo`; used together with `metrics_server_image_tag` when `metrics_server_enabled` is true.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
