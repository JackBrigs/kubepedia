---
id: VARIABLE-KUBE_PROXY_CONNTRACK_TCP_ESTABLISHED_TIMEOUT
type: variable
title: kube_proxy_conntrack_tcp_established_timeout
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_proxy_conntrack_tcp_established_timeout
tags:
  - kube-proxy
  - conntrack
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    note: "Defines conntrack.tcpEstablishedTimeout for kube-proxy; default 24h0m0s"
relations:
  - type: see_also
    target: VARIABLE-KUBE_PROXY_MODE
---

# kube_proxy_conntrack_tcp_established_timeout

## Summary
How long an idle established TCP connection is kept open in the conntrack table (`conntrack.tcpEstablishedTimeout`). Must be greater than 0 to set. Default is `24h0m0s`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/kube-proxy.yml`:

```yaml
kube_proxy_conntrack_tcp_established_timeout: 24h0m0s
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (same file, line 42 in each tag).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Part of the kube-proxy conntrack block alongside `kube_proxy_conntrack_tcp_close_wait_timeout`.

## References
- roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
