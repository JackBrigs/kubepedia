---
id: VARIABLE-KUBE_NETWORK_NODE_PREFIX
type: variable
title: kube_network_node_prefix
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - kube_network_node_prefix
tags:
  - networking
  - cidr
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    lines: "265 (v2.31.0)"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "kube_network_node_prefix: 24 (default, unchanged v2.29.0–v2.31.0)"
relations:
  - type: see_also
    target: VARIABLE-KUBE_PODS_SUBNET
---

# kube_network_node_prefix

## Summary

`kube_network_node_prefix` is the subnet prefix length each node gets carved out
of [[VARIABLE-KUBE_PODS_SUBNET]] for its pods. The default is `24` across
`v2.29.0`–`v2.31.0` (256 pod IPs per node).

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/main.yml` (`24`, unchanged
across all four tags). Together with `kube_pods_subnet` it determines the maximum
number of nodes: e.g. a `/18` pod subnet split into `/24` blocks yields up to 64
node blocks.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: default `24`.
- Lower the prefix (larger blocks) for more pods per node; raise it for more nodes.
  Balance against the size of `kube_pods_subnet`.

## References

- `roles/kubespray_defaults/defaults/main/main.yml` — default (L252 in v2.29.0,
  L265 in v2.31.0; shifts by tag).
- Tags: v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`.
