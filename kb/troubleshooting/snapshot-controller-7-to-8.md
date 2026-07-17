---
id: TROUBLE-SNAPSHOT_CONTROLLER_7_TO_8
type: troubleshooting
title: "external-snapshotter 7→8: one class per driver, webhook removed"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=8.0.0 <=8.6.0"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - external-snapshotter v8 upgrade
  - snapshot controller 8 breaking
  - volumesnapshotclass one per driver
  - snapshot validation webhook removed
tags:
  - troubleshooting
  - storage
  - csi
  - snapshots
  - upgrade
sources:
  - type: docs
    path: external-snapshotter v8.0.0 release notes
    url: https://github.com/kubernetes-csi/external-snapshotter/releases/tag/v8.0.0
    note: "one VolumeSnapshotClass per driver enforced; validation webhook deprecated→removed; CRD validation, min K8s 1.25"
relations:
  - type: see_also
    target: COMPONENT-SNAPSHOT_CONTROLLER
  - type: see_also
    target: CONCEPT-ADDON_SNAPSHOTTER
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# external-snapshotter 7→8: one class per driver, webhook removed

## Summary

external-snapshotter **v8.0.0** (2024-05-23) tightened `VolumeSnapshotClass` handling and
added CRD validation rules. If you have **more than one default VolumeSnapshotClass per CSI
driver**, or relied on the validation webhook, the v7→v8 upgrade will surface errors. The base
ships **7.0.2** (Kubespray) / addon **6.3.0**, so this is the horizon jump.

## Problem

- Snapshots fail or are ambiguous after upgrade because there are multiple default
  VolumeSnapshotClasses for one driver.
- Objects that previously passed now fail CRD validation.
- The snapshot validation webhook stops mattering / is gone.

## Context

- Applies to external-snapshotter **8.0.0–8.6.0** (base: 7.0.2 / addon 6.3.0 —
  [[COMPONENT-SNAPSHOT_CONTROLLER]], [[CONCEPT-ADDON_SNAPSHOTTER]]).

## Diagnostics

- **At most one default `VolumeSnapshotClass` per CSI driver** is now expected — remove/aliase
  extra defaults so each driver has exactly one.
- The **validation webhook is deprecated and removed** in the v8 line — validation now lives
  in the **CRDs** (CRD validation rules require **Kubernetes ≥1.25**). Drop the standalone
  webhook deployment.
- Run **exactly one** snapshot-controller per cluster — a second one (e.g. bundled by a CSI
  driver chart) conflicts.

## Known Issues

- Coordinate with backup tools that depend on snapshots (Velero, VolSync) — validate their
  VolumeSnapshotClass references after the upgrade ([[CONCEPT-ADDON_VOLSYNC]]).

## References

- external-snapshotter v8.0.0 release notes (above); component:
  [[COMPONENT-SNAPSHOT_CONTROLLER]]; addon: [[CONCEPT-ADDON_SNAPSHOTTER]]; horizon:
  [[CONCEPT-UPGRADE_HORIZON]].
