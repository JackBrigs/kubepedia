---
id: CONCEPT-K8S_1_30_CHANGES
type: concept
title: "Kubernetes 1.30 — operator-relevant changes"
status: active
kubespray_version: null
kubernetes_version: "1.30"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - kubernetes 1.30 changes
  - what changed in 1.30
  - 1.30 upgrade notes
  - validatingadmissionpolicy GA
  - node swap beta
tags:
  - kubernetes
  - upgrade
  - release-notes
sources:
  - type: docs
    path: CHANGELOG/CHANGELOG-1.30.md
    url: https://raw.githubusercontent.com/kubernetes/kubernetes/master/CHANGELOG/CHANGELOG-1.30.md
    note: "v1.30.0 changelog (official)"
  - type: code
    path: pkg/features/kube_features.go
    url: https://raw.githubusercontent.com/kubernetes/kubernetes/v1.35.4/pkg/features/kube_features.go
    note: "feature-gate stages confirmed from code"
relations:
  - type: see_also
    target: CONCEPT-K8S_FEATURE_GATES
  - type: see_also
    target: CONCEPT-K8S_1_29_CHANGES
  - type: see_also
    target: CONCEPT-KUBERNETES_VERSION_SUPPORT
---

# Kubernetes 1.30 — operator-relevant changes

## Summary

Kubernetes `1.30` is in the extended range's lower band (installed by early Kubespray
`v2.27.x`/`v2.28.x` boundaries). It is a comparatively quiet release for **breaking**
changes: no major API removals. The notable graduations are **ValidatingAdmissionPolicy
GA** (CEL-based admission without webhooks), **PodSchedulingReadiness GA**, and **kubelet
swap** reaching Beta.

## Context

- Kubernetes `1.30`; in the extended `v2.27.0`–`v2.31.0` range's lower band.
- Highlights: `v1.30.0` changelog + code-confirmed feature-gate graduations.

## Implementation

**Behaviour changes / new capabilities**

- **ValidatingAdmissionPolicy is GA** — enforce admission policies with **CEL
  expressions** in-cluster, no external webhook needed (an alternative to
  webhook-based validation — [[TROUBLE-ADMISSION_WEBHOOK_BLOCKING]] is the
  webhook-outage class this helps avoid).
- **`PodSchedulingReadiness` GA** — `schedulingGates` hold a Pod unschedulable until gates
  are cleared (quota/gang-scheduling patterns).
- **kubelet swap (`NodeSwap`) Beta** — swap support advances toward GA (which lands in
  1.34).
- Structured/contextual logging and several `ServiceAccountToken*` gates advance to Beta.

**Notable feature-gate graduations** (confirmed from code)

- GA (locked): `PodSchedulingReadiness*`.
- Beta (on): `NodeSwap`, `ImageMaximumGCAge`, `PodLifecycleSleepAction`,
  `ContainerCheckpoint`, `ServiceAccountTokenJTI`,
  `ServiceAccountTokenNodeBindingValidation`, `ServiceAccountTokenPodNodeInfo`.
- Beta (opt-in): `UserNamespacesSupport [off]`, `OrderedNamespaceDeletion [off]`,
  `NodeLogQuery [off]`.

## Compatibility

- **No major API removals** in 1.30 — the notable removal in this range is 1.29
  (flowcontrol `v1beta2`, [[CONCEPT-K8S_1_29_CHANGES]]) and 1.32 (flowcontrol `v1beta3`).
- ValidatingAdmissionPolicy GA lets you replace some validating webhooks with in-process
  CEL policy — fewer moving parts, no webhook SPOF.

## References

- `v1.30.0` changelog; feature gates: [[CONCEPT-K8S_FEATURE_GATES]]; 1.29:
  [[CONCEPT-K8S_1_29_CHANGES]]; version window: [[CONCEPT-KUBERNETES_VERSION_SUPPORT]].
