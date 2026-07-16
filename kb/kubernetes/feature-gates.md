---
id: CONCEPT-K8S_FEATURE_GATES
type: concept
title: Kubernetes feature gates — graduations and removals across 1.31–1.35
status: active
kubespray_version: null
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - feature gates
  - removed feature gates
  - feature gate graduations
tags:
  - kubernetes
  - feature-gates
  - upgrade
sources:
  - type: code
    path: pkg/features/kube_features.go
    url: https://raw.githubusercontent.com/kubernetes/kubernetes/v1.35.4/pkg/features/kube_features.go
    note: "versioned feature-gate specs parsed from tag v1.35.4 (full stage history per gate)"
  - type: docs
    path: kubernetes.io feature-gates (removed)
    url: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates-removed/
    note: "authoritative list of removed feature gates per version"
relations:
  - type: see_also
    target: CONCEPT-KUBERNETES_VERSION_SUPPORT
  - type: see_also
    target: CONCEPT-K8S_API_REMOVALS
---

# Kubernetes feature gates — graduations and removals across 1.31–1.35

## Summary

A **feature gate** toggles a Kubernetes feature. Each gate moves through stages —
`Alpha` (off by default) → `Beta` (usually **on** by default) → `GA` (locked to
its default, cannot be disabled) — and is **removed** a few releases after GA. Two
things matter for operators upgrading a cluster:

1. **Graduations flip default behavior.** When a gate reaches `Beta` (on) or `GA`,
   a previously-off feature becomes active — even if you never set
   `--feature-gates`. This is the most common source of "behaviour changed after
   upgrade".
2. **Removed gates break start-up.** A removed gate can no longer be passed on the
   command line; any stale `--feature-gates=…` entry makes the component fail to
   start. Drop such entries once the gate is removed.

The stage tables below are **parsed from the Kubernetes source**
(`pkg/features/kube_features.go`, tag `v1.35.4`) and are therefore `confirmed` —
each gate's versioned spec records the exact release where its stage changed.
`*` = GA and **locked to default** (`LockToDefault`); `[off]` = Beta but default
**off** (opt-in).

## Context

- Applies to Kubernetes `1.31`–`1.35` (the versions Kubespray `v2.29.0`–`v2.31.0`
  install — see [[CONCEPT-KUBERNETES_VERSION_SUPPORT]]).
- Covers the Kubernetes-specific gates in `kube_features.go`. A handful of generic
  apiserver gates (e.g. flowcontrol) live in the apiserver staging tree and are not
  listed here; API-level removals are tracked separately in
  [[CONCEPT-K8S_API_REMOVALS]].
- Kubespray does not, by default, set explicit `--feature-gates`; these defaults
  apply as-is unless you override them in inventory.

## Implementation

### Notable graduations per version (behaviour-changing)

**Kubernetes 1.31** — new Beta (on by default):

- `NFTablesProxyMode` — kube-proxy `nftables` backend becomes usable (opt-in via
  `kube_proxy_mode`).
- `KubeletCgroupDriverFromCRI` — kubelet auto-detects the cgroup driver from the
  CRI, reducing driver-mismatch failures.
- `ServiceTrafficDistribution`, `MatchLabelKeysInPodAffinity`,
  `PortForwardWebsockets`, `RecursiveReadOnlyMounts`, `HonorPVReclaimPolicy`,
  `ServiceAccountTokenNodeBinding`.
- **Deprecated:** `DisableNodeKubeProxyVersion` (the `Node.Status.NodeInfo.KubeProxyVersion`
  field is being retired).

**Kubernetes 1.32** — new GA / new Beta:

- GA: `MemoryManager*`, `TopologyManagerPolicyOptions`, `ServiceAccountTokenJTI*`,
  `ServiceAccountTokenNodeBindingValidation*`, `ServiceAccountTokenPodNodeInfo*`.
- Beta (on): `AuthorizeNodeWithSelectors` (tighter Node authorizer),
  `RecoverVolumeExpansionFailure`, `RelaxedEnvironmentVariableValidation`,
  `SchedulerQueueingHints`, `SystemdWatchdog`, `JobManagedBy`.
