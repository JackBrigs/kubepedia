---
id: VARIABLE-METRICS_SERVER_REPLICAS
type: variable
title: metrics_server_replicas
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - metrics_server_replicas
tags:
  - kubernetes-apps
  - metrics-server
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/metrics_server/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/metrics_server/defaults/main.yml
    note: "default: 1"
relations: []
---
<!-- generated: variable-stub -->

# metrics_server_replicas

## Summary

Kubespray variable `metrics_server_replicas` — default `1`. Defined in `roles/kubernetes-apps/metrics_server/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/metrics_server/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
metrics_server_replicas: 1
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/metrics_server/defaults/main.yml` (Kubespray `v2.31.0`).
