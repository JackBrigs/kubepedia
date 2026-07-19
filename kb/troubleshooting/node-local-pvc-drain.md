---
id: TROUBLE-NODE_LOCAL_PVC_DRAIN
type: troubleshooting
title: "Draining/removing a node with node-local PVCs (local-path) strands the workload and loses data"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-19"
confidence: confirmed
aliases:
  - local-path pvc node drain
  - drain node local storage service down
  - pod pending after drain volume node affinity
  - local-path data loss remove node
  - node-local pvc can't reschedule
  - remove node with local storage
tags:
  - troubleshooting
  - storage
  - local-path
  - node
sources:
  - type: code
    path: roles/kubernetes-apps/external_provisioner/local_path_provisioner
    url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0/roles/kubernetes-apps/external_provisioner/local_path_provisioner
    note: "local-path PVs are backed by a directory on one node's disk; PV carries nodeAffinity to that node"
relations:
  - type: see_also
    target: COMPONENT-LOCAL_PATH_PROVISIONER
  - type: see_also
    target: COMPONENT-LOCAL_VOLUME_PROVISIONER
  - type: see_also
    target: PRACTICE-RUNBOOK_REMOVE_NODE
  - type: see_also
    target: PRACTICE-RUNBOOK_NODE_MAINTENANCE
---

# Draining/removing a node with node-local PVCs (local-path) strands the workload and loses data

## Summary

A **local-path** (or local-volume / hostPath) PVC is backed by a directory on **one node's local
disk**, and its PV carries a **nodeAffinity** pinning it to that node. So a pod using such a PVC can
only run on that node. When you **drain** the node, the pod is evicted but **cannot reschedule
anywhere else** → it sits `Pending` and the service is **down until the node is uncordoned**. If the
node is being **removed**, the data goes away with the disk — a **service outage + data loss** that a
"just drain and remove the node" procedure silently causes. Always check for node-local PVCs on a node
**before** draining or removing it.

## Problem

- After `kubectl drain <node>` (or a node-maintenance / remove-node run), a pod (often a DB / stateful
  single-replica) is stuck `Pending` with `node(s) had volume node affinity conflict` / `waiting for a
  volume to be created`.
- The service stays down as long as the node is cordoned, and never recovers if the node is removed.
- After removing the node, the PVC's data is gone (it lived on that node's disk).

## Context

- Applies across the Kubespray range (**v2.27.0–v2.31.0**); local-path-provisioner is a managed addon
  ([[COMPONENT-LOCAL_PATH_PROVISIONER]]); local-volume-provisioner is the same class
  ([[COMPONENT-LOCAL_VOLUME_PROVISIONER]]).
- **Why it strands:** local-path uses `volumeBindingMode: WaitForFirstConsumer` and creates the PV on
  the node where the first consumer landed; the PV's `nodeAffinity` then binds the pod to that node
  forever. Draining removes the pod but the scheduler can't place it elsewhere (the volume is on the
  drained node).
- **Why data is lost:** the default reclaim path and the storage itself are **node-local** — the bytes
  are a directory on that node's disk. Removing the node (or deleting the PVC) destroys them. local-path
  is **not HA by design**.

## Diagnostics

**Before** draining/removing a node, list what's node-local on it:

```bash
# pods running on the target node
kubectl get pods -A --field-selector spec.nodeName=<node> -o wide

# PVs pinned to this node (local-path / local storage carry nodeAffinity)
kubectl get pv -o json | python3 -c '
import json,sys
node=sys.argv[1]
for pv in json.load(sys.stdin)["items"]:
    na=(pv.get("spec",{}).get("nodeAffinity") or {}).get("required",{})
    vals=[v for t in na.get("nodeSelectorTerms",[]) for e in t.get("matchExpressions",[]) for v in e.get("values",[])]
    if node in vals:
        print(pv["metadata"]["name"], pv["spec"].get("storageClassName"), pv["spec"].get("claimRef",{}).get("name"))
' <node>
```

Any PV printed = a workload that will be stranded / lose data on drain.

## Known Issues

- **Fix (migrate first):** for each node-local PVC on the target node, **migrate the data before
  draining** — back up the volume, recreate the workload's PVC on a **different node / a networked
  (CSI) storage class**, restore the data, and only then drain/remove the node. For a StatefulSet,
  move/reschedule the replica onto surviving storage first.
- **Fix (accept the trade-off):** if the data is disposable (cache, scratch), confirm that and proceed
  — the workload will re-provision an empty volume on a new node.
- **Prevent:** don't run data you can't lose on **local-path** — it's node-local and non-HA. Use
  networked/replicated storage (a CSI driver) for anything that must survive a node; keep local-path
  for ephemeral/scratch.
- **This is a mandatory pre-check** for node maintenance and node removal
  ([[PRACTICE-RUNBOOK_NODE_MAINTENANCE]], [[PRACTICE-RUNBOOK_REMOVE_NODE]]) — draining a node with a
  live node-local PVC is a silent outage.

## References

- Kubespray `roles/kubernetes-apps/external_provisioner/local_path_provisioner` (v2.31.0). Component
  [[COMPONENT-LOCAL_PATH_PROVISIONER]]; local-volume [[COMPONENT-LOCAL_VOLUME_PROVISIONER]]; node
  removal [[PRACTICE-RUNBOOK_REMOVE_NODE]]; node maintenance [[PRACTICE-RUNBOOK_NODE_MAINTENANCE]].
