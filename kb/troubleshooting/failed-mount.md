---
id: TROUBLE-FAILEDMOUNT
type: troubleshooting
title: "Pod can't mount volume (FailedMount — ConfigMap/Secret/PVC)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - FailedMount
  - MountVolume.SetUp failed
  - configmap not found volume
  - secret not found
  - unable to attach or mount volumes
  - failed to mount volume
  - volume node affinity conflict
tags:
  - troubleshooting
  - storage
  - volumes
  - pods
sources:
  - type: docs
    path: Kubernetes configure pod storage / debug
    url: https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/
    note: "FailedMount events name the missing/blocked volume source"
relations:
  - type: see_also
    target: TROUBLE-PVC_PENDING_NO_STORAGECLASS
  - type: see_also
    target: CONCEPT-CSI_LAYER
  - type: see_also
    target: TROUBLE-POD_CONTAINERCREATING
---

# Pod can't mount volume (FailedMount — ConfigMap/Secret/PVC)

## Summary

`FailedMount` / `MountVolume.SetUp failed` keeps a pod in `ContainerCreating` because the
kubelet can't set up one of its volumes. The event names the volume and the reason — most
often a **referenced ConfigMap/Secret that doesn't exist** (or is in the wrong namespace),
or a **PVC/CSI volume that can't attach or bind**.

## Problem

Pod is stuck `ContainerCreating`; `kubectl describe pod` shows `FailedMount` /
`Unable to attach or mount volumes` / `MountVolume.SetUp failed for volume …` with a
specific reason.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`.
- A volume source must exist **in the pod's own namespace** (ConfigMaps/Secrets are
  namespaced); PVC-backed volumes additionally need a bound PV and a working CSI
  attach/mount.

## Diagnostics

- **`kubectl describe pod <pod>`** — the `FailedMount` event states the volume name and
  cause (`not found`, `timed out waiting for the condition`, `volume node affinity
  conflict`, attach errors).
- **ConfigMap/Secret:** `kubectl -n <ns> get configmap,secret` — does the referenced name
  exist **in this namespace**? Check for typos and namespace mismatch.
- **PVC:** `kubectl -n <ns> get pvc` — is it `Bound`? If `Pending`, that's the root cause
  ([[TROUBLE-PVC_PENDING_NO_STORAGECLASS]]).
- **CSI:** `kubectl -n <driver-ns> get pods` — is the CSI driver (controller + node) running
  on the pod's node? ([[CONCEPT-CSI_LAYER]]).

## Known Issues

Map the reason to its fix:

- **`configmap/secret "X" not found`** — create it, fix the name, or move the pod/object to
  the same namespace. A pod referencing a not-yet-created ConfigMap waits indefinitely.
- **Missing key / subPath** — the ConfigMap/Secret exists but lacks the `key` the volume
  mounts (`items`/`subPath`); add the key.
- **PVC not bound** — no provisioner/StorageClass or the pool is exhausted
  ([[TROUBLE-PVC_PENDING_NO_STORAGECLASS]]).
- **`volume node affinity conflict`** — the PV is pinned to a zone/node the pod can't be
  scheduled to (local volumes, topology). Align pod scheduling with the PV's node affinity.
- **Attach/mount timeout** — CSI driver not running on the node, node not registered, or
  the backend (SAN/cloud API) unreachable. Check the CSI node pod and its logs.
- **RWO already attached elsewhere** — a `ReadWriteOnce` PV can't attach to a second node;
  the old pod/node must release it first (common on failover). Ensure the previous
  attachment is gone.
- **Permission / fsGroup / SELinux** — the volume mounts but the app can't write; set an
  appropriate `securityContext.fsGroup`, or check SELinux labels.

**Gotchas:**

- FailedMount holds the pod in `ContainerCreating` — it's a sub-case of that state
  ([[TROUBLE-POD_CONTAINERCREATING]]).
- Projected **serviceAccount token** volumes rarely fail unless RBAC/SA is broken — a
  FailedMount on the default token points at a control-plane/SA issue, not app config.

## References

- Kubernetes debug-running-pod. PVC binding: [[TROUBLE-PVC_PENDING_NO_STORAGECLASS]]; CSI:
  [[CONCEPT-CSI_LAYER]]; parent state: [[TROUBLE-POD_CONTAINERCREATING]].
