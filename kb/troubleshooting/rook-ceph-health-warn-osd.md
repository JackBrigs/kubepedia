---
id: TROUBLE-ROOK_CEPH_HEALTH_WARN_OSD
type: troubleshooting
title: "Rook-Ceph: HEALTH_WARN / OSD down / PGs degraded"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.18.0 <=1.20.2"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - ceph health_warn
  - rook osd down
  - ceph pgs degraded
  - ceph osd not creating
tags:
  - troubleshooting
  - rook
  - ceph
  - storage
sources:
  - type: docs
    path: Rook Ceph common issues
    url: https://rook.io/docs/rook/latest/Troubleshooting/ceph-common-issues/
    note: "OSD, health, PG troubleshooting"
relations:
  - type: see_also
    target: CONCEPT-ADDON_ROOK_CEPH
---

# Rook-Ceph: HEALTH_WARN / OSD down / PGs degraded

## Summary

The Ceph cluster reports `HEALTH_WARN`/`HEALTH_ERR`, an OSD is `down`, or PGs are
`degraded`/`undersized`. Use the **toolbox** to read `ceph status` and locate the failing
OSD/host, then address the disk, capacity, or CRUSH placement cause.

## Problem

- `CephCluster` shows a non-`HEALTH_OK` phase; volumes slow or read-only.
- An OSD pod is `CrashLoopBackOff` or the OSD is `down`/`out`.
- PGs stuck `degraded`, `undersized`, or `inactive`.

## Context

- Applies to Rook **1.18–1.20** (owner runs 1.18.9 — [[CONCEPT-ADDON_ROOK_CEPH]]).

## Diagnostics

Use the Rook toolbox:

1. `ceph status` / `ceph health detail` — the specific warning (OSD down, near-full, PG
   states).
2. **OSD down:** `ceph osd tree` to find it; check that OSD pod's logs and the underlying
   disk (SMART/errors). A failed disk → replace the OSD; a transient restart → it should
   re-peer.
3. **`OSD_NEARFULL`/`OSD_FULL`:** capacity — add OSDs/nodes or free data; a full cluster goes
   read-only. Rebalance/reweight if data is skewed.
4. **PGs degraded/undersized:** usually too few up OSDs for the pool's replica size, or a bad
   **CRUSH** hierarchy (failure domain vs number of hosts). New clusters are rejected at
   creation on a bad topology.
5. **OSDs not created:** the disk must be **raw/unformatted** (no partition table/filesystem);
   Rook won't consume a disk with existing data.

## Known Issues

- **Ceph v20.2.0 (Tentacle)** has a data-corruption bug with "read affinity" enabled — wait
  for v20.2.1. Ceph CVE-2025-52555 affects some 18.2.x/19.x patches.
- StorageClass immutability breaks `helm upgrade` of the cluster chart
  ([[TROUBLE-ROOK_CEPH_UPGRADE_SC_IMMUTABLE]]).

## References

- Rook Ceph common issues (above); addon: [[CONCEPT-ADDON_ROOK_CEPH]].
