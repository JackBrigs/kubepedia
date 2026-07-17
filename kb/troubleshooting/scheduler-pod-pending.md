---
id: TROUBLE-SCHEDULER_POD_PENDING
type: troubleshooting
title: "kube-scheduler: pod Pending / FailedScheduling (taints, resources, volume, GPU)"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - pod pending failedscheduling
  - 0 nodes are available insufficient cpu
  - untolerated taint
  - volume node affinity conflict
  - insufficient nvidia.com/gpu
  - schedulerName pod never scheduled
tags:
  - troubleshooting
  - scheduler
  - scheduling
  - control-plane
sources:
  - type: docs
    path: Taints and tolerations / pod-priority
    url: https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/
    note: "FailedScheduling message anatomy"
  - type: docs
    path: StorageClass volumeBindingMode
    url: https://kubernetes.io/docs/concepts/storage/storage-classes/#volume-binding-mode
    note: "WaitForFirstConsumer vs Immediate (volume node affinity conflict)"
relations:
  - type: see_also
    target: CONCEPT-TROUBLESHOOTING_MAP
  - type: see_also
    target: TROUBLE-SCHEDULER_TOPOLOGY_SPREAD
  - type: see_also
    target: TROUBLE-SCHEDULER_PREEMPTION_GATES
---

# kube-scheduler: pod Pending / FailedScheduling (taints, resources, volume, GPU)

## Summary

A pod stays `Pending`. `kubectl describe pod` → the `FailedScheduling` event **explains
exactly why** — read the whole message: `0/N nodes are available: <reasons>. preemption:
<preemption verdict>`. The common reasons are insufficient resources, untolerated taints, a
volume zone conflict, missing device resources, or an unmatched `schedulerName`.

## Problem

- `kubectl get pod` → `Pending`; `describe` shows `FailedScheduling`, e.g.
  `0/5 nodes are available: 3 Insufficient cpu, 2 node(s) had untolerated taint {...}`.
- Or `... node(s) had volume node affinity conflict`.
- Or `Insufficient nvidia.com/gpu` despite GPU nodes.
- Or the pod is `Pending` with **no `FailedScheduling` event at all**.

## Context

- Applies to Kubernetes **1.29–1.35** (message formats stable). Topology-spread and
  preemption/gates are separate docs ([[TROUBLE-SCHEDULER_TOPOLOGY_SPREAD]],
  [[TROUBLE-SCHEDULER_PREEMPTION_GATES]]).

## Diagnostics

- **Insufficient cpu/memory:** scheduling uses **requests**, not usage. Check
  `kubectl describe node <n>` → "Allocated resources"; lower requests, add/autoscale nodes.
- **Untolerated taint:** control-plane nodes carry
  `node-role.kubernetes.io/control-plane:NoSchedule` by default; add matching `tolerations` or
  target other nodes. `describe node` → `Taints`.
- **`volume node affinity conflict`:** a PV is pinned to one zone (e.g. single-AZ disk) but the
  pod is being placed elsewhere. Use **`volumeBindingMode: WaitForFirstConsumer`** so the
  volume is provisioned in a schedulable zone, or constrain the pod to the PV's zone
  (`topology.kubernetes.io/zone`).
- **`Insufficient nvidia.com/gpu`:** the node advertises **0 allocatable** GPUs — the
  device-plugin chain (NFD → driver → toolkit → device-plugin) is broken or the containerd
  `nvidia` runtime is misconfigured; with MIG the resource is `nvidia.com/mig-*`; integer GPUs
  aren't oversubscribable. Check node `Allocatable` and device-plugin/kubelet logs.
- **Pending with no event / unmatched `schedulerName`:** `spec.schedulerName` names a scheduler
  that isn't running — the default scheduler ignores such pods entirely. Check `schedulerName`;
  run that scheduler or unset to `default-scheduler`.

## Known Issues

- The `preemption:` tail of the message matters: `No preemption victims found` / `Preemption is
  not helpful for scheduling` explain why eviction won't rescue the pod
  ([[TROUBLE-SCHEDULER_PREEMPTION_GATES]]).

## References

- Taint/toleration + volumeBindingMode docs (above); GPU: NVIDIA k8s-device-plugin issues
  #348/#71; multi-scheduler: kubernetes.io configure-multiple-schedulers. Siblings:
  [[TROUBLE-SCHEDULER_TOPOLOGY_SPREAD]], [[TROUBLE-SCHEDULER_PREEMPTION_GATES]].
