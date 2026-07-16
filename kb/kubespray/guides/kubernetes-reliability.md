---
id: PRACTICE-KUBERNETES_RELIABILITY
type: best_practice
title: "Node failure detection tuning (kubelet ↔ controller-manager)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - kubernetes-reliability
tags:
  - operations
  - reliability
sources:
  - type: docs
    path: docs/advanced/kubernetes-reliability.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/advanced/kubernetes-reliability.md
    note: "digest of the tag doc"
relations:
  - type: see_also
    target: PRACTICE-NODE_NOT_READY
---

# Node failure detection tuning (kubelet ↔ controller-manager)

## Summary

How fast the cluster detects and reacts to a failed node is governed by a few timing parameters. Defaults trade detection speed for stability; tune them for faster failover at the cost of more API/etcd load and false positives.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`.
- Relevant when a node dies and you want workloads rescheduled sooner (or fewer false NotReady flaps).

## Implementation

Key timings: kubelet posts status every `--node-status-update-frequency` (default **10s**); controller-manager checks every `--node-monitor-period` (**5s**) and marks a node unhealthy after `--node-monitor-grace-period` (**40s**). These work asynchronously, so real detection includes network/API/etcd latency. Lowering them speeds failover but increases control-plane load and false NotReady under latency — change carefully and test. Pairs with pod eviction/tolerations for the reschedule behavior.

## References

- `docs/advanced/kubernetes-reliability.md` (tag v2.31.0 `1c9add4`).
