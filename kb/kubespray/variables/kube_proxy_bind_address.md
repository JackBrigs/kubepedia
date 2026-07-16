---
id: VARIABLE-KUBE_PROXY_BIND_ADDRESS
type: variable
title: kube_proxy_bind_address
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_proxy_bind_address
tags:
  - networking
  - kube-proxy
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    note: "IP address kube-proxy binds to; defaults to '0.0.0.0'."
relations: []
---

# kube_proxy_bind_address

## Summary
The IP address that kube-proxy binds to (the `bindAddress` field of the kube-proxy configuration). Defaults to `'0.0.0.0'`, binding to all IPv4 interfaces.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/kube-proxy.yml` as:

```yaml
kube_proxy_bind_address: '0.0.0.0'
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 3 in every tag).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Part of the kube-proxy configuration defaults; related variables include `kube_proxy_mode` and other `kube_proxy_*` tunables in the same file.

## References
- roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
