---
id: CONCEPT-K8S_1_35_CHANGES
type: concept
title: Kubernetes 1.35 — operator-relevant changes
status: active
kubespray_version: null
kubernetes_version: "1.35"
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - kubernetes 1.35 changes
  - what changed in 1.35
  - 1.35 upgrade notes
  - cgroup v1 deprecation
tags:
  - kubernetes
  - upgrade
  - release-notes
sources:
  - type: docs
    path: CHANGELOG/CHANGELOG-1.35.md
    url: https://raw.githubusercontent.com/kubernetes/kubernetes/master/CHANGELOG/CHANGELOG-1.35.md
    note: "v1.35.0 Urgent Upgrade Notes + Changes by Kind (official changelog)"
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

# Kubernetes 1.35 — operator-relevant changes

## Summary

Kubernetes `1.35` is the **default** in Kubespray `v2.31.0` (paired with **etcd
3.6**). It carries the most disruptive operator action in the whole range: **cgroup
v1 is now an error by default** — nodes will **not start** on a cgroup v1 host unless
you explicitly opt out. It also removes the kubelet `--pod-infra-container-image`
flag, deprecates **kube-proxy `ipvs` mode**, and GA-locks in-place Pod resize and DRA.

## Context

- Kubernetes `1.35`; Kubespray mapping: **default** in `v2.31.0`.
- Highlights are `v1.35.0` "Urgent Upgrade Notes" + code-confirmed graduations.

## Implementation

**Breaking / action required**

- **cgroup v1 → error by default (`failCgroupV1=true` from 1.35).** Nodes will not
  start on a cgroup v1 host. `kubeadm` `init`/`join`/`upgrade` SystemVerification
  preflight now **errors** (not warns) when cgroup v1 is detected with kubelet
  `v1.35`+. To keep running on cgroup v1 you must (a) ignore that preflight error and
  (b) set `failCgroupV1: false` in the `kube-system/kubelet-config` ConfigMap **before**
  upgrading. Strongly prefer migrating hosts to **cgroup v2** instead.
- **kubelet removed `--pod-infra-container-image`.** Non-kubeadm clusters must remove
  this flag from the kubelet config manually or the kubelet fails to start. For
  kubeadm clusters, remove it from `extraArgs` if you set it.
- **StorageVersionMigration `v1alpha1` removed** (only `v1beta1` remains) — delete any
  `v1alpha1` StorageVersionMigration resources before upgrading.

**Deprecations**

- **kube-proxy `ipvs` mode deprecated** (to be removed later) — migrate to
  **`nftables`** (`kube_proxy_mode: nftables`; nftables is GA since 1.33). See
  [[CONCEPT-K8S_1_33_CHANGES]].

**Behaviour changes**

- **In-place Pod vertical scaling is GA** (`InPlacePodVerticalScaling*`).
- **DRA core locked GA** (`DynamicResourceAllocation*` can no longer be disabled).
- **`kubectl get -o kyaml` enabled by default** (disable with `KUBECTL_KYAML=false`).
- `--min-compatibility-version` flag added to apiserver/controller-manager/scheduler
  (emulated-version compatibility).
- CSI drivers can opt into receiving SA tokens via the secrets field
  (`CSIServiceAccountTokenSecrets`, Beta) to avoid token exposure in logs.
- Alpha `RestartAllContainersOnContainerExit` restarts all containers when a source
  container in a restart rule exits.

**Notable feature-gate graduations** (confirmed from code)

- GA (locked): `InPlacePodVerticalScaling`, `DynamicResourceAllocation` (locked),
  `SupplementalGroupsPolicy`, `PodObservedGenerationTracking`, `ImageMaximumGCAge`,
  `ExecProbeTimeout`, `PreferSameTrafficDistribution`, `SystemdWatchdog`, `JobManagedBy`.
- Beta (on): `ImageVolume`, `ContainerRestartRules`, `EnvFiles`, `HostnameOverride`,
  `HPAConfigurableTolerance`, `KubeletCrashLoopBackOffMax`,
  `DeploymentReplicaSetTerminatingReplicas`.

## References

- `v1.35.0` Urgent Upgrade Notes (CHANGELOG-1.35.md).
- Feature gates: [[CONCEPT-K8S_FEATURE_GATES]]; Kubespray window:
  [[CONCEPT-KUBERNETES_VERSION_SUPPORT]], [[UPGRADE-V2_30_0__V2_31_0]].
