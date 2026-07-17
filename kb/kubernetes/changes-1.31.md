---
id: CONCEPT-K8S_1_31_CHANGES
type: concept
title: "Kubernetes 1.31 — operator-relevant changes"
status: active
kubespray_version: null
kubernetes_version: "1.31"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - kubernetes 1.31 changes
  - what changed in 1.31
  - 1.31 upgrade notes
  - nftables kube-proxy 1.31
  - kubelet cgroup driver from cri
tags:
  - kubernetes
  - upgrade
  - release-notes
sources:
  - type: docs
    path: CHANGELOG/CHANGELOG-1.31.md
    url: https://raw.githubusercontent.com/kubernetes/kubernetes/master/CHANGELOG/CHANGELOG-1.31.md
    note: "v1.31.0 changelog (official)"
  - type: code
    path: pkg/features/kube_features.go
    url: https://raw.githubusercontent.com/kubernetes/kubernetes/v1.35.4/pkg/features/kube_features.go
    note: "feature-gate stages confirmed from code"
relations:
  - type: see_also
    target: CONCEPT-K8S_FEATURE_GATES
  - type: see_also
    target: CONCEPT-K8S_1_30_CHANGES
  - type: see_also
    target: CONCEPT-K8S_1_32_CHANGES
  - type: see_also
    target: CONCEPT-KUBERNETES_VERSION_SUPPORT
---

# Kubernetes 1.31 — operator-relevant changes

## Summary

Kubernetes `1.31` ("Elli") is the **minimum** version for Kubespray `v2.29.0` and the floor of
its 1.31–1.33 window. Headline operator items: the **nftables kube-proxy backend** reaches Beta,
the kubelet can **auto-detect the cgroup driver from the CRI** (fewer driver-mismatch
failures), and a batch of long-GA **feature gates is removed** — including the AppArmor and
in-tree cloud-provider gates.

## Context

- Kubernetes `1.31`; Kubespray mapping: the **default/minimum** for `v2.29.0`
  ([[CONCEPT-KUBERNETES_VERSION_SUPPORT]]).
- Highlights are the `v1.31.0` changelog + code-confirmed feature-gate stages.

## Implementation

**Behaviour changes / new capabilities**

- **`NFTablesProxyMode` (Beta):** kube-proxy gains a usable **`nftables`** backend — an
  alternative to `iptables` that scales better on large Services. Opt in via the proxy mode
  (`kube_proxy_mode: nftables` in Kubespray). It later goes **GA in 1.33**
  ([[CONCEPT-K8S_1_33_CHANGES]]).
- **`KubeletCgroupDriverFromCRI` (Beta):** the kubelet auto-detects the cgroup driver from the
  container runtime instead of relying on matching static config — reduces the classic
  cgroup-driver-mismatch node failure ([[TROUBLE-CGROUP_DRIVER_MISMATCH]]).
- **`RecursiveReadOnlyMounts` (Beta):** truly read-only mounts (incl. submounts).
- Also Beta (on): `ServiceTrafficDistribution` (topology-aware routing preference),
  `MatchLabelKeysInPodAffinity`, `PortForwardWebsockets`, `HonorPVReclaimPolicy`,
  `ServiceAccountTokenNodeBinding`.

**Deprecations**

- **`DisableNodeKubeProxyVersion`:** the `Node.Status.NodeInfo.KubeProxyVersion` field is being
  retired (it was never reliable) — don't depend on it.

## Compatibility

- **Removed feature gates** (must not appear in `--feature-gates` — referencing a removed gate
  aborts start-up): the **AppArmor** gates (`AppArmor`, `AppArmorFields` — AppArmor is GA via
  the `securityContext.appArmorProfile` fields), and the in-tree cloud-provider gates
  (`CloudDualStackNodeIPs`, `DisableCloudProviders`,
  `DisableKubeletCloudCredentialProviders`). Drop any stale entries before upgrading.
- **No major API-version removals** in 1.31 (the flow-control `v1beta3` removal is 1.32 —
  [[CONCEPT-K8S_API_REMOVALS]]).

## References

- `v1.31.0` changelog; feature gates: [[CONCEPT-K8S_FEATURE_GATES]]; API removals:
  [[CONCEPT-K8S_API_REMOVALS]]; adjacent: [[CONCEPT-K8S_1_30_CHANGES]],
  [[CONCEPT-K8S_1_32_CHANGES]]; version window: [[CONCEPT-KUBERNETES_VERSION_SUPPORT]].
