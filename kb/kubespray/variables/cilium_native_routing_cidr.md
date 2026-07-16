---
id: VARIABLE-CILIUM_NATIVE_ROUTING_CIDR
type: variable
title: cilium_native_routing_cidr
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_native_routing_cidr
tags:
  - cilium
  - cni
  - routing
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Default cilium_native_routing_cidr: \"\" (empty)"
relations: []
---

# cilium_native_routing_cidr

## Summary
Explicitly specifies the IPv4 CIDR for native routing. When set, Cilium assumes networking for this CIDR is preconfigured and hands traffic destined for that range to the Linux network stack without applying SNAT. Default `""` (empty, disabled). Required for auto-direct-node-routes setups.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as `cilium_native_routing_cidr: ""`. Consumed by `roles/network_plugin/cilium/templates/values.yaml.j2` as `ipv4NativeRoutingCIDR` (unquoted in v2.29.0-v2.30.0, quoted `"{{ cilium_native_routing_cidr }}"` in v2.31.0). The default empty value is unchanged across v2.29.0-v2.31.0 (line number shifts: 93 in v2.29.0/v2.29.1, 91 in v2.30.0, 76 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variables: `cilium_native_routing_cidr_ipv6`, `cilium_auto_direct_node_routes`, `cilium_tunnel_mode`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
