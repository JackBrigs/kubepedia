---
id: CONCEPT-K8S_FEATURE_GATES
type: concept
title: Kubernetes feature gates removed across 1.31–1.35
status: active
kubespray_version: null
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - feature gates
  - removed feature gates
tags:
  - kubernetes
  - feature-gates
  - upgrade
sources:
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

# Kubernetes feature gates removed across 1.31–1.35

## Summary

Each Kubernetes minor release graduates feature gates to GA and then **removes**
them a few releases later (locking the behavior to its default). A **removed**
feature gate can no longer be set on the command line — passing it makes the
component fail to start. This matters for upgrades: any explicit
`--feature-gates=…` entry (in inventory or component flags) must be dropped once
that gate is removed.

## Context

- Applies to Kubernetes `1.31`–`1.35` (the versions Kubespray `v2.29.0`–`v2.31.0`
  install).
- The authoritative, complete per-version list is the upstream
  "Feature Gates (removed)" reference — consult it before an upgrade; the examples
  below are illustrative, not exhaustive.

## Implementation

Pattern and notable examples (from the upstream reference, verified 2026-07-16):

- **v1.31** removes several GA-locked gates, e.g. `AppArmor`, `AppArmorFields`,
  `CloudDualStackNodeIPs`, `DisableCloudProviders`,
  `DisableKubeletCloudCredentialProviders` (all GA, locked to `true`).
- **v1.32** removes a large batch of long-GA gates, e.g. `CPUManager`,
  `CSIMigrationAWS`, `CSIMigrationAzureDisk`, `CSIMigrationGCE`,
  `BoundServiceAccountTokenVolume`, `AggregatedDiscoveryEndpoint`,
  `AdmissionWebhookMatchConditions`, `APIListChunking` (GA, locked to `true`).
- **v1.33–v1.35** continue removing individual GA-locked gates.

Because these gates are locked to their GA default, removing them from your
configuration is a no-op behaviorally — it only avoids the start-up failure from
referencing an unknown gate.

## References

- Kubernetes "Feature Gates (removed)" reference (kubernetes.io) — the complete,
  authoritative per-version list. Verified 2026-07-16; consult the source for the
  exact set per release (this document captures the pattern and examples, not an
  exhaustive list).
- Kubespray version→Kubernetes mapping: [[CONCEPT-KUBERNETES_VERSION_SUPPORT]].
