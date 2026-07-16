---
id: VARIABLE-CILIUM_TUNNEL_MODE
type: variable
title: cilium_tunnel_mode
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - cilium_tunnel_mode
tags:
  - cilium
  - networking
  - datapath
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "cilium_tunnel_mode: vxlan (default, unchanged v2.29.0–v2.31.0)"
relations:
  - type: part_of
    target: COMPONENT-CILIUM
---

# cilium_tunnel_mode

## Summary

`cilium_tunnel_mode` selects Cilium's overlay encapsulation for pod traffic. The
default is `vxlan` across `v2.29.0`–`v2.31.0`. Other values (e.g. `geneve`, or
disabling tunneling for native/direct routing) change how pod packets traverse the
underlay.

## Implementation

Defined in `roles/network_plugin/cilium/defaults/main.yml` (`vxlan`, unchanged
across all four tags). With `vxlan`, pod-to-pod traffic between nodes is
VXLAN-encapsulated, which works on most underlays without extra routing. Applies
only when [[COMPONENT-CILIUM]] is the CNI.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: default `vxlan`.
- Effective only with `kube_network_plugin: cilium`.
- Native-routing setups change this together with related Cilium routing options;
  confirm the underlay supports the chosen mode.

## References

- `roles/network_plugin/cilium/defaults/main.yml` — default (tags v2.29.0
  `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`).
