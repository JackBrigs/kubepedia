---
id: TROUBLE-CILIUM_BGP_V1_REMOVED
type: troubleshooting
title: "Cilium 1.19 BGP stops working — BGPv1 (CiliumBGPPeeringPolicy) removed, migrate to v2"
status: active
kubespray_version: ">=v2.30.0 <=v2.31.0"
kubernetes_version: ">=1.33 <=1.35"
component_version: ">=1.18.2 <=1.19.3"
verified_at: "2026-07-18"
confidence: confirmed
aliases:
  - CiliumBGPPeeringPolicy removed
  - cilium bgp v1 to v2 migration
  - cilium bgp not advertising after upgrade
  - CiliumBGPClusterConfig
  - bgpControlPlane v2alpha1 removed
tags:
  - cilium
  - troubleshooting
  - bgp
  - upgrade
sources:
  - type: docs
    path: Documentation/operations/upgrade.rst
    url: https://github.com/cilium/cilium/blob/v1.19.3/Documentation/operations/upgrade.rst
    note: "1.18 deprecates BGP v2alpha1→v2; 1.19 fully removes CiliumBGPPeeringPolicy / BGPv1"
relations:
  - type: see_also
    target: UPGRADE-CILIUM_1_15_TO_1_19
  - type: see_also
    target: COMPONENT-CILIUM
  - type: see_also
    target: TROUBLE-CILIUM_BGP_ADVERTISEMENT_LABELS
---

# Cilium 1.19 BGP stops working — BGPv1 (CiliumBGPPeeringPolicy) removed, migrate to v2

## Summary

Cilium removed the **BGPv1 control plane** and its `CiliumBGPPeeringPolicy` CRD in **1.19**. If your
cluster advertised routes via the old BGP API, BGP **stops working** after Kubespray moves Cilium to
**1.19.3 (v2.31.0)** unless you migrated to the **`cilium.io/v2` BGP CRDs** first
(`CiliumBGPClusterConfig`, `CiliumBGPPeerConfig`, `CiliumBGPAdvertisement`, `CiliumBGPNodeConfig`).
This is a staged trap: `v2alpha1` was **deprecated in 1.18** (v2.29.0/v2.30.0) and **removed in 1.19**.

## Problem

- After upgrading to Kubespray v2.31.0 (Cilium 1.19.3), BGP peers **drop** / routes are **no longer
  advertised**; LoadBalancer/pod-CIDR routes vanish from the fabric.
- `CiliumBGPPeeringPolicy` resources are ignored or rejected; the BGP control plane appears inactive.

## Context

- Applies to Cilium **1.19+** → Kubespray **v2.31.0** ([[COMPONENT-CILIUM]],
  [[UPGRADE-CILIUM_1_15_TO_1_19]]). The `v2alpha1` BGP CRDs were **deprecated in 1.18** and the whole
  **BGPv1** path (`CiliumBGPPeeringPolicy`) **removed in 1.19** (`upgrade.rst`@v1.19.3).
- The modern API is the **BGPv2** resource set under `cilium.io/v2`; it separates cluster config, peer
  config, advertisements, and per-node config.

## Diagnostics

- `kubectl get ciliumbgppeeringpolicies` — if these still exist and you're on 1.19, they're dead.
- `kubectl get ciliumbgpclusterconfigs ciliumbgppeerconfigs ciliumbgpadvertisements` — the v2 objects
  that should exist instead.
- `cilium bgp peers` (cilium CLI) shows session state; empty/absent after upgrade = unmigrated.

## Known Issues

- **Fix:** migrate BGP config from `CiliumBGPPeeringPolicy` to the **v2** CRDs **before** the v2.30.0 →
  v2.31.0 upgrade — translate peers/advertisements into `CiliumBGPClusterConfig` +
  `CiliumBGPPeerConfig` + `CiliumBGPAdvertisement`. Validate BGP sessions come up on a canary before
  rolling ([[PRACTICE-RUNBOOK_CONFIG_CHANGE]]).
- **Also removed earlier:** `metallb-bgp` support was removed back in **1.17** (Kubespray v2.28.0) —
  Cilium BGP control plane is the only in-Cilium BGP path across the range.
- Label/selector pitfalls in advertisements: [[TROUBLE-CILIUM_BGP_ADVERTISEMENT_LABELS]].

## References

- Cilium `Documentation/operations/upgrade.rst`@v1.19.3 (BGPv1 removed) / @v1.18.2 (v2alpha1→v2).
  Full jump [[UPGRADE-CILIUM_1_15_TO_1_19]]; component [[COMPONENT-CILIUM]]; advertisement labels
  [[TROUBLE-CILIUM_BGP_ADVERTISEMENT_LABELS]].
