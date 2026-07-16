---
id: VARIABLE-CILIUM_NATIVE_ROUTING_CIDR_IPV6
type: variable
title: cilium_native_routing_cidr_ipv6
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_native_routing_cidr_ipv6
tags:
  - cilium
  - cni
  - routing
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Default cilium_native_routing_cidr_ipv6: \"\" (empty)"
relations: []
---

# cilium_native_routing_cidr_ipv6

## Summary
Explicitly specifies the IPv6 CIDR for native routing (the IPv6 counterpart of `cilium_native_routing_cidr`). Default `""` (empty, disabled). Rendered into the Cilium Helm values as `ipv6NativeRoutingCIDR`.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as `cilium_native_routing_cidr_ipv6: ""`. Consumed by `roles/network_plugin/cilium/templates/values.yaml.j2` as `ipv6NativeRoutingCIDR` (unquoted in v2.29.0-v2.30.0, quoted `"{{ cilium_native_routing_cidr_ipv6 }}"` in v2.31.0). The default empty value is unchanged across v2.29.0-v2.31.0 (line number shifts: 96 in v2.29.0/v2.29.1, 94 in v2.30.0, 79 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variables: `cilium_native_routing_cidr`, `cilium_auto_direct_node_routes`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
