---
id: VARIABLE-KUBE_PROXY_CONFIG_SYNC_PERIOD
type: variable
title: kube_proxy_config_sync_period
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_proxy_config_sync_period
tags:
  - kube-proxy
  - networking
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    note: "Defines configSyncPeriod for kube-proxy; default 15m0s"
relations: []
---

# kube_proxy_config_sync_period

## Summary
How often kube-proxy refreshes its configuration from the API server (`configSyncPeriod`). Must be greater than 0. Default is `15m0s`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/kube-proxy.yml`:

```yaml
kube_proxy_config_sync_period: 15m0s
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (same file, line 24 in each tag).

## Compatibility
Kubespray v2.29.0 through v2.31.0.

## References
- roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
