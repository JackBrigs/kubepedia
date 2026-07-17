---
id: TROUBLE-VELERO_BACKUP_RESTORE_FAILS
type: troubleshooting
title: "Velero backup/restore PartiallyFailed or Failed"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - velero backup partiallyfailed
  - velero restore failed
  - velero snapshot not created
  - velero backupstoragelocation unavailable
  - velero no volume snapshots
  - restic kopia backup failed
tags:
  - troubleshooting
  - backup
  - velero
  - storage
sources:
  - type: docs
    path: Velero troubleshooting / debugging
    url: https://velero.io/docs/main/troubleshooting/
    note: "backup/restore phases, BackupStorageLocation, CSI snapshot vs file-level failures (verified)"
relations:
  - type: see_also
    target: CONCEPT-VELERO
  - type: see_also
    target: CONCEPT-CSI_LAYER
  - type: see_also
    target: PRACTICE-BACKUP_DR
---

# Velero backup/restore PartiallyFailed or Failed

## Summary

A Velero backup/restore ending `PartiallyFailed`/`Failed` almost always means one of:
the **object store is unreachable** (BackupStorageLocation unavailable), **PV data wasn't
captured** (no CSI snapshot class / driver, or file-level copy failed), or **RBAC** blocked
restoring some objects. `velero backup describe … --details` + `velero backup logs` name
the exact resource and error.

## Problem

`velero backup get` / `velero restore get` shows `PartiallyFailed` or `Failed`; the app's
PV data is missing after restore, or the backup completed with warnings/errors.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0` clusters running Velero ([[CONCEPT-VELERO]]).
- Two moving parts fail independently: **object storage** (backup metadata + file-level PV
  data) and **volume snapshots** (CSI/`VolumeSnapshot`).

## Diagnostics

- **`velero backup describe <b> --details`** and **`velero backup logs <b>`** — the phase,
  warnings, and the specific resource/volume that failed.
- **BackupStorageLocation:** `velero backup-location get` — `Unavailable` means the object
  store (S3/MinIO/…) creds/endpoint/bucket are wrong or unreachable.
- **VolumeSnapshotLocation / CSI:** `kubectl get volumesnapshots,volumesnapshotcontents -A`
  — were snapshots actually created? Empty = snapshot path not working
  ([[CONCEPT-CSI_LAYER]]).
- **Restore warnings:** `velero restore describe <r> --details` — `already exists` /
  `forbidden` per resource.

## Known Issues

- **BackupStorageLocation `Unavailable`** — fix the object-store credentials/endpoint/
  region/bucket; without it nothing is stored. The most common first failure.
- **No PV data / snapshots not created** — the CSI snapshot path needs the
  **snapshot-controller enabled** + a `VolumeSnapshotClass` labelled for Velero
  (`velero.io/csi-volumesnapshot-class`) + a snapshot-capable driver
  ([[CONCEPT-CSI_LAYER]]). Otherwise use **file-level** (kopia/restic) with the node-agent
  DaemonSet running and the volume annotated for FS backup.
- **`VolumeSnapshotClass` API mismatch** — use the **v1** snapshot API (older `v1beta1` is
  retired); align Velero's CSI plugin with your Kubernetes version.
- **Restore `forbidden`** — Velero's SA lacks RBAC to create some restored kind
  ([[TROUBLE-RBAC_FORBIDDEN]]).
- **Restore `already exists`** — the namespace/objects still exist; restore into a fresh
  namespace or use an existing-resource policy.
- **PV won't rebind** — the restored PVC references a StorageClass/zone the target cluster
  doesn't have ([[TROUBLE-PVC_PENDING_NO_STORAGECLASS]]).

**Gotchas:**

- **`PartiallyFailed` still produced a backup** — but with gaps; don't treat it as good.
  Read the details and fix the gap.
- **Snapshots ≠ file backup:** CSI snapshots are storage-side and fast but tie you to that
  storage; kopia/restic copies files and is portable but slower. Pick per volume.
- **Rehearse the restore** — a green backup that has never been restored is unproven
  ([[PRACTICE-BACKUP_DR]]).

## References

- Velero troubleshooting docs. Component: [[CONCEPT-VELERO]]; CSI/snapshots:
  [[CONCEPT-CSI_LAYER]]; DR: [[PRACTICE-BACKUP_DR]].