- Beta (opt-in): `DynamicResourceAllocation [off]`.

**Kubernetes 1.33** — big graduation release:

- GA (locked): **`NFTablesProxyMode*`** (kube-proxy nftables is GA),
  `MultiCIDRServiceAllocator`, `ServiceTrafficDistribution*`, `AnyVolumeDataSource*`,
  `CPUManagerPolicyOptions*`, `MatchLabelKeysInPodAffinity*`,
  `RecursiveReadOnlyMounts*`, `TopologyAwareHints*`, `JobBackoffLimitPerIndex*`,
  `JobSuccessPolicy*`, `HonorPVReclaimPolicy*`.
- Beta (on): `InPlacePodVerticalScaling` (in-place Pod resize), `UserNamespacesSupport`,
  `SupplementalGroupsPolicy`, `OrderedNamespaceDeletion`, `ProcMountType`,
  `SchedulerAsyncPreemption`.

**Kubernetes 1.34** — new GA:

- GA (locked): **`DynamicResourceAllocation*`** (DRA core is GA), **`NodeSwap*`**,
  `VolumeAttributesClass`, `AuthorizeNodeWithSelectors*`, `KubeletCgroupDriverFromCRI*`,
  `KubeletTracing*`, `RecoverVolumeExpansionFailure*`, `MultiCIDRServiceAllocator*`,
  `JobPodReplacementPolicy*`, `RelaxedEnvironmentVariableValidation*`.
- Beta (on): `PodLevelResources`, `PodObservedGenerationTracking`,
  `WindowsGracefulNodeShutdown`, `PreferSameTrafficDistribution`.

**Kubernetes 1.35** — new GA / new Beta:

- GA (locked): **`InPlacePodVerticalScaling*`** (in-place resize is GA),
  `DynamicResourceAllocation*` (locked — can no longer be disabled),
  `SupplementalGroupsPolicy*`, `PodObservedGenerationTracking*`, `ImageMaximumGCAge*`,
  `ExecProbeTimeout*`, `PreferSameTrafficDistribution*`, `SystemdWatchdog*`,
  `JobManagedBy*`.
- Beta (on): `ImageVolume`, `ContainerRestartRules`, `EnvFiles`, `HostnameOverride`,
  `HPAConfigurableTolerance`, `KubeletCrashLoopBackOffMax`,
  `DeploymentReplicaSetTerminatingReplicas`.

### Removed gates (must not appear in `--feature-gates`)

A removed gate is one whose GA behaviour has been locked long enough that the flag
itself is deleted. Referencing it aborts start-up. Notable batches:

- **v1.31** removes e.g. `AppArmor`, `AppArmorFields`, `CloudDualStackNodeIPs`,
  `DisableCloudProviders`, `DisableKubeletCloudCredentialProviders`.
- **v1.32** removes a large batch of long-GA gates, e.g. `CPUManager`,
  `CSIMigrationAWS`, `CSIMigrationAzureDisk`, `CSIMigrationGCE`,
  `BoundServiceAccountTokenVolume`, `AggregatedDiscoveryEndpoint`,
  `AdmissionWebhookMatchConditions`, `APIListChunking`.
- **v1.33–v1.35** continue removing individual GA-locked gates.

Removing a locked/removed gate from your configuration is behaviourally a no-op —
it only avoids the start-up failure from referencing an unknown gate.

## References

- Source of truth for stages: `pkg/features/kube_features.go` at each tag
  (parsed from `v1.35.4`, which carries the full versioned history).
- Removed-gate list: Kubernetes "Feature Gates (removed)" reference (kubernetes.io).
- Per-version operator highlights: [[CONCEPT-K8S_1_32_CHANGES]],
  [[CONCEPT-K8S_1_33_CHANGES]], [[CONCEPT-K8S_1_34_CHANGES]],
  [[CONCEPT-K8S_1_35_CHANGES]].
- Kubespray version→Kubernetes mapping: [[CONCEPT-KUBERNETES_VERSION_SUPPORT]].
