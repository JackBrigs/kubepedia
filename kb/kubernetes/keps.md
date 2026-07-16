---
id: CONCEPT-K8S_KEPS
type: concept
title: Notable KEPs driving Kubernetes 1.31–1.35 behaviour
status: active
kubespray_version: null
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - KEPs
  - Kubernetes Enhancement Proposals
  - enhancements 1.31 1.35
  - dynamic resource allocation DRA
  - node swap KEP
  - in-place pod resize KEP
  - nftables proxy KEP
  - user namespaces KEP
tags:
  - kubernetes
  - keps
  - enhancements
  - upgrade
sources:
  - type: code
    path: keps/ (directory tree)
    url: https://github.com/kubernetes/enhancements/tree/master/keps
    note: "KEP numbers and SIG ownership taken from the enhancements repo tree (verified)"
  - type: code
    path: pkg/features/kube_features.go
    url: https://raw.githubusercontent.com/kubernetes/kubernetes/v1.35.4/pkg/features/kube_features.go
    note: "stage-by-version confirmed from code"
relations:
  - type: see_also
    target: CONCEPT-K8S_FEATURE_GATES
  - type: see_also
    target: CONCEPT-K8S_1_33_CHANGES
  - type: see_also
    target: CONCEPT-K8S_1_35_CHANGES
---

# Notable KEPs driving Kubernetes 1.31–1.35 behaviour

## Summary

This is a **curated index** of the Kubernetes Enhancement Proposals whose graduations
change cluster behaviour across `1.31`–`1.35` — the "why" behind the feature-gate
flips in [[CONCEPT-K8S_FEATURE_GATES]] and the per-version change notes. It is not a
full KEP catalogue; it lists the operator-relevant enhancements with their **KEP
number + owning SIG** (verified from the `kubernetes/enhancements` tree) and their
**stage path in this range** (confirmed from `kube_features.go`). Use it for
traceability: each behaviour maps to a KEP you can read upstream.

## Context

- Applies to Kubernetes `1.31`–`1.35` (Kubespray `v2.29.0`–`v2.31.0`).
- "Stage path" shows the gate stage at each release inside our range;
  `GA*` = GA locked-to-default. Features that were already GA before `1.31` are
  listed only when they gained a notable sub-option in range.
- KEP directory names sometimes differ from the feature-gate name; the mapping below
  is by feature, not by literal string.

## Implementation

### Networking (SIG Network)

- **KEP-3866 — nftables proxy** → gate `NFTablesProxyMode`: Beta `1.31` → **GA
  `1.33`**. Production-ready `nftables` kube-proxy backend. Related **KEP-5343
  (nftables-to-default)** tracks making it the default and deprecating `ipvs`
  (`ipvs` deprecated in `1.35`, see [[CONCEPT-K8S_1_35_CHANGES]]).
- **KEP-536 — topology-aware routing** → gate `ServiceTrafficDistribution`: Beta
  `1.31` → **GA `1.33`** (`spec.trafficDistribution: PreferClose`).
- **KEP-2433 — topology-aware hints** → `TopologyAwareHints`: **GA `1.33`**. The
  older `service.kubernetes.io/topology-mode` annotation is deprecated in favour of
  `spec.trafficDistribution`.

### Node / workloads (SIG Node)

- **KEP-3063 — Dynamic Resource Allocation (DRA)** → `DynamicResourceAllocation`:
  Beta `1.32` → **GA `1.34`** → **locked `1.35`**. Structured GPU/device requests
  via ResourceClaims; admin-access namespace label required from `1.33`.
- **KEP-1287 — in-place Pod vertical scaling** → `InPlacePodVerticalScaling`: Beta
  `1.33` → **GA `1.35`**. Resize CPU/memory without restart; `status.resize`
  replaced by `PodResizeInProgress`/`PodResizePending` conditions in `1.33`.
- **KEP-2400 — node swap** → `NodeSwap`: **GA `1.34`** (kubelet swap;
  `kubelet_fail_swap_on`/`memorySwap.swapBehavior`).
- **KEP-127 — user namespaces** → `UserNamespacesSupport`: **Beta (on) `1.33`**.
- **KEP-3619 — supplemental groups policy** → `SupplementalGroupsPolicy`: Beta
  `1.33` → **GA `1.35`**.
- **KEP-4265 — proc mount** → `ProcMountType`: **Beta `1.33`**.
- **KEP-693 — topology manager policy options** → `TopologyManagerPolicyOptions`:
  **GA `1.32`**. **KEP-3570 — CPU manager** policy options → `CPUManagerPolicyOptions`:
  **GA `1.33`**.
- **KEP-2831 — kubelet tracing** → `KubeletTracing`: **GA `1.34`**.
- **KEP-4603 / KEP-5593 — CrashLoopBackOff tuning** → `KubeletCrashLoopBackOffMax`
  (per-node max backoff `1s`–`300s`, Beta by `1.35`) and cluster-wide
  `ReduceDefaultCrashLoopBackOffDecay`.

### cgroups (SIG Node)

- **KEP-2254 — cgroup v2** (long GA) underlies node cgroup behaviour.
- **KEP-4569 (cgroup v1 maintenance mode) / KEP-5573 (remove cgroup v1)** — drive the
  **`1.35` `failCgroupV1=true`** default: nodes refuse to start on cgroup v1. See
  [[CONCEPT-K8S_1_35_CHANGES]] and [[CONFIG-KUBELET_CONFIGURATION]].

### Storage (SIG Storage)

- **KEP-2644 — honor PV reclaim policy** → `HonorPVReclaimPolicy`: Beta `1.31` →
  **GA `1.33`**.
- **KEP-3751 — VolumeAttributesClass** → `VolumeAttributesClass`: **GA `1.34`**
  (mutable volume QoS/params).
- **KEP-4049 — storage-capacity scoring** → alpha `StorageCapacityScoring` in `1.33`
  (replaces `VolumeCapacityPriority`, inverts the default preference).

### Apps / scheduling / API

- **KEP-3998 — Job success/completion policy** → `JobSuccessPolicy`: **GA `1.33`**.
- **KEP-5080 — ordered namespace deletion** → `OrderedNamespaceDeletion`: **Beta
  (on) `1.33`** (deletes Pods before other resources for safer teardown).
- **KEP-3104 — kuberc** → kubeconfig `preferences` field deprecated in `1.34` in
  favour of the `kuberc` file.

## References

- KEP numbers/SIG: `kubernetes/enhancements` `keps/` tree (verified).
- Stage-by-version: `pkg/features/kube_features.go` (confirmed) — see
  [[CONCEPT-K8S_FEATURE_GATES]].
- Per-version operator notes: [[CONCEPT-K8S_1_32_CHANGES]],
  [[CONCEPT-K8S_1_33_CHANGES]], [[CONCEPT-K8S_1_34_CHANGES]],
  [[CONCEPT-K8S_1_35_CHANGES]].
