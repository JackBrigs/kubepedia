---
id: CONCEPT-K8S_1_32_CHANGES
type: concept
title: Kubernetes 1.32 — operator-relevant changes
status: active
kubespray_version: null
kubernetes_version: "1.32"
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - kubernetes 1.32 changes
  - what changed in 1.32
  - 1.32 upgrade notes
tags:
  - kubernetes
  - upgrade
  - release-notes
sources:
  - type: docs
    path: CHANGELOG/CHANGELOG-1.32.md
    url: https://raw.githubusercontent.com/kubernetes/kubernetes/master/CHANGELOG/CHANGELOG-1.32.md
    note: "v1.32.0 Urgent Upgrade Notes + Changes by Kind (official changelog)"
  - type: code
    path: pkg/features/kube_features.go
    url: https://raw.githubusercontent.com/kubernetes/kubernetes/v1.35.4/pkg/features/kube_features.go
    note: "feature-gate stages confirmed from code"
relations:
  - type: see_also
    target: CONCEPT-K8S_FEATURE_GATES
  - type: see_also
    target: CONCEPT-K8S_API_REMOVALS
  - type: see_also
    target: UPGRADE-V2_29_1__V2_30_0
---

# Kubernetes 1.32 — operator-relevant changes

## Summary

Kubernetes `1.32` is the version Kubespray first ships as **default** in `v2.30.0`
and as **minimum** after `v2.30.0`. The single most important operator item at this
boundary is the **API removal of `flowcontrol.apiserver.k8s.io/v1beta3`** (see
[[CONCEPT-K8S_API_REMOVALS]] / [[API-FLOWCONTROL_APISERVER]]) — migrate those
manifests to `/v1` **before** upgrading. Beyond that, 1.32 removes a large batch of
long-GA feature gates and changes some kubelet/OOM defaults.

## Context

- Kubernetes `1.32`; Kubespray mapping: default in `v2.30.0`, still supported in
  `v2.31.0` only up to the window (`1.33`–`1.35`) — a cluster on `1.32` must move to
  `1.33`+ before adopting `v2.31.0`.
- Highlights below are the "Urgent Upgrade Notes" of `v1.32.0` plus code-confirmed
  feature-gate graduations; not an exhaustive changelog.

## Implementation

**Breaking / action required**

- **API removal:** `flowcontrol.apiserver.k8s.io/v1beta3` (FlowSchema,
  PriorityLevelConfiguration) is removed — use `/v1`. [[CONCEPT-K8S_API_REMOVALS]].
- **Feature-gate removals:** a large batch of long-GA gates is removed (e.g.
  `CPUManager`, `CSIMigrationAWS/AzureDisk/GCE`, `BoundServiceAccountTokenVolume`,
  `AggregatedDiscoveryEndpoint`, `AdmissionWebhookMatchConditions`,
  `APIListChunking`). Drop them from any explicit `--feature-gates`
  ([[CONCEPT-K8S_FEATURE_GATES]]).
- `DisableNodeKubeProxyVersion` reverted to **default-off** (extends the deprecation
  window for the `Node.Status…KubeProxyVersion` field).

**Behaviour changes**

- **kubelet OOM (cgroups v2):** new `singleProcessOOMKill` kubelet flag — when
  `true`, an OOM kill of a single process in a container no longer kills the whole
  container's process group. Review if you tune OOM behaviour.
- **Pod resize:** a new `/resize` subresource is added to request Pod resource
  resizing; clients that resize Pods must target `/resize`.
- `KubeletCrashLoopBackOffMax` (per-node max backoff, `1s`–`300s`) becomes settable
  via kubelet config.
- Alpha `AllowUnsafeMalformedObjectDeletion` adds an opt-in path to delete corrupt
  (undecryptable/undecodable) objects (`ignoreStoreReadErrorWithClusterBreakingPotential`).

**Notable feature-gate graduations** (confirmed from code)

- GA: `MemoryManager`, `TopologyManagerPolicyOptions`, `ServiceAccountTokenJTI`,
  `ServiceAccountTokenNodeBindingValidation`, `ServiceAccountTokenPodNodeInfo`.
- Beta (on): `AuthorizeNodeWithSelectors` (tighter Node authorizer),
  `RecoverVolumeExpansionFailure`, `SchedulerQueueingHints`, `SystemdWatchdog`,
  `JobManagedBy`. Beta (opt-in): `DynamicResourceAllocation`.

## References

- `v1.32.0` Urgent Upgrade Notes (CHANGELOG-1.32.md).
- Feature gates: [[CONCEPT-K8S_FEATURE_GATES]]; API removals:
  [[CONCEPT-K8S_API_REMOVALS]]; Kubespray crossing: [[UPGRADE-V2_29_1__V2_30_0]].
