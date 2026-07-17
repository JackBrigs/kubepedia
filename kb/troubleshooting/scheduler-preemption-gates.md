---
id: TROUBLE-SCHEDULER_PREEMPTION_GATES
type: troubleshooting
title: "kube-scheduler: preemption not happening / SchedulingGated forever"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - no preemption victims found
  - preemption is not helpful for scheduling
  - preemptionPolicy Never
  - pod stuck schedulinggated
  - pod scheduling readiness gate
tags:
  - troubleshooting
  - scheduler
  - preemption
  - scheduling
sources:
  - type: docs
    path: Pod priority and preemption
    url: https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/
    note: "preemption verdicts, preemptionPolicy, PDB best-effort"
  - type: docs
    path: Pod scheduling readiness
    url: https://kubernetes.io/docs/concepts/scheduling-eviction/pod-scheduling-readiness/
    note: "schedulingGates (GA 1.30)"
relations:
  - type: see_also
    target: TROUBLE-SCHEDULER_POD_PENDING
  - type: see_also
    target: CONCEPT-TROUBLESHOOTING_MAP
---

# kube-scheduler: preemption not happening / SchedulingGated forever

## Summary

Two adjacent "pod won't schedule" classes: **preemption** that doesn't evict lower-priority
pods, and pods held by **scheduling gates** (`PodSchedulingReadiness`).

## Problem

- High-priority pod Pending; `preemption: ... No preemption victims found` /
  `Preemption is not helpful for scheduling`.
- A high-priority pod jumps the queue but **never evicts** running pods.
- `kubectl get pod` STATUS `SchedulingGated`, never progresses.

## Context

- Applies to Kubernetes **1.29–1.35**. Pod Scheduling Readiness is GA in **1.30** (beta 1.27).
  Companion: [[TROUBLE-SCHEDULER_POD_PENDING]].

## Diagnostics

**Preemption:**

- **`No preemption victims found`:** no lower-priority pods whose removal makes a node fit
  (victims are equal/higher priority, or removal still wouldn't fit). Confirm the pod's
  `priorityClassName` actually outranks candidates, and that lower-priority pods run on feasible
  nodes.
- **`Preemption is not helpful for scheduling`:** constraints (taints/required affinity) mean no
  node ever fits — removing pods won't help; loosen affinity or add capacity.
- **`preemptionPolicy: Never`:** the PriorityClass jumps the queue by priority but **never
  evicts** — high-priority batch then sits behind lower-priority services. Remove it (default is
  `PreemptLowerPriority`) if eviction is intended.
- **PDBs are best-effort during preemption:** the scheduler prefers victims that don't violate a
  PDB but **preempts anyway** if none exist — don't rely on PDB as a hard block; use priority
  design to protect critical pods.

**Scheduling gates:**

- `SchedulingGated` means `.spec.schedulingGates` is non-empty — scheduling is blocked until a
  **controller removes every gate**. Inspect: `kubectl get pod <p> -o
  jsonpath='{.spec.schedulingGates}'`; metric `scheduler_pending_pods{queue="gated"}`.
- If the gate-owning controller is down/buggy the pod hangs forever (e.g. a Kueue unsuspend that
  hit 1.30's stricter pod-mutation validation — kueue#2029). Ensure the controller runs; gates
  can only be **removed** after creation (last resort: patch the gate out).

## Known Issues

- A gate-owning controller that upgrades independently (e.g. Kueue vs Kubernetes 1.30) can start
  failing to remove gates after a cluster upgrade — a stuck `SchedulingGated` fleet often means
  that controller broke, not the scheduler.
- `preemptionPolicy: Never` + high priority is a subtle starvation trap for batch workloads.

## References

- Pod priority/preemption + scheduling-readiness docs (above); Red Hat solution 7055911;
  kueue#2029. Pending triage: [[TROUBLE-SCHEDULER_POD_PENDING]].
