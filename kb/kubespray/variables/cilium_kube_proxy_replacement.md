---
id: VARIABLE-CILIUM_KUBE_PROXY_REPLACEMENT
type: variable
title: cilium_kube_proxy_replacement
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - cilium_kube_proxy_replacement
tags:
  - cilium
  - kube-proxy
  - networking
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "cilium_kube_proxy_replacement: false (default, unchanged v2.29.0–v2.31.0)"
relations:
  - type: part_of
    target: COMPONENT-CILIUM
  - type: see_also
    target: VARIABLE-KUBE_PROXY_MODE
---

# cilium_kube_proxy_replacement

## Summary

`cilium_kube_proxy_replacement` controls whether Cilium replaces kube-proxy with
its eBPF datapath. The default is `false` across `v2.29.0`–`v2.31.0`, meaning
kube-proxy still runs (in the mode set by [[VARIABLE-KUBE_PROXY_MODE]]) and Cilium
does not take over service load balancing.

## Implementation

Defined in `roles/network_plugin/cilium/defaults/main.yml` (`false`, unchanged
across all four tags). When set to a replacement mode, Cilium programs service
handling in eBPF and kube-proxy can be removed; with the default `false`,
kube-proxy is retained. Applies only when [[COMPONENT-CILIUM]] is the CNI
(`kube_network_plugin: cilium`).

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: default `false`.
- Effective only with `kube_network_plugin: cilium`.
- Enabling it is the way to run a kube-proxy-free cluster with Cilium; verify the
  Cilium version supports the chosen replacement mode.

## References

- `roles/network_plugin/cilium/defaults/main.yml` — default (tags v2.29.0
  `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`).
