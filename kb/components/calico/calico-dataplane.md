---
id: CONFIG-CALICO_DATAPLANE
type: configuration
title: "Calico dataplane & encapsulation modes (Kubespray)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: ">=3.30.3 <=3.31.5"
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - calico vxlan bgp ipip
  - calico ebpf dataplane
  - calico network backend
  - calico encapsulation mode
  - calico wireguard nftables
tags:
  - calico
  - networking
  - configuration
  - dataplane
sources:
  - type: code
    path: roles/network_plugin/calico_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/calico_defaults/defaults/main.yml
    note: "calico_network_backend/vxlan/ipip/bpf/wireguard/nftable defaults"
relations:
  - type: see_also
    target: COMPONENT-CALICO
  - type: see_also
    target: CONCEPT-CLUSTER_NETWORKING
---

# Calico dataplane & encapsulation modes (Kubespray)

## Summary

Calico's networking is a choice of **dataplane** (iptables / eBPF / nftables) and
**encapsulation** (VXLAN / IPIP / none-BGP), plus optional WireGuard encryption. Kubespray
defaults to the **iptables dataplane with VXLAN** encapsulation; this doc lists the modes, the
Kubespray variables that select them, and the trade-offs.

## Configuration

Calico's behaviour is largely a choice of **dataplane** and **encapsulation**. Kubespray's
defaults (`calico_defaults`) and the alternatives:

**Encapsulation / backend.**

- **`calico_network_backend`** — **`vxlan`** (Kubespray default) or **`bird`** (BGP). VXLAN
  works on any L3 network without router config; BGP peers with the fabric for
  native/unencapsulated routing.
- **VXLAN** (default on): `calico_vxlan_mode: Always` (VNI **4096**, port **4789**);
  `CrossSubnet` encapsulates only across subnets, `Never` disables it.
- **IPIP** (default **off**): `calico_ipip_mode: Never`, `calico_ipv4pool_ipip: "Off"` — the
  older encapsulation; VXLAN is preferred now.
- Use **VXLAN or IPIP, not both**; on the same subnet `CrossSubnet` avoids needless
  encapsulation.

**BGP mode** (`calico_network_backend: bird`).

- `global_as_num: 64512`, `calico_bgp_listen_port: 179`; peer with the physical fabric
  (`peer_with_router`) or with **route reflectors** (`peer_with_calico_rr`, the `calico/rr`
  role) to avoid a full node-to-node mesh at scale.
- Can **advertise** Service IPs to the fabric: `calico_advertise_service_external_ips`,
  `calico_advertise_service_loadbalancer_ips`.

**eBPF dataplane** (`calico_bpf_enabled: false` by default).

- Enables a higher-performance eBPF datapath and can **replace kube-proxy**
  (`calico_bpf_service_mode: Tunnel`|`DSR`). Switching dataplane on a live cluster is
  disruptive — treat as its own change.

**nftables dataplane** (`calico_nftable_mode: "Disabled"`).

- Opt-in nftables datapath (alternative to iptables); `calico_iptables_backend: Auto` otherwise
  auto-selects the iptables variant.

**WireGuard encryption** (`calico_wireguard_enabled: false`).

- Enables in-cluster **WireGuard** encryption of pod traffic (needs the kernel module /
  packages). Independent of the encapsulation choice.

## Compatibility

- **MTU:** encapsulation reduces the usable MTU (VXLAN ≈ −50 bytes, IPIP ≈ −20, WireGuard ≈
  −60). A wrong MTU causes intermittent large-packet drops — set the Calico MTU to match the
  underlay minus overhead. See [[TROUBLE-CALICO_NODE_ISSUES]].
- **Switching modes** (VXLAN↔BGP, enabling eBPF/WireGuard/nftables) is a **disruptive**
  cluster-wide change — plan a maintenance window; don't flip it casually.
- eBPF mode with kube-proxy replacement means **not** running kube-proxy — coordinate the two.

## References

- `calico_defaults/defaults/main.yml` (v2.31.0, above); component: [[COMPONENT-CALICO]];
  networking: [[CONCEPT-CLUSTER_NETWORKING]]; troubleshooting: [[TROUBLE-CALICO_NODE_ISSUES]].
