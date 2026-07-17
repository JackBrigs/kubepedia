---
id: TROUBLE-CONTROL_PLANE_LEADER_ELECTION
type: troubleshooting
title: "Control plane: scheduler / controller-manager restart on lease renewal"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - failed to renew lease context deadline exceeded
  - leaderelection lost
  - kube-scheduler crashloop lease
  - kube-controller-manager crashloop lease
tags:
  - troubleshooting
  - control-plane
  - leader-election
  - scheduler
  - controller-manager
sources:
  - type: docs
    path: kube-controller-manager lease-renewal issue
    url: https://github.com/kubernetes/kubernetes/issues/74340
    note: "failed to renew lease → process exits"
  - type: docs
    path: kube-scheduler lease-renewal issue
    url: https://github.com/kubernetes/kubernetes/issues/87800
    note: "scheduler flapping on lease renew"
relations:
  - type: see_also
    target: TROUBLE-ETCD_QUORUM_LOSS
  - type: see_also
    target: CONCEPT-TROUBLESHOOTING_MAP
---

# Control plane: scheduler / controller-manager restart on lease renewal

## Summary

`kube-scheduler` or `kube-controller-manager` logs `failed to renew lease … context deadline
exceeded`, then `leaderelection lost` and the process **exits** (CrashLoopBackOff, forced
re-election). This is almost always **etcd/apiserver latency**, not a bug in the component.

## Problem

- Logs: `failed to renew lease kube-system/kube-{scheduler,controller-manager}: failed to
  tryAcquireOrRenew context deadline exceeded` → process restarts.
- While flapping: scheduling stalls; pending CSRs; node status/eviction not reconciled;
  workloads not scaled.

## Context

- Applies to Kubernetes **1.29–1.35** — both components use the same lease-based leader
  election, so both fail this way.

## Diagnostics

- **Root cause is usually latency:** the leader can't round-trip the lease update within
  `renewDeadline`. Check **etcd** health (`etcd_disk_wal_fsync_duration_seconds`,
  `etcd_disk_backend_commit_duration_seconds`, disk IO), apiserver latency, CPU throttling on
  the control-plane, and network loss ([[TROUBLE-ETCD_QUORUM_LOSS]]).
- **Tune only after fixing latency** (if flaps persist on a healthy but high-latency setup):
  raise `--leader-elect-lease-duration`, `--leader-elect-renew-deadline`,
  `--leader-elect-retry-period` — keep `renew-deadline < lease-duration`.
- **Confirm it's just re-election, not a real outage:** a single flap re-elects a new leader and
  service resumes; repeated flaps point at sustained control-plane pressure.

## Known Issues

- The **etcd defrag/upgrade** briefly stalls in-flight apiserver requests, which can trip a lease
  renewal — expect a transient re-election during maintenance.

## References

- kube-controller-manager #74340, kube-scheduler #87800 (above); etcd:
  [[TROUBLE-ETCD_QUORUM_LOSS]].
