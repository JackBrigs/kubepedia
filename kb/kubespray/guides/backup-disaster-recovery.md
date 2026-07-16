---
id: PRACTICE-BACKUP_DR
type: best_practice
title: "Backup & disaster recovery strategy"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - backup
  - disaster recovery
  - DR
  - what to back up kubernetes
  - restore cluster
  - RPO RTO
tags:
  - operations
  - backup
  - disaster-recovery
  - best-practice
sources:
  - type: docs
    path: docs/operations/recover-control-plane.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/operations/recover-control-plane.md
    note: "recovery flows incl. lost-quorum snapshot restore (tag v2.31.0)"
relations:
  - type: see_also
    target: PRACTICE-ETCD_BACKUP_RESTORE
  - type: see_also
    target: PRACTICE-RECOVER_CONTROL_PLANE
  - type: see_also
    target: TROUBLE-ETCD_QUORUM_LOSS
---

# Backup & disaster recovery strategy

## Summary

The cluster's recoverability rests on **three** things: **etcd** (all API objects), the
**PKI** (the CA and certs), and your **inventory** (config-as-code). Back up all three and
most disasters are recoverable; miss etcd and the cluster state is gone. This ties the
individual runbooks into one strategy: what to save, and which recovery path fits which
failure.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`.
- Kubernetes stores **all** cluster state in **etcd** — losing it without a snapshot means
  rebuilding every object. Workload manifests should additionally live in Git (GitOps) so
  applications are re-appliable independently of etcd.

## Implementation

**What to back up (and how):**

- **etcd snapshots** — the crown jewels. Take regular `etcdctl snapshot save` backups and
  copy them **off the node**; snapshot frequency = your RPO ([[PRACTICE-ETCD_BACKUP_RESTORE]]).
- **PKI** — `/etc/kubernetes/ssl` (the CA + certs). Preserving the **CA** lets a rebuilt
  cluster keep the same trust root and existing kubeconfigs ([[CONCEPT-CLUSTER_PKI]]).
- **Inventory** — your `inventory/<cluster>/` (hosts + group_vars) in Git; it's the recipe
  to rebuild identical nodes.
- **Workloads** — in Git (Helm/manifests) so they re-apply onto a restored control plane.

**Recovery paths by failure:**

- **One control-plane node broken, quorum intact** → provision a replacement and re-add;
  no restore needed ([[PRACTICE-RECOVER_CONTROL_PLANE]]).
- **etcd quorum lost** → restore from an etcd snapshot; Kubespray's
  `recover-control-plane.yml` does this (auto or `-e etcd_snapshot=…`)
  ([[TROUBLE-ETCD_QUORUM_LOSS]]).
- **Full cluster loss** → rebuild from inventory, restore etcd from snapshot, restore the
  PKI/CA (or regenerate and re-issue kubeconfigs), then re-apply workloads from Git.

## Compatibility

- **Rehearse restores** on a throwaway clone — an untested backup is a hope, not a plan
  (restore rewinds etcd to snapshot time, losing changes since).
- **Off-node, off-cluster** storage for snapshots and the CA — a backup on the failed node
  is worthless.
- **etcd 3.6** (Kubernetes 1.35) adds downgrade tooling but the backup/restore discipline
  is unchanged ([[CONCEPT-ETCD_3_6_CHANGES]]).
- Match snapshot cadence to your **RPO**; match rebuild automation (inventory-in-Git) to
  your **RTO** — a cluster you can `cluster.yml` from scratch recovers far faster.

## References

- `docs/operations/recover-control-plane.md` at tag `v2.31.0`. etcd backup:
  [[PRACTICE-ETCD_BACKUP_RESTORE]]; quorum loss: [[TROUBLE-ETCD_QUORUM_LOSS]]; PKI:
  [[CONCEPT-CLUSTER_PKI]].
