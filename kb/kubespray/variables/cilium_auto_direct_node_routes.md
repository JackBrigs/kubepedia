---
id: VARIABLE-CILIUM_AUTO_DIRECT_NODE_ROUTES
type: variable
title: cilium_auto_direct_node_routes
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_auto_direct_node_routes
tags:
  - cilium
  - cni
  - routing
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Enables Cilium auto direct node routes; default false"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_auto_direct_node_routes

## Summary
Controls Cilium's `auto-direct-node-routes` option, which installs direct routes between nodes when they share an L2 network. Defaults to `false`.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as:

```yaml
cilium_auto_direct_node_routes: false
```

The default value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line number shifts: 81 in v2.29.0/v2.29.1, 79 in v2.30.0, 64 in v2.31.0).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Cilium CNI only. Typically used with native routing (non-tunnel) modes where all nodes are on the same L2 segment.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
