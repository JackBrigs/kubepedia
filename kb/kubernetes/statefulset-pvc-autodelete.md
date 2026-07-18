---
id: CONCEPT-K8S_STATEFULSET_PVC_AUTODELETE
type: concept
title: "StatefulSet PVC auto-delete — persistentVolumeClaimRetentionPolicy (GA 1.32)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.32 <=1.35"
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - StatefulSetAutoDeletePVC
  - persistentVolumeClaimRetentionPolicy
  - statefulset deletes pvc
  - statefulset data loss retention policy
  - whenDeleted whenScaled
tags:
  - kubernetes
  - storage
  - workloads
sources:
  - type: code
    path: keps/sig-apps/1847-autoremove-statefulset-pvcs
    url: https://github.com/kubernetes/enhancements/tree/master/keps/sig-apps/1847-autoremove-statefulset-pvcs
    note: "kep.yaml: alpha 1.23, beta 1.27, stable 1.32"
relations:
  - type: see_also
    target: CONCEPT-K8S_UPGRADE_SILENT_CHANGES
  - type: see_also
    target: CONCEPT-K8S_FEATURE_GATES
---

# StatefulSet PVC auto-delete — persistentVolumeClaimRetentionPolicy (GA 1.32)

## Summary

A StatefulSet can now **automatically delete its PVCs** (and thus the backing PVs, if the storage
class reclaim policy is `Delete`) when the StatefulSet is deleted or scaled down, via
`spec.persistentVolumeClaimRetentionPolicy`. `StatefulSetAutoDeletePVC` reached **GA in K8s 1.32**
(Kubespray v2.29.0+). This is a **data-lifecycle** change: the historical guarantee that StatefulSet
PVCs **survive** deletion is no longer absolute — it depends on a field you may not have set.

## Context

- Milestone (`keps/sig-apps/1847-...` kep.yaml): alpha **1.23**, beta **1.27**, stable **1.32**.
- **Field:** `persistentVolumeClaimRetentionPolicy` with `whenDeleted` and `whenScaled`, each
  `Retain` (default — old behavior) or `Delete`. **Default is `Retain`**, so nothing changes unless you
  set `Delete`.
- **The risk:** the feature being GA means the field is honored everywhere — a chart/manifest that sets
  `whenScaled: Delete` or `whenDeleted: Delete` will now **destroy data** on scale-down/delete on any
  cluster in range. Audit StatefulSet manifests (especially third-party charts) before assuming PVCs
  are safe.
- **Operator action:** for stateful data you must keep, leave the policy at **`Retain`** (or unset) and
  verify no overlay sets `Delete`; combine with a `Retain` storage-class reclaim policy for defense in
  depth.

## References

- `keps/sig-apps/1847-autoremove-statefulset-pvcs` (kep.yaml GA 1.32). Silent changes
  [[CONCEPT-K8S_UPGRADE_SILENT_CHANGES]]; gates [[CONCEPT-K8S_FEATURE_GATES]].
