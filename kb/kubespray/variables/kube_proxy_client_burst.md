---
id: VARIABLE-KUBE_PROXY_CLIENT_BURST
type: variable
title: kube_proxy_client_burst
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_proxy_client_burst
tags:
  - networking
  - kube-proxy
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    note: "Client burst QPS for kube-proxy connections to the API server; defaults to 10."
relations: []
---

# kube_proxy_client_burst

## Summary
Sets the `burst` field of the kube-proxy client connection, allowing extra queries to the API server to accumulate when a client is exceeding its steady-state rate limit. Defaults to `10`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/kube-proxy.yml` as:

```yaml
kube_proxy_client_burst: 10
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 11 in every tag).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Part of the kube-proxy `clientConnection` defaults; related variables include `kube_proxy_client_accept_content_types` and other `kube_proxy_client_*` tunables in the same file.

## References
- roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
