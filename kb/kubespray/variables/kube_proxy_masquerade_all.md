---
id: VARIABLE-KUBE_PROXY_MASQUERADE_ALL
type: variable
title: kube_proxy_masquerade_all
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_proxy_masquerade_all
tags:
  - kube-proxy
  - iptables
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    note: "Defines kube_proxy_masquerade_all, default false"
relations:
  - type: see_also
    target: VARIABLE-KUBE_PROXY_MODE
---

# kube_proxy_masquerade_all

## Summary
Controls kube-proxy `masqueradeAll` — when true, kube-proxy SNAT-masquerades all traffic sent through service cluster IPs. Default is `false`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/kube-proxy.yml`:

```yaml
kube_proxy_masquerade_all: false
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 53 in each tag).

## Compatibility
Applies to Kubespray v2.29.0–v2.31.0. Feeds the kube-proxy `KubeProxyConfiguration`. Related variable: `kube_proxy_masquerade_bit`.

## References
- roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
