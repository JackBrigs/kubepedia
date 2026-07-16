---
id: VARIABLE-CILIUM_OPERATOR_CUSTOM_ARGS
type: variable
title: cilium_operator_custom_args
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_operator_custom_args
tags:
  - cilium
  - cni
  - operator
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Default cilium_operator_custom_args: [] (deprecated)"
relations: []
---

# cilium_operator_custom_args

## Summary
Extra arguments for the Cilium Operator. Default `[]` (empty list). Marked deprecated in the code (`# deprecated` inline comment); `cilium_operator_extra_args` is the current equivalent.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as `cilium_operator_custom_args: [] # deprecated`. The default empty list and the deprecated marker are unchanged across v2.29.0-v2.31.0 (line number shifts: 240 in v2.29.0/v2.29.1, 238 in v2.30.0, 223 in v2.31.0). Exposed to users (commented) in the sample inventory `k8s-net-cilium.yml`.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Deprecated in favor of `cilium_operator_extra_args`. Related variable: `cilium_operator_api_serve_addr`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
