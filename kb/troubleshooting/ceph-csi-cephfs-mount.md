---
id: TROUBLE-CEPH_CSI_CEPHFS_MOUNT
type: troubleshooting
title: "ceph-csi-cephfs: PVC Pending / mount fails — clusterID mismatch, secret, MDS, subvolumegroup"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.32"
component_version: ">=3.13.0 <=3.14.2"
verified_at: "2026-07-19"
confidence: confirmed
aliases:
  - cephfs pvc pending
  - ceph-csi mount failed
  - no mds server available
  - cephfs clusterID mismatch
  - subvolumegroup not found
tags:
  - troubleshooting
  - storage
  - ceph
  - csi
sources:
  - type: external
    path: ceph-csi cephfs troubleshooting
    url: https://github.com/ceph/ceph-csi/blob/v3.14.2/docs/deploy-cephfs.md
    note: "clusterID must match the csi ConfigMap; adminID/adminKey secret; subvolumegroup; MDS/Ceph health"
relations:
  - type: see_also
    target: CONCEPT-ADDON_CEPH_CSI_CEPHFS
  - type: see_also
    target: CONCEPT-CSI_LAYER
  - type: see_also
    target: TROUBLE-PVC_PENDING_NO_PROVISIONER
---

# ceph-csi-cephfs: PVC Pending / mount fails — clusterID mismatch, secret, MDS, subvolumegroup

## Summary

A CephFS PVC won't provision or a pod won't mount — almost always a **clusterID mismatch**, a bad **cephx secret**, a missing **subvolumegroup**, or a **down MDS** on the Ceph side. The driver pod looks fine; the failure is in the Ceph coordinates it was handed.

## Problem

- A CephFS PVC stays `Pending` (no volume provisioned), or the pod fails to mount with
  `MountVolume.MountDevice failed`, `no mds server is up` / `clusterID <x> not found`, or
  `subvolumegroup ... does not exist`.

## Context

- ceph-csi-cephfs `3.13.0`/`3.14.2` ([[CONCEPT-ADDON_CEPH_CSI_CEPHFS]]); requires Ceph Pacific
  (≥16.2.0) with a healthy MDS. It's a CSI external provisioner ([[CONCEPT-CSI_LAYER]]).
- **clusterID** in the StorageClass must match the `clusterID` → `monitors` entry in the ceph-csi
  **ConfigMap** (`ceph-csi-config`). A copy-pasted SC with the wrong/blank clusterID is the #1 cause.
- The provisioner/node plugins authenticate with the **csi-cephfs-secret** (`adminID`/`adminKey`, or
  `userID`/`userKey`). Wrong/rotated keys → auth errors.
- CephFS needs an existing **subvolumegroup** (default `csi`); the driver won't create the group
  itself in all setups.
- A CephFS mount needs a reachable **MDS**; if the Ceph cluster's MDS is down/failed over, mounts hang.

## Diagnostics

```bash
kubectl -n <ns> describe pvc <pvc>                       # provisioning events
kubectl -n ceph-csi logs deploy/ceph-csi-cephfs-provisioner -c csi-cephfsplugin | tail
kubectl -n ceph-csi get cm ceph-csi-config -o yaml       # clusterID <-> monitors
# on a Ceph mon:
ceph -s ; ceph fs status                                 # HEALTH, MDS up? fs active?
ceph fs subvolumegroup ls <fsname>                       # does the group exist?
```

## Known Issues

- **clusterID mismatch — fix:** align the StorageClass `clusterID` with the `ceph-csi-config`
  ConfigMap entry; the value is the Ceph **fsid** (`ceph fsid`), not an arbitrary name.
- **auth — fix:** recreate `csi-cephfs-secret` with a valid `adminID`/`adminKey` (a cephx user with
  the right caps on the fs/pool); rotated keys must be updated in the secret.
- **subvolumegroup — fix:** create it (`ceph fs subvolumegroup create <fs> csi`) or point the SC at an
  existing group.
- **MDS/health — fix:** restore MDS (`ceph fs status`); mounts resume once an MDS is active. A degraded
  Ceph cluster ([[CONCEPT-ADDON_CEPH_CSI_CEPHFS]] backs onto Rook/external Ceph) blocks provisioning.
- **Stale mounts after node reboot:** delete the stuck volumeattachment / restart the node plugin pod
  so the driver re-establishes the mount.

## References

- ceph-csi `deploy-cephfs.md` (v3.14.2). Addon [[CONCEPT-ADDON_CEPH_CSI_CEPHFS]]; CSI layer
  [[CONCEPT-CSI_LAYER]]; generic provisioning [[TROUBLE-PVC_PENDING_NO_PROVISIONER]].
