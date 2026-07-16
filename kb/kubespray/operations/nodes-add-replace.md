---
id: PRACTICE-NODES_ADD_REPLACE
type: best_practice
title: Adding, replacing, and removing nodes
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
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

## Compatibility

- Verified against `v2.31.0` docs; the scale/remove workflow is stable across the
  indexed range. Always keep etcd quorum when changing control-plane/etcd nodes.

## References

- `docs/operations/nodes.md` (tag `v2.31.0` `1c9add4`).
