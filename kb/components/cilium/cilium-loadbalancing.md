---
id: CONCEPT-CILIUM_LOADBALANCING
type: concept
title: "Cilium service load-balancing (LB IPAM, L2 announcements, BGP)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium loadbalancer
  - cilium lb ipam
  - cilium l2 announcements
  - cilium bgp
  - cilium replace metallb
  - CiliumLoadBalancerIPPool
tags:
  - cilium
  - load-balancer
  - bgp
  - networking
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "cilium_loadbalancer_mode/_ip_pools, cilium_l2announcements, cilium_enable_bgp_control_plane + bgpv2 config (tag v2.31.0)"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
  - type: see_also
    target: CONCEPT-CILIUM_DATAPATH
  - type: see_also
    target: TROUBLE-METALLB_SERVICE_PENDING
---

# Cilium service load-balancing (LB IPAM, L2 announcements, BGP)

## Summary

Cilium can serve `type: LoadBalancer` Services **itself** — assigning external IPs from
its own IP pools and announcing them over **L2** or **BGP** — which can **replace
MetalLB**. All of it is **off by default** in Kubespray; you enable the IP pool plus one
announcement mechanism.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`, `kube_network_plugin: cilium`.
- Two independent concerns: **allocating** the external IP (LB IPAM) and **announcing**
  it to the network (L2 or BGP).

## Implementation

**LB IPAM (allocation):**

- `cilium_loadbalancer_ip_pools: []` — define `CiliumLoadBalancerIPPool`s (CIDRs/ranges)
  from which LoadBalancer Services get their external IP.
- `cilium_loadbalancer_mode: snat` (default) — datapath mode for LB traffic; `dsr` for
  direct-server-return.

**L2 announcements (replaces MetalLB L2):**

- `cilium_l2announcements: false` — when enabled, Cilium announces LoadBalancer/ExternalIP
  addresses over **ARP/L2**, the direct analogue of MetalLB's L2 mode. If you turn this
  on, you typically **remove MetalLB** to avoid two controllers fighting over the same
  IPs ([[TROUBLE-METALLB_SERVICE_PENDING]]).

**BGP (routed announcement):**

- `cilium_enable_bgp_control_plane: false` — enables Cilium's BGP control plane.
- New **bgpv2** API (Cilium ≥ 1.16): `cilium_bgp_cluster_configs`,
  `cilium_bgp_peer_configs`, `cilium_bgp_advertisements`,
  `cilium_bgp_node_config_overrides`.
- Legacy API: `cilium_bgp_peering_policies` (older `CiliumBGPPeeringPolicy`).

## Compatibility

- **Cilium LB vs MetalLB:** pick **one**. Cilium LB IPAM + L2/BGP is a native alternative
  to MetalLB; running both risks duplicate ARP/route announcements for the same VIPs.
- **L2** needs all nodes on the same L2 segment as the LB range (like MetalLB L2);
  **BGP** needs your routers peered with Cilium — same trade-off as MetalLB L2 vs BGP.
- The **bgpv2** config keys require Cilium `≥ 1.16` (our range ships `1.18`–`1.19`, so
  they apply); don't mix bgpv2 keys with the legacy peering-policy on the same cluster.
- LB datapath builds on the base datapath ([[CONCEPT-CILIUM_DATAPATH]]); with eBPF
  kube-proxy replacement, Cilium already owns Service routing.

## References

- `cilium/defaults/main.yml` (LB/L2/BGP knobs) at tag `v2.31.0`. Datapath:
  [[CONCEPT-CILIUM_DATAPATH]]; MetalLB alternative: [[TROUBLE-METALLB_SERVICE_PENDING]].
