---
id: CONCEPT-CILIUM_DATAPATH
type: concept
title: "Cilium datapath in Kubespray (tunnel vs native routing, IPAM, kube-proxy replacement)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium datapath
  - cilium tunnel mode vxlan
  - cilium native routing
  - cilium kube-proxy replacement
  - cilium ipam cluster-pool
  - cilium bpf masquerade
tags:
  - cilium
  - cni
  - networking
  - ebpf
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "cilium tunnel/ipam/kube-proxy-replacement/masquerade defaults (tag v2.31.0)"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
  - type: see_also
    target: CONCEPT-KUBE_PROXY
  - type: see_also
    target: TROUBLE-CILIUM_CONFIG_VALIDATION
---

# Cilium datapath in Kubespray (tunnel vs native routing, IPAM, kube-proxy replacement)

## Summary

Cilium's datapath has a few big switches that decide how pod traffic is carried and how
Services are handled. Kubespray's defaults are **VXLAN tunnel**, **cluster-pool IPAM**,
kube-proxy **kept** (Cilium not replacing it), and BPF masquerade **off**. Knowing these
defaults — and what flipping them implies — is the core of operating Cilium.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`, `kube_network_plugin: cilium`.
- Config knobs live in `roles/network_plugin/cilium/defaults/main.yml`; override in
  inventory (`k8s-net-cilium.yml` / group_vars).

## Implementation

**Traffic carriage:**

- `cilium_tunnel_mode: vxlan` (default) — overlay via VXLAN (UDP 8472; open it —
  [[TROUBLE-FIREWALL_PORTS_BLOCKED]]). Alternative `geneve`, or **native routing**.
- **Native routing** — set `cilium_native_routing_cidr` and often
  `cilium_auto_direct_node_routes: true` (default `false`); routes pod traffic without an
  overlay (requires an L3 fabric that can route the pod CIDR). Leaving
  `cilium_native_routing_cidr` empty while expecting native routing is a common
  misconfig ([[TROUBLE-CILIUM_CONFIG_VALIDATION]]).

**IP allocation:**

- `cilium_ipam_mode: cluster-pool` (default) — Cilium allocates pod IPs from a
  cluster-wide pool it manages (vs `kubernetes` host-scope IPAM).
- `cilium_identity_allocation_mode: crd` (default) — identities in CRDs (vs `kvstore`).

**Service handling:**

- `cilium_kube_proxy_replacement: false` (default) — kube-proxy stays; Cilium does **not**
  handle Services. Set it to `strict`/`true` for **eBPF kube-proxy replacement**, which
  makes Kubespray **skip** the kubeadm `addon/kube-proxy` ([[CONCEPT-KUBE_PROXY]]).
- `cilium_loadbalancer_mode: snat` (default) — LB datapath mode; `dsr` for
  direct-server-return.
- `cilium_loadbalancer_ip_pools: []` — LoadBalancer IP pools for Cilium's own LB IPAM.

**Performance:**

- `cilium_enable_bpf_masquerade: false`, `cilium_enable_bandwidth_manager: false` —
  eBPF-based masquerade and bandwidth shaping, opt-in.

## Compatibility

- Switching tunnel ↔ native routing on a running cluster changes the datapath and needs a
  Cilium restart and a routable pod CIDR — plan it, don't toggle casually.
- Enabling kube-proxy replacement mid-life must be coordinated with removing kube-proxy
  ([[CONCEPT-KUBE_PROXY]]); a half-migrated node double-handles Services.
- Config-validation asserts (identity mode, encryption pairing) run before deploy —
  [[TROUBLE-CILIUM_CONFIG_VALIDATION]].

## References

- `cilium/defaults/main.yml` at tag `v2.31.0`. Component: [[COMPONENT-CILIUM]];
  kube-proxy interaction: [[CONCEPT-KUBE_PROXY]].
