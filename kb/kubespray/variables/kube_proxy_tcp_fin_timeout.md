---
id: VARIABLE-KUBE_PROXY_TCP_FIN_TIMEOUT
type: variable
title: kube_proxy_tcp_fin_timeout
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_proxy_tcp_fin_timeout
tags:
  - kube-proxy
  - ipvs
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    note: "Defines kube_proxy_tcp_fin_timeout with default 0s"
relations:
  - type: see_also
    target: VARIABLE-KUBE_PROXY_MODE
---

# kube_proxy_tcp_fin_timeout

## Summary
Timeout value used for IPVS TCP sessions after receiving a FIN. Default is `0s`, which preserves the current timeout value on the system.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/kube-proxy.yml` at line 89:

```yaml
kube_proxy_tcp_fin_timeout: 0s
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Available in Kubespray v2.29.0 through v2.31.0. Applies to IPVS proxy mode. Related to `kube_proxy_tcp_timeout` and `kube_proxy_udp_timeout` in the same file.

## References
- roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
