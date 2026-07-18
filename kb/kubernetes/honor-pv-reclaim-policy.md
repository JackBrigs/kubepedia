---
id: CONCEPT-K8S_HONOR_PV_RECLAIM_POLICY
type: concept
title: "Honor PV reclaim policy — Delete respected regardless of delete order (on 1.31, GA 1.33)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - HonorPVReclaimPolicy
  - pv not deleted storage leak
  - reclaim policy delete order
  - pv reclaim policy honored
tags:
  - kubernetes
  - storage
  - csi
sources:
  - type: code
    path: keps/sig-storage/2644-honor-pv-reclaim-policy
    url: https://github.com/kubernetes/enhancements/tree/master/keps/sig-storage/2644-honor-pv-reclaim-policy
    note: "kep.yaml: alpha 1.23, beta/on-by-default 1.31, stable 1.33"
relations:
  - type: see_also
    target: CONCEPT-K8S_UPGRADE_SILENT_CHANGES
  - type: see_also
    target: CONCEPT-K8S_FEATURE_GATES
---

# Honor PV reclaim policy — Delete respected regardless of delete order (on 1.31, GA 1.33)

## Summary

Previously, if a **PV** was deleted **before** its bound **PVC**, a `reclaimPolicy: Delete` PV could be
removed **without** deleting the backing storage — a silent **storage leak** (orphaned cloud disks /
CSI volumes). `HonorPVReclaimPolicy` fixes this: the Delete reclaim is honored **whatever the deletion
order**. It is **on by default from K8s 1.31** and **GA in 1.33** (Kubespray v2.29.0+).

## Context

- Milestone (`keps/sig-storage/2644-...` kep.yaml): alpha **1.23**, beta/on **1.31**, stable **1.33**.
- **Mechanism:** a finalizer (`external-provisioner.volume.kubernetes.io/finalizer`) on the PV ensures
  the CSI/volume deletion happens before the PV object is removed, regardless of whether PVC or PV was
  deleted first.
- **Operator impact (positive):** fewer orphaned volumes/disks accumulating cost; no action needed —
  it's an automatic correctness fix. Just be aware that a `Delete`-policy PV now **reliably** removes
  the underlying storage, so it is even more important that PVs holding data you want to keep use
  **`Retain`** (see [[CONCEPT-K8S_STATEFULSET_PVC_AUTODELETE]] for the StatefulSet-PVC angle).

## References

- `keps/sig-storage/2644-honor-pv-reclaim-policy` (kep.yaml GA 1.33). Silent changes
  [[CONCEPT-K8S_UPGRADE_SILENT_CHANGES]]; gates [[CONCEPT-K8S_FEATURE_GATES]].
