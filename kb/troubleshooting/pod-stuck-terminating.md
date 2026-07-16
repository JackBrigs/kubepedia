---
id: TROUBLE-POD_STUCK_TERMINATING
type: troubleshooting
title: "Pod stuck in Terminating"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: probable
aliases:
  - pod-stuck-terminating
tags:
  - troubleshooting
  - operations
  - operations
sources:
  - type: docs
    url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
    note: "Pod lifecycle / finalizers"
relations:
  - type: see_also
    target: PRACTICE-NODE_NOT_READY
---

# Pod stuck in Terminating

## Summary

A pod stays `Terminating` indefinitely after deletion.

## Problem

Usual causes: a **finalizer** that never completes, a **lost node** (kubelet gone, so it cannot confirm deletion), or a container that ignores SIGTERM until the grace period. On a lost node, the pod is not force-deleted automatically.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0` clusters. This is a general Kubernetes/component operational issue (not tied to one Kubespray version); the relevant tunables are noted in Known Issues.

## Diagnostics

```bash
kubectl get pod <p> -o jsonpath="{.metadata.finalizers}"   # stuck finalizer?
kubectl get pod <p> -o wide                                # is its node Ready?
kubectl describe pod <p> | tail -20
```

## Known Issues

If a node is gone, cordon/remove it (PRACTICE-NODE_NOT_READY / PLAYBOOK-REMOVE_NODE) so pods reschedule. Remove a stuck finalizer only when you understand the controller. Force delete as a last resort: `kubectl delete pod <p> --grace-period=0 --force` (does NOT clean up on a dead node).

## References

- https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/ — Pod lifecycle / finalizers (verified behavior, 2026-07-16).
