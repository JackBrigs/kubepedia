---
id: TROUBLE-POD_PENDING_UNSCHEDULABLE
type: troubleshooting
title: "Pod Pending / Unschedulable (scheduler can't place it)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - pod pending
  - unschedulable
  - FailedScheduling
  - insufficient cpu memory
  - node had taints that the pod did not tolerate
  - no nodes available
tags:
  - troubleshooting
  - scheduling
  - pods
  - resources
sources:
  - type: docs
    path: Kubernetes scheduling / assigning pods to nodes
    url: https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/
    note: "scheduler filters: resources, taints/tolerations, affinity, topology"
relations:
  - type: see_also
    target: TROUBLE-POD_CONTAINERCREATING
  - type: see_also
    target: CONFIG-NODE_LABELS_TAINTS
  - type: see_also
    target: TROUBLE-PVC_PENDING_NO_STORAGECLASS
---

# Pod Pending / Unschedulable (scheduler can't place it)

## Summary

A Pod is `Pending` with reason `Unschedulable`/`FailedScheduling` when the scheduler finds
**no node** that satisfies its constraints — usually insufficient CPU/memory, an
untolerated **taint**, a **node selector / affinity** that matches nothing, or an unbound
**volume**. This is *before* the kubelet runs it (distinct from `ContainerCreating`, which
is *after* scheduling — [[TROUBLE-POD_CONTAINERCREATING]]).

## Problem

`kubectl get pod` shows `Pending`; `kubectl describe pod` Events show
`0/N nodes are available: …` with per-node reasons (e.g. `Insufficient cpu`,
`node(s) had untolerated taint`, `node(s) didn't match Pod's node affinity/selector`).

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`.
- The scheduler **filters** nodes by: resource **requests** (not limits) vs Allocatable,
  **taints** vs the Pod's tolerations ([[CONFIG-NODE_LABELS_TAINTS]]), `nodeSelector` /
  node **affinity**, **topology spread**, and volume/zone constraints.
- The `describe` message aggregates why *each* node was rejected — read it literally.

## Diagnostics

- **`kubectl describe pod <name>`** — the `FailedScheduling` event lists node counts and
  reasons (`Insufficient cpu/memory`, `untolerated taint`, `didn't match affinity`,
  `had volume node affinity conflict`).
- Capacity: `kubectl describe node <node>` → Allocatable and `Allocated resources` (sum of
  requests) — is there room?
- Taints: `kubectl get nodes -o json | jq '.items[].spec.taints'` — does the Pod tolerate
  them?
- Selectors: compare the Pod's `nodeSelector`/affinity to actual node labels
  (`kubectl get nodes --show-labels`).

## Known Issues

Match the `describe` reason to its fix:

- **`Insufficient cpu` / `memory`** — the Pod's **requests** exceed free Allocatable on
  every node. Lower requests, add/enlarge nodes, or free capacity. Remember Allocatable is
  Capacity minus `kube_reserved`/`system_reserved` ([[PRACTICE-CGROUPS]]).
- **`untolerated taint`** — add the matching toleration to the Pod, or remove/adjust the
  taint ([[CONFIG-NODE_LABELS_TAINTS]]). Control-plane nodes are tainted by default — apps
  need a toleration to land there.
- **`didn't match node affinity/selector`** — the `nodeSelector`/affinity references labels
  no node has; fix the selector or label the nodes.
- **`volume node affinity conflict` / unbound PVC** — the volume is tied to a zone/node the
  Pod can't use, or no volume exists ([[TROUBLE-PVC_PENDING_NO_STORAGECLASS]]).
- **Topology spread / anti-affinity too strict** — relax `maxSkew`/`whenUnsatisfiable` or
  the anti-affinity rule.

**Gotchas:**

- `Pending` **Unschedulable** ≠ `Pending` **ContainerCreating**: the former is the
  scheduler (no node), the latter is the kubelet (node chosen, setup failing) —
  [[TROUBLE-POD_CONTAINERCREATING]].
- Scheduling uses **requests**, not limits — a Pod with no requests always "fits" but can
  then starve/OOM at runtime ([[TROUBLE-OOMKILLED]]).
- A brand-new node that's `NotReady`/cordoned isn't schedulable — check node readiness too.

## References

- Kubernetes scheduling reference. Related: [[TROUBLE-POD_CONTAINERCREATING]],
  [[CONFIG-NODE_LABELS_TAINTS]], [[TROUBLE-PVC_PENDING_NO_STORAGECLASS]], [[TROUBLE-OOMKILLED]].
