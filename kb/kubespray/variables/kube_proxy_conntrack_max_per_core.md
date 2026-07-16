---
id: VARIABLE-KUBE_PROXY_CONNTRACK_MAX_PER_CORE
type: variable
title: kube_proxy_conntrack_max_per_core
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_proxy_conntrack_max_per_core
tags:
  - kube-proxy
  - conntrack
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    note: "Defines conntrack.maxPerCore for kube-proxy; default 32768"
relations: []
---

# kube_proxy_conntrack_max_per_core

## Summary
Maximum number of NAT connections kube-proxy tracks per CPU core (`conntrack.maxPerCore`). Set to 0 to leave the limit as-is and ignore min. Default is `32768`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/kube-proxy.yml`:

```yaml
kube_proxy_conntrack_max_per_core: 32768
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (same file, line 29 in each tag).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Part of the kube-proxy conntrack block alongside `kube_proxy_conntrack_min`.

## References
- roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
