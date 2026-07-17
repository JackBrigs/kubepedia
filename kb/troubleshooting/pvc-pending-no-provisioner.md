---
id: TROUBLE-PVC_PENDING_NO_PROVISIONER
type: troubleshooting
title: "PVC stuck Pending: no provisioner / no matching PV"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - pvc pending
  - no persistent volumes available
  - waitforfirstconsumer pvc pending
  - storageclass not found
tags:
  - troubleshooting
  - storage
  - csi
  - pvc
sources:
  - type: docs
    path: Kubernetes persistent volumes
    url: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
    note: "StorageClass, binding modes, provisioning"
relations:
  - type: see_also
    target: COMPONENT-SNAPSHOT_CONTROLLER
  - type: see_also
    target: CONCEPT-ADDON_ROOK_CEPH
  - type: see_also
    target: CONCEPT-ADDON_LVM_LOCALPV
---

# PVC stuck Pending: no provisioner / no matching PV

## Summary

A `PersistentVolumeClaim` stays `Pending` and the pod using it won't start. Either no
`StorageClass`/provisioner is fulfilling it, the CSI driver isn't healthy, or (for
`WaitForFirstConsumer`) no schedulable node/topology matches.

## Problem

- `kubectl get pvc` shows `Pending`; the pod is `Pending`/`ContainerCreating`.
- Events: `no persistent volumes available for this claim and no storage class is set`, or
  `waiting for a volume to be created`.

## Context

- Applies to any CSI/storage backend (Rook-Ceph [[CONCEPT-ADDON_ROOK_CEPH]], lvm-localpv
  [[CONCEPT-ADDON_LVM_LOCALPV]], cloud CSI). Diagnosis is generic.

## Diagnostics

1. `kubectl describe pvc <name>` — the event says which layer is stuck.
2. **No StorageClass:** the PVC has no `storageClassName` and there is **no default**
   StorageClass — set one or mark a class default
   (`storageclass.kubernetes.io/is-default-class`).
3. **Provisioner not running/healthy:** the CSI controller/provisioner for that class must be
   up — check its pods and logs; a CrashLooping external-provisioner leaves PVCs `Pending`.
4. **`WaitForFirstConsumer`:** the PVC binds only once a **pod is scheduled**; if the pod is
   unschedulable (taints/resources/topology), the PVC stays `Pending` by design — fix pod
   scheduling. For node-local volumes (lvm-localpv), the node must have the VG/capacity.
5. **Capacity/topology:** the backend may be full, or `allowedTopologies`/zone constraints
   exclude every node.
6. **Immutable class mismatch:** requesting a class that doesn't exist → `Pending` with
   `storageclass.storage.k8s.io "<x>" not found`.

## Known Issues

- Snapshot-restore PVCs additionally need a working snapshot-controller +
  `VolumeSnapshotClass` ([[COMPONENT-SNAPSHOT_CONTROLLER]]).

## References

- Kubernetes PV docs (above); Rook: [[CONCEPT-ADDON_ROOK_CEPH]]; local:
  [[CONCEPT-ADDON_LVM_LOCALPV]].
