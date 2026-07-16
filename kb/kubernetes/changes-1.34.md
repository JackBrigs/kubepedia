---
id: CONCEPT-K8S_1_34_CHANGES
type: concept
title: Kubernetes 1.34 — operator-relevant changes
status: active
kubespray_version: null
kubernetes_version: "1.34"
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - kubernetes 1.34 changes
  - what changed in 1.34
  - 1.34 upgrade notes
tags:
  - kubernetes
  - upgrade
  - release-notes
sources:
  - type: docs
    path: CHANGELOG/CHANGELOG-1.34.md
    url: https://raw.githubusercontent.com/kubernetes/kubernetes/master/CHANGELOG/CHANGELOG-1.34.md
    note: "v1.34.0 Urgent Upgrade Notes + Changes by Kind (official changelog)"
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

# Kubernetes 1.34 — operator-relevant changes

## Summary

Kubernetes `1.34` is the **default** in Kubespray `v2.30.0` and supported through
`v2.31.0`. Headline items: **Dynamic Resource Allocation (DRA) core reaches GA**,
**swap (`NodeSwap`) reaches GA**, the kubelet drops the long-deprecated
`--cloud-config` flag, and a broad **metrics-label rename** across apiserver/etcd
metrics that will affect dashboards and alerts.

## Context

- Kubernetes `1.34`; Kubespray mapping: default in `v2.30.0`, supported in `v2.31.0`.
- Highlights are `v1.34.0` "Urgent Upgrade Notes" + code-confirmed graduations.

## Implementation

**Breaking / action required**

- **kubelet removed `--cloud-config`** — remove it from kubelet args before upgrading
  or the kubelet fails to start.
- **Static pods referencing API objects are now denied admission** by the kubelet
  (previously they could silently run after mirror-pod creation failed). Audit static
  pods that reference Secrets/ConfigMaps/etc.
- **Metrics label rename (dashboards/alerts action):** many apiserver/etcd metrics
  replace `resource_prefix`/`type`/`kind` labels with API `group`+`resource` labels
  (e.g. `etcd_request_duration_seconds`, `apiserver_cache_list_*`,
  `apiserver_watch_events_*`, `apiserver_storage_list_*`). Update Grafana/Prometheus
  rules that group by the old labels.

**Deprecations**

- kubeconfig `preferences` field deprecated in favour of **`kuberc`**.
- DRA kubelet gRPC API graduated to **v1** (`v1beta1` deprecated from 1.34).

**Behaviour changes**

- **DRA core GA:** Dynamic Resource Allocation is on by default (`DynamicResourceAllocation*`).
- **Swap GA:** `NodeSwap*` — kubelet swap support is GA.
- Container-level restart rules (alpha `ContainerRestartRules`) and `FileKeyRef`
  env-from-file (`EnvFiles` gate) introduced.
- In-place Pod resize gains a detailed completion event.

**Notable feature-gate graduations** (confirmed from code)

- GA (locked): `DynamicResourceAllocation`, `NodeSwap`, `VolumeAttributesClass`,
  `AuthorizeNodeWithSelectors`, `KubeletCgroupDriverFromCRI`, `KubeletTracing`,
  `RecoverVolumeExpansionFailure`, `MultiCIDRServiceAllocator`,
  `JobPodReplacementPolicy`, `RelaxedEnvironmentVariableValidation`.
- Beta (on): `PodLevelResources`, `PodObservedGenerationTracking`,
  `WindowsGracefulNodeShutdown`, `PreferSameTrafficDistribution`.

## References

- `v1.34.0` Urgent Upgrade Notes (CHANGELOG-1.34.md).
- Feature gates: [[CONCEPT-K8S_FEATURE_GATES]]; Kubespray window:
  [[CONCEPT-KUBERNETES_VERSION_SUPPORT]], [[UPGRADE-V2_30_0__V2_31_0]].
