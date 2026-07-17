---
id: COMPONENT-KUBE_OVN
type: component
title: Kube-OVN (CNI)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: "1.12.21"
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - kube-ovn
  - kube_ovn
  - ovn cni
  - kube_network_plugin kube-ovn
tags:
  - cni
  - networking
  - kube-ovn
  - ovn
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "kube_ovn_version 1.12.21 (+ dpdk 19.11-v...)"
relations:
  - type: depends_on
    target: VARIABLE-KUBE_NETWORK_PLUGIN
  - type: see_also
    target: COMPONENT-CALICO
---

# Kube-OVN (CNI)

## Summary

Kube-OVN (`kube_network_plugin: kube-ovn`) brings **OVN/OVS** (SDN) networking to Kubernetes —
the most feature-rich Kubespray CNI: per-namespace **subnets**, **VPCs**, static IPs,
QoS/bandwidth, gateways, and optional **DPDK**. At v2.31.0 it ships **1.12.21**. It's powerful
but heavier operationally than Calico/Flannel.

## Context

- Covers Kubespray `v2.29.0`–`v2.31.0`. Select via [[VARIABLE-KUBE_NETWORK_PLUGIN]]. Choose it
  when you need OVN features (multi-tenant subnets/VPC, advanced L2/L3); otherwise Calico is
  simpler ([[COMPONENT-CALICO]]).

## Implementation

- Deploys the OVN central DB (`ovn-central`), `ovs-ovn` (per node), and `kube-ovn-controller`/
  `kube-ovn-cni`. Networking is programmed via OVN logical switches/routers.
- Version tracks `kube_ovn_version` (1.12.21); a DPDK image variant exists
  (`kube_ovn_dpdk_version`).

## Configuration

- Core objects: **`Subnet`** (CIDR, gateway, per-namespace), **`Vpc`** (isolated routers),
  `IptablesEIP`/gateways for external access. Default subnet vs custom per-namespace subnets.
- DPDK is opt-in (userspace datapath) for high-throughput NFV — extra host requirements.

## Compatibility

- **Kubernetes:** kube-ovn 1.12.x supports the base's 1.31–1.35 window.
- **Operational weight:** the OVN/OVS control plane (central DB, per-node OVS) is more to run
  and debug than an iptables/eBPF CNI — factor in the OVN skill requirement.
- **Switching CNI** on a live cluster is disruptive.

## References

- kube-ovn download vars (v2.31.0, above); selection: [[VARIABLE-KUBE_NETWORK_PLUGIN]];
  alternative: [[COMPONENT-CALICO]].
