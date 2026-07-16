---
id: VARIABLE-METRICS_SERVER_VERSION
type: variable
title: metrics_server_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - metrics_server_version
tags:
  - addons
  - metrics-server
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Metrics Server component version default"
relations:
  - type: see_also
    target: COMPONENT-METRICS_SERVER
---

# metrics_server_version

## Summary
Pins the Metrics Server component version. Its value feeds `metrics_server_image_tag` (`v{{ metrics_server_version }}`). Default is `0.8.0` through v2.30.0 and `0.8.1` in v2.31.0.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`. The default value changes between tags:

| Tag | Value |
| --- | --- |
| v2.29.0 | 0.8.0 |
| v2.29.1 | 0.8.0 |
| v2.30.0 | 0.8.0 |
| v2.31.0 | 0.8.1 |

## Compatibility
Kubespray v2.29.0 through v2.31.0. Consumed by `metrics_server_image_tag`; effective only when `metrics_server_enabled` is true.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
