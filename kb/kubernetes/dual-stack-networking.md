---
id: CONFIG-DUAL_STACK
type: configuration
title: "Dual-stack (IPv4/IPv6) networking in Kubespray"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - dual stack
  - enable_dual_stack_networks
  - ipv6 kubernetes
  - kube_pods_subnet_ipv6
  - kube_service_addresses_ipv6
tags:
  - networking
  - dual-stack
  - ipv6
  - configuration
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "enable_dual_stack_networks, kube_*_ipv6 CIDR defaults (tag v2.31.0)"
relations:
  - type: see_also
    target: CONCEPT-SAMPLE_INVENTORY_LAYOUT
  - type: see_also
    target: TROUBLE-KUBESPRAY_PREFLIGHT_FAILS
---

# Dual-stack (IPv4/IPv6) networking in Kubespray

## Summary

Kubespray can deploy a **dual-stack** cluster (IPv4 **and** IPv6) with
`enable_dual_stack_networks` (default `false`). When enabled, pods and Services get both
an IPv4 and an IPv6 address from separate CIDRs. It is a cluster-wide, install-time
decision — plan the CIDRs and node addressing up front.

## Configuration

Defaults (`roles/kubespray_defaults/defaults/main/main.yml`):

| Variable | Default | Purpose |
|----------|---------|---------|
| `enable_dual_stack_networks` | `false` | master switch (drives `ipv6_stack`) |
| `kube_pods_subnet` | `10.233.64.0/18` | IPv4 pod CIDR |
| `kube_pods_subnet_ipv6` | `fd85:ee78:d8a6:8607::1:0000/112` | IPv6 pod CIDR |
| `kube_service_addresses` | `10.233.0.0/18` | IPv4 service CIDR |
| `kube_service_addresses_ipv6` | `fd85:ee78:d8a6:8607::1000/116` | IPv6 service CIDR |
| `kube_network_node_prefix` | `24` | per-node IPv4 pod subnet size |

- Set `enable_dual_stack_networks: true` and provide routable/ULA IPv6 CIDRs (the
  defaults are example ULA ranges — replace them for real networks).
- Nodes must actually **have** IPv6 addresses; the `ip`/`access_ip` and node config must
  reflect both families.
- The CNI must support dual-stack (Cilium and Calico do); confirm CNI-specific dual-stack
  settings for your plugin.

## Compatibility

- Applies to Kubespray `v2.29.0`–`v2.31.0`. Dual-stack is a **day-0** choice — converting
  a single-stack cluster to dual-stack in place is not a supported flip; plan it at
  install.
- Kubernetes **`MultiCIDRServiceAllocator`** graduated to GA in `1.33`
  ([[CONCEPT-K8S_FEATURE_GATES]]), improving service-CIDR handling relevant to dual-stack.
- Firewall/routing must permit the IPv6 pod/service CIDRs the same way as IPv4
  ([[TROUBLE-KUBESPRAY_PREFLIGHT_FAILS]] covers the `ip`-matches-host preflight, which
  applies to IPv6 too).
- kube-proxy/CNI backend must be IPv6-capable (nftables/ipvs/iptables all support it on a
  modern kernel).

## References

- `enable_dual_stack_networks` and `kube_*_ipv6` CIDRs at tag `v2.31.0`. Inventory:
  [[CONCEPT-SAMPLE_INVENTORY_LAYOUT]]; service-CIDR feature: [[CONCEPT-K8S_FEATURE_GATES]].
