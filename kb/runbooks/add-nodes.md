---
id: PRACTICE-RUNBOOK_ADD_NODES
type: best_practice
title: "Runbook: add worker or control-plane nodes (scale.yml / cluster.yml)"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - add node runbook
  - scale up cluster
  - scale.yml add worker
  - add control plane node
  - grow cluster kubespray
  - join new node
tags:
  - runbook
  - operations
  - scaling
sources:
  - type: docs
    path: docs/operations/nodes.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/operations/nodes.md
    note: "worker via scale.yml (--limit, facts.yml first); control-plane via cluster.yml, append to end, restart nginx-proxy"
  - type: code
    path: scale.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/scale.yml
    note: "adds nodes without touching the rest of the cluster"
relations:
  - type: part_of
    target: CONCEPT-RUNBOOKS_INDEX
  - type: see_also
    target: PRACTICE-NODES_ADD_REPLACE
  - type: see_also
    target: ROLE-KUBERNETES_NODE
  - type: see_also
    target: PRACTICE-CLUSTER_HEALTH_CHECKS
  - type: see_also
    target: PRACTICE-NETCHECK
  - type: see_also
    target: TROUBLE-ADD_NODE_GOTCHAS
---

# Runbook: add worker or control-plane nodes (scale.yml / cluster.yml)

## Summary

Adding a **worker** and adding a **control-plane** node are different playbooks and this is the #1
thing operators get wrong: workers use **`scale.yml`** (non-disruptive), control-plane nodes use
**`cluster.yml`** (`scale.yml` will **not** join a control-plane node — [[PRACTICE-NODES_ADD_REPLACE]]).
Both start from adding the host to the inventory. Adds are low-risk (the existing cluster keeps
running); the care is in **not disturbing** the nodes you already have.

## Context

- **Worker → `scale.yml`.** Only converges the new node; use `--limit=<node>` to avoid touching
  others — but run **`facts.yml` first without `--limit`** so the fact cache is fresh (a stale cache
  under `--limit` is a classic source of wrong config on the new node).
- **Control-plane → `cluster.yml`.** You **cannot** use `scale.yml`. **Append** the new control-plane
  host to the **end** of the `kube_control_plane` group — adding it in the **first** position is
  unsupported and fails the run. After the run, **restart the `nginx-proxy`** static pod on every
  node so it reloads the updated apiserver list.
- Stable across **v2.27.0–v2.31.0**. New nodes must match the cluster's OS/kernel/runtime and pick up
  the same `kube_version`.

## Implementation

### Add a worker node

**Step 1 — Inventory:** add the host to `kube_node`.

**Step 2 — Refresh facts (no limit), then scale (limited):**

```bash
ansible-playbook -i inventory/<cluster>/hosts.yaml kubespray/facts.yml
ansible-playbook -i inventory/<cluster>/hosts.yaml kubespray/scale.yml -b --limit=<new-node>
```

**Step 3 — Verify:** `kubectl get node <new-node>` is `Ready`, CNI pod scheduled on it, a test pod
runs there ([[PRACTICE-NETCHECK]]).

### Add a control-plane node

**Step 1 — Inventory:** append the host to the **end** of `kube_control_plane` (and `etcd` if it is
also an etcd member). Never insert at the front.

**Step 2 — Converge with `cluster.yml`:**

```bash
ansible-playbook -i inventory/<cluster>/hosts.yaml kubespray/cluster.yml -b
```

**Step 3 — Reload the API proxy on every node** (Kubespray updates the config but the pod must
restart):

```bash
crictl ps | grep nginx-proxy | awk '{print $1}' | xargs crictl stop   # containerd
```

**Step 4 — Verify:** new control-plane node `Ready`; if it joined `etcd`, `etcdctl member list`
shows it `started` and healthy ([[COMPONENT-ETCD]]); API stays responsive throughout.

**Rollback.** An add is reversible by **removing** the node again ([[PRACTICE-RUNBOOK_REMOVE_NODE]]).
If a control-plane add destabilises etcd quorum, remove the new member first, then investigate — do
not leave a half-joined etcd member in place.

## References

- `docs/operations/nodes.md`, `scale.yml`, `cluster.yml` (tag `v2.31.0`). Mechanics:
  [[PRACTICE-NODES_ADD_REPLACE]]; node role [[ROLE-KUBERNETES_NODE]]; verify
  [[PRACTICE-CLUSTER_HEALTH_CHECKS]] / [[PRACTICE-NETCHECK]]; removal
  [[PRACTICE-RUNBOOK_REMOVE_NODE]]; index [[CONCEPT-RUNBOOKS_INDEX]].
