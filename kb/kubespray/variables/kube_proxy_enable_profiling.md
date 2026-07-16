---
id: VARIABLE-KUBE_PROXY_ENABLE_PROFILING
type: variable
title: kube_proxy_enable_profiling
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_proxy_enable_profiling
tags:
  - kube-proxy
  - profiling
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    note: "Defines enableProfiling for kube-proxy; default false"
relations:
  - type: see_also
    target: VARIABLE-KUBE_PROXY_MODE
---

# kube_proxy_enable_profiling

## Summary
Enables profiling via the web interface on the `/debug/pprof` handler (`enableProfiling`); profiling handlers are served by the metrics server. Default is `false`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/kube-proxy.yml`:

```yaml
kube_proxy_enable_profiling: false
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (same file, line 46 in each tag).

## Compatibility
Kubespray v2.29.0 through v2.31.0.

## References
- roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
