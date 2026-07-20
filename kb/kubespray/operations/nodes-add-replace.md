---
id: PRACTICE-NODES_ADD_REPLACE
type: best_practice
title: Adding, replacing, and removing nodes
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-20
confidence: verified
aliases:
  - add node
  - remove node
  - scale
tags:
  - operations
  - scaling
sources:
  - type: docs
    path: docs/operations/nodes.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/operations/nodes.md
    note: "scale.yml / remove-node.yml; facts.yml; reset_nodes / allow_ungraceful_removal"
  - type: code
    path: roles/remove_node/pre_remove/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.29.0/roles/remove_node/pre_remove/tasks/main.yml
    note: "remove path drains the node: kubectl drain --force --ignore-daemonsets --grace-period 300 --timeout 360s --delete-emptydir-data; allow_ungraceful_removal skips the drain wait — evidence for the disruption profile"
relations:
  - type: see_also
    target: TAG-RESET
  - type: see_also
    target: TAG-ETCD
---

# Adding, replacing, and removing nodes

## Summary

Worker nodes are added with `scale.yml` and removed with `remove-node.yml`.
Control-plane and etcd node changes are more involved and touch quorum, so they
follow stricter steps.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`.
- Adding/replacing a **worker** is the simplest case; control-plane/etcd changes
  affect HA and etcd membership.

## Implementation

**Add a worker:**

1. Add the node to the inventory.
2. Run `scale.yml` (optionally `--limit=NODE_NAME`). Before using `--limit`, run
   `facts.yml` without a limit to refresh the fact cache for all nodes.

**Remove a node:** with the node still in the inventory, run `remove-node.yml`
with `-e node=NODE_NAME`. If the node is offline, also pass
`-e reset_nodes=false -e allow_ungraceful_removal=true` (use this even for
control-plane/etcd nodes). The `reset` step is [[TAG-RESET]]. Then remove the node
from the inventory.

**Control-plane / etcd nodes:** require care for quorum and etcd membership (see
[[TAG-ETCD]]); replace one at a time and keep a functional majority.

## Service impact

Adding and removing sit at opposite ends of the disruption scale. Verified against
`roles/remove_node/pre_remove/tasks/main.yml` (v2.29.0):

- **Add a worker (`scale.yml`): low impact.** Plays target the new `kube_node`
  (plus `kube_control_plane[0]` for the image cache and cert upload); existing
  nodes are **not drained** and running workloads are untouched. The new node
  simply joins and becomes schedulable.
- **Remove a node (`remove-node.yml`): disruptive on the target node.** The
  `pre_remove` role runs `kubectl drain --force --ignore-daemonsets
  --grace-period 300 --timeout 360s --delete-emptydir-data`, so every pod on that
  node is **evicted and rescheduled elsewhere** — single-replica workloads and
  those without a PodDisruptionBudget see **downtime**, `--force` also deletes
  standalone/unmanaged pods (not recreated), and **emptyDir data on the node is
  destroyed**. DaemonSets are left in place. Then the `reset` role wipes the node.
- **`allow_ungraceful_removal=true`** (offline node) **skips the drain/volume
  wait** — pods on the dead node are force-removed without graceful eviction.
- **Control-plane / etcd nodes:** removing an etcd member reconfigures etcd
  membership and a control-plane replacement briefly **reduces API HA**. Replace
  **one at a time** and keep a functional quorum/majority throughout.

Not a rollback: cluster state is preserved; disruption is confined to the workloads
on the node being removed (and their reschedule window).

## Compatibility

- Verified against `v2.31.0` docs; the scale/remove workflow is stable across the
  indexed range. Always keep etcd quorum when changing control-plane/etcd nodes.

## References

- `docs/operations/nodes.md` (tag `v2.31.0` `1c9add4`).
