---
id: VARIABLE-CILIUM_OPERATOR_API_SERVE_ADDR
type: variable
title: cilium_operator_api_serve_addr
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_operator_api_serve_addr
tags:
  - cilium
  - cni
  - operator
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Default cilium_operator_api_serve_addr: \"127.0.0.1:9234\""
relations: []
---

# cilium_operator_api_serve_addr

## Summary
The address at which the Cilium operator binds its health-check API. Default `"127.0.0.1:9234"`. Exposed to users (commented) in the sample inventory `k8s-net-cilium.yml`.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as `cilium_operator_api_serve_addr: "127.0.0.1:9234"` (under the comment "The address at which the cillium operator bind health check api"). The default value is unchanged across v2.29.0-v2.31.0 (line number shifts: 227 in v2.29.0/v2.29.1, 225 in v2.30.0, 210 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variables: `cilium_operator_replicas`, `cilium_operator_custom_args`, `cilium_operator_extra_args`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
