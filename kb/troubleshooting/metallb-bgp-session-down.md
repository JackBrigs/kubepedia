---
id: TROUBLE-METALLB_BGP_SESSION_DOWN
type: troubleshooting
title: "MetalLB: BGP session not established / routes not advertised"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.13.0 <=0.16.1"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - metallb bgp session down
  - metallb routes not advertised
  - bgppeer not connecting
  - metallb frr session idle
tags:
  - troubleshooting
  - metallb
  - bgp
  - networking
sources:
  - type: docs
    path: MetalLB BGP configuration
    url: https://metallb.universe.tf/configuration/_advanced_bgp_configuration/
    note: "BGPPeer, BGPAdvertisement, FRR mode"
relations:
  - type: see_also
    target: COMPONENT-METALLB
  - type: see_also
    target: TROUBLE-METALLB_CONFIG_CRD_FRR
  - type: see_also
    target: TROUBLE-FIREWALL_PORTS_BLOCKED
---

# MetalLB: BGP session not established / routes not advertised

## Summary

In BGP mode a `LoadBalancer` IP isn't reachable because the **BGP session** to the router is
not `Established`, or the pool isn't advertised. Check the `BGPPeer`/`BGPAdvertisement` CRs,
ASNs, and TCP/179 reachability.

## Problem

- Service external IP assigned but not routable from outside.
- BGP session stuck `Idle`/`Connect`/`Active` (never `Established`).
- Some pools advertised, others not.

## Context

- Applies to MetalLB **0.13–0.16** (base 0.13.9 — [[COMPONENT-METALLB]]). Config is CRD-only
  ([[TROUBLE-METALLB_CONFIG_CRD_FRR]]).

## Diagnostics

1. **BGPPeer:** verify `myASN`, `peerASN`, `peerAddress`, and (if eBGP multihop) `ebgpMultiHop`
   and source address. A mismatch keeps the session down.
2. **Session state:** check the speaker/FRR pod — in FRR mode exec `vtysh -c "show bgp summary"`
   to see neighbor state; the upstream router must also be configured to peer back.
3. **Ports/reachability:** **TCP/179** must be open both ways between the node and the router
   ([[TROUBLE-FIREWALL_PORTS_BLOCKED]]).
4. **Advertisement:** a `BGPAdvertisement` must reference the pool (via `ipAddressPools` or
   labels) — without it the pool's IPs aren't advertised even with a healthy session. Check
   `aggregationLength`/communities if the router filters routes.
5. **Node selection:** advertisements originate from speaker nodes; confirm the speaker
   DaemonSet runs where expected and node selectors match.

## Known Issues

- FRR vs native mode must match your CRs and be chosen at install
   ([[TROUBLE-METALLB_CONFIG_CRD_FRR]]); the newer `FRR-K8s` mode changes how BGP config is
   delivered.

## References

- MetalLB BGP docs (above); component: [[COMPONENT-METALLB]]; config model:
  [[TROUBLE-METALLB_CONFIG_CRD_FRR]].
