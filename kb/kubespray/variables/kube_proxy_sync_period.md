---
id: VARIABLE-KUBE_PROXY_SYNC_PERIOD
type: variable
title: kube_proxy_sync_period
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_proxy_sync_period
tags:
  - kube-proxy
  - networking
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    note: "Defines kube_proxy_sync_period with default 30s"
relations: []
---

# kube_proxy_sync_period

## Summary
Maximum interval at which kube-proxy refreshes iptables or ipvs rules. Default is `30s`. Must be greater than 0.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/kube-proxy.yml` at line 65:

```yaml
kube_proxy_sync_period: 30s
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Available in Kubespray v2.29.0 through v2.31.0. Related to `kube_proxy_min_sync_period` (default `0s`) in the same file.

## References
- roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
