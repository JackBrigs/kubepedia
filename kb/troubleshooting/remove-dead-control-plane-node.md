---
id: TROUBLE-REMOVE_DEAD_CONTROL_PLANE_NODE
type: troubleshooting
title: "Remove a dead control-plane node (etcd member + reset)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - remove dead master node
  - remove_node.yml control plane
  - etcdctl member remove
  - offline control plane node removal
tags:
  - troubleshooting
  - control-plane
  - etcd
  - kubespray
  - operations
sources:
  - type: code
    path: playbooks/remove_node.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/remove_node.yml
    note: "drain + reset + remove; pre-remove role"
relations:
  - type: see_also
    target: UPGRADE-KUBESPRAY_SEQUENTIAL
  - type: see_also
    target: TROUBLE-ETCD_QUORUM_LOSS
  - type: see_also
    target: TROUBLE-KCM_NODE_LIFECYCLE
---

# Remove a dead control-plane node (etcd member + reset)

## Summary

A control-plane node died and can't come back. Removing it cleanly means **removing its etcd
member** and its node object, then re-balancing quorum — not just `kubectl delete node`.
Kubespray provides **`playbooks/remove_node.yml`**; for a fully-offline node you do the etcd
member removal manually.

## Problem

- A dead CP node still counts toward etcd quorum; the cluster is fragile (a second failure loses
  quorum). Node stays `NotReady`; pods may hang ([[TROUBLE-KCM_NODE_LIFECYCLE]]).

## Context

- Applies to Kubespray **v2.29.0–v2.31.0**. Etcd is usually Kubespray's own host etcd
  ([[CONCEPT-KUBESPRAY_ETCD_OWNERSHIP]]), so member removal is via `etcdctl`.

## Diagnostics

- **If the node is reachable:** run `playbooks/remove_node.yml` limited to it
  (`--limit=<node> -e node=<node>`) — it drains, resets kubeadm/etcd, and removes the node.
- **If the node is fully offline:**
  1. **Remove the etcd member** from a healthy etcd node:
     `etcdctl member list` → `etcdctl member remove <memberID>` (mind quorum — never drop below
     majority; [[TROUBLE-ETCD_QUORUM_LOSS]]).
  2. `kubectl delete node <name>`.
  3. Update the inventory (drop the node) and re-run the relevant Kubespray plays so the
     remaining CP configs / local API proxies stop pointing at it.
- **Keep an odd member count:** 3 or 5 etcd members — after removing one from a 3-member cluster
  you're at 2 (even, no fault tolerance); add a replacement CP node to return to 3.

## Known Issues

- Removing an etcd member **before** the node is truly gone (it comes back) causes a split — only
  remove members for genuinely dead nodes.
- Restoring/replacing a lost majority is a different, harder procedure (restore from snapshot) —
  keep etcd snapshots.

## References

- `playbooks/remove_node.yml` (v2.31.0, above); etcd ownership:
  [[CONCEPT-KUBESPRAY_ETCD_OWNERSHIP]]; quorum: [[TROUBLE-ETCD_QUORUM_LOSS]]; node lifecycle:
  [[TROUBLE-KCM_NODE_LIFECYCLE]].
