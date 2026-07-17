---
id: TROUBLE-KCM_VOLUME_MULTIATTACH
type: troubleshooting
title: "Multi-Attach error / RWO volume stuck attached after node loss"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - multi-attach error for volume
  - volume already exclusively attached to one node
  - out-of-service taint force detach
  - pod containercreating rwo node down
tags:
  - troubleshooting
  - controller-manager
  - storage
  - csi
sources:
  - type: docs
    path: Non-graceful node shutdown (GA 1.28)
    url: https://kubernetes.io/blog/2023/08/16/kubernetes-1-28-non-graceful-node-shutdown-ga/
    note: "out-of-service taint forces detach + pod deletion"
  - type: docs
    path: Node shutdown docs
    url: https://kubernetes.io/docs/concepts/cluster-administration/node-shutdown/
relations:
  - type: see_also
    target: TROUBLE-KCM_NODE_LIFECYCLE
  - type: see_also
    target: TROUBLE-PVC_PENDING_NO_PROVISIONER
---

# Multi-Attach error / RWO volume stuck attached after node loss

## Summary

After a node dies, a replacement pod using the same **RWO** volume is stuck `ContainerCreating`
with a **Multi-Attach** error, and there's a ~6-minute wait before force-detach. The
**out-of-service taint** (GA 1.28) cuts that wait once you've confirmed the node is off.

## Problem

- `Warning FailedAttachVolume Multi-Attach error for volume "pvc-…": Volume is already
  exclusively attached to one node and can't be attached to another`.
- Pod stuck `ContainerCreating` for minutes after a node loss.

## Context

- Applies to Kubernetes **1.29–1.35** (the remedy is GA since 1.28). Companion:
  [[TROUBLE-KCM_NODE_LIFECYCLE]].

## Diagnostics

- **Cause:** the RWO volume is still recorded as attached to the dead node (kubelet never ran
  detach), so the `VolumeAttachment` persists; the attach/detach controller waits ~6 minutes
  before force-detaching from an unreachable node.
- **Fast remedy (Non-Graceful Node Shutdown, GA 1.28):** after **confirming the node is powered
  off**, apply the taint **`node.kubernetes.io/out-of-service:NoExecute`** — this force-deletes
  the pods and triggers **immediate detach**, skipping the 6-minute wait. Remove the taint once
  the node is recovered/replaced.
- **Only taint a genuinely dead node** — applying it to a live node force-deletes its pods and
  detaches volumes (data risk).
- **Last resort:** delete the stale `VolumeAttachment` object manually.

## Known Issues

- Pair this with node deletion / eviction handling ([[TROUBLE-KCM_NODE_LIFECYCLE]]); a
  half-recovered node can re-attach. Genuine CSI attach limits are a different Pending cause
  ([[TROUBLE-PVC_PENDING_NO_PROVISIONER]]).

## References

- Non-graceful node shutdown GA blog + node-shutdown docs (above); PR #108486. Node lifecycle:
  [[TROUBLE-KCM_NODE_LIFECYCLE]].
