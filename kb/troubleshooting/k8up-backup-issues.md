---
id: TROUBLE-K8UP_BACKUP_ISSUES
type: troubleshooting
title: "k8up: stale restic locks, false success, permission/empty backups"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: ">=2.12.0 <=2.15.0"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - k8up repository already locked
  - restic unlock k8up
  - k8up backup succeeded but failed
  - k8up rwo volume node affinity conflict
  - k8up empty snapshot permission denied
tags:
  - troubleshooting
  - k8up
  - backup
  - restic
sources:
  - type: docs
    path: k8up RWO backup explanation
    url: https://docs.k8up.io/k8up/2.11/explanations/rwo.html
    note: "RWO backup pod scheduled onto the app's node"
  - type: docs
    path: k8up issue #547 (stale locks / stuck sidecar)
    url: https://github.com/k8up-io/k8up/issues/547
    note: "restic lock + sidecar not exiting"
relations:
  - type: see_also
    target: CONCEPT-ADDON_K8UP
---

# k8up: stale restic locks, false success, permission/empty backups

## Summary

Community-sourced k8up failure modes: **stale restic repository locks** blocking
backup/prune/check, a **failed backup reported as succeeded**, **permission/empty** backups on
non-root workloads, and **RWO PVC** backup pods stuck Pending. Most trace to the restic
backend or pod scheduling/permissions.

## Problem

- `unable to create lock in backend: repository is already locked exclusively by PID <n>`.
- Backup pod stuck `1/2 Ready` though logs say "finished successfully".
- Backup marked `Succeeded` while logs show `exit code 1 / source file could not be read`.
- Backup pod `Pending`: `node(s) had volume node affinity conflict`.
- Snapshot created but empty / `Permission denied` on the app's mount afterwards.

## Context

- Applies to k8up app **2.12–2.15** (owner runs chart 4.8.4 / app 2.12.0 —
  [[CONCEPT-ADDON_K8UP]]).

## Diagnostics

- **Stale lock:** an interrupted op (pod kill/OOM/reboot/network drop) leaves a lock. Run
  `restic unlock` (add `--remove-all` for exclusive locks). Ensure **one schedule per repo**
  and that prune/check don't overlap backups (issue #547, restic #926).
- **False "Succeeded":** older status logic didn't propagate restic's non-zero exit (fixed in
  PR #1027) — verify actual restic exit in the job logs, upgrade.
- **RWO PVC Pending:** k8up schedules the backup pod onto the **same node** as the app pod
  holding the RWO volume (via `k8up.io/hostname` + PV NodeAffinity). It breaks if the app pod
  moved or the node is cordoned — keep the app pod running during the backup window (issue
  #319).
- **Empty/permission backup:** the backup runs with a different UID than the workload and
  can't read a `770`/non-root data dir — align `securityContext`/`fsGroup`/supplemental group;
  verify with `restic ls` (issues #779/#912).
- **S3 errors** (`401`, `301 Moved Permanently`, `Access Denied`, clock-skew): check
  `backend.s3.endpoint`/region/bucket, both Secret refs, `repoPasswordSecretRef`, repo init,
  and NTP.

## Known Issues

- **CRDs are not installed by the chart** — install/upgrade them separately (the `k8upcrd`
  chart).
- **Future landmine:** k8up **4.9.0** switches pod-exec SPDY→WebSocket (app-aware backups) —
  set `INSECURE_ALLOW_PODEXEC_SPDY_FALLBACK=true` if needed (PR #1183).

## References

- k8up RWO docs, issue #547 (above); issues #319/#779/#912/#910, PR #1027.
- Addon: [[CONCEPT-ADDON_K8UP]].
