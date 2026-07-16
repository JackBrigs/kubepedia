---
id: VARIABLE-KUBE_PODS_SUBNET
type: variable
title: kube_pods_subnet
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - kube_pods_subnet
tags:
  - networking
  - cidr
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    lines: "248 (v2.31.0)"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "kube_pods_subnet: 10.233.64.0/18 (default, unchanged v2.29.0–v2.31.0)"
relations:
  - type: see_also
    target: VARIABLE-KUBE_SERVICE_ADDRESSES
  - type: see_also
    target: VARIABLE-KUBE_NETWORK_NODE_PREFIX
---

# kube_pods_subnet

## Summary

`kube_pods_subnet` is the CIDR from which pod IPs are allocated (the cluster pod
network). The default is `10.233.64.0/18` across `v2.29.0`–`v2.31.0`.

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/main.yml` (`10.233.64.0/18`,
unchanged across all four tags). The CNI carves this into per-node blocks sized by
[[VARIABLE-KUBE_NETWORK_NODE_PREFIX]]. It must not overlap with
[[VARIABLE-KUBE_SERVICE_ADDRESSES]] or the node/underlay network.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: default `10.233.64.0/18`.
- Its size, together with `kube_network_node_prefix`, caps how many nodes and pods
  the cluster can address.
- For dual-stack, a separate `kube_pods_subnet_ipv6` applies.
- Changing it after install is disruptive; set it before the first deploy.

## References

- `roles/kubespray_defaults/defaults/main/main.yml` — default (L235 in v2.29.0,
  L248 in v2.31.0; shifts by tag).
- Tags: v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`.
