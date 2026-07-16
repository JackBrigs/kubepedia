---
id: VARIABLE-KUBE_PROXY_MIN_SYNC_PERIOD
type: variable
title: kube_proxy_min_sync_period
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_proxy_min_sync_period
tags:
  - kube-proxy
  - tuning
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    note: "Defines kube_proxy_min_sync_period, default 0s"
relations:
  - type: see_also
    target: VARIABLE-KUBE_PROXY_MODE
---

# kube_proxy_min_sync_period

## Summary
Sets the kube-proxy `minSyncPeriod` — the minimum interval between applying rule changes (iptables/ipvs). Default is `0s`, meaning changes are applied immediately.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/kube-proxy.yml`:

```yaml
kube_proxy_min_sync_period: 0s
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 61 in each tag).

## Compatibility
Applies to Kubespray v2.29.0–v2.31.0. Feeds the kube-proxy `KubeProxyConfiguration`.

## References
- roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
