---
id: PRACTICE-RUNBOOK_ETCD_BACKUP
type: best_practice
title: "Runbook: take and verify an etcd snapshot (scheduled backup)"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - etcd backup runbook
  - etcd snapshot save
  - scheduled etcd backup
  - back up kubernetes cluster state
  - etcd snapshot verify
tags:
  - runbook
  - operations
  - etcd
  - backup
sources:
  - type: docs
    path: docs/operations/etcd.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/operations/etcd.md
    note: "etcdctl snapshot save; etcdutl snapshot status; member coordination"
relations:
  - type: part_of
    target: CONCEPT-RUNBOOKS_INDEX
  - type: depends_on
    target: PRACTICE-ETCD_BACKUP_RESTORE
  - type: see_also
    target: PRACTICE-RUNBOOK_ETCD_RESTORE
  - type: see_also
    target: COMPONENT-ETCD
  - type: see_also
    target: TAG-ETCDCTL
---

# Runbook: take and verify an etcd snapshot (scheduled backup)

## Summary

etcd **is** the cluster state, so a verified, off-node etcd snapshot is the rollback anchor every
other runbook depends on ([[CONCEPT-RUNBOOKS_INDEX]] spine, step 3). This is the routine procedure —
take → **verify** → move off-node → retain — meant to run on a schedule, not just before risky ops.
An unverified or on-node-only snapshot is not a backup. Mechanics: [[PRACTICE-ETCD_BACKUP_RESTORE]];
this runbook is the operational discipline around them.

## Context

- **Take it from an etcd member**, with that member's client certs. One healthy member's snapshot is
  a complete cluster state — you don't need all members.
- **Verify every snapshot** — a save that "succeeded" can still be truncated/corrupt; `etcdutl
  snapshot status` is the cheap proof.
- **Off-node is mandatory.** A snapshot sitting on the node whose disk you're trying to survive is
  not a backup. Store it with the **matching PKI** — a snapshot without its CA can't rebuild a
  cluster.
- **Restore pairs with this** — a backup you've never test-restored is a hope, not a plan
  ([[PRACTICE-RUNBOOK_ETCD_RESTORE]]). Stable across **v2.27.0–v2.31.0**.

## Implementation

**Step 1 — Point etcdctl at the local member** ([[TAG-ETCDCTL]]):

```bash
export ETCDCTL_API=3
export ETCDCTL_CACERT=/etc/ssl/etcd/ssl/ca.pem
export ETCDCTL_CERT=/etc/ssl/etcd/ssl/admin-$(hostname).pem
export ETCDCTL_KEY=/etc/ssl/etcd/ssl/admin-$(hostname)-key.pem
export ETCDCTL_ENDPOINTS=https://127.0.0.1:2379
etcdctl endpoint health          # only snapshot a healthy member
```

**Step 2 — Take the snapshot:**

```bash
SNAP=/var/backups/etcd-$(date +%F-%H%M).db
etcdctl snapshot save "$SNAP"
```

**Step 3 — Verify it** (never skip — this is what makes it a backup):

```bash
etcdutl snapshot status "$SNAP" --write-out=table   # revision, total keys, hash, size
```

A snapshot that won't `status` cleanly is corrupt — re-take it.

**Step 4 — Move off-node and retain:** copy `$SNAP` to remote/object storage **with the cluster
PKI** (`/etc/ssl/etcd/ssl/`); apply a retention policy (e.g. hourly×24, daily×7, weekly×4). Automate
Steps 1–4 as a cron/systemd timer on an etcd node.

**Step 5 — Periodically test-restore** into a throwaway environment
([[PRACTICE-RUNBOOK_ETCD_RESTORE]]) — an untested backup is unproven.

**Rollback.** N/A — a backup is non-destructive. The failure mode is a **useless** backup
(unverified, on-node, or PKI-less); Steps 3–5 exist to prevent exactly that.

## References

- `docs/operations/etcd.md` (tag `v2.31.0`). Restore counterpart
  [[PRACTICE-RUNBOOK_ETCD_RESTORE]]; mechanics [[PRACTICE-ETCD_BACKUP_RESTORE]]; component
  [[COMPONENT-ETCD]]; index [[CONCEPT-RUNBOOKS_INDEX]].
