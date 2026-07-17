---
id: TROUBLE-MULTIPLE_SNAPSHOT_CONTROLLERS
type: troubleshooting
title: "Snapshots misbehave: more than one snapshot-controller in the cluster"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - two snapshot controllers conflict
  - volumesnapshot stuck
  - velero volsync snapshot conflict
  - duplicate snapshot crds
tags:
  - troubleshooting
  - cross-component
  - storage
  - snapshots
sources:
  - type: docs
    path: external-snapshotter (one controller per cluster)
    url: https://github.com/kubernetes-csi/external-snapshotter#usage
    note: "the snapshot controller and CRDs are cluster-singletons"
relations:
  - type: see_also
    target: COMPONENT-SNAPSHOT_CONTROLLER
  - type: see_also
    target: CONCEPT-ADDON_SNAPSHOTTER
  - type: see_also
    target: CONCEPT-ADDON_VOLSYNC
---

# Snapshots misbehave: more than one snapshot-controller in the cluster

## Summary

A **cross-component** pitfall: the CSI **snapshot-controller** and the `VolumeSnapshot*` CRDs
are **cluster-singletons**, but several charts try to install them — Kubespray
([[COMPONENT-SNAPSHOT_CONTROLLER]]), a standalone external-snapshotter
([[CONCEPT-ADDON_SNAPSHOTTER]]), Rook, and backup tools (Velero, VolSync
[[CONCEPT-ADDON_VOLSYNC]]). Two controllers or mismatched CRD versions cause stuck or
duplicated snapshots.

## Problem

- `VolumeSnapshot`/`VolumeSnapshotContent` stuck `readyToUse: false` or churning.
- CRD apply conflicts / two controller Deployments reconciling the same objects.
- Backup tools report VolumeSnapshotClass or CRD-version errors.

## Context

- Applies wherever more than one component ships the snapshot-controller/CRDs. In this
  platform that's Kubespray + the `snapshotter` addon (6.3.0) + potentially Velero/VolSync/Rook.

## Diagnostics

1. **Count the controllers:** `kubectl get deploy -A | grep snapshot-controller` — there must
   be **exactly one**. Disable the snapshot-controller in every chart except the one you choose
   to own it (most charts have a `snapshotController.enabled`/`installCRDs` toggle).
2. **CRD ownership/version:** `kubectl get crd | grep snapshot` — one set of
   `volumesnapshots.snapshot.storage.k8s.io` etc.; the **newest** controller in the cluster
   dictates the required CRD version. Mismatched CRDs (v6 vs v8) break validation
   ([[TROUBLE-SNAPSHOT_CONTROLLER_7_TO_8]]).
3. **VolumeSnapshotClass:** the backup tool's referenced class must exist and point at the CSI
   driver's `deletionPolicy`/driver name.
4. **Pick an owner:** decide which component owns snapshots cluster-wide (usually the standalone
   external-snapshotter or the CSI platform), and make Velero/VolSync **consume** it, not
   install their own.

## Known Issues

- external-snapshotter v8 enforces **one default VolumeSnapshotClass per driver** and removed
  the validation webhook — align CRDs to the single owner
  ([[TROUBLE-SNAPSHOT_CONTROLLER_7_TO_8]]).

## References

- external-snapshotter usage (above); Kubespray: [[COMPONENT-SNAPSHOT_CONTROLLER]]; addon:
  [[CONCEPT-ADDON_SNAPSHOTTER]]; consumer: [[CONCEPT-ADDON_VOLSYNC]].
