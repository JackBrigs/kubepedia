---
id: COMPONENT-KUBE_ROUTER
type: component
title: Kube-router (CNI)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: "2.1.1"
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - kube-router
  - kube_router
  - kube_network_plugin kube-router
  - kube-router bgp
tags:
  - cni
  - networking
  - kube-router
  - bgp
sources:
  - type: code
    path: roles/network_plugin/kube-router/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/kube-router/defaults/main.yml
    note: "run_router/firewall/service_proxy, enable_dsr"
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "kube_router_version 2.1.1"
relations:
  - type: depends_on
    target: VARIABLE-KUBE_NETWORK_PLUGIN
  - type: see_also
    target: COMPONENT-CALICO
---

# Kube-router (CNI)

## Summary

Kube-router (`kube_network_plugin: kube-router`) is an **all-in-one** networking daemon: a
**BGP** router (pod routing, no overlay), a **NetworkPolicy** firewall (ipset/iptables), and an
optional **service proxy** (IPVS, kube-proxy replacement). At v2.31.0 it ships **2.1.1**. One
DaemonSet does routing + policy + (optionally) services.

## Context

- Covers Kubespray `v2.29.0`–`v2.31.0`. Select via [[VARIABLE-KUBE_NETWORK_PLUGIN]]. Attractive
  where you want native BGP routing + policy without a separate proxy, on a BGP-capable fabric.

## Implementation

- One DaemonSet enables three roles independently:
  - **`kube_router_run_router: true`** — BGP-based pod routing (peers with the fabric / other
    nodes; native routing, no encapsulation by default).
  - **`kube_router_run_firewall: true`** — NetworkPolicy enforcement.
  - **`kube_router_run_service_proxy: false`** — opt-in IPVS service proxy (replaces kube-proxy
    when enabled).
- `kube_router_enable_dsr` (Direct Server Return) and metrics are optional.

## Configuration

- **BGP:** peer with the physical routers for native pod routing; without a BGP fabric you rely
  on node-to-node BGP (full mesh at small scale).
- **Service proxy:** enabling `run_service_proxy` means **not** running kube-proxy — coordinate
  the two (like Cilium/Calico-eBPF kube-proxy replacement).

## Compatibility

- **Kubernetes:** kube-router 2.1.x supports the base's 1.31–1.35 window.
- **Native routing needs an L3/BGP-friendly underlay** — on networks that can't route pod CIDRs
  you'd need an overlay (kube-router is happiest with BGP).
- **Switching CNI** on a live cluster is disruptive.

## References

- kube-router defaults + download vars (v2.31.0, above); selection:
  [[VARIABLE-KUBE_NETWORK_PLUGIN]]; alternative: [[COMPONENT-CALICO]].
