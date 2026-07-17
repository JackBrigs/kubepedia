---
id: TROUBLE-SCHEDULER_TOPOLOGY_SPREAD
type: troubleshooting
title: "kube-scheduler: PodTopologySpread keeps pods Pending / skew regressions"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - didn't match pod topology spread constraints
  - maxskew donotschedule pending
  - minDomains ignored
  - matchLabelKeys spread regression 1.34
tags:
  - troubleshooting
  - scheduler
  - topology-spread
  - scheduling
sources:
  - type: docs
    path: Pod topology spread constraints
    url: https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/
    note: "whenUnsatisfiable, maxSkew, minDomains, matchLabelKeys, node policies"
relations:
  - type: see_also
    target: TROUBLE-SCHEDULER_POD_PENDING
  - type: see_also
    target: CONCEPT-TROUBLESHOOTING_MAP
---

# kube-scheduler: PodTopologySpread keeps pods Pending / skew regressions

## Summary

Replicas stay `Pending` with `node(s) didn't match pod topology spread constraints`, or spread
behaviour **changes after an upgrade**. Topology spread is easy to make a hard blocker; a few
version-specific graduations also shift behaviour.

## Problem

- `FailedScheduling ... node(s) didn't match pod topology spread constraints`; pods Pending
  when one domain (zone/node) is full.
- Spread suddenly behaves differently right after upgrading to 1.33/1.34.

## Context

- Applies to Kubernetes **1.29–1.35**. Companion to [[TROUBLE-SCHEDULER_POD_PENDING]].

## Diagnostics

- **`whenUnsatisfiable: DoNotSchedule` is a HARD constraint** (the default): if placing the pod
  would exceed **`maxSkew`** on every feasible node, it stays Pending. Use **`ScheduleAnyway`**
  for a soft preference where Pending is worse than imbalance.
- **`minDomains` "ignored":** `minDomains` (valid only with `DoNotSchedule`) treats the global
  minimum as 0 until that many eligible domains exist. The gate `MinDomainsInPodTopologySpread`
  is default-on since 1.28 (field available by default from 1.30; can be disabled on 1.29).
- **`matchLabelKeys` regression after 1.34:** `matchLabelKeys` computes skew per rollout
  revision (e.g. `pod-template-hash`). In **1.34** kube-apiserver now merges those keys into the
  `labelSelector` (previously done implicitly in the scheduler plugin); the new default-on gate
  **`MatchLabelKeysInPodTopologySpreadSelectorMerge`** reverts to the old behaviour if disabled
  — toggle it if spread regresses right after the 1.34 upgrade.
- **Node policies GA at 1.33:** `nodeAffinityPolicy`/`nodeTaintsPolicy`
  (`NodeInclusionPolicyInPodTopologySpread`) are GA in 1.33 — they change which nodes count
  toward domains.

## Known Issues

- Combining tight `maxSkew: 1` + `DoNotSchedule` + few domains is the classic "won't schedule"
  trap — loosen `maxSkew` or use `ScheduleAnyway`.

## References

- Pod topology spread docs (above); pending triage: [[TROUBLE-SCHEDULER_POD_PENDING]].
