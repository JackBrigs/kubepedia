---
id: TROUBLE-ROLLOUT_STUCK
type: troubleshooting
title: "Deployment rollout stuck / not progressing"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - rollout stuck
  - deployment not progressing
  - ProgressDeadlineExceeded
  - kubectl rollout status hangs
  - update stuck old pods
  - pdb blocks rollout
tags:
  - troubleshooting
  - deployment
  - rollout
  - workloads
sources:
  - type: docs
    path: Kubernetes Deployments (rollout / progress)
    url: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
    note: "rollout stalls when new pods aren't Ready or old pods can't be removed within maxUnavailable/PDB"
relations:
  - type: see_also
    target: TROUBLE-CRASHLOOPBACKOFF
  - type: see_also
    target: TROUBLE-POD_PENDING_UNSCHEDULABLE
  - type: see_also
    target: CONCEPT-TROUBLESHOOTING_MAP
---

# Deployment rollout stuck / not progressing

## Summary

`kubectl rollout status` hangs or reports `ProgressDeadlineExceeded` when the new
ReplicaSet's pods **don't become Ready**, or the update rules won't let old pods go. The
Deployment itself is rarely the bug — the **new pods are failing** (crash/image/pending),
or **maxUnavailable/PDB** creates a deadlock. Find why the new pods aren't Ready.

## Problem

`kubectl rollout status deploy/<name>` never completes; `kubectl get deploy` shows
`UP-TO-DATE`/`AVAILABLE` stuck below desired; `describe deploy` shows
`ProgressDeadlineExceeded` or `ReplicaSetUpdated` not advancing.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0` (Kubernetes-native rollout behaviour).
- A `RollingUpdate` brings up new pods (up to `maxSurge`) and removes old ones (down to
  `maxUnavailable`) **only as new pods become Ready**. If new pods never go Ready, the
  rollout can't proceed; `progressDeadlineSeconds` (default 600s) then marks it failed.

## Diagnostics

- **The new ReplicaSet's pods:** `kubectl get rs -l app=<x>` (newest has the new revision),
  then `kubectl get pods` for that RS — are they `Ready`? Usually **no**, and *that* pod
  state is the real problem.
- **Why aren't they Ready?** `kubectl describe pod <new-pod>` → route by state:
  `CrashLoopBackOff` ([[TROUBLE-CRASHLOOPBACKOFF]]), `ImagePullBackOff`
  ([[TROUBLE-IMAGEPULLBACKOFF]]), `Pending` ([[TROUBLE-POD_PENDING_UNSCHEDULABLE]]),
  `ContainerCreating` ([[TROUBLE-POD_CONTAINERCREATING]]), or a failing **readiness probe**.
- **Deployment conditions:** `kubectl describe deploy <name>` — `Progressing`/`Available`
  conditions and the reason.
- **PDB:** `kubectl get pdb -A` — a PodDisruptionBudget that won't allow eviction stalls
  the removal of old pods.

## Known Issues

Fix the **cause the new pods expose**, then the rollout finishes on its own:

- **New pods failing** — the update shipped a bad image/config/probe; the new RS pods
  crash/can't pull/can't schedule. Fix the root (linked hubs above) or
  `kubectl rollout undo deploy/<name>` to revert while you investigate.
- **Readiness probe never passes** — pods run but never Ready (wrong path/port, too-short
  `initialDelaySeconds`); the rollout waits forever. Fix the probe.
- **`maxUnavailable: 0` + no room** — with `maxUnavailable: 0` and `maxSurge: 0`, or a
  cluster with no capacity for the surge pod, the rollout can't place a new pod without
  removing an old one — deadlock. Allow surge or free capacity
  ([[TROUBLE-POD_PENDING_UNSCHEDULABLE]]).
- **PDB too strict** — a PDB requiring more available replicas than the rollout can keep
  blocks old-pod eviction; relax `minAvailable`/`maxUnavailable` on the PDB.

**Gotchas:**

- `ProgressDeadlineExceeded` **fails** the rollout but doesn't roll back — old pods keep
  serving; you must fix-forward or `rollout undo`.
- A **StatefulSet** rollout is stricter (ordered, one at a time) — one stuck pod blocks all
  subsequent ordinals; the pod-level cause is the same triage.
- "Stuck" can also be **paused**: `kubectl rollout resume deploy/<name>` if someone paused
  it.

## References

- Kubernetes Deployment rollout. Pod-state hubs: [[TROUBLE-CRASHLOOPBACKOFF]],
  [[TROUBLE-POD_PENDING_UNSCHEDULABLE]], [[TROUBLE-IMAGEPULLBACKOFF]]; map:
  [[CONCEPT-TROUBLESHOOTING_MAP]].
