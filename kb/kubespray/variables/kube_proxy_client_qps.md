---
id: VARIABLE-KUBE_PROXY_CLIENT_QPS
type: variable
title: kube_proxy_client_qps
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_proxy_client_qps
tags:
  - kube-proxy
  - networking
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    note: "Defines clientConnection.qps for kube-proxy; default 5"
relations: []
---

# kube_proxy_client_qps

## Summary
Number of queries per second allowed for kube-proxy's connection to the API server (`clientConnection.qps`). Default is `5`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/kube-proxy.yml`:

```yaml
kube_proxy_client_qps: 5
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (same file, line 21 in each tag).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Part of the kube-proxy `clientConnection` block alongside `kube_proxy_client_content_type` and `kube_proxy_client_kubeconfig`.

## References
- roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
