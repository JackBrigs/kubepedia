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
    target: TROUBLE-CEPH_CSI_CEPHFS_MOUNT
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

## Upstream issues & upgrade notes (mined 2026-07-19)

**Future upgrade context** beyond pinned **3.14.2** (from upstream releases):
- **⚠ 3.17.0 breaking:** the **NFS CSIDriver `spec.attachRequired` becomes `true`** — you must **delete and recreate** the CSIDriver object; NVMe-oF StorageClass now requires publish secrets (recreate); `--setmetadata` deprecated (always on).
- 3.15/3.16 add RBD QoS, controller-publish-secret caching, and (experimental) NVMe-oF; **Ceph-CSI-Operator is the recommended deploy path from 3.16+**. Kubernetes ServiceAccount-based volume-access restriction landed in 3.17.

**Open upstream issues (as of 2026-07-19):** exclusive **RBD locking to prevent inadvertent multi-node RWO access** (#578) — relevant to the multi-attach class; run-as-non-root / configurable UID/GID (#2519); multi-Ceph topology-aware provisioning (#5177).

## Older-version CVEs & security history (mined 2026-07-19)

ceph-csi's own CVE record is thin; the real older-version exposure is the **Ceph cluster version** behind it (Ceph CVEs) and old base images. The RWO exclusive-lock gap (#578) is a data-safety, not a CVE, concern. Keep the driver current (Ceph-CSI-Operator path from 3.16+) and the Ceph cluster patched.

## Guides & how-to (official)

- **Deploy CephFS:** https://github.com/ceph/ceph-csi/blob/devel/docs/deploy-cephfs.md ; **Ceph-CSI-Operator (3.16+):** https://github.com/ceph/ceph-csi-operator
- **How to upgrade:** update the driver manifests/Helm to the target tag; **3.17 breaking** — the NFS CSIDriver `attachRequired` flips → **delete/recreate the CSIDriver**; from 3.16+ prefer the Ceph-CSI-Operator deploy path. Keep the Ceph cluster patched.
## References

- ceph-csi v3.14.2 / v3.13.0 READMEs + release notes (above).
- Catalog: [[CONCEPT-ADDON_CATALOG]]; Rook/Ceph: [[CONCEPT-ADDON_ROOK_CEPH]].
