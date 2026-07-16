---
id: VARIABLE-KUBE_PROXY_IPVS_MODULES
type: variable
title: kube_proxy_ipvs_modules
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_proxy_ipvs_modules
tags:
  - kube-proxy
  - ipvs
  - kernel-modules
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Defines kube_proxy_ipvs_modules, the list of IPVS kernel modules to load"
relations: []
---

# kube_proxy_ipvs_modules

## Summary
List of IPVS kernel modules that must be loaded on nodes when kube-proxy runs in IPVS mode. Default list: `ip_vs`, `ip_vs_rr`, `ip_vs_wrr`, `ip_vs_sh`, `ip_vs_wlc`, `ip_vs_lc`.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml`:

```yaml
kube_proxy_ipvs_modules:
  - ip_vs
  - ip_vs_rr
  - ip_vs_wrr
  - ip_vs_sh
  - ip_vs_wlc
  - ip_vs_lc
```

The list is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 178 in v2.29.0/v2.29.1, line 175 in v2.30.0, line 177 in v2.31.0).

## Compatibility
Applies to Kubespray v2.29.0–v2.31.0. Relevant when `kube_proxy_mode` is `ipvs`. Related IPVS variable: `kube_proxy_scheduler`.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
