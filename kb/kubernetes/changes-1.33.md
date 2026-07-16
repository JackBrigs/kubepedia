---
id: CONCEPT-K8S_1_33_CHANGES
type: concept
title: Kubernetes 1.33 — operator-relevant changes
status: active
kubespray_version: null
kubernetes_version: "1.33"
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - kubernetes 1.33 changes
  - what changed in 1.33
  - 1.33 upgrade notes
tags:
  - kubernetes
  - upgrade
  - release-notes
sources:
  - type: docs
    path: CHANGELOG/CHANGELOG-1.33.md
    url: https://raw.githubusercontent.com/kubernetes/kubernetes/master/CHANGELOG/CHANGELOG-1.33.md
    note: "v1.33.0 Urgent Upgrade Notes + Changes by Kind (official changelog)"
  - type: code
    path: pkg/features/kube_features.go
    url: https://raw.githubusercontent.com/kubernetes/kubernetes/v1.35.4/pkg/features/kube_features.go
    note: "feature-gate stages confirmed from code"
relations:
  - type: see_also
    target: CONCEPT-K8S_FEATURE_GATES
  - type: see_also
    target: CONCEPT-KUBERNETES_VERSION_SUPPORT
  - type: see_also
    target: UPGRADE-V2_30_0__V2_31_0
---

# Kubernetes 1.33 — operator-relevant changes

## Summary

Kubernetes `1.33` is the **minimum** version in Kubespray `v2.31.0`. It is a heavy
graduation release: **kube-proxy `nftables` mode reaches GA**, in-place Pod resize
goes Beta, and several networking APIs are deprecated in favour of newer ones
(`v1 Endpoints` → EndpointSlice, topology-mode annotation → `spec.trafficDistribution`).
No API **removals** land in 1.33.

## Context

- Kubernetes `1.33`; Kubespray mapping: supported from `v2.29.0` onward, **minimum**
  in `v2.31.0`.
- Highlights are `v1.33.0` "Urgent Upgrade Notes" + code-confirmed graduations.

## Implementation

**Deprecations (still supported, plan migration)**

- **`v1 Endpoints` API officially deprecated** (not removed) — migrate consumers to
  the **EndpointSlice** API.
- **EndpointSlice `hints` GA**; the beta annotation
  `service.kubernetes.io/topology-mode` is deprecated and will **not** graduate —
  use the Service `spec.trafficDistribution` field for topology-aware routing.
- **Pod `status.resize` deprecated** and no longer set — resize state is now exposed
  via two conditions: `PodResizeInProgress` and `PodResizePending`. Update anything
  that reads `status.resize`.
- `WatchFromStorageWithoutResourceVersion` deprecated and can no longer be enabled.

**Behaviour changes**

- **kube-proxy nftables is GA** (`NFTablesProxyMode*` locked). The `nftables` backend
  is production-ready; still opt-in via `kube_proxy_mode` in Kubespray.
- **In-place Pod vertical scaling (Beta, on):** resize CPU/memory without restart,
  including Pods with sidecars (`initContainers` with `restartPolicy: Always`).
- **DRA admin access:** from 1.33, only users with access to a namespace labelled
  `kubernetes.io/dra-admin-access` may create ResourceClaim/ResourceClaimTemplate
  with `adminAccess`.
- **DRA scheduling:** asking for "All" devices now only picks nodes with **≥1**
  device (was: schedule anywhere). Max Pods per ResourceClaim raised 32 → 256
  (downgrade to 1.32.0 unsupported if used).
- HPA gains a per-object `tolerance` field (alpha `HPAConfigurableTolerance`).
- CrashLoopBackOff decay can be reduced cluster-wide via the
  `ReduceDefaultCrashLoopBackOffDecay` gate (recommended `1s`/`60s`).

**Notable feature-gate graduations** (confirmed from code)

- GA (locked): `NFTablesProxyMode`, `MultiCIDRServiceAllocator`,
  `ServiceTrafficDistribution`, `AnyVolumeDataSource`, `CPUManagerPolicyOptions`,
  `MatchLabelKeysInPodAffinity`, `RecursiveReadOnlyMounts`, `TopologyAwareHints`,
  `JobBackoffLimitPerIndex`, `JobSuccessPolicy`, `HonorPVReclaimPolicy`.
- Beta (on): `InPlacePodVerticalScaling`, `UserNamespacesSupport`,
  `SupplementalGroupsPolicy`, `OrderedNamespaceDeletion`, `ProcMountType`,
  `SchedulerAsyncPreemption`.

## References

- `v1.33.0` Urgent Upgrade Notes (CHANGELOG-1.33.md).
- Feature gates: [[CONCEPT-K8S_FEATURE_GATES]]; Kubespray window:
  [[CONCEPT-KUBERNETES_VERSION_SUPPORT]], [[UPGRADE-V2_30_0__V2_31_0]].
