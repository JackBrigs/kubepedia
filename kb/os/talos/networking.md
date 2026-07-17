---
id: CONCEPT-TALOS_NETWORKING
type: concept
title: "Talos networking — interfaces, control-plane VIP, KubeSpan, CNI"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "1.13.6"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - talos network config
  - talos control plane vip
  - talos kubespan wireguard
  - talos cni cilium
  - talos machine network
tags:
  - os
  - talos
  - networking
  - documentation
sources:
  - type: docs
    path: Talos network configuration
    url: https://www.talos.dev/latest/talos-guides/network/
    note: "interfaces, VIP, KubeSpan, host DNS"
  - type: docs
    path: Talos CNI
    url: https://www.talos.dev/latest/kubernetes-guides/network/deploying-cilium/
    note: "default Flannel; cni.name none + Cilium"
relations:
  - type: see_also
    target: CONCEPT-TALOS_OS_K8S
  - type: see_also
    target: CONCEPT-TALOS_MACHINE_CONFIG
  - type: see_also
    target: COMPONENT-CILIUM
---

# Talos networking — interfaces, control-plane VIP, KubeSpan, CNI

## Summary

Talos node networking is declared under **`machine.network`**; cluster networking (pod/service
subnets, CNI) under **`cluster.network`**. Two Talos-specific features matter: a built-in
**control-plane VIP** for API HA without an external load balancer, and **KubeSpan**, a managed
WireGuard mesh.

## Context

- Applies to Talos **1.13.x** ([[CONCEPT-TALOS_OS_K8S]]). Configured via machine config
  ([[CONCEPT-TALOS_MACHINE_CONFIG]]).

## Implementation

**Interfaces / addressing.** Under `machine.network.interfaces[]`: static addresses or DHCP,
routes, bonds, VLANs, MTU, plus `hostname` and `nameservers`. Host DNS resolver is controlled
by `machine.features.hostDNS`.

**Control-plane VIP (API HA).**

- Set `machine.network.interfaces[].vip.ip: <shared-ip>` on the control-plane nodes. Talos
  elects a holder via **etcd** (the current leader owns the VIP at layer 2), so the API endpoint
  **floats** to a healthy CP node — **no external load balancer needed** for the control plane.
- Use the VIP as the `cluster.controlPlane.endpoint` and in `certSANs`.

**KubeSpan (WireGuard mesh).**

- `machine.network.kubespan.enabled: true` + the discovery service builds a **full WireGuard
  mesh** between nodes, even across different networks / behind NAT — useful for hybrid/edge
  clusters. Talos 1.13 adds `excludeAdvertisedNetworks` in `KubeSpanConfig` to filter which
  networks a node advertises.

**CNI.**

- Talos's **default CNI is Flannel**. To run another CNI (e.g. **Cilium** — the platform's
  choice, [[COMPONENT-CILIUM]]), set `cluster.network.cni.name: none` and install it yourself
  (Helm/manifests), typically with Cilium configured for the Talos environment (e.g. kube-proxy
  replacement, correct cgroup/host paths).

## Compatibility

- The VIP is a **layer-2** mechanism (nodes must share an L2 segment); on clouds that block ARP
  VIPs, use a cloud LB for the API instead (same constraint as other L2 VIPs).
- Running Cilium in kube-proxy-replacement mode means **not** deploying kube-proxy — set
  `cluster.proxy.disabled: true` accordingly.

## References

- Talos network + CNI guides (above); config: [[CONCEPT-TALOS_MACHINE_CONFIG]]; Cilium:
  [[COMPONENT-CILIUM]]; overview: [[CONCEPT-TALOS_OS_K8S]].
