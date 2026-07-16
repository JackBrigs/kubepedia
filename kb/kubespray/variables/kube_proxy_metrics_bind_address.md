---
id: VARIABLE-KUBE_PROXY_METRICS_BIND_ADDRESS
type: variable
title: kube_proxy_metrics_bind_address
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_proxy_metrics_bind_address
tags:
  - kube-proxy
  - metrics
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    note: "Defines kube_proxy_metrics_bind_address, default 127.0.0.1:10249"
relations: []
---

# kube_proxy_metrics_bind_address

## Summary
Sets the kube-proxy `metricsBindAddress` — the IP address and port where kube-proxy serves its Prometheus metrics endpoint. Default is `127.0.0.1:10249`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/kube-proxy.yml`:

```yaml
kube_proxy_metrics_bind_address: 127.0.0.1:10249
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 97 in each tag).

## Compatibility
Applies to Kubespray v2.29.0–v2.31.0. Feeds the kube-proxy `KubeProxyConfiguration`. Related binding variable: `kube_proxy_healthz_bind_address`.

## References
- roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
