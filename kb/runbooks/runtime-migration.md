---
id: PRACTICE-RUNBOOK_RUNTIME_MIGRATION
type: best_practice
title: "Runbook: migrate container runtime (Docker → containerd)"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - runtime migration runbook
  - docker to containerd migration
  - change container_manager
  - switch container runtime
  - remove docker runtime
tags:
  - runbook
  - operations
  - container-runtime
sources:
  - type: docs
    path: docs/upgrades/migrate_docker2containerd.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/upgrades/migrate_docker2containerd.md
    note: "experimental, manual, node-by-node; not officially supported; reset+redeploy is safer"
relations:
  - type: part_of
    target: CONCEPT-RUNBOOKS_INDEX
  - type: depends_on
    target: PRACTICE-MIGRATE_DOCKER_TO_CONTAINERD
  - type: depends_on
    target: VARIABLE-CONTAINER_MANAGER
  - type: see_also
    target: COMPONENT-CONTAINERD
  - type: see_also
    target: PRACTICE-RUNBOOK_RESET
---

# Runbook: migrate container runtime (Docker → containerd)

## Summary

Switching a running cluster's container engine from Docker to containerd is **not officially
supported** — Kubespray's own docs call the in-place path experimental and manual
([[PRACTICE-MIGRATE_DOCKER_TO_CONTAINERD]]). containerd has been the **default since 2.18.0**, so
this is a legacy-cleanup operation. The honest recommendation up front: **reset & redeploy** with
`container_manager: containerd` is safer than in-place. If you must migrate live, do it **one node at
a time** with drain, accepting downtime and no guarantees.

## Context

- **Prefer rebuild.** A blue-green / reset+redeploy ([[PRACTICE-RUNBOOK_RESET]] →
  [[PRACTICE-RUNBOOK_BOOTSTRAP]]) avoids the dual-runtime mess entirely and has a clean rollback (the
  old cluster). Choose in-place only when a rebuild is impossible.
- **In-place is per-node and disruptive:** each node is cordoned/drained, Docker removed by hand,
  then re-converged with containerd. Node has no runtime mid-switch.
- **Do not change anything else** during the migration ([[VARIABLE-CONTAINER_MANAGER]] is the only
  intended change) — mixing config changes in makes failures impossible to attribute.
- Requires full root on every node. Stable guidance across **v2.27.0–v2.31.0**
  ([[COMPONENT-CONTAINERD]]).

## Implementation

**Step 0 — Freeze, gate, back up** ([[CONCEPT-RUNBOOKS_INDEX]] spine): snapshot etcd, confirm cluster
healthy, record which nodes still run Docker (`kubectl get nodes -o wide` CONTAINER-RUNTIME column).

**Step 1 — Decide strategy.** If a rebuild is viable, stop here and use
[[PRACTICE-RUNBOOK_RESET]] + [[PRACTICE-RUNBOOK_BOOTSTRAP]] with `container_manager: containerd`. The
rest is the in-place path.

**Step 2 — Set the runtime** in inventory: `container_manager: containerd`
([[VARIABLE-CONTAINER_MANAGER]]).

**Step 3 — Per node, one at a time:**

```bash
kubectl cordon <node>
kubectl drain <node> --ignore-daemonsets --delete-emptydir-data --timeout=300s
# on the node: stop/remove Docker packages and its state
ansible-playbook -i inventory/<cluster>/hosts.yaml kubespray/cluster.yml -b --limit=<node>
kubectl uncordon <node>
```

**Step 4 — Verify the node** before the next: `kubectl get node <node> -o wide` shows
`containerd://…` as the runtime, node `Ready`, its pods rescheduled and `Running`, `crictl ps` works
on the node. Only then proceed to the next node.

**Step 5 — Confirm cluster-wide:** no node still reports `docker://`; all workloads healthy.

**Rollback.** In-place runtime migration is **not cleanly reversible** — Docker state on a converted
node is gone. Real rollback is **restore the etcd snapshot into a rebuilt (old-runtime) cluster**, or
— the reason rebuild is preferred — **cut back to the untouched old cluster**. Decide before Step 3.

## References

- `docs/upgrades/migrate_docker2containerd.md` (tag `v2.31.0`). Guide
  [[PRACTICE-MIGRATE_DOCKER_TO_CONTAINERD]]; variable [[VARIABLE-CONTAINER_MANAGER]]; rebuild path
  [[PRACTICE-RUNBOOK_RESET]] / [[PRACTICE-RUNBOOK_BOOTSTRAP]]; index [[CONCEPT-RUNBOOKS_INDEX]].
