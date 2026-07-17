---
id: TROUBLE-SCHEDULER_PERF
type: troubleshooting
title: "kube-scheduler: slow scheduling / clumped placement / requeue OOM"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - scheduler slow at scale
  - percentageOfNodesToScore
  - scheduler_e2e_scheduling_duration_seconds
  - queueinghint scheduler oom
tags:
  - troubleshooting
  - scheduler
  - performance
  - scale
sources:
  - type: docs
    path: Scheduler performance tuning
    url: https://kubernetes.io/docs/concepts/scheduling-eviction/scheduler-perf-tuning/
    note: "percentageOfNodesToScore ramp"
  - type: docs
    path: QueueingHint blog (v1.32)
    url: https://kubernetes.io/blog/2024/12/12/scheduler-queueinghint/
    note: "SchedulerQueueingHints requeue behaviour"
relations:
  - type: see_also
    target: TROUBLE-SCHEDULER_POD_PENDING
  - type: see_also
    target: CONCEPT-TROUBLESHOOTING_MAP
---

# kube-scheduler: slow scheduling / clumped placement / requeue OOM

## Summary

At scale the scheduler is either **slow** (too many nodes scored per pod) or **clumps** pods
(too few scored), and older `SchedulerQueueingHints` behaviour caused requeue anomalies/OOM.
Watch `scheduler_e2e_scheduling_duration_seconds`.

## Problem

- High scheduling latency / throughput bottleneck on large clusters.
- Pods clump onto few nodes instead of spreading.
- Scheduler memory spikes / OOM, or unschedulable pods requeue slowly.

## Context

- Applies to Kubernetes **1.29–1.35** (large clusters). Companion:
  [[TROUBLE-SCHEDULER_POD_PENDING]].

## Diagnostics

- **`percentageOfNodesToScore`** caps how many feasible nodes are scored per cycle. The default
  is a linear ramp (~50% at 100 nodes down to a 5% floor near 5000). **Keep the default** for
  small/medium clusters; **lower** it only when throughput matters more than optimal placement
  (setting `0` uses the compiled-in default). Too low → clumped placement; too high → latency.
- **Metrics:** `scheduler_e2e_scheduling_duration_seconds`, `scheduler_pending_pods`,
  `scheduler_schedule_attempts_total`, `scheduler_scheduling_attempt_duration_seconds` show
  where time goes.
- **`SchedulerQueueingHints`:** requeues unschedulable pods only when a plugin hint returns
  `Queue`. The first default-on attempt caused scheduler OOM and was defaulted back off in the
  1.28 line, then reworked and enabled by default around **1.32**. If you see requeue anomalies
  or scheduler OOM around those versions, check the gate state.

## Known Issues

- Aggressively lowering `percentageOfNodesToScore` trades placement quality for speed — verify
  spread/utilization after tuning.

## References

- Scheduler perf-tuning + QueueingHint blog (above). Pending triage:
  [[TROUBLE-SCHEDULER_POD_PENDING]].
