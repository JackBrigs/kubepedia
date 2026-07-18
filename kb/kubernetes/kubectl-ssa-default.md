---
id: CONCEPT-K8S_KUBECTL_SSA_DEFAULT
type: concept
title: "kubectl apply uses server-side apply by default (GA 1.32)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.32 <=1.35"
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - kubectl server-side apply default
  - kubectl apply SSA
  - field manager conflict kubectl
  - kubectl apply managedFields
tags:
  - kubernetes
  - kubectl
  - apiserver
sources:
  - type: code
    path: keps/sig-cli/3805-ssa-default
    url: https://github.com/kubernetes/enhancements/tree/master/keps/sig-cli/3805-ssa-default
    note: "kep.yaml: alpha 1.27, beta 1.30, stable 1.32 — kubectl apply defaults to server-side apply"
relations:
  - type: see_also
    target: CONCEPT-K8S_UPGRADE_SILENT_CHANGES
  - type: see_also
    target: CONCEPT-K8S_ADMISSION_POLICIES
---

# kubectl apply uses server-side apply by default (GA 1.32)

## Summary

`kubectl apply` now uses **server-side apply (SSA)** by default (GA in **1.32**), instead of the old
client-side three-way merge. Ownership of fields is tracked server-side via **`managedFields`** and a
**field manager**. For most users this is transparent, but scripts and controllers that share objects
can hit **field-manager conflicts** or behave differently around field ownership and pruning.

## Context

- Milestone (`keps/sig-cli/3805-ssa-default` kep.yaml): alpha **1.27**, beta **1.30**, stable **1.32**
  (Kubespray v2.29.0+).
- **What changes:** SSA computes the diff **on the apiserver** using `managedFields`; two actors editing
  the **same field** get a **conflict** (resolvable with `--force-conflicts`). Client-side apply's
  `kubectl.kubernetes.io/last-applied-configuration` annotation is no longer the source of truth.
- **Operator impact:** (1) automation that both `kubectl apply` **and** patch the same fields (or that
  two controllers co-own) may see conflicts — set an explicit `--field-manager` and use
  `--force-conflicts` deliberately; (2) removal semantics differ (SSA prunes fields the manager owned
  and dropped); (3) GitOps tools already use SSA — this aligns `kubectl` with them. Pairs with CEL
  admission policies for server-side governance ([[CONCEPT-K8S_ADMISSION_POLICIES]]).

## References

- `keps/sig-cli/3805-ssa-default` (kep.yaml GA 1.32). Silent changes [[CONCEPT-K8S_UPGRADE_SILENT_CHANGES]];
  admission policies [[CONCEPT-K8S_ADMISSION_POLICIES]].
