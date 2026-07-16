---
id: VARIABLE-CILIUM_BGP_CLUSTER_CONFIGS
type: variable
title: cilium_bgp_cluster_configs
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_bgp_cluster_configs
tags:
  - cilium
  - cni
  - bgp
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "List of Cilium BGP cluster config resources; default []"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_bgp_cluster_configs

## Summary
Holds the list of Cilium BGP cluster configuration definitions (e.g. `CiliumBGPClusterConfig` resources). Defaults to an empty list `[]`, meaning no BGP cluster config is created.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as:

```yaml
cilium_bgp_cluster_configs: []
```

The default value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line number shifts: 317 in v2.29.0/v2.29.1, 315 in v2.30.0, 297 in v2.31.0).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Cilium CNI only. Part of the Cilium BGP control-plane variable set alongside `cilium_bgp_peer_configs`, `cilium_bgp_advertisements`, and `cilium_bgp_node_config_overrides`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
