---
id: TROUBLE-NODE_DRAIN_GOTCHAS
type: troubleshooting
title: "Node drain gotchas — PDB hangs it, emptyDir data lost, bare pods force-deleted"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-19"
confidence: confirmed
aliases:
  - kubectl drain hangs
  - drain stuck PodDisruptionBudget
  - drain emptyDir data loss
  - drain force deletes bare pods
  - cannot evict pod PDB
  - drain single replica downtime
tags:
  - troubleshooting
  - node
  - drain
  - storage
sources:
  - type: external
    path: kubectl drain / eviction API
    url: https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/
    note: "eviction respects PDBs; --delete-emptydir-data deletes emptyDir; --force deletes unmanaged pods"
  - type: code
    path: playbooks/upgrade_cluster.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/upgrade_cluster.yml
    note: "Kubespray drain vars: drain_grace_period, drain_timeout, drain_retries"
relations:
  - type: see_also
    target: PRACTICE-RUNBOOK_NODE_MAINTENANCE
  - type: see_also
    target: PRACTICE-RUNBOOK_REMOVE_NODE
  - type: see_also
    target: TROUBLE-NODE_LOCAL_PVC_DRAIN
  - type: see_also
    target: TROUBLE-KCM_VOLUME_MULTIATTACH
---

# Node drain gotchas — PDB hangs it, emptyDir data lost, bare pods force-deleted

## Summary

Draining a node for maintenance/removal is where "correct behavior bites you". Four community-classic
traps beyond the node-local-storage one ([[TROUBLE-NODE_LOCAL_PVC_DRAIN]]): a **PodDisruptionBudget**
can **hang the drain** indefinitely; **`--delete-emptydir-data`** silently **deletes emptyDir data**;
**`--force`** **permanently deletes** pods with no controller; and a **single-replica** workload takes
**downtime** on eviction. Kubespray's `upgrade-cluster.yml` drives the same eviction (with
`drain_timeout`/`drain_retries`), so these bite during upgrades too.

## Problem

- `kubectl drain` (or the Kubespray upgrade) **stalls**: `Cannot evict pod as it would violate the
  pod's disruption budget` / `error when evicting pods ... still waiting`.
- A pod's **emptyDir** data (cache, scratch, a mis-configured DB) is **gone** after drain.
- **Bare pods** (created without a Deployment/StatefulSet/DaemonSet) **vanish** after `--force` and
  never come back.
- A single-replica service is **down** during the drain window.

## Context

- Applies across **v2.27.0–v2.31.0** and any `kubectl drain`. Kubespray's graceful upgrade drains via
  the eviction API with `drain_grace_period`, `drain_timeout` (default `360s`), `drain_retries`
  ([[PRACTICE-RUNBOOK_NODE_MAINTENANCE]]).
- **PDB hang:** eviction respects **PodDisruptionBudgets**. A PDB with `maxUnavailable: 0`, or
  `minAvailable` equal to the replica count, or a **single-replica** workload with any PDB, means the
  API server **refuses every eviction** — the drain retries until `drain_timeout`, then fails.
- **emptyDir loss:** the drain won't evict pods with an `emptyDir` unless you pass
  **`--delete-emptydir-data`** — and that flag **discards** the emptyDir contents. Data on `emptyDir`
  is node-local scratch by definition; it does not survive the pod moving.
- **Bare pods / `--force`:** pods **not** owned by a controller aren't evicted by a normal drain; only
  **`--force`** removes them, and then they are **deleted permanently** (nothing recreates them).
  `--force` also skips graceful handling — use it deliberately.
- **DaemonSets:** `--ignore-daemonsets` (Kubespray default) skips DS pods — usually fine, but a DS that
  provides node-critical function (a storage/CSI agent, log shipper) stops on that node.
- **RWO volume after node loss:** a networked RWO volume can get stuck attached to the departed node
  ([[TROUBLE-KCM_VOLUME_MULTIATTACH]]) — different from emptyDir but another drain-time storage trap.

## Diagnostics

- Drain stalling? Find the blocking PDB: `kubectl get pdb -A` and the workload's replicas vs
  `minAvailable`/`maxUnavailable`.
- emptyDir users on the node: `kubectl get pods -A --field-selector spec.nodeName=<node> -o json |
  python3 -c 'import json,sys;[print(p["metadata"]["namespace"],p["metadata"]["name"]) for p in
  json.load(sys.stdin)["items"] if any("emptyDir" in v for v in p["spec"].get("volumes",[]))]'`.
- Bare pods (no ownerReferences): `kubectl get pods -A -o json | python3 -c 'import json,sys;[print(
  p["metadata"]["namespace"],p["metadata"]["name"]) for p in json.load(sys.stdin)["items"] if not
  p["metadata"].get("ownerReferences")]'`.

## Known Issues

- **PDB hang — fix:** ensure enough replicas/headroom so one can move, or **temporarily relax** the PDB
  (raise `maxUnavailable` / lower `minAvailable`) for the maintenance window; don't `--force` blindly
  (that bypasses the PDB and can violate real availability guarantees).
- **emptyDir — fix:** confirm the emptyDir data is disposable before `--delete-emptydir-data`; if it
  isn't, it shouldn't be on emptyDir — back it up / move to a PVC first.
- **Bare pods — fix:** put workloads under a controller (Deployment/StatefulSet) so they reschedule;
  only `--force`-delete bare pods you're willing to lose.
- **Single-replica — fix:** scale to ≥2 with a PDB, or accept and schedule the downtime; combine with
  the node-local-storage check ([[TROUBLE-NODE_LOCAL_PVC_DRAIN]]).
- **Pace it (Kubespray):** tune `drain_timeout`/`drain_retries` and use `upgrade_node_confirm` /
  `serial: 1` so a stuck drain fails one node at a time, not the whole roll.

## References

- Upstream `kubectl drain` / eviction API; Kubespray drain vars (`upgrade_cluster.yml`, v2.31.0). Node
  maintenance [[PRACTICE-RUNBOOK_NODE_MAINTENANCE]]; node removal [[PRACTICE-RUNBOOK_REMOVE_NODE]];
  node-local storage [[TROUBLE-NODE_LOCAL_PVC_DRAIN]]; RWO-after-node-loss [[TROUBLE-KCM_VOLUME_MULTIATTACH]].
