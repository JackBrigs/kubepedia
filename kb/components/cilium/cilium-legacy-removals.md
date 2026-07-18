---
id: CONCEPT-CILIUM_LEGACY_REMOVALS
type: concept
title: "Cilium legacy integrations removed across 1.16–1.18 (Consul, managed etcd, External Workloads, metallb-bgp)"
status: active
kubespray_version: ">=v2.28.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: ">=1.17.3 <=1.19.3"
verified_at: "2026-07-18"
confidence: confirmed
aliases:
  - cilium consul removed
  - cilium managed etcd removed
  - cilium external workloads removed
  - cilium metallb-bgp removed
  - cilium legacy flags removed
tags:
  - cilium
  - upgrade
  - deprecations
sources:
  - type: docs
    path: Documentation/operations/upgrade.rst
    url: https://github.com/cilium/cilium/blob/v1.18.2/Documentation/operations/upgrade.rst
    note: "1.17 removes Consul, managed etcd-in-pod-network, metallb-bgp; 1.18 removes External Workloads"
relations:
  - type: see_also
    target: UPGRADE-CILIUM_1_15_TO_1_19
  - type: see_also
    target: COMPONENT-CILIUM
  - type: see_also
    target: COMPONENT-ETCD
---

# Cilium legacy integrations removed across 1.16–1.18 (Consul, managed etcd, External Workloads, metallb-bgp)

## Summary

Across the Kubespray range Cilium **removed several legacy integrations**. If your setup depended on
any of them, it breaks at the version shown: **Consul** kvstore, Cilium-**managed etcd in the pod
network**, and **metallb-bgp** removed in **1.17** (Kubespray v2.28.0); **External Workloads** removed
in **1.18** (Kubespray v2.29.0). These are one-way removals — migrate off before the corresponding
upgrade.

## Context

Removed integrations and their replacements (`upgrade.rst`@v1.17.3 / @v1.18.2 —
[[UPGRADE-CILIUM_1_15_TO_1_19]]):

- **Consul kvstore (removed 1.17):** Cilium no longer supports Consul as its kvstore. Use the default
  (CRD-backed) identity storage or etcd. Rare in Kubespray (Kubespray never wired Consul), but a
  hand-customized cluster might.
- **Managed etcd in pod network (removed 1.17):** Cilium's option to run its **own** etcd inside the
  cluster network is gone. Use CRD mode (default) or an external/dedicated etcd — Kubespray runs etcd
  as a host/control-plane component anyway ([[COMPONENT-ETCD]]), so standard clusters are unaffected.
- **metallb-bgp (removed 1.17):** the old MetalLB-style BGP announcement built into Cilium is gone;
  the Helm `bgp.*` keys and the `bgp-announce-*` flags were removed. Use the **Cilium BGP control
  plane** (v2 CRDs) — see [[TROUBLE-CILIUM_BGP_V1_REMOVED]] for the subsequent BGPv1→v2 change.
- **External Workloads (removed 1.18):** the feature for joining non-Kubernetes VMs into the mesh is
  removed; on upgrade `kubectl delete crd ciliumexternalworkloads.cilium.io`. Standard node-only
  clusters are unaffected.

**Also gone in the range (flags/Helm):** `enable-remote-node-identity`, `endpoint-status`,
`sidecar-istio-proxy-image` (1.16); `--datapath-mode=lb-only`, ipcache high-scale mode (1.17/1.18).
Most Kubespray clusters use none of these; the risk is a **hand-customized** inventory carrying a
removed flag into `cilium-agent`, which then fails to start.

## References

- Cilium `Documentation/operations/upgrade.rst`@v1.17.3 / @v1.18.2. Full jump
  [[UPGRADE-CILIUM_1_15_TO_1_19]]; component [[COMPONENT-CILIUM]]; etcd [[COMPONENT-ETCD]]; BGP change
  [[TROUBLE-CILIUM_BGP_V1_REMOVED]].
