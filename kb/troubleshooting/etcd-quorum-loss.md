---
id: TROUBLE-ETCD_QUORUM_LOSS
type: troubleshooting
title: etcd quorum loss — API server down, cluster read-only/unavailable
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - etcd quorum lost
  - lost quorum
  - etcd majority down
  - apiserver etcd unavailable
  - recover control plane etcd
tags:
  - troubleshooting
  - etcd
  - control-plane
  - disaster-recovery
sources:
  - type: docs
    path: docs/operations/recover-control-plane.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/operations/recover-control-plane.md
    note: "Kubespray recover-control-plane runbook incl. lost-quorum restore (tag v2.31.0)"
  - type: code
    path: playbooks/recover_control_plane.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/recover_control_plane.yml
    note: "recovery playbook (tag v2.31.0)"
relations:
  - type: see_also
    target: PLAYBOOK-RECOVER_CONTROL_PLANE
  - type: see_also
    target: PRACTICE-ETCD_BACKUP_RESTORE
  - type: see_also
    target: TROUBLE-ETCD_DB_SPACE_EXCEEDED
---

# etcd quorum loss — API server down, cluster read-only/unavailable

## Summary

etcd needs a **majority** of members healthy to serve writes (2 of 3, 3 of 5). Lose
the majority and etcd stops accepting writes — the API server errors and the cluster
becomes effectively read-only or unavailable. Kubespray recovers this with the
**`recover-control-plane.yml`** playbook, which detects lost quorum and restores from a
snapshot. This is a disaster-recovery scenario: know the steps before you need them.

## Problem

kube-apiserver returns errors like `etcdserver: request timed out` /
`context deadline exceeded`; `kubectl` hangs or fails; one or more control-plane nodes
are down. With a majority of etcd members gone, quorum is lost.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0` (stacked or external etcd).
- Quorum math: a cluster of `N` members tolerates `floor((N-1)/2)` failures — 3 members
  tolerate 1, 5 tolerate 2. An even member count gives no extra tolerance, so run an
  **odd** number.
- Losing quorum is recoverable **only from a snapshot** if you can't bring members back
  — hence a working etcd backup is mandatory ([[PRACTICE-ETCD_BACKUP_RESTORE]]).

## Diagnostics

From a control-plane node (use the etcd client env / certs — see the `etcdctl` tag):

- Member health: `etcdctl endpoint health --cluster` — shows which members are
  unhealthy.
- Member status: `etcdctl endpoint status --cluster -w table` — leader, DB size, raft
  term/index per member.
- Member list: `etcdctl member list -w table` — expected vs actual members.
- Count healthy members and compare to the majority threshold. If fewer than
  `ceil((N+1)/2)` are healthy, quorum is lost.

## Known Issues

**Recovery with Kubespray (`recover-control-plane.yml`):**

1. Provision new nodes to replace the broken ones.
2. Put broken etcd hosts in a **`broken_etcd`** group (set `etcd_member_name` for each);
   put broken control-plane hosts in **`broken_kube_control_plane`**.
3. Run: `ansible-playbook -i inventory/.../hosts.yaml recover-control-plane.yml
   --limit etcd,kube_control_plane -e etcd_retries=10` (raise `etcd_retries` further if
   needed — the required count is hard to predict).
4. **Lost quorum:** the playbook detects it and takes a snapshot from the **first** node
   in the `etcd` group, then restores from it. To restore from a specific snapshot set
   `-e etcd_snapshot=/tmp/etcd_snapshot`.

**Caveats:**

- **Rehearse first.** Break a *clone* of your cluster the same way and practice the
  recovery before touching production — restore rewinds etcd to snapshot time, losing
  any writes since.
- Prefer restoring members over full snapshot-restore when you still have one good
  member — bringing a member back preserves more recent state than an older snapshot.
- Keep an **odd** member count and off-node snapshots; a single-member etcd has zero
  fault tolerance.
- Distinct from `mvcc: database space exceeded` (writes blocked but quorum intact) —
  that is defrag/alarm-disarm, not restore ([[TROUBLE-ETCD_DB_SPACE_EXCEEDED]]).

## References

- `docs/operations/recover-control-plane.md` and `recover-control-plane.yml` at tag
  `v2.31.0`; playbook doc [[PLAYBOOK-RECOVER_CONTROL_PLANE]]; backups
  [[PRACTICE-ETCD_BACKUP_RESTORE]].
