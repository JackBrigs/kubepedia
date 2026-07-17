---
id: CONCEPT-RUNBOOKS_INDEX
type: concept
title: "Operational runbooks — index & the shared safety spine"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - runbook
  - runbooks
  - operational runbook
  - runbook index
  - step by step procedure kubespray
  - how do I upgrade / restore / migrate
  - safe operation checklist
tags:
  - runbook
  - operations
  - index
sources:
  - type: docs
    path: docs/operations/upgrades.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/operations/upgrades.md
    note: "graceful upgrade, recover-control-plane, etcd ops — the procedures these runbooks order"
relations:
  - type: see_also
    target: PRACTICE-UPGRADE_PREFLIGHT
  - type: see_also
    target: PRACTICE-CLUSTER_HEALTH_CHECKS
  - type: see_also
    target: PRACTICE-ETCD_BACKUP_RESTORE
  - type: see_also
    target: CONCEPT-ESCAPE_HATCHES
---

# Operational runbooks — index & the shared safety spine

## Summary

The knowledge base has deep **mechanics** docs (how drain works, how etcd restores, how CNI is
selected) and ~170 **troubleshooting** docs (what breaks and why). A **runbook** is the third
thing: a single **ordered, executable procedure** for one operation — *do this, verify that, and
if it fails jump here* — that stitches the mechanics and the troubleshooting into one path with an
explicit **rollback**. This page is the catalog, and it defines the **safety spine** every runbook
shares so the individual runbooks don't repeat it.

## Context

**The safety spine (every destructive operation follows it):**

1. **Freeze & record** — capture current state so you can prove what changed and roll back to it:
   `kubectl get nodes,pods -A -o wide`, `kubeadm certs check-expiration`, the current Kubespray
   tag (`git -C kubespray describe --tags`) and inventory `kube_version`.
2. **Health gate** — never operate on a broken cluster. All nodes `Ready`, no crash-looping
   system pods, etcd healthy ([[PRACTICE-CLUSTER_HEALTH_CHECKS]]). If it's already broken, fix
   that first — the operation will only compound it.
3. **Back up** — an **etcd snapshot stored off-node** is the universal rollback anchor for
   control-plane state ([[PRACTICE-ETCD_BACKUP_RESTORE]]); keep it with the cluster PKI.
4. **Execute** — the runbook's ordered steps, **one blast-radius unit at a time** (one node, one
   member, one minor). Kubespray's own serial/drain machinery enforces this for upgrades
   ([[PRACTICE-GRACEFUL_UPGRADE]]).
5. **Verify** — after **each** unit, not just at the end: node `Ready`, system pods up, a smoke
   workload reschedules. Pause between units (`upgrade_node_pause_seconds` / `upgrade_node_confirm`)
   so a bad unit is caught before it rolls to the rest.
6. **Rollback** — know the reversal *before* you start. For most operations rollback = restore the
   etcd snapshot + re-run at the previous tag; a half-applied change is worse than a clean revert.

**The runbooks:**

| Runbook | Operation | Rollback anchor |
|---------|-----------|-----------------|
| [[PRACTICE-RUNBOOK_UPGRADE_ONE_MINOR]] | Upgrade the cluster by exactly one Kubespray minor | etcd snapshot + previous tag |
| [[PRACTICE-RUNBOOK_ETCD_RESTORE]] | Restore control-plane state from an etcd snapshot (DR) | the snapshot itself + `recover-control-plane.yml` |
| [[PRACTICE-RUNBOOK_CNI_MIGRATION]] | Change the CNI plugin on a running cluster | etcd snapshot; CNI swap is not cleanly reversible in place |

**When you don't need a runbook.** A single diagnostic lookup (one symptom → one fix) is a
troubleshooting doc, not a runbook — go straight to the `TROUBLE-*` doc. Reach for a runbook when
the operation has **ordering, a health gate, and a rollback** that must not be improvised.

**Version scope.** The upgrade model (`upgrade-cluster.yml`, `serial`, `drain_nodes`,
one-minor-at-a-time), etcd snapshot/restore, and CNI selection are **stable across
v2.27.0–v2.31.0**; per-version deltas (playbook paths, `serial` defaults, role names) are called
out inside each runbook rather than here.

## References

- `docs/operations/{upgrades,recover-control-plane,etcd}.md` (tag `v2.31.0`). Preflight gate:
  [[PRACTICE-UPGRADE_PREFLIGHT]]; health gate: [[PRACTICE-CLUSTER_HEALTH_CHECKS]]; backup anchor:
  [[PRACTICE-ETCD_BACKUP_RESTORE]]; customization index: [[CONCEPT-ESCAPE_HATCHES]].
