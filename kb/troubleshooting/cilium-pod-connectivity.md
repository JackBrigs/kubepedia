---
id: TROUBLE-CILIUM_POD_CONNECTIVITY
type: troubleshooting
title: "Cilium: pod-to-pod / cross-node connectivity broken"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.18.0 <=1.19.6"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - cilium pods cant reach each other
  - cilium cross node connectivity
  - cilium endpoint not ready
  - cilium connectivity test
tags:
  - troubleshooting
  - cilium
  - networking
  - cni
sources:
  - type: docs
    path: Cilium troubleshooting
    url: https://docs.cilium.io/en/stable/operations/troubleshooting/
    note: "cilium status, connectivity test, endpoint/identity"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
  - type: see_also
    target: TROUBLE-NFTABLES_KERNEL_TOO_LOW
---

# Cilium: pod-to-pod / cross-node connectivity broken

## Summary

Pods can't reach each other (often only **across nodes**), or new pods have no network. Start
with `cilium status` and the agent/endpoint state, then check the datapath (routing/tunnel,
kernel, and any conflicting CNI or NetworkPolicy).

## Problem

- Cross-node pod-to-pod traffic times out (same-node works).
- New pods stuck without an IP / `NetworkNotReady`.
- Intermittent drops; DNS or service VIPs unreachable.

## Context

- Applies to Cilium **1.18–1.19.6** (base ≤1.19.3 — [[COMPONENT-CILIUM]]).

## Diagnostics

1. `cilium status` (in the agent pod) — agent health, KVStore/kube-apiserver connectivity,
   `Controller Status`, IPAM.
2. `cilium endpoint list` — endpoints should be `ready`; identities resolved. Endpoints stuck
   `waiting-for-identity` point at the operator/kube-apiserver.
3. `cilium connectivity test` (the built-in suite) isolates same-node vs cross-node vs
   service vs DNS.
4. **Cross-node specifically:** verify the routing mode — **tunnel (VXLAN/Geneve)** needs its
   UDP ports open between nodes (8472/6081); **native routing** needs the underlay to route pod
   CIDRs. A blocked port or MTU mismatch breaks only cross-node traffic
   ([[TROUBLE-FIREWALL_PORTS_BLOCKED]]).
5. **Kernel floor:** features like the nftables/eBPF datapath, WireGuard encryption need a
   recent kernel ([[TROUBLE-NFTABLES_KERNEL_TOO_LOW]]).
6. **NetworkPolicy:** a default-deny or too-broad CiliumNetworkPolicy can be the "connectivity
   broke" cause — check policies and Hubble flows.

## Known Issues

- A second CNI or leftover iptables/CNI config from a previous plugin causes partial
  connectivity — ensure only Cilium manages the datapath.
- Cilium 1.18–1.19 patches close several CVEs — stay current within the minor.

## References

- Cilium troubleshooting docs (above); component: [[COMPONENT-CILIUM]]; kernel floor:
  [[TROUBLE-NFTABLES_KERNEL_TOO_LOW]].
