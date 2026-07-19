---
id: PRACTICE-RUNBOOK_ETCD_RESTORE
type: best_practice
title: "Runbook: restore control-plane state from an etcd snapshot"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - etcd restore runbook
  - restore from etcd snapshot
  - disaster recovery kubernetes
  - recover-control-plane.yml
  - etcd snapshot restore procedure
  - control plane rebuild
tags:
  - runbook
  - operations
  - etcd
  - disaster-recovery
sources:
  - type: docs
    path: docs/operations/recover-control-plane.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/operations/recover-control-plane.md
    note: "broken_etcd / broken_kube_control_plane groups; recover-control-plane.yml --limit etcd,kube_control_plane"
  - type: docs
    path: docs/operations/etcd.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/operations/etcd.md
    note: "etcdctl/etcdutl snapshot save/status/restore; member coordination"
relations:
  - type: part_of
    target: CONCEPT-RUNBOOKS_INDEX
  - type: depends_on
    target: PRACTICE-ETCD_BACKUP_RESTORE
  - type: see_also
    target: PRACTICE-RECOVER_CONTROL_PLANE
  - type: see_also
    target: COMPONENT-ETCD
  - type: see_also
    target: PRACTICE-CLUSTER_HEALTH_CHECKS
---

# Runbook: restore control-plane state from an etcd snapshot

## Summary

The ordered procedure to bring a cluster back after **etcd / control-plane loss**, using a snapshot
taken by [[PRACTICE-ETCD_BACKUP_RESTORE]]. etcd **is** the cluster state — restoring it restores every
object. Two paths: for a partially-degraded control plane, prefer Kubespray's
`recover-control-plane.yml` ([[PRACTICE-RECOVER_CONTROL_PLANE]]), which rebuilds etcd membership; a
manual `etcdutl snapshot restore` is the last resort and must be coordinated across all members to
avoid split-brain. Follow the [[CONCEPT-RUNBOOKS_INDEX]] spine — and here **the snapshot is the
rollback anchor**, so protect it.

## Context

- **⚠ Service impact — control-plane outage.** A **full snapshot restore** takes the **API server /
  control plane DOWN** for its duration: no `kubectl`, no scheduling, no new pods, controllers stop
  reconciling — and on completion the **whole cluster state is rewound to snapshot time** (objects
  created after it vanish). **Running workloads keep running** (kubelet + CNI operate without the API),
  so it's primarily a **control-plane** outage, not automatically a data-plane one — but anything that
  needs the API (scaling, new pods, LB/ingress reconciliation) is stalled until recovery. The
  **recover-control-plane path** (surviving majority) is much lighter: it replaces dead members without
  rewinding state — a brief control-plane blip, not a full rollback. Treat a full restore as a **major
  incident recovery** with a comms plan, not a routine change.
- **Restore ≠ per-object recovery.** This rewinds the **whole cluster** to snapshot time — anything
  created after the snapshot is gone. If you only lost one object, recover that object, not etcd.
- **Quorum decides the path.** Surviving-majority etcd → replace the dead members with
  `recover-control-plane.yml` (no full restore needed). Lost majority / total loss → restore from
  snapshot.
- **Cert paths** follow the host etcd deployment (`/etc/ssl/etcd/ssl/…`); the snapshot must be paired
  with the **matching PKI** — a snapshot without its CA/certs cannot form a working cluster.
- Stable across **v2.27.0–v2.31.0**; etcd `3.5.x`/`3.6.x` ([[COMPONENT-ETCD]]). `etcdctl` for
  save/health, `etcdutl` for offline snapshot status/restore.

## Implementation

**Step 0 — Confirm the failure mode** (don't restore a cluster that only needs a member replaced):

```bash
export ETCDCTL_API=3
export ETCDCTL_CACERT=/etc/ssl/etcd/ssl/ca.pem
export ETCDCTL_CERT=/etc/ssl/etcd/ssl/admin-$(hostname).pem
export ETCDCTL_KEY=/etc/ssl/etcd/ssl/admin-$(hostname)-key.pem
export ETCDCTL_ENDPOINTS=https://127.0.0.1:2379
etcdctl endpoint health; etcdctl member list --write-out=table
```

- **Majority alive** → skip to Step 2 (member replacement). **Majority lost** → Step 1 (restore).

**Step 1 — Locate and validate the snapshot** (never restore an unverified file):

```bash
etcdutl snapshot status /var/backups/etcd-<date>.db --write-out=table   # revision, hash, size
```

**Step 2 — Rebuild via Kubespray** (the supported path — [[PRACTICE-RECOVER_CONTROL_PLANE]]):

1. Provision replacements for dead nodes.
2. Put broken members in `broken_etcd` (set `etcd_member_name` each) and broken control-plane nodes
   in `broken_kube_control_plane`.
3. In the `etcd` and `kube_control_plane` groups list **surviving nodes first**, then the new ones.
4. Run limited to those groups, with generous etcd retries:

```bash
ansible-playbook -i inventory/<cluster>/hosts.yaml kubespray/recover-control-plane.yml \
  --limit etcd,kube_control_plane -e etcd_retries=10
```

Increase `etcd_retries` if recovery stalls — the required count is hard to predict.

**Step 3 — Manual snapshot restore** (only if Step 2 can't apply — total etcd loss): restore into a
**fresh** data dir on **each** member with matching `--name` / `--initial-cluster` /
`--initial-advertise-peer-urls`, then start etcd pointing at the new dir. All members must restore
from the **same** snapshot with a consistent initial-cluster token or you get split-brain.

**Step 4 — Verify** ([[PRACTICE-CLUSTER_HEALTH_CHECKS]]): `etcdctl endpoint status` shows one leader
and all members with the same raft index; API server serves; nodes report `Ready`; a smoke workload
schedules. Expect objects created after the snapshot to be **absent** — reconcile from GitOps/source
of truth.

**Rollback.** Recovery is itself the rollback for control-plane loss; there is no rollback *of* a
restore beyond **keeping the original snapshot untouched**. Always restore from a **copy** so a
failed attempt can be retried against the pristine snapshot.

## References

- `docs/operations/recover-control-plane.md`, `docs/operations/etcd.md` (tag `v2.31.0`). Backup
  source: [[PRACTICE-ETCD_BACKUP_RESTORE]]; Kubespray recovery: [[PRACTICE-RECOVER_CONTROL_PLANE]];
  component: [[COMPONENT-ETCD]]; index: [[CONCEPT-RUNBOOKS_INDEX]].
