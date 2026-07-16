---
id: CONCEPT-K8S_API_REMOVALS
type: concept
title: Kubernetes API removals across 1.31–1.35
status: active
kubespray_version: null
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - api removals
  - api deprecations
tags:
  - kubernetes
  - api
  - upgrade
sources:
  - type: docs
    path: kubernetes.io deprecation guide
    url: https://kubernetes.io/docs/reference/using-api/deprecation-guide/
    note: "official Kubernetes API deprecation/removal guide"
relations:
  - type: see_also
    target: API-FLOWCONTROL_APISERVER
  - type: see_also
    target: CONCEPT-KUBERNETES_VERSION_SUPPORT
---

# Kubernetes API removals across 1.31–1.35

## Summary

Across the Kubernetes minor versions that Kubespray `v2.29.0`–`v2.31.0` install
(`1.31`–`1.35`), the upstream API deprecation guide lists a **single** removed API
version: `flowcontrol.apiserver.k8s.io/v1beta3` is removed in **v1.32**. Manifests
using removed APIs must be migrated before upgrading past the removal version.

## Context

- Applies to Kubernetes `1.31`–`1.35`.
- Relevant to Kubespray upgrades because upgrading across the `1.32` boundary (e.g.
  from a `v2.29.x` cluster on `1.31` to `v2.30.0` on `1.32`+) crosses the removal.
- Source: the official Kubernetes deprecation guide (upstream, not Kubespray).

## Implementation

Removals in range:

| Kubernetes | Removed API version | Resources | Replacement |
|------------|---------------------|-----------|-------------|
| 1.32 | `flowcontrol.apiserver.k8s.io/v1beta3` | FlowSchema, PriorityLevelConfiguration | `flowcontrol.apiserver.k8s.io/v1` (since 1.29) |

No API-version removals are documented for `1.31`, `1.33`, `1.34`, or `1.35` in the
upstream guide as of this writing. (Deprecations that are not yet removed may still
exist; only removals are listed here.)

See [[API-FLOWCONTROL_APISERVER]] for the flow-control detail.

## References

- Kubernetes API deprecation guide (kubernetes.io) — verified 2026-07-16.
- Kubespray version→Kubernetes mapping: [[CONCEPT-KUBERNETES_VERSION_SUPPORT]].
