---
id: TROUBLE-DISK_PRESSURE_EVICTION
type: troubleshooting
title: "DiskPressure: pods evicted, images garbage-collected"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - disk-pressure-eviction
tags:
  - troubleshooting
  - operations
  - operations
sources:
  - type: docs
    url: https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/
    note: "node-pressure eviction"
relations:
  - type: see_also
    target: PRACTICE-NODE_NOT_READY
---

# DiskPressure: pods evicted, images garbage-collected

## Summary

Pods are evicted with `The node was low on resource: ephemeral-storage` / `DiskPressure`, and the node may flap NotReady.

## Problem

kubelet enforces eviction thresholds; when the node/imagefs free space drops below them it evicts pods and garbage-collects images. Common on nodes with small `/var/lib/containerd` or heavy log/image churn.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0` clusters. This is a general Kubernetes/component operational issue (not tied to one Kubespray version); the relevant tunables are noted in Known Issues.

## Diagnostics

```bash
kubectl describe node <node> | grep -iE "DiskPressure|ephemeral"
df -h /var/lib/containerd /var/lib/kubelet /var
crictl images | wc -l          # image bloat?
```

## Known Issues

Free space / grow the disk; prune unused images; set/verify `system_reserved` and eviction thresholds; move container/kubelet dirs to a larger volume. See PRACTICE-NODE_NOT_READY.

## References

- https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/ — node-pressure eviction (verified behavior, 2026-07-16).
