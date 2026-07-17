---
id: TROUBLE-ROOK_CEPH_UPGRADE_SC_IMMUTABLE
type: troubleshooting
title: "rook-ceph-cluster helm upgrade fails: StorageClass is immutable"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.18.0 <=1.20.2"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - rook helm upgrade storageclass immutable
  - rook csi operator conversion
  - rook-ceph-cluster upgrade fails
tags:
  - troubleshooting
  - rook
  - ceph
  - storage
  - upgrade
sources:
  - type: docs
    path: Rook v1.18 upgrade guide
    url: https://rook.io/docs/rook/v1.18/Upgrade/rook-upgrade/
    note: "StorageClass immutability; CSI operator conversion; operator-before-cluster"
relations:
  - type: see_also
    target: CONCEPT-ADDON_ROOK_CEPH
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# rook-ceph-cluster helm upgrade fails: StorageClass is immutable

## Summary

`helm upgrade` of `rook-ceph-cluster` (v1.18+) fails because the chart tries to modify an
existing **immutable StorageClass** (new params were added), and/or the operator's CSI
migration errors. Delete the affected SC first (or drop the new params), upgrade the operator
chart before the cluster chart, and know the CSI-operator revert flag.

## Problem

- `helm upgrade` errors: cannot patch StorageClass — field is immutable.
- After upgrade, RBD/CephFS provisioning breaks with CSI-operator conversion errors.
- `CephCluster` creation rejected on a bad CRUSH/topology hierarchy.

## Context

- Applies to Rook **1.18.0–1.20.2** (owner runs 1.18.9 — [[CONCEPT-ADDON_ROOK_CEPH]]). v1.18
  raised the K8s minimum to **1.29**.

## Diagnostics

- **StorageClasses are immutable.** v1.18 added SC params
  (`controller-publish-secret-name`/`-namespace`) — `helm upgrade` can't patch an existing SC.
  Delete and recreate the SC, or remove the new params from values for the upgrade.
- **CSI operator now required** for RBD/CephFS/NFS: Rook auto-converts legacy CSI settings to
  CSI-operator CRs. If conversion fails, set **`ROOK_USE_CSI_OPERATOR: false`** to revert.
- **Upgrade order:** operator chart **before** the cluster chart.

## Known Issues

- **Ceph v20.2.0 (Tentacle) has a data-corruption bug when "read affinity" is enabled** —
  wait for v20.2.1. Cluster is also exposed to **Ceph CVE-2025-52555** if running an affected
  Ceph patch (18.2.1–18.2.4 / 19.0.0–19.2.2; fixed 18.2.5 / 19.2.3).

## References

- Rook v1.18 upgrade guide (above); addon: [[CONCEPT-ADDON_ROOK_CEPH]]; horizon:
  [[CONCEPT-UPGRADE_HORIZON]].
