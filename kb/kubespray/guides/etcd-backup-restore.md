---
id: PRACTICE-ETCD_BACKUP_RESTORE
type: best_practice
title: etcd health, backup and restore (day-2 runbook)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-20"
confidence: verified
aliases:
  - etcd backup
  - etcd restore
  - etcdctl snapshot
  - etcd health
tags:
  - operations
  - etcd
  - diagnostics
sources:
  - type: docs
    path: docs/operations/etcd.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/operations/etcd.md
    note: "etcd operations; etcdctl/etcdutl installed by the etcdctl tag"
  - type: code
    path: roles/recover_control_plane/etcd/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.29.0/roles/recover_control_plane/etcd/tasks/main.yml
    note: "restore path checks quorum, removes the etcd data dir and rebuilds membership on etcd[0] — evidence for the restore disruption profile"
relations:
  - type: see_also
    target: COMPONENT-ETCD
  - type: see_also
    target: TAG-ETCDCTL
  - type: see_also
    target: PRACTICE-RECOVER_CONTROL_PLANE
---

# etcd health, backup and restore (day-2 runbook)

## Summary

etcd is the cluster's source of truth; losing it loses the cluster. This runbook
covers checking etcd health, taking snapshots, and restoring. Kubespray installs
`etcdctl`/`etcdutl` on etcd/control-plane nodes (see [[TAG-ETCDCTL]]); in the
default `host` deployment ([[VARIABLE-ETCD_DEPLOYMENT_TYPE]]) etcd runs as a
systemd service.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`; etcd `3.5.x`/`3.6.x` (see
  [[COMPONENT-ETCD]]).
- Run on an etcd node. The env vars below point etcdctl at the local member with
  its client certs (paths from the etcd deployment).

## Diagnostics

```bash
export ETCDCTL_API=3
export ETCDCTL_CACERT=/etc/ssl/etcd/ssl/ca.pem
export ETCDCTL_CERT=/etc/ssl/etcd/ssl/admin-$(hostname).pem
export ETCDCTL_KEY=/etc/ssl/etcd/ssl/admin-$(hostname)-key.pem
export ETCDCTL_ENDPOINTS=https://127.0.0.1:2379

etcdctl endpoint health                 # is this member healthy?
etcdctl endpoint status --write-out=table   # leader, db size, raft index
etcdctl member list --write-out=table   # all members present/started?
```

If the DB is large or slow, defragment (one member at a time):

```bash
etcdctl defrag
```

## Implementation

**Backup (snapshot):**

```bash
etcdctl snapshot save /var/backups/etcd-$(date +%F).db
etcdutl snapshot status /var/backups/etcd-$(date +%F).db --write-out=table
```

Automate snapshots off-node; keep them with the cluster's PKI.

**Restore:** for a degraded control plane, prefer Kubespray's
`recover-control-plane.yml` ([[PRACTICE-RECOVER_CONTROL_PLANE]]), which rebuilds
etcd membership. For a manual single-node restore, `etcdutl snapshot restore`
into a fresh data dir, then start etcd pointing at it — but coordinate across all
members to avoid split-brain.

## Service impact

The three tasks span the full disruption range:

- **Diagnostics + snapshot save: safe, non-disruptive.** `endpoint health/status`,
  `member list`, and `snapshot save` are **read-only** — run them anytime, including
  on a healthy production cluster. A snapshot adds only brief disk/CPU I/O; take it
  **before** any risky change.
- **`defrag`: brief per-member stall.** Defragmentation **blocks the member it runs
  on** while it rewrites the DB, so run it **one member at a time** and off-peak;
  with quorum intact the cluster stays available through it.
- **Restore: control-plane outage + data rewind — incident recovery, not routine.**
  Restoring rolls etcd back to the snapshot's point in time, so **everything
  created or changed after the snapshot is lost**. `recover-control-plane.yml`
  (verified: `roles/recover_control_plane/etcd`) checks quorum, **removes the etcd
  data dir**, and **rebuilds membership on `etcd[0]`** — expect **API unavailability**
  (no `kubectl`, scheduling stalls) while etcd is rebuilt and restarted. Running
  workloads keep running (kubelet + CNI operate without the API), but objects that
  existed only after the snapshot **vanish**. A manual `etcdutl snapshot restore`
  must be coordinated across **all** members or you get split-brain.

## References

- `docs/operations/etcd.md`; standard `etcdctl`/`etcdutl` (installed via
  [[TAG-ETCDCTL]]).
- Cert paths follow the `host` etcd deployment.
