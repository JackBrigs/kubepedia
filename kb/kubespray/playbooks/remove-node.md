---
id: PLAYBOOK-REMOVE_NODE
type: playbook
title: remove-node.yml
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - remove-node.yml
tags:
  - playbook
  - scaling
sources:
  - type: code
    path: playbooks/remove_node.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/remove_node.yml
    note: "drain, reset and remove a specific node"
relations:
  - type: see_also
    target: PRACTICE-NODES_ADD_REPLACE
  - type: see_also
    target: TAG-RESET
---

# remove-node.yml

## Summary

`remove-node.yml` removes a specific node from the cluster: it validates and
confirms the target, drains it, resets it, and removes it from Kubernetes and (for
etcd nodes) from the etcd cluster. The target must be passed with
`-e node=NODE_NAME`.

## Implementation

Play sequence (`playbooks/remove_node.yml`):

1. **Validate nodes for removal** (`localhost`).
2. `boilerplate.yml`; **Confirm node removal** (interactive) on the target host.
3. `internal_facts.yml`.
4. **Reset node** (`{{ node }}`): `remove_node/pre_remove` (`pre-remove`), then the
   `reset` role (`reset`, when `reset_nodes | default(True)`; see [[TAG-RESET]]),
   and post-removal cleanup from etcd/Kubernetes.

For an offline node, add `-e reset_nodes=false -e allow_ungraceful_removal=true`.
After the run, remove the node from the inventory. See
[[PRACTICE-NODES_ADD_REPLACE]].

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- Use the same flags even when removing control-plane/etcd nodes; keep etcd quorum.

## References

- `playbooks/remove_node.yml` (tag `v2.31.0` `1c9add4`).
- Root `remove-node.yml` imports it.
