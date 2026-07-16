---
id: PRACTICE-GRACEFUL_UPGRADE
type: best_practice
title: "Graceful upgrade mechanics (drain, serial, pause)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - graceful upgrade
  - upgrade-cluster.yml
  - drain_nodes
  - upgrade_node_confirm
  - serial upgrade
  - rolling node upgrade
tags:
  - operations
  - upgrade
  - drain
  - best-practice
sources:
  - type: code
    path: playbooks/upgrade_cluster.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/upgrade_cluster.yml
    note: "serial handling (control-plane serial 1, nodes 20%) (tag v2.31.0)"
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "drain_nodes/upgrade_node_confirm/pause + drain timeouts (tag v2.31.0)"
relations:
  - type: see_also
    target: UPGRADE-KUBESPRAY_SEQUENTIAL
  - type: see_also
    target: PRACTICE-UPGRADE_PREFLIGHT
  - type: see_also
    target: PRACTICE-NODES_ADD_REPLACE
---

# Graceful upgrade mechanics (drain, serial, pause)

## Summary

`upgrade-cluster.yml` upgrades the cluster **node by node**: it cordons and drains each
node, upgrades it, then uncordons — so workloads reschedule instead of dropping. A few
variables control how aggressively it rolls and whether it pauses for you. Use this
playbook (not `cluster.yml`) for upgrades to get the rolling, drain-safe behaviour.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`.
- `upgrade-cluster.yml` sets **`serial`**: control-plane nodes upgrade **one at a time**
  (`serial: 1`, preserving etcd/API quorum), worker nodes at **`serial: 20%`** by default
  (override with `-e serial=…`).
- Pairs with the version rules in [[UPGRADE-KUBESPRAY_SEQUENTIAL]] (one minor at a time)
  and the checklist in [[PRACTICE-UPGRADE_PREFLIGHT]].

## Implementation

**Drain (default on):**

- `drain_nodes: true` — cordon + drain each node before upgrading it.
- `drain_grace_period: 300` — pod termination grace (seconds).
- `drain_timeout: 360s` — give up draining after this.
- `drain_retries: 3`, `drain_retry_delay_seconds: 10` — retry a stuck drain.

**Pacing:**

- `upgrade_node_pause_seconds: 0` — sleep N seconds between nodes (soak time to verify
  health before continuing).
- `upgrade_node_confirm: false` — set `true` to **pause for manual confirmation** before
  each node (a controlled, one-node-at-a-time upgrade).
- `-e serial=1` — upgrade strictly one worker at a time (slowest, safest); larger values
  or percentages go faster with more disruption.

**Run:**

```bash
ansible-playbook -i inventory/<cluster>/hosts.yaml upgrade-cluster.yml -b
# controlled: -e upgrade_node_confirm=true  (or -e upgrade_node_pause_seconds=60)
```

## Compatibility

- Draining respects **PodDisruptionBudgets** — a too-strict PDB can stall the drain until
  `drain_timeout`; ensure workloads have enough replicas/headroom to move.
- Set `upgrade_node_pause_seconds` or `upgrade_node_confirm` on critical clusters so you
  can catch a bad node before it rolls to the rest.
- Control-plane is always `serial: 1` regardless of your `serial` override — don't try to
  parallelize control-plane upgrades (quorum).
- Don't use `cluster.yml` for upgrades of a running cluster expecting graceful behaviour —
  `upgrade-cluster.yml` is the drain-aware path.

## References

- `playbooks/upgrade_cluster.yml` (serial) and drain/pause defaults at tag `v2.31.0`.
  Version steps: [[UPGRADE-KUBESPRAY_SEQUENTIAL]]; preflight: [[PRACTICE-UPGRADE_PREFLIGHT]].
