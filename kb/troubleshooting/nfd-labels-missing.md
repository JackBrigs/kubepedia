---
id: TROUBLE-NFD_LABELS_MISSING
type: troubleshooting
title: "node-feature-discovery: feature labels not applied"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: ">=0.16.0 <=0.19.0"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - nfd labels missing
  - feature.node.kubernetes.io labels absent
  - nfd worker not labeling
  - gpu nodes not labeled
tags:
  - troubleshooting
  - node-feature-discovery
  - scheduling
  - nodes
sources:
  - type: docs
    path: NFD documentation
    url: https://kubernetes-sigs.github.io/node-feature-discovery/
    note: "nfd-master/worker, feature labels, NodeFeatureRule"
relations:
  - type: see_also
    target: COMPONENT-NODE_FEATURE_DISCOVERY
  - type: see_also
    target: CONCEPT-ADDON_GPU_OPERATOR
---

# node-feature-discovery: feature labels not applied

## Summary

Expected `feature.node.kubernetes.io/*` labels are missing, so workloads that node-select on
them (e.g. GPU, CPU features) won't schedule. Usually the **nfd-worker** isn't running on the
node, the **master↔worker** gRPC link is broken, or a `NodeFeatureRule` doesn't match.

## Problem

- Nodes lack `feature.node.kubernetes.io/...` labels.
- GPU/feature-gated pods stay `Pending` (nodeSelector/affinity unmatched).
- Some nodes labeled, others not.

## Context

- Applies to NFD **0.16–0.19** (base 0.16.4 — [[COMPONENT-NODE_FEATURE_DISCOVERY]]). The GPU
  Operator bundles its own NFD — watch for **two NFD instances** ([[CONCEPT-ADDON_GPU_OPERATOR]]).

## Diagnostics

1. **Worker present?** `nfd-worker` is a DaemonSet — confirm a pod runs on the unlabeled node
   (tolerations/nodeSelector may exclude it). Check its logs for detected features.
2. **Master↔worker:** the worker sends features to `nfd-master` over gRPC (or via
   `NodeFeature` objects in newer versions) — a broken Service/DNS/RBAC stops labeling; check
   `nfd-master` logs.
3. **RBAC:** nfd-master needs permission to patch node labels; a missing ClusterRole binding
   blocks all labeling.
4. **Rules:** custom `NodeFeatureRule`s only add labels when their matchers hit — verify the
   rule and the raw features the worker reports.
5. **Two NFDs:** if the GPU Operator also deploys NFD, running a second cluster-wide NFD can
   conflict — pick one owner.

## Known Issues

- Label prefix/namespace changes across NFD versions can break selectors after an upgrade —
  confirm the label key the current version emits.

## References

- NFD docs (above); component: [[COMPONENT-NODE_FEATURE_DISCOVERY]]; GPU:
  [[CONCEPT-ADDON_GPU_OPERATOR]].
