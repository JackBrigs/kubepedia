---
id: CONFIG-NODE_LABELS_TAINTS
type: configuration
title: "Node labels and taints via inventory (node_labels / node_taints)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - node_labels
  - node_taints
  - label nodes kubespray
  - taint nodes
  - dedicate nodes
  - NoSchedule taint
tags:
  - operations
  - scheduling
  - nodes
  - configuration
sources:
  - type: docs
    path: docs/ansible/vars.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/ansible/vars.md
    note: "node_labels (dict) / node_taints (list key=value:effect) format (tag v2.31.0)"
relations:
  - type: see_also
    target: TAG-NODE_LABEL
  - type: see_also
    target: CONCEPT-SAMPLE_INVENTORY_LAYOUT
---

# Node labels and taints via inventory (node_labels / node_taints)

## Summary

Kubespray can apply **labels** and **taints** to nodes declaratively from inventory, so
node roles/scheduling constraints are managed as code instead of ad-hoc `kubectl`
commands. `node_labels` and `node_taints` are set per-host or per-group; Kubespray applies
them via `kubectl label node` / `kubectl taint node`.

## Configuration

**Labels** — `node_labels` must be a **dict**:

```yaml
node_labels:
  label1_name: label1_value
  topology.kubernetes.io/zone: zone-a
```

**Taints** — `node_taints` must be a **list of strings** `key=value:effect`:

```yaml
node_taints:
  - "node.example.com/external=true:NoSchedule"
```

- Set them **per host** (in `host_vars` / the inventory host entry) to target specific
  nodes, or in `group_vars/<group>/` to apply to a whole group (see
  [[CONCEPT-SAMPLE_INVENTORY_LAYOUT]]).
- Kubespray merges inventory labels with role-provided ones (e.g. a GPU role adds
  `nvidia.com/gpu=true`).
- The `node-label` run-tag re-applies labels on demand ([[TAG-NODE_LABEL]]).

## Compatibility

- Applies to Kubespray `v2.29.0`–`v2.31.0`.
- **Format matters:** `node_labels` as a dict, `node_taints` as `key=value:effect` strings
  — wrong types silently mis-apply or error. Valid effects: `NoSchedule`,
  `PreferNoSchedule`, `NoExecute`.
- Taints applied here are the same taints the scheduler honours — use them to **dedicate**
  nodes (with matching Pod tolerations) or drain-by-taint (`NoExecute`).
- Kubespray manages these declaratively: a label/taint removed from inventory is not
  necessarily removed from the node on the next run — verify the reconcile behaviour before
  relying on removal, and clean up stale ones with `kubectl` if needed.
- Control-plane nodes already carry the standard control-plane taint from kubeadm; don't
  duplicate it.

## References

- `docs/ansible/vars.md` (`node_labels` / `node_taints`) at tag `v2.31.0`. Run-tag:
  [[TAG-NODE_LABEL]]; inventory layout: [[CONCEPT-SAMPLE_INVENTORY_LAYOUT]].
