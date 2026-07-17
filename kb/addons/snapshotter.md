---
id: CONCEPT-ADDON_SNAPSHOTTER
type: concept
title: "external-snapshotter (addon v6.3.0) — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.20 <=1.35"
component_version: "6.3.0"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - snapshotter
  - external-snapshotter
  - snapshot-controller addon
tags:
  - addons
  - storage
  - csi
  - snapshots
sources:
  - type: docs
    path: kubernetes-csi/external-snapshotter
    url: https://github.com/kubernetes-csi/external-snapshotter
    note: "snapshot-controller + CRDs; v1 snapshot API"
relations:
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
  - type: see_also
    target: COMPONENT-SNAPSHOT_CONTROLLER
  - type: see_also
    target: CONCEPT-ADDON_VOLSYNC
---

# external-snapshotter (addon v6.3.0) — addon

## Summary

The owner's independent external-snapshotter install — **v6.3.0** — provides the
snapshot-controller and VolumeSnapshot CRDs (CSI snapshot `v1` API). It overlaps the
Kubespray-managed [[COMPONENT-SNAPSHOT_CONTROLLER]] (a different, independently-pinned
version); other addons like [[CONCEPT-ADDON_VOLSYNC]] depend on it.

## Context

- Class: upstream addon; `snapshotter` row in [[CONCEPT-ADDON_CATALOG]] (local chart,
  overlaps the Kubespray snapshot-controller).

## Implementation

- Chart/app **v6.3.0** — snapshot-controller Deployment + the `VolumeSnapshot`,
  `VolumeSnapshotContent`, `VolumeSnapshotClass` CRDs. The **CSI driver** must ship the
  companion csi-snapshotter sidecar; the controller alone does not take snapshots.
- v6.3.0 is an older line (upstream is now v8.x) — pin CRD and controller versions together.

## Configuration

- Exactly **one** snapshot-controller should run per cluster — a second one (e.g. from a CSI
  driver chart) conflicts. Ensure a `VolumeSnapshotClass` exists for the CSI driver in use.

## Compatibility

- **Kubernetes range:** snapshot `v1` API is GA since K8s 1.20, so v6.3.0 works across
  **1.20–1.35**; the exact tested upper bound for this older line is **unverified** — prefer a
  current (v8.x) release on newer clusters.
- **CVEs:** none found for `github.com/kubernetes-csi/external-snapshotter/v6` at 6.3.0
  (OSV empty).

## References

- kubernetes-csi/external-snapshotter (above).
- Catalog: [[CONCEPT-ADDON_CATALOG]]; Kubespray sibling: [[COMPONENT-SNAPSHOT_CONTROLLER]];
  consumer: [[CONCEPT-ADDON_VOLSYNC]].
