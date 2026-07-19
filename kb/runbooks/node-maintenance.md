---
id: PRACTICE-RUNBOOK_NODE_MAINTENANCE
type: best_practice
title: "Runbook: node maintenance (drain, reboot / OS-patch, uncordon)"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - node maintenance runbook
  - drain and reboot node
  - os patching kubernetes node
  - cordon drain uncordon
  - kernel upgrade node
  - safe node restart
tags:
  - runbook
  - operations
  - maintenance
sources:
  - type: docs
    path: docs/operations/upgrades.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/operations/upgrades.md
    note: "drain_nodes / drain_timeout / upgrade_node_confirm semantics reused for maintenance"
  - type: external
    path: kubectl drain
    url: https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/
    note: "PDB-respecting eviction; cordon/uncordon"
relations:
  - type: part_of
    target: CONCEPT-RUNBOOKS_INDEX
  - type: see_also
    target: PRACTICE-GRACEFUL_UPGRADE
  - type: see_also
    target: PRACTICE-NODE_NOT_READY
  - type: see_also
    target: PRACTICE-CLUSTER_HEALTH_CHECKS
  - type: see_also
    target: COMPONENT-ETCD
---

# Runbook: node maintenance (drain, reboot / OS-patch, uncordon)

## Summary

The safe pattern for taking a node down for OS patching, a kernel bump, or hardware work **without
running any Kubespray playbook**: cordon → drain → do the work → uncordon → verify. It is pure
`kubectl` + host actions, one node at a time. The same drain semantics Kubespray uses during
upgrades apply here ([[PRACTICE-GRACEFUL_UPGRADE]]) — the difference is you drive it manually and
control the host work in between.

## Context

- **One node at a time**, always. Draining respects **PodDisruptionBudgets**, so a too-strict PDB
  or a single-replica workload blocks the drain — fix headroom first, don't `--force` blindly.
- **Control-plane / etcd nodes:** only maintain **one at a time** and confirm quorum is intact
  before touching the next — losing a second etcd member mid-maintenance can lose quorum
  ([[COMPONENT-ETCD]]).
- **After a reboot**, a node can come back `NotReady` briefly while kubelet/CNI re-init; give it time
  and check [[PRACTICE-NODE_NOT_READY]] if it stays down.
- **Node-local storage:** a pod using a **local-path / local-volume PVC** can't reschedule off the
  node (the PV is pinned to it), so draining strands it and the service stays down until you uncordon
  — pre-check and migrate first ([[TROUBLE-NODE_LOCAL_PVC_DRAIN]]).
- No playbook, no version coupling — valid across **v2.27.0–v2.31.0** and any running cluster.

## Implementation

**Step 0 — Pick the node and confirm the cluster is healthy** ([[PRACTICE-CLUSTER_HEALTH_CHECKS]])
so you don't start maintenance on top of an existing problem.

**Step 1 — Cordon** (stop new scheduling):

```bash
kubectl cordon <node>
```

**Step 2 — Drain** (evict workloads, respecting PDBs):

```bash
kubectl drain <node> --ignore-daemonsets --delete-emptydir-data --timeout=300s
# if the drain stalls: identify the blocking PDB/pod and add replicas — avoid --force unless you
# accept the disruption
```

**Step 3 — Do the maintenance:** OS/security patches, kernel upgrade, firmware, hardware. Reboot if
needed. For a kernel change, verify modules/sysctls the cluster relies on are still present after
reboot ([[PRACTICE-KERNEL_REQUIREMENTS]]).

**Step 4 — Uncordon** (return to service):

```bash
kubectl uncordon <node>
```

**Step 5 — Verify** before moving to the next node: node `Ready`, its DaemonSet pods (CNI, kube-proxy)
`Running`, workloads rescheduling onto it, and — for etcd/control-plane nodes — `etcdctl endpoint
health` green and quorum intact. Only then repeat for the next node.

**Rollback.** Maintenance is inherently reversible per node: if a node won't return healthy,
**keep it cordoned** (workloads already moved off in Step 2) and diagnose
([[PRACTICE-NODE_NOT_READY]]) — the rest of the cluster is unaffected because you did one node at a
time. A node that is beyond repair becomes a **remove + re-add** ([[PRACTICE-RUNBOOK_REMOVE_NODE]],
[[PRACTICE-RUNBOOK_ADD_NODES]]).

## References

- `docs/operations/upgrades.md` (drain semantics), upstream `kubectl drain` (tag `v2.31.0`). Drain
  detail [[PRACTICE-GRACEFUL_UPGRADE]]; recovery [[PRACTICE-NODE_NOT_READY]]; kernel prereqs
  [[PRACTICE-KERNEL_REQUIREMENTS]]; index [[CONCEPT-RUNBOOKS_INDEX]].
