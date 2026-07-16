---
id: VARIABLE-METRICS_SERVER_IMAGE_TAG
type: variable
title: metrics_server_image_tag
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - metrics_server_image_tag
tags:
  - addons
  - metrics-server
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Computed Metrics Server image tag from metrics_server_version"
relations: []
---

# metrics_server_image_tag

## Summary
Container image tag for the Metrics Server addon. Computed as `v{{ metrics_server_version }}`, so it follows the value of `metrics_server_version`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as `metrics_server_image_tag: "v{{ metrics_server_version }}"`. The expression itself is unchanged across v2.29.0-v2.31.0, but the resolved tag changes with `metrics_server_version`: it resolves to `v0.8.0` in v2.29.0-v2.30.0 and `v0.8.1` in v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on `metrics_server_version`; used with `metrics_server_image_repo` when `metrics_server_enabled` is true.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
