---
id: TROUBLE-KUBELET_PLEG_NOT_HEALTHY
type: troubleshooting
title: "kubelet: PLEG is not healthy → node flaps NotReady / mount timeouts"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - PLEG is not healthy
  - pleg was last seen active
  - node flaps notready pleg
  - unable to attach or mount volumes timed out
  - evented pleg panic
tags:
  - troubleshooting
  - kubelet
  - nodes
  - runtime
sources:
  - type: docs
    path: kubelet PLEG relist issue
    url: https://github.com/kubernetes/kubernetes/issues/61117
    note: "PLEGRelistThreshold 3m; serial CRI calls"
  - type: docs
    path: volume mount timeout coupled to PLEG
    url: https://github.com/kubernetes/kubernetes/issues/114167
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
  - type: see_also
    target: TROUBLE-KUBELET_MEMORY_OOM
---

# kubelet: PLEG is not healthy → node flaps NotReady / mount timeouts

## Summary

A node oscillates `Ready`/`NotReady` with `PLEG is not healthy: pleg was last seen active …
ago; threshold is 3m0s`. The **PLEG relist** couldn't finish a full CRI state resync within the
hardcoded 3-minute threshold — almost always a **slow/overloaded runtime** or **high pod
density/churn**. Volume-mount timeouts are a common side-effect.

## Problem

- `PLEG is not healthy: pleg was last seen active 3m5s ago; threshold is 3m0s` (delta grows);
  node flaps NotReady.
- Pods stuck `ContainerCreating` 5–6 min: `Unable to attach or mount volumes ...: timed out
  waiting for the condition`, then `MountVolume.SetUp succeeded` minutes later.

## Context

- Applies to Kubernetes **1.29–1.35** on containerd ([[COMPONENT-CONTAINERD]]). A **1.33.7 vs
  1.32.5 regression** stretched PLEG-unhealthy recovery (~900 pods, 3-node reboot) from ~30 min
  to ~90 min with no CPU/mem/IO pressure (issue #137798).

## Diagnostics

- **Root cause:** generic PLEG `relist()` must complete a full CRI resync within the 3-minute
  `PLEGRelistThreshold`; it calls CRI **serially per pod**, so a slow runtime, heavy disk I/O,
  or high pod density/churn exceeds 3m and kubelet stops syncing (issue #61117).
- **Check runtime responsiveness:** `crictl ps` / `crictl stats` latency, disk I/O; a wedged
  relist clears after **restarting the runtime, then kubelet**.
- **Reduce pressure:** lower pod density/churn per node; a node near its pod cap under churn is
  the classic trigger.
- **Volume-mount timeout is a PLEG symptom:** the volume manager waits on the pod cache
  populated by relist; under churn relist misses 3 min while the ~2-min mount timeout fires — a
  race with nothing wrong in storage (issue #114167). (The same error string can also mean a
  genuine CSI/attach failure — check CSI logs to distinguish.)
- **Evented PLEG panic:** with the `EventedPLEG` gate on, resource-constrained nodes hit a
  `panic: send on closed channel` (issue #132266) — keep `EventedPLEG` **disabled** (it's
  alpha/off by default) and rely on generic PLEG.

## Known Issues

- No merged fix for the 1.33.7 recovery regression — reduce density/churn and speed up the
  runtime as mitigation.

## References

- kubelet issues #61117 / #137798 / #114167 / #132266 (above); runtime: [[COMPONENT-CONTAINERD]].
