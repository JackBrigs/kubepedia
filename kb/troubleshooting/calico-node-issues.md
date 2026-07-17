---
id: TROUBLE-CALICO_NODE_ISSUES
type: troubleshooting
title: "Calico: calico-node CrashLoop / node NotReady / no pod networking"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: "3.31.5"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - calico-node crashloopbackoff
  - calico node not ready
  - calico bgp not peering
  - calico ip autodetection wrong interface
  - calico mtu packet drops
tags:
  - troubleshooting
  - calico
  - cni
  - networking
sources:
  - type: docs
    path: Calico component status / troubleshooting
    url: https://docs.tigera.io/calico/latest/operations/troubleshoot/
    note: "calicoctl node status, Felix/BIRD, IP autodetection"
relations:
  - type: see_also
    target: COMPONENT-CALICO
  - type: see_also
    target: CONFIG-CALICO_DATAPLANE
  - type: see_also
    target: TROUBLE-NFTABLES_KERNEL_TOO_LOW
---

# Calico: calico-node CrashLoop / node NotReady / no pod networking

## Summary

`calico-node` pods crashloop or nodes stay `NotReady` with `network plugin is not ready`, or
pod-to-pod traffic fails across nodes. The usual causes: **IP autodetection** picking the wrong
interface, **BGP** not peering, an **encapsulation/MTU** mismatch, or a kernel/dataplane
prerequisite.

## Problem

- `calico-node` `CrashLoopBackOff` / readiness failing; nodes `NotReady`
  (`cni plugin not initialized`).
- Cross-node pod traffic times out (same-node works); intermittent large-packet drops.
- BGP sessions never establish (BGP mode).

## Context

- Applies to Calico **3.31.x** (Kubespray default CNI — [[COMPONENT-CALICO]]); dataplane modes
  in [[CONFIG-CALICO_DATAPLANE]].

## Diagnostics

- **Node status:** `calicoctl node status` (or check `calico-node` logs) — shows the Felix/BIRD
  health and BGP peer state.
- **IP autodetection (very common):** on multi-NIC nodes Calico may pick the wrong source IP.
  Set the autodetection method (`IP_AUTODETECTION_METHOD`, e.g. `interface=eth0` or
  `cidr=<node-subnet>`) so calico-node advertises the right address — a wrong pick breaks
  cross-node routing and can crashloop the node.
- **BGP not peering:** verify `global_as_num`, peer addresses, and that **TCP/179** is open both
  ways; at scale use route reflectors (`peer_with_calico_rr`) instead of a full mesh
  ([[CONFIG-CALICO_DATAPLANE]]).
- **Encapsulation/MTU:** a wrong MTU (not accounting for VXLAN ≈50 / IPIP ≈20 / WireGuard ≈60
  overhead) causes intermittent failures on large packets — set the Calico MTU to underlay
  minus overhead. Ensure you're not mixing VXLAN and IPIP.
- **Kernel prerequisites:** eBPF dataplane, WireGuard, and nftables mode need recent kernel
  features — an old kernel makes calico-node fail to start
  ([[TROUBLE-NFTABLES_KERNEL_TOO_LOW]]).
- **RPF / firewall:** reverse-path filtering or a host firewall can drop encapsulated traffic;
  `calico_node_ignorelooserpf` and the VXLAN/BGP ports must be allowed.
- **Datastore (kdd):** calico-node needs API access to its CRDs — RBAC/apiserver problems show
  as calico-node not becoming ready.

## Known Issues

- Switching dataplane/encapsulation on a live cluster is disruptive — a half-applied switch
  leaves mixed-mode nodes that can't talk ([[CONFIG-CALICO_DATAPLANE]]).
- Large clusters without **Typha** put heavy watch load on the API server — enable
  `typha_enabled` past a few hundred nodes.

## References

- Calico troubleshooting docs (above); component: [[COMPONENT-CALICO]]; dataplane:
  [[CONFIG-CALICO_DATAPLANE]]; kernel floor: [[TROUBLE-NFTABLES_KERNEL_TOO_LOW]].
