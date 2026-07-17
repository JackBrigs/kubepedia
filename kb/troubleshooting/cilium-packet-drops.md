---
id: TROUBLE-CILIUM_PACKET_DROPS
type: troubleshooting
title: "Cilium: packet drops (identity, CT map full, policy)"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: ">=1.18.0 <=1.19.6"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - cilium monitor drop
  - CT Map insertion failed
  - cilium conntrack table full
  - cilium identity not propagated
  - bpf-ct-global-max
tags:
  - troubleshooting
  - cilium
  - networking
  - cni
sources:
  - type: docs
    path: Cilium monitor / drops
    url: https://docs.cilium.io/en/stable/operations/troubleshooting/
    note: "cilium-dbg monitor --type drop; CT map"
relations:
  - type: see_also
    target: TROUBLE-CILIUM_POD_CONNECTIVITY
  - type: see_also
    target: COMPONENT-CILIUM
---

# Cilium: packet drops (identity, CT map full, policy)

## Summary

Intermittent connection failures/latency with Cilium, but pods are "up". Use
**`cilium-dbg monitor --type drop`** to see the drop **reason** — the common ones are a
**policy** deny, an **identity** not yet propagated, or the **conntrack (CT) BPF map full**.

## Problem

- Intermittent drops/timeouts; `cilium-dbg monitor --type drop` shows `Policy denied`,
  `Stale or unroutable IP`, or `CT: Map insertion failed`.
- Distinct from a total connectivity break ([[TROUBLE-CILIUM_POD_CONNECTIVITY]]).

## Context

- Applies to Cilium **1.18–1.19.6** ([[COMPONENT-CILIUM]]).

## Diagnostics

- **See the drops:** in the agent pod, `cilium-dbg monitor --type drop` (and `cilium-dbg
  status`) — the reason string points at the layer.
- **`Policy denied`:** a CiliumNetworkPolicy/default-deny is dropping it — review policies and
  Hubble flows; a too-broad default-deny is a frequent cause.
- **Identity not propagated:** `cilium-dbg endpoint list` shows endpoints stuck
  `waiting-for-identity`, or drops reference an unknown identity — the operator/kvstore
  (or kube-apiserver) is slow/unreachable; check `cilium-dbg status` (KVStore, kube-apiserver).
- **`CT: Map insertion failed` / conntrack full:** the CT BPF map is exhausted (high connection
  churn) → raise **`bpf-ct-global-tcp-max` / `bpf-ct-global-any-max`** (Helm
  `bpf.ctTcpMax`/`ctAnyMax`), which reallocates the BPF maps (agent restart).
- **MTU/underlay** drops on large packets are a separate class (set the CNI MTU —
  [[CONFIG-CNI_MTU]]).

## Known Issues

- Bumping BPF map sizes increases memory per node — size to the real connection count, don't
  over-allocate.

## References

- Cilium troubleshooting/monitor docs (above); broad connectivity:
  [[TROUBLE-CILIUM_POD_CONNECTIVITY]]; MTU: [[CONFIG-CNI_MTU]]; component: [[COMPONENT-CILIUM]].
