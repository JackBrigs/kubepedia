---
id: CONCEPT-K8S_1_29_CHANGES
type: concept
title: "Kubernetes 1.29 — operator-relevant changes"
status: active
kubespray_version: null
kubernetes_version: "1.29"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - kubernetes 1.29 changes
  - what changed in 1.29
  - 1.29 upgrade notes
  - sidecar containers 1.29
  - kubeadm super-admin.conf
tags:
  - kubernetes
  - upgrade
  - release-notes
sources:
  - type: docs
    path: CHANGELOG/CHANGELOG-1.29.md
    url: https://raw.githubusercontent.com/kubernetes/kubernetes/master/CHANGELOG/CHANGELOG-1.29.md
    note: "v1.29.0 Urgent Upgrade Notes (official changelog)"
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
    target: CONCEPT-KUBERNETES_VERSION_SUPPORT
---

# Kubernetes 1.29 — operator-relevant changes

## Summary

Kubernetes `1.29` is the **minimum** Kubernetes version for early Kubespray in the
extended range (`v2.27.0` sets `kube_version_min_required: 1.29.0`). Headline operator
items: **native sidecar containers** reach Beta (on), kubeadm splits the admin credential
into **`admin.conf` (kubeadm:cluster-admins)** and **`super-admin.conf` (system:masters)**,
and the API-priority-and-fairness **`v1beta2`** API is removed.

## Context

- Kubernetes `1.29`; Kubespray mapping: the **floor** of the extended range
  (`v2.27.0`–`v2.28.x` support it; `v2.29.0` raises the minimum).
- Highlights are `v1.29.0` "Urgent Upgrade Notes" + code-confirmed feature-gate
  graduations.

## Implementation

**Breaking / action required**

- **API removal:** `flowcontrol.apiserver.k8s.io/v1beta2` (FlowSchema,
  PriorityLevelConfiguration) is removed — use `v1beta3`/`v1`. See
  [[CONCEPT-K8S_API_REMOVALS]].
- **kubeadm admin credential split:** a new **`super-admin.conf`** is deployed bound to
  the `system:masters` break-glass group; the regular **`admin.conf`** User is now bound
  to the new **`kubeadm:cluster-admins`** RBAC group (with `cluster-admin` ClusterRole)
  instead of `system:masters`. `kubeadm init`/`upgrade apply` migrate to the two-file
  setup; `kubeadm join --control-plane` generates only the less-privileged `admin.conf`.
  (Kubespray adopts `kubeadm:cluster-admins` for its admin kubeconfig in later releases.)
- `kubeadm upgrade plan --config` stops accepting kube-proxy/kubelet component config.

**Behaviour changes**

- **Native sidecar containers (Beta, on):** `initContainers` with `restartPolicy: Always`
  run for the Pod's lifetime — the supported way to do sidecars (no more hacks).

**Notable feature-gate graduations** (confirmed from code)

- Beta (on): `SidecarContainers`, `JobBackoffLimitPerIndex`, `JobPodReplacementPolicy`,
  `PodReadyToStartContainersCondition`, `SeparateTaintEvictionController`.

## References

- `v1.29.0` Urgent Upgrade Notes (CHANGELOG-1.29.md). Feature gates:
  [[CONCEPT-K8S_FEATURE_GATES]]; API removals: [[CONCEPT-K8S_API_REMOVALS]]; version
  window: [[CONCEPT-KUBERNETES_VERSION_SUPPORT]].
