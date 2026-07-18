---
id: CONCEPT-K8S_DRA
type: concept
title: "Dynamic Resource Allocation (DRA) structured parameters — GPU/device API (GA 1.34)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.32 <=1.35"
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - DynamicResourceAllocation
  - DRA structured parameters
  - ResourceClaim ResourceSlice DeviceClass
  - gpu allocation kubernetes DRA
  - dra driver kubelet plugin
tags:
  - kubernetes
  - scheduling
  - node
  - devices
sources:
  - type: code
    path: keps/sig-node/4381-dra-structured-parameters
    url: https://github.com/kubernetes/enhancements/tree/master/keps/sig-node/4381-dra-structured-parameters
    note: "kep.yaml: alpha 1.30, beta/on-by-default 1.32, stable 1.34; classic-DRA KEP 3063 withdrawn"
relations:
  - type: see_also
    target: CONCEPT-K8S_UPGRADE_SILENT_CHANGES
  - type: see_also
    target: CONCEPT-K8S_FEATURE_GATES
---

# Dynamic Resource Allocation (DRA) structured parameters — GPU/device API (GA 1.34)

## Summary

**DRA** is the modern way to request and share **specialized devices** (GPUs, accelerators, NICs) —
replacing the limited device-plugin `resources` model with structured API objects and scheduler
awareness. The **structured-parameters** flavor (`DynamicResourceAllocation`) reached **beta/on-by-
default in 1.32** and **GA in 1.34** (Kubespray v2.29.0+). It is a **major new subsystem**: enabling it
requires **DRA driver(s)** and a **kubelet plugin**; without a driver it does nothing, but the API and
scheduler integration are present.

## Context

- Milestone (`keps/sig-node/4381-...` kep.yaml): alpha **1.30**, beta/on **1.32**, stable **1.34**. The
  original control-plane-controller DRA (`keps/sig-node/3063-...`, gate `DRAControlPlaneController`) was
  **withdrawn** — use structured parameters, not the old gate.
- **API objects:** `DeviceClass`, `ResourceClaim` / `ResourceClaimTemplate`, `ResourceSlice`; pods
  reference claims in `spec.resourceClaims`. The scheduler allocates devices from `ResourceSlice`s a
  driver publishes.
- **Ecosystem extensions in range:** admin access (`DRAAdminAccess` beta 1.34), prioritized list
  (beta 1.34), partitionable devices / device taints (alpha 1.33), PodResources API for DRA (beta 1.34).
- **Operator impact:** on by default from 1.32 but **inert without a DRA driver** (e.g. NVIDIA DRA
  driver). If you run GPUs, DRA is the path forward from device plugins; verify the exact gate/driver
  compatibility per release ([[CONCEPT-K8S_FEATURE_GATES]]). Kubespray does not install DRA drivers.

## References

- `keps/sig-node/4381-dra-structured-parameters` (kep.yaml GA 1.34). Silent changes
  [[CONCEPT-K8S_UPGRADE_SILENT_CHANGES]]; gates [[CONCEPT-K8S_FEATURE_GATES]].
