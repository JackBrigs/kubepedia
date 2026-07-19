---
id: TROUBLE-PVC_VOLUME_EXPANSION
type: troubleshooting
title: "PVC volume expansion doesn't take effect — allowVolumeExpansion, FileSystemResizePending, can't shrink"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-19"
confidence: confirmed
aliases:
  - pvc resize not working
  - volume expansion no effect
  - allowVolumeExpansion false
  - FileSystemResizePending
  - grow pvc kubernetes
  - cannot shrink pvc
  - RecoverVolumeExpansionFailure
tags:
  - troubleshooting
  - storage
  - pvc
  - expansion
sources:
  - type: external
    path: expanding persistent volumes claims
    url: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#expanding-persistent-volumes-claims
    note: "allowVolumeExpansion on the StorageClass; filesystem resize is deferred to next pod (FileSystemResizePending); expand-only"
relations:
  - type: see_also
    target: CONCEPT-CSI_LAYER
  - type: see_also
    target: TROUBLE-PVC_PV_DELETION
---

# PVC volume expansion doesn't take effect — allowVolumeExpansion, FileSystemResizePending, can't shrink

## Summary

Growing a PVC looks like a one-liner (`kubectl edit pvc` → bigger `resources.requests.storage`) but
three things bite: the **StorageClass must set `allowVolumeExpansion: true`** or the edit is rejected;
for many drivers the block device grows online but the **filesystem resize is deferred until the pod
restarts** (the PVC sits with a `FileSystemResizePending` condition and the app still sees the old
size); and expansion is **grow-only** — you can never shrink a PVC.

## Problem

- Editing the PVC size is **rejected**: `persistentvolumeclaims "x" is forbidden: only dynamically
  provisioned pvc ... field can be expanded` / `...forbidden ... allowVolumeExpansion`.
- The PVC `capacity` updated but the **app/`df` still shows the old size** — the filesystem wasn't
  grown.
- Trying to **lower** the size is rejected outright.

## Context

- Applies across **v2.27.0–v2.31.0** and any CSI/in-tree class that supports expansion
  ([[CONCEPT-CSI_LAYER]]).
- **`allowVolumeExpansion`:** a per-StorageClass boolean, **default false**. If it isn't `true`, the API
  server refuses to increase the PVC request. Not every driver/class supports it.
- **Two-phase resize:** expansion is (1) grow the backing volume/device, then (2) grow the filesystem.
  Many CSI drivers do (1) online but **defer (2) to the next mount** — the PVC gets a
  **`FileSystemResizePending`** condition and the extra space only appears **after the consuming pod is
  recreated** (remount triggers the FS resize). Some drivers do online FS resize without a restart; it
  is driver-dependent.
- **Grow-only:** Kubernetes has **no shrink** — `resources.requests.storage` can only increase.
- **Failed expansion:** if a too-large request fails at the backend, `RecoverVolumeExpansionFailure`
  (K8s feature, beta in this range) lets you **reduce the request back down** to a value ≥ current
  actual size and retry — without it, a failed expansion could wedge the PVC.

## Diagnostics

- Class supports it? `kubectl get sc <name> -o jsonpath='{.allowVolumeExpansion}'` → must be `true`.
- Stuck pending FS resize: `kubectl describe pvc <name>` → condition `FileSystemResizePending`
  ("Waiting for user to (re-)start a pod to finish file system resize").
- Actual vs requested: compare `.status.capacity.storage` (actual) with `.spec.resources.requests.storage`
  (requested).

## Known Issues

- **Rejected edit — fix:** ensure the StorageClass has `allowVolumeExpansion: true` (edit the class or
  move the PVC to one that supports it); it can't be enabled retroactively on a class that doesn't
  support the operation in the driver.
- **New space not visible — fix:** if the PVC shows `FileSystemResizePending`, **restart / recreate the
  consuming pod** (for a StatefulSet, delete the pod so it's recreated) to complete the filesystem
  grow; then `df` inside the pod shows the new size.
- **Shrink — not possible:** to reduce size, create a new smaller PVC and migrate the data (snapshot/
  copy); there is no in-place shrink.
- **Failed/oversized expansion:** with `RecoverVolumeExpansionFailure`, patch the request back down to a
  valid size and retry; otherwise you may need to restore from snapshot onto a correctly-sized PVC.

## References

- Upstream "expanding persistent volumes claims". CSI layer [[CONCEPT-CSI_LAYER]]; deletion/lifecycle
  [[TROUBLE-PVC_PV_DELETION]].
