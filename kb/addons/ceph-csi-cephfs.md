---
id: CONCEPT-ADDON_CEPH_CSI_CEPHFS
type: concept
title: "ceph-csi-cephfs — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.32"
component_version: "3.14.2"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - ceph-csi-cephfs
  - csi-cephfs
  - cephfs csi driver
tags:
  - addons
  - storage
  - ceph
  - csi
sources:
  - type: docs
    path: ceph-csi v3.14.2 README
    url: https://raw.githubusercontent.com/ceph/ceph-csi/v3.14.2/README.md
    note: "tested K8s v1.30–v1.32; requires Ceph Pacific v16.2.0+"
  - type: docs
    path: ceph-csi v3.13.0 README
    url: https://raw.githubusercontent.com/ceph/ceph-csi/v3.13.0/README.md
    note: "tested K8s v1.29–v1.31"
relations:
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
  - type: see_also
    target: CONCEPT-ADDON_ROOK_CEPH
---

# ceph-csi-cephfs — addon

## Summary

The CephFS CSI driver provides shared filesystem PVs from a Ceph cluster. The inventory runs
two versions: **3.14.2** (tested K8s **1.30–1.32**) and **3.13.0** (tested K8s **1.29–1.31**).
Both require **Ceph Pacific (≥ v16.2.0)+**.

## Context

- Class: upstream addon; `csi-cephfs` row in [[CONCEPT-ADDON_CATALOG]]. Often used alongside
  [[CONCEPT-ADDON_ROOK_CEPH]] (or an external Ceph cluster).

## Implementation

- Chart→app matches version: 3.14.2 / 3.13.0. Chart `kubeVersion`: **none** (tag Chart.yaml
  is a `canary` placeholder; released charts confirmed via Artifact Hub).
- **N.(x-1) support policy** — only the latest and previous minor are supported (3.14.x
  current, 3.13.0 now behind the active window).

## Configuration

- Provide the Ceph cluster connection (monitors, secret) and a CephFS subvolume group.
- Some VolumeGroupSnapshot features need **K8s 1.31+**.

## Compatibility

- **Kubernetes range:** **3.14.2 → 1.30–1.32**; **3.13.0 → 1.29–1.31**.
- **Known issues:** VolumeGroupSnapshot needs K8s 1.31+; cryptsetup hangs (mitigated by added
  timeouts in 3.14.2). 3.14.2 fixes `flattenClonedRbdImages` namespace handling.
- **CVEs:** none against `ceph/ceph-csi`. The backing CephFS is exposed to Ceph-side
  **CVE-2025-52555** if the Ceph cluster runs an affected patch level (see
  [[CONCEPT-ADDON_ROOK_CEPH]]).

## References

- ceph-csi v3.14.2 / v3.13.0 READMEs + release notes (above).
- Catalog: [[CONCEPT-ADDON_CATALOG]]; Rook/Ceph: [[CONCEPT-ADDON_ROOK_CEPH]].
