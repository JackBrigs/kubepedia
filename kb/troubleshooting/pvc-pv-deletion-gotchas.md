---
id: TROUBLE-PVC_PV_DELETION
type: troubleshooting
title: "PVC/PV deletion gotchas — stuck Terminating (finalizers), reclaim-policy data loss / orphaned Released PV"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-19"
confidence: confirmed
aliases:
  - pvc stuck terminating
  - pvc-protection finalizer
  - pv released cannot rebind
  - reclaim policy delete data lost
  - orphaned released pv
  - clear pv claimRef
tags:
  - troubleshooting
  - storage
  - pvc
  - lifecycle
sources:
  - type: external
    path: storage object in-use protection / reclaim policy
    url: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
    note: "kubernetes.io/pvc-protection & pv-protection finalizers; reclaimPolicy Retain leaves Released PV with a stale claimRef"
relations:
  - type: see_also
    target: CONCEPT-CSI_LAYER
  - type: see_also
    target: CONCEPT-K8S_HONOR_PV_RECLAIM_POLICY
  - type: see_also
    target: CONCEPT-K8S_STATEFULSET_PVC_AUTODELETE
  - type: see_also
    target: TROUBLE-NODE_LOCAL_PVC_DRAIN
---

# PVC/PV deletion gotchas — stuck Terminating (finalizers), reclaim-policy data loss / orphaned Released PV

## Summary

Deleting storage is where two classic surprises live. A PVC/PV **won't delete** while in use — the
`kubernetes.io/pvc-protection` / `pv-protection` **finalizers** hold it `Terminating` until the
consumer is gone (people then wrongly force-remove the finalizer and orphan data). And the
**reclaimPolicy** cuts both ways: **`Delete`** destroys the backing volume + data when the PVC is
deleted (surprise "it was reversible, right?"), while **`Retain`** leaves the PV `Released` with a
**stale `claimRef`** so it **can't rebind** to a new PVC — a stuck, orphaned volume.

## Problem

- `kubectl delete pvc/pv` hangs in **`Terminating`** and never completes.
- After deleting a PVC, the **data is gone** (reclaimPolicy `Delete`).
- A `Retain` PV sits in **`Released`** and a new (even identical) PVC **stays `Pending`** — it won't
  bind to the released PV.

## Context

- Applies across **v2.27.0–v2.31.0** and any CSI/storage class ([[CONCEPT-CSI_LAYER]]).
- **Finalizers (stuck Terminating):** `kubernetes.io/pvc-protection` keeps a PVC from deleting **while
  a pod still references it**; `kubernetes.io/pv-protection` keeps a PV while a PVC is bound. The
  object shows `Terminating` until the consumer is removed. Force-removing the finalizer deletes the
  API object but can **leave the backing volume + data orphaned** in the storage backend.
- **reclaimPolicy `Delete` (common default):** deleting the PVC deletes the PV **and the backing
  volume** — data is gone, not recoverable from the cluster ([[CONCEPT-K8S_HONOR_PV_RECLAIM_POLICY]]
  makes this reliable even across delete-ordering).
- **reclaimPolicy `Retain`:** deleting the PVC leaves the PV in **`Released`** carrying the old PVC's
  `claimRef` (uid). Binding logic **won't reuse** a PV with a stale `claimRef` — so a fresh PVC never
  binds to it. You must clear the `claimRef` to make it `Available`.
- StatefulSet PVCs can now auto-delete on scale-down/delete ([[CONCEPT-K8S_STATEFULSET_PVC_AUTODELETE]])
  — another way data disappears if the retention policy is `Delete`.

## Diagnostics

- Stuck PVC: `kubectl describe pvc <name>` → `Finalizers: [kubernetes.io/pvc-protection]` and `Used By`
  lists the pod still holding it. Find it: `kubectl get pods -A -o json | ... spec.volumes[].persistentVolumeClaim`.
- `Released` PV: `kubectl get pv` shows `RECLAIM POLICY Retain` + `STATUS Released`; `kubectl get pv
  <name> -o jsonpath='{.spec.claimRef}'` shows the stale claim.

## Known Issues

- **Stuck Terminating — fix:** delete/evict the **consuming pod** (or the workload) first; the finalizer
  clears and the PVC/PV deletes cleanly. **Do not** blindly `kubectl patch ... finalizers=null` — that
  deletes the object while leaving the real volume/data orphaned in the backend.
- **`Delete` data loss — prevent:** for data you must keep, use a StorageClass with **`reclaimPolicy:
  Retain`** (and/or a `Retain` StatefulSet PVC retention policy) so a stray `delete pvc` doesn't wipe
  the volume; snapshot before deleting.
- **`Released` PV won't rebind — fix:** clear the stale claimRef to make it `Available` again:
  `kubectl patch pv <name> -p '{"spec":{"claimRef":null}}'`; then a matching PVC can bind. (Confirm you
  want the old data reused — the PV still points at the retained volume.)

## References

- Upstream persistent-volumes (finalizers, reclaim policy). CSI layer [[CONCEPT-CSI_LAYER]]; reclaim
  honoring [[CONCEPT-K8S_HONOR_PV_RECLAIM_POLICY]]; StatefulSet PVC auto-delete
  [[CONCEPT-K8S_STATEFULSET_PVC_AUTODELETE]]; node-local storage [[TROUBLE-NODE_LOCAL_PVC_DRAIN]].
