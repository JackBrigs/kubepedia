---
id: TROUBLE-SNAPSHOT_CONTROLLER_2_1_DEFECTS
type: troubleshooting
title: "snapshot-controller 2.1: defects fixed in the 2.1 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.1.0 <2.2.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - snapshot-controller 2.1 known issues
  - snapshot-controller 2.1 fixed in
  - is this snapshot-controller bug already fixed
tags:
  - troubleshooting
  - upgrade
  - snapshot-controller
sources:
  - type: docs
    path: kubernetes-csi/external-snapshotter release notes for the 2.1 line — bug-fix entries
    url: https://github.com/kubernetes-csi/external-snapshotter/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# snapshot-controller 2.1: defects fixed in the 2.1 line

## Summary

**8 defects** the project fixed across **4 releases** of the 2.1 line, from 2.1.0 to
2.1.5. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.1.0

- Fixes a problem of not removing the PVC finalizer when it is no longer used by a snapshot as source. ([#283](https://github.com/kubernetes-csi/external-snapshotter/pull/283), [@xing-yang](https://github.com/xing-yang))
- Fixes a problem deleting VolumeSnapshotContent with `Retain` policy for pre-provisioned snapshots. ([#249](https://github.com/kubernetes-csi/external-snapshotter/pull/249), [@xing-yang](https://github.com/xing-yang))
- Fixes a create snapshot timeout issue. ([#261](https://github.com/kubernetes-csi/external-snapshotter/pull/261), [@xing-yang](https://github.com/xing-yang))

### 2.1.1

- Cherry pick PR #293: Fixes issue #290. Disallow a pre-provisioned VolumeSnapshot pointing to a dynamically created VolumeSnapshotContent. ([#303](https://github.com/kubernetes-csi/external-snapshotter/pull/303), [@yuxiangqian](https://github.com/yuxiangqian))
- Cherry pick PR #293: Fixes issue #291. Verify VolumeSnapshot and VolumeSnapshotContent are bi-directional bound before initializing a deletion on a VolumeSnapshotContent which the to-be-deleted VolumeSnapshot points to. ([#303](https://github.com/kubernetes-csi/external-snapshotter/pull/303), [@yuxiangqian](https://github.com/yuxiangqian))
- Cherry pick PR #293: Fixes issue #292. Allow deletion of a VolumeSnapshot when the VolumeSnapshotContent's DeletionPolicy has been updated from Delete to Retain. ([#303](https://github.com/kubernetes-csi/external-snapshotter/pull/303), [@yuxiangqian](https://github.com/yuxiangqian))

### 2.1.3

- Backports fix #381 for crashloop when there are errors in the VolumeSnapshot, like a missing VolumeSnapshotClass. ([#446](https://github.com/kubernetes-csi/external-snapshotter/pull/446), [@mattcary](https://github.com/mattcary))

### 2.1.5

- Cherry pick of [#413](https://github.com/kubernetes-csi/external-snapshotter/pull/413): Bug fix to allow creation of snapshot content if pvc finalizer exists, even if pvc is marked for deletion. ([#488](https://github.com/kubernetes-csi/external-snapshotter/pull/488), [@mattcary](https://github.com/mattcary))


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.1.5**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `kubernetes-csi/external-snapshotter`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/snapshot-controller.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
