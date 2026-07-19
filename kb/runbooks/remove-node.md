---
id: PRACTICE-RUNBOOK_REMOVE_NODE
type: best_practice
title: "Runbook: remove / decommission a node (remove-node.yml)"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - remove node runbook
  - decommission node kubespray
  - remove-node.yml
  - delete node from cluster
  - remove control plane node
  - allow_ungraceful_removal
tags:
  - runbook
  - operations
  - scaling
sources:
  - type: docs
    path: docs/operations/nodes.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/operations/nodes.md
    note: "remove-node.yml -e node=NAME; offline: reset_nodes=false allow_ungraceful_removal=true; first control-plane special case"
  - type: code
    path: remove_node.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/remove_node.yml
    note: "pre_remove drain -> reset node -> post_remove etcd member removal"
relations:
  - type: part_of
    target: CONCEPT-RUNBOOKS_INDEX
  - type: depends_on
    target: PRACTICE-ETCD_BACKUP_RESTORE
  - type: see_also
    target: TROUBLE-ETCD_REMOVE_NODE_NOT_IDEMPOTENT
  - type: see_also
    target: TROUBLE-ETCD_REMOVE_EXTERNAL_MEMBER_FAILS
  - type: see_also
    target: PRACTICE-NODES_ADD_REPLACE
---

# Runbook: remove / decommission a node (remove-node.yml)

## Summary

`remove-node.yml` drains the target, resets it, and (for etcd/control-plane nodes) removes its etcd
membership — in that order. Two traps dominate: an **offline** node needs explicit
`reset_nodes=false -e allow_ungraceful_removal=true` or the run stalls, and the **first**
control-plane/etcd node **cannot** be removed directly (reorder the inventory first). Because etcd
membership changes, take a snapshot first ([[PRACTICE-ETCD_BACKUP_RESTORE]]) and follow the
[[CONCEPT-RUNBOOKS_INDEX]] spine.

## Context

- **Always pass `-e node=<NAME>`** to scope the run to the node being removed — without it the
  playbook's target is ambiguous.
- **Online vs offline node:** a reachable node is drained and reset cleanly. An **unreachable** node
  can't be reset, so tell the playbook not to try: `-e reset_nodes=false -e allow_ungraceful_removal=true`
  (use these for worker, control-plane **and** etcd nodes).
- **etcd-member removal is not idempotent** — a re-run or a partially-removed member can error
  ([[TROUBLE-ETCD_REMOVE_NODE_NOT_IDEMPOTENT]], [[TROUBLE-ETCD_REMOVE_EXTERNAL_MEMBER_FAILS]]);
  verify membership after, don't blindly re-run.
- **Quorum:** removing an etcd member shrinks the quorum — never drop below a healthy majority (go
  3→1 only deliberately). Stable across **v2.27.0–v2.31.0**.
- **Node-local storage is a silent trap:** if any pod on the node uses a **local-path / local-volume /
  hostPath PVC**, draining strands that workload (`Pending`, volume node-affinity conflict) and
  removing the node **destroys its data** — the PV lives on this node's disk. This is a **mandatory
  pre-check** ([[TROUBLE-NODE_LOCAL_PVC_DRAIN]]).

## Implementation

**Step 0 — Snapshot etcd** ([[PRACTICE-ETCD_BACKUP_RESTORE]]) — removals touch membership.

**Step 0.5 — Pre-check node-local storage** ([[TROUBLE-NODE_LOCAL_PVC_DRAIN]]): list pods on the node
and any PVs pinned to it; **migrate that data first** (or confirm it's disposable), or the drain in
Step 1 takes the service down and loses the volume.

```bash
kubectl get pods -A --field-selector spec.nodeName=<NAME> -o wide
kubectl get pv -o wide | grep -Ei 'local-path|local-storage'   # cross-ref claimRef + nodeAffinity
```

**Step 1 — Remove an online node:**

```bash
ansible-playbook -i inventory/<cluster>/hosts.yaml kubespray/remove-node.yml -b -e node=<NAME>
```

This cordons/drains ([[TAG-PRE_REMOVE]]), resets the node, and removes its etcd member
([[TAG-POST_REMOVE]]).

**Step 2 — Remove an offline / dead node** (can't be reset):

```bash
ansible-playbook -i inventory/<cluster>/hosts.yaml kubespray/remove-node.yml -b \
  -e node=<NAME> -e reset_nodes=false -e allow_ungraceful_removal=true
```

**Step 3 — Special case: the first control-plane/etcd node** (cannot be removed directly). Reorder
so it is no longer first, converge, then remove:

1. In `kube_control_plane`, `kube_node` **and** `etcd`, move the first host to a later position.
2. Run `upgrade-cluster.yml` (or `cluster.yml`) to apply the new order.
3. `remove-node.yml -e node=<old-first>` as in Step 1/2.
4. Fix references to the old node: `kubectl edit cm -n kube-public cluster-info` (update the
   `server` / `certificate-authority-data` to a live control-plane node).

**Step 4 — Remove the host from the inventory** so future runs don't target it.

**Step 5 — Verify:** `kubectl get nodes` no longer lists it; for etcd nodes
`etcdctl member list` shows only surviving members, one leader, matching raft index
([[COMPONENT-ETCD]]). If a stale member lingers, remove it manually with `etcdctl member remove`
rather than re-running the playbook.

**Rollback.** A removed worker is re-added via [[PRACTICE-RUNBOOK_ADD_NODES]]. A wrongly-removed
etcd member that broke quorum is a **restore** situation — go to [[PRACTICE-RUNBOOK_ETCD_RESTORE]]
with the Step 0 snapshot.

## References

- `docs/operations/nodes.md`, `remove_node.yml` (tag `v2.31.0`). etcd-removal gotchas:
  [[TROUBLE-ETCD_REMOVE_NODE_NOT_IDEMPOTENT]], [[TROUBLE-ETCD_REMOVE_EXTERNAL_MEMBER_FAILS]];
  add-back [[PRACTICE-RUNBOOK_ADD_NODES]]; index [[CONCEPT-RUNBOOKS_INDEX]].
