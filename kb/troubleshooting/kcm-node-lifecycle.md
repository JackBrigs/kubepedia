---
id: TROUBLE-KCM_NODE_LIFECYCLE
type: troubleshooting
title: "controller-manager: node NotReady not evicted / not deleted / pods stuck"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - node notready pods not rescheduled
  - unreachable taint missing noexecute
  - node not deleted after vm gone
  - pods stuck terminating node gone
  - node ready false still in endpoints
tags:
  - troubleshooting
  - controller-manager
  - nodes
  - control-plane
sources:
  - type: docs
    path: kcm missing unreachable taint issue
    url: https://github.com/kubernetes/kubernetes/issues/101674
    note: "node NotReady but NoExecute taint not applied"
  - type: docs
    path: node not deleted after cloud VM gone
    url: https://github.com/kubernetes/kubernetes/issues/92512
    note: "node stays NotReady; pods stuck Terminating"
relations:
  - type: see_also
    target: TROUBLE-KCM_VOLUME_MULTIATTACH
  - type: see_also
    target: CONCEPT-TROUBLESHOOTING_MAP
---

# controller-manager: node NotReady not evicted / not deleted / pods stuck

## Summary

The node-lifecycle controllers in kube-controller-manager can leave a bad node in a limbo
state: **NotReady but not tainted/evicted**, **still in Endpoints**, or **never deleted** after
the VM is gone — so pods aren't rescheduled and can hang `Terminating`.

## Problem

- Node `NotReady` but the expected `node.kubernetes.io/unreachable:NoExecute` taint is missing →
  taint-based eviction never fires, pods not rescheduled.
- Node `Ready=False` yet still renewing its Lease → its pods stay in Endpoints and receive
  traffic.
- Cloud VM deleted but the Node object persists NotReady; StatefulSet pods stuck `Terminating`.
- After a brief node flap, containers keep running `1/1` but pods stay `Ready=False`.

## Context

- Applies to Kubernetes **1.29–1.35** (node lifecycle is now via the external CCM for cloud
  deletion). Volume side-effects: [[TROUBLE-KCM_VOLUME_MULTIATTACH]].

## Diagnostics

- **Missing NoExecute taint:** races in the taint-manager around node-state transitions (a
  heartbeat arriving between taint applications) can skip the taint. Verify with
  `kubectl describe node`; check `--node-monitor-grace-period`; manually taint or `kubectl
  delete node` a genuinely dead node (issues #101674 / #80968).
- **Ready=False but lease still renewing:** the controller only reconciles the node's pod
  readiness once the Lease hasn't renewed past `nodeMonitorGracePeriod` — a live lease + Ready
  =False doesn't trigger it, so pods stay in Endpoints. **Cordon/drain or fully power off** so
  the lease stops (issue #125618).
- **Node not deleted after VM gone:** either the cloud provider can't confirm the VM is gone
  (declines the delete) or RBAC is missing (`cloud-node-lifecycle-controller ... cannot delete
  nodes`, `Node <name> no longer present in nodeLister!`). Ensure `system:controller:node-
  controller` RBAC; `kubectl delete node` after confirming the VM is gone (issues #92512/#102479).
- **Pods `Ready=False` after a flap:** kubelet didn't re-run `status_manager.syncPod()` after a
  brief apiserver disconnect — delete/restart the affected pods to force a re-sync (issue
  #120256).

## Known Issues

- A dead node holding an **RWO volume** additionally causes Multi-Attach errors on the
  replacement pod — [[TROUBLE-KCM_VOLUME_MULTIATTACH]].

## References

- kcm issues #101674/#80968/#125618/#92512/#102479/#120256 (above); volumes:
  [[TROUBLE-KCM_VOLUME_MULTIATTACH]].
