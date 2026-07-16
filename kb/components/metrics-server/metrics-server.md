---
id: COMPONENT-METRICS_SERVER
type: component
title: metrics-server
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: ">=0.8.0 <=0.8.1"
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - metrics-server
tags:
  - metrics
  - metrics-server
  - addons
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    lines: "297,298"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "metrics_server_version; image registry.k8s.io/metrics-server/metrics-server"
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    lines: "454"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "metrics_server_enabled: false (opt-in)"
relations:
  - type: see_also
    target: TAG-APPS
---

# metrics-server

## Summary

metrics-server provides the resource-metrics API (CPU/memory) used by
`kubectl top` and the Horizontal Pod Autoscaler. It is an **opt-in** add-on
(`metrics_server_enabled: false` by default). The pinned version is `0.8.0` in
`v2.29.0`–`v2.30.0` and `0.8.1` in `v2.31.0`.

## Context

- Covers Kubespray `v2.29.0`–`v2.31.0`.
- Disabled by default; enabled with `metrics_server_enabled: true`.
- Deployed as part of the cluster add-ons (see [[TAG-APPS]]).

## Implementation

The version is a literal
(`roles/kubespray_defaults/defaults/main/download.yml`):

```yaml
metrics_server_version: "0.8.1"   # value shown for v2.31.0
metrics_server_image_repo: "{{ kube_image_repo }}/metrics-server/metrics-server"  # registry.k8s.io/metrics-server/metrics-server
```

Per tag:

| Kubespray | metrics-server version |
|-----------|------------------------|
| v2.29.0   | 0.8.0                  |
| v2.29.1   | 0.8.0                  |
| v2.30.0   | 0.8.0                  |
| v2.31.0   | 0.8.1                  |

## Configuration

- Enablement: `metrics_server_enabled` (default `false`).
- Version: `metrics_server_version`.
- Image: `registry.k8s.io/metrics-server/metrics-server:v{{ metrics_server_version }}`.

## Compatibility

- Kubespray `v2.29.0`–`v2.30.0` → metrics-server `0.8.0`; `v2.31.0` → `0.8.1`.
- Applies to the Kubernetes versions these releases install (`>=1.31`).

## References

- `roles/kubespray_defaults/defaults/main/download.yml:297,298`.
- `roles/kubespray_defaults/defaults/main/main.yml:454` (`metrics_server_enabled`).
- Tags: v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`.
