---
id: TROUBLE-VOLSYNC_MOVER_ISSUES
type: troubleshooting
title: "VolSync: mover retries on lock, AZ affinity, SCC/xattr, cache full"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: ">=0.15.0 <=0.16.0"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - volsync restic locked retry loop
  - volsync volume node affinity conflict
  - volsync setgid failed privileged movers
  - volsync cache pvc enospc
  - volsync restore selinux xattr
tags:
  - troubleshooting
  - volsync
  - storage
  - backup
sources:
  - type: docs
    path: VolSync permission model
    url: https://volsync.readthedocs.io/en/stable/usage/permissionmodel.html
    note: "privileged vs unprivileged movers, xattr/SELinux"
  - type: docs
    path: VolSync issue #1429 (restic lock retry)
    url: https://github.com/backube/volsync/issues/1429
    note: "restic exit 11 handled via podFailurePolicy"
relations:
  - type: see_also
    target: CONCEPT-ADDON_VOLSYNC
  - type: see_also
    target: TROUBLE-MULTIPLE_SNAPSHOT_CONTROLLERS
---

# VolSync: mover retries on lock, AZ affinity, SCC/xattr, cache full

## Summary

Community-sourced VolSync mover failures: the **restic mover retries indefinitely** on a
locked repo, mover/cache pods are **unschedulable across zones**, restore fails on **restricted
SCC/SELinux xattr**, or the **restic cache PVC fills up**. Most are permission-model or
snapshot-dependency issues.

## Problem

- Restic mover job retries forever when the repo is locked.
- Mover/cache pod `Pending`: `node(s) had volume node affinity conflict`.
- Rsync mover fails `@ERROR: setgid failed` (exit 5).
- Restore fails writing xattrs on OpenShift restricted SCC.
- Cache PVC hits `ENOSPC` with no warning.

## Context

- Applies to VolSync **0.15–0.16** (owner runs 0.15.0 — [[CONCEPT-ADDON_VOLSYNC]]). Depends on
  CSI snapshots — see [[TROUBLE-MULTIPLE_SNAPSHOT_CONTROLLERS]].

## Diagnostics

- **Locked repo retry loop:** VolSync historically treated restic exit **11** ("already
  locked") as generic-retryable — let the cycle exhaust retries (auto-unlock next run) or
  `restic unlock`. The fix uses `podFailurePolicy: FailJob` on exit 11 (needs restic ≥0.17.0,
  K8s ≥1.31) (issue #1429).
- **Multi-AZ affinity conflict:** the source snapshot/clone PVC and the restic **cache** PVC
  land in different zones. Use a StorageClass with **`volumeBindingMode: WaitForFirstConsumer`**
  or regional disks (issue #1329).
- **`setgid failed` / restricted movers:** the mover lacks `CAP_SETGID` under a hardened SCC.
  Annotate the namespace **`volsync.backube/privileged-movers=true`** or align
  `moverSecurityContext` (issue #728).
- **SELinux/xattr on restore:** restic ≥0.17 restores xattrs, which needs `CAP_SYS_ADMIN`;
  `security.selinux` xattrs can't be rewritten under OpenShift restricted SCC — use privileged
  movers (SELinux xattrs still blocked) (restic #5089).
- **Cache full:** raise `spec.restic.cacheCapacity` (users report 1–15Gi for large repos)
  (issue #1159).
- **copyMethod Snapshot:** set a `volumeSnapshotClassName` matching the PVC's CSI driver, else
  use `copyMethod: Direct`.

## Known Issues

- **0.15.0 removed the `kube-rbac-proxy` sidecar** — ServiceMonitor/metrics-auth setups may
  need adjustment.

## References

- VolSync permission model + issue #1429 (above); issues #1329/#728/#1159, restic #5089.
- Addon: [[CONCEPT-ADDON_VOLSYNC]]; snapshots: [[TROUBLE-MULTIPLE_SNAPSHOT_CONTROLLERS]].
