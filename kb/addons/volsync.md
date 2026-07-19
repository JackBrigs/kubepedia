---
id: CONCEPT-ADDON_VOLSYNC
type: concept
title: "VolSync — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.20 <=1.35"
component_version: "0.15.0"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - volsync
  - volsync 0.15.0
  - pv replication
tags:
  - addons
  - storage
  - backup
  - replication
sources:
  - type: code
    path: helm/volsync/Chart.yaml
    url: https://raw.githubusercontent.com/backube/volsync/v0.15.0/helm/volsync/Chart.yaml
    note: "kubeVersion ^1.20.0-0; appVersion 0.15.0"
  - type: docs
    path: volsync v0.15.0 release
    url: https://github.com/backube/volsync/releases/tag/v0.15.0
    note: "kube-rbac-proxy removed; rclone 1.73.1; CRDs unchanged"
relations:
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
  - type: see_also
    target: COMPONENT-SNAPSHOT_CONTROLLER
---

# VolSync — addon

## Summary

VolSync asynchronously replicates PersistentVolume data (`ReplicationSource`/
`ReplicationDestination`) using restic/rsync/rclone movers — for backup and cross-cluster
DR. Chart/app **0.15.0**. **Version correction:** the inventory's "app 3.5.0" is wrong —
VolSync chart and app are lock-stepped at **0.15.0** (no 3.5.0 exists).

## Context

- Class: upstream addon; catalog row in [[CONCEPT-ADDON_CATALOG]]. Depends on CSI snapshots —
  see [[COMPONENT-SNAPSHOT_CONTROLLER]].

## Implementation

- Chart→app: 0.15.0 (lock-stepped). Chart `kubeVersion`: **`^1.20.0-0`** (needs v1 CSI
  snapshots). CRDs unchanged — `ReplicationSource`/`ReplicationDestination` stay `v1alpha1`
  (no API bump).

## Configuration

- **Requires snapshot-controller + a `VolumeSnapshotClass`** and a StorageClass that supports
  snapshot/clone — the most common misconfig is a missing VolumeSnapshotClass, which fails
  snapshot-copyMethod replication.
- **`kube-rbac-proxy` sidecar removed** in 0.15.0 — metrics auth now uses the
  controller-runtime built-in; revisit metrics scraping/RBAC.

## Compatibility

- **Kubernetes range:** chart floor **`^1.20.0-0`**; no stated max — upper end of 1.29–1.35
  **unverified** but expected to work.
- **CVEs:** none for `backube/volsync`. Bundled **rclone 1.73.1** carries GHSA-25qr-6mpr-f7qx
  (CVE-2026-41176) / GHSA-jfwf-28xr-xw6q (CVE-2026-41179) rc-API auth-bypass (fixed rclone
  1.73.5) — exploitable only if the rclone `rcd`/`--rc` server is enabled, which VolSync's
  mover does **not** do (low practical exposure, but the vulnerable binary ships).

## Upstream issues & upgrade notes (mined 2026-07-19)

**Future upgrade context** beyond pinned **0.15.0** (from upstream releases):
- **0.16.0:** `rsync-tls` **enforces TLS 1.3 as the minimum** and sets ciphers per OpenShift TLS-profile compliance (may break older rsync-tls peers); Restic → 0.18.1, Rclone → 1.74.2.

**Open upstream bugs (as of 2026-07-19):** **restic repos constantly getting locked, jobs pile up until manually unlocked** (#1042) — corroborates the mover-lock trouble doc; metrics show a volume **out of sync even after the replication object is deleted** (#1194); selective folder include/exclude not supported (#959).

## Older-version CVEs & security history (mined 2026-07-19)

VolSync publishes **no GitHub security advisories** of its own; historical exposure is driven by the **bundled mover versions** (Restic/Rclone/Syncthing/rsync-tls) in older images. Older releases carried older Restic/Rclone with their own CVEs and weaker TLS defaults (the TLS-1.3 floor only arrived in 0.16.0). For older clusters, upgrade to pull patched movers and the stricter rsync-tls profile.

## References

- `Chart.yaml`, v0.15.0 release notes (above); VolSync install docs.
- Catalog: [[CONCEPT-ADDON_CATALOG]]; snapshots: [[COMPONENT-SNAPSHOT_CONTROLLER]].
