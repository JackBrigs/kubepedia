---
id: VARIABLE-CILIUM_BGP_PEER_CONFIGS
type: variable
title: cilium_bgp_peer_configs
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_bgp_peer_configs
tags:
  - cilium
  - cni
  - bgp
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "List of Cilium BGP peer config resources; default []"
relations: []
---

# cilium_bgp_peer_configs

## Summary
Holds the list of Cilium BGP peer configuration definitions (e.g. `CiliumBGPPeerConfig` resources). Defaults to an empty list `[]`, meaning no BGP peer configs are created.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as:

```yaml
cilium_bgp_peer_configs: []
```

The default value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line number shifts: 320 in v2.29.0/v2.29.1, 318 in v2.30.0, 300 in v2.31.0).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Cilium CNI only. Part of the Cilium BGP control-plane variable set alongside `cilium_bgp_cluster_configs`, `cilium_bgp_advertisements`, and `cilium_bgp_node_config_overrides`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
