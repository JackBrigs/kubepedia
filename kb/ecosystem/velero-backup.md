---
id: CONCEPT-VELERO
type: concept
title: "Application & PV backup/restore with Velero"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - velero
  - application backup kubernetes
  - persistent volume backup
  - namespace backup restore
  - disaster recovery workloads
  - csi snapshot backup
tags:
  - backup
  - disaster-recovery
  - velero
  - storage
  - ecosystem
sources:
  - type: docs
    path: Velero documentation
    url: https://velero.io/docs/
    note: "namespace/PV backup to object storage; CSI snapshots or file-level (kopia/restic) (verified)"
relations:
  - type: see_also
    target: PRACTICE-BACKUP_DR
  - type: see_also
    target: CONCEPT-CSI_LAYER
  - type: see_also
    target: PRACTICE-ETCD_BACKUP_RESTORE
---

# Application & PV backup/restore with Velero

## Summary

**Velero** backs up **application objects and persistent-volume data** to object storage,
and restores them — the piece **etcd backup doesn't cover**. An etcd snapshot captures all
API objects but **not** the data inside PVs; Velero captures selected namespaces plus their
PV contents (via CSI snapshots or file-level copy). Use both: etcd/PKI for the whole
control plane, Velero for app-level backup, migration, and selective restore.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`. Velero is **not** Kubespray-managed — install
  it via its Helm chart/CLI (evidence: upstream docs, `verified`).
- Needs **object storage** (S3/MinIO/GCS/Azure Blob) for backups and a provider plugin.

## Implementation

**What Velero does:**

- **Backup** a set of namespaces/labels → API objects (as JSON) + PV data, stored in a
  bucket. **Restore** re-creates them (same or different cluster → migration/DR).
- **Scheduled backups** (cron) with retention TTL.
- **PV data**, two ways:
  - **CSI snapshots** — Velero triggers `VolumeSnapshot`s via the cluster's
    **snapshot-controller + VolumeSnapshotClass** ([[CONCEPT-CSI_LAYER]]) — enable
    `csi_snapshot_controller_enabled` and a snapshot-capable CSI driver.
  - **File-level (kopia/restic)** — copies PV file contents; works when the storage has no
    snapshot support, but slower.

**Integration with the cluster:**

- Runs in its own namespace; its ServiceAccount needs RBAC to read/restore the resources
  it manages.
- For CSI snapshot backups the **snapshot-controller must be enabled** and a
  `VolumeSnapshotClass` present — otherwise Velero falls back to file-level or skips PV
  data ([[TROUBLE-PVC_PENDING_NO_STORAGECLASS]] for the storage side).

## Compatibility

- **Complements, not replaces, etcd backup.** etcd snapshot = *all* objects for full
  control-plane restore ([[PRACTICE-ETCD_BACKUP_RESTORE]]); Velero = *selected* namespaces
  + PV data. Full DR strategy uses both ([[PRACTICE-BACKUP_DR]]).
- **CSI snapshot API:** `VolumeSnapshot` is GA; use the `v1` API (older `v1beta1` is
  retired) — align Velero's CSI plugin with your Kubernetes version.
- **Cross-cluster restore** requires matching CRDs and compatible storage on the target;
  test migrations before relying on them.
- **Rehearse restores** — an untested backup is a hope, not a plan.

## References

- Velero docs. DR strategy: [[PRACTICE-BACKUP_DR]]; CSI/snapshots: [[CONCEPT-CSI_LAYER]];
  etcd backup: [[PRACTICE-ETCD_BACKUP_RESTORE]].
