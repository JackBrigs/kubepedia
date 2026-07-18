---
id: VARIABLE-METRICS_SERVER_HOST_NETWORK
type: variable
title: metrics_server_host_network
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - metrics_server_host_network
tags:
  - kubernetes-apps
  - metrics-server
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/metrics_server/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/metrics_server/defaults/main.yml
    note: "default: false"
relations: []
---
<!-- generated: variable-stub -->

# metrics_server_host_network

## Summary

Kubespray variable `metrics_server_host_network` — default `false`. Defined in `roles/kubernetes-apps/metrics_server/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/metrics_server/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
metrics_server_host_network: false
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/metrics_server/defaults/main.yml` (Kubespray `v2.31.0`).
