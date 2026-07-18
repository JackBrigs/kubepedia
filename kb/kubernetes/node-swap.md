---
id: CONCEPT-K8S_NODE_SWAP
type: concept
title: "Node swap support — Burstable pods can use swap on cgroup v2 (GA 1.34)"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.30 <=1.35"
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - kubernetes swap support
  - NodeSwap
  - memorySwap swapBehavior
  - kubelet swap LimitedSwap
  - swap on kubernetes nodes
tags:
  - kubernetes
  - kubelet
  - node
sources:
  - type: code
    path: keps/sig-node/2400-node-swap
    url: https://github.com/kubernetes/enhancements/tree/master/keps/sig-node/2400-node-swap
    note: "kep.yaml: alpha 1.22, beta 1.30, stable 1.34"
relations:
  - type: see_also
    target: PRACTICE-CGROUPS
  - type: see_also
    target: CONCEPT-K8S_UPGRADE_SILENT_CHANGES
  - type: see_also
    target: PRACTICE-KERNEL_REQUIREMENTS
---

# Node swap support — Burstable pods can use swap on cgroup v2 (GA 1.34)

## Summary

Kubernetes can now let workloads use **swap**: `NodeSwap` reached **beta in 1.30** and **GA in 1.34**.
On **cgroup v2** nodes, **Burstable** QoS pods may use swap per the kubelet `memorySwap.swapBehavior`
setting (`LimitedSwap`). This reverses the long-standing "swap must be off" rule for those cases and
changes memory-pressure/eviction behavior — an operator decision, not an automatic one, but the
capability is on by default at the node level from 1.34.

## Context

- Milestone (`keps/sig-node/2400-...` kep.yaml): alpha **1.22**, beta **1.30**, stable **1.34**.
- **Requirements/scope:** **cgroup v2** only ([[PRACTICE-CGROUPS]]); swap usable by **Burstable** pods
  (not Guaranteed, not BestEffort by default); controlled by kubelet `memorySwap.swapBehavior:
  LimitedSwap`. Guaranteed pods and system-critical pods still don't swap.
- **Kubespray note:** Kubespray has historically **disabled swap** in preflight (the classic kubeadm
  requirement). Using node swap means deliberately provisioning swap **and** relaxing that — it is not
  a default Kubespray configuration; treat it as an opt-in node-level change, kernel/cgroup-v2 gated
  ([[PRACTICE-KERNEL_REQUIREMENTS]]).
- **Impact:** changes memory-pressure eviction dynamics; monitor swap usage, and understand that swap
  can mask memory limits and degrade latency.

## References

- `keps/sig-node/2400-node-swap` (kep.yaml GA 1.34). cgroups [[PRACTICE-CGROUPS]]; kernel
  [[PRACTICE-KERNEL_REQUIREMENTS]]; silent changes [[CONCEPT-K8S_UPGRADE_SILENT_CHANGES]].
