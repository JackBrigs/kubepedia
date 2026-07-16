---
id: VARIABLE-KUBE_PROXY_EXCLUDE_CIDRS
type: variable
title: kube_proxy_exclude_cidrs
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_proxy_exclude_cidrs
tags:
  - kube-proxy
  - ipvs
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    note: "Defines ipvs.excludeCIDRs for kube-proxy; default [] (empty list)"
relations: []
---

# kube_proxy_exclude_cidrs

## Summary
Comma-separated list of CIDRs the ipvs proxier should not touch when cleaning up IPVS rules (`ipvs.excludeCIDRs`). Default is an empty list `[]`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/kube-proxy.yml`:

```yaml
kube_proxy_exclude_cidrs: []
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (same file, line 68 in each tag).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Relevant when `kube_proxy_mode` is `ipvs`.

## References
- roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
