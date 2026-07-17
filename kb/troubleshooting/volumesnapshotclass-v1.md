---
id: TROUBLE-VOLUMESNAPSHOTCLASS_V1
type: troubleshooting
title: "snapshot-controller: VolumeSnapshotClass still on a pre-v1 API"
status: active
kubespray_version: ">=v2.29.0 <=v2.30.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - volumesnapshotclass-v1
tags:
  - troubleshooting
sources:
  - type: pull_request
    url: https://github.com/kubernetes-sigs/kubespray/pull/12775
    note: "fix merged in v2.31.0 (PR #12775)"
  - type: code
    path: roles/kubernetes-apps
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps
    note: "fixed file"
relations:
  - type: see_also
    target: CONCEPT-CSI_LAYER
---

# snapshot-controller: VolumeSnapshotClass still on a pre-v1 API

## Summary

The snapshot-controller add-on used an older VolumeSnapshotClass API version, which fails on clusters where only `snapshot.storage.k8s.io/v1` is served. Fixed in **v2.31.0** (PR #12775).

## Problem

Kubespray's VolumeSnapshotClass manifest was updated to `v1`; the older version could be rejected by the API server on current Kubernetes.

## Context

- Affected Kubespray: `>=v2.29.0 <=v2.30.0`. Fixed in: `v2.31.0`.
- Confirmed via the merged PR #12775 and the tag code.

## Diagnostics

```bash
kubectl get volumesnapshotclass -o yaml | grep apiVersion
kubectl api-resources | grep volumesnapshot
```

## Known Issues

Root cause fixed by PR #12775 (in `roles/kubernetes-apps`). Workaround before upgrading: apply your VolumeSnapshotClass as `snapshot.storage.k8s.io/v1`, or upgrade to v2.31.0. The
durable fix is to upgrade to `v2.31.0` or later.

## References

- PR https://github.com/kubernetes-sigs/kubespray/pull/12775 — fixed in `v2.31.0`.
- `roles/kubernetes-apps`.
