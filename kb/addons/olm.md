---
id: CONCEPT-ADDON_OLM
type: concept
title: "Operator Lifecycle Manager (OLM v0) — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "0.32.0"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - operator-lifecycle-manager
  - olm
  - olm 0.32.0
tags:
  - addons
  - operators
  - olm
sources:
  - type: docs
    path: OLM v0.32.0 release
    url: https://github.com/operator-framework/operator-lifecycle-manager/releases/tag/v0.32.0
    note: "operator-registry v1.55.0, K8s libs 0.32.x, NetworkPolicy support"
relations:
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
---

# Operator Lifecycle Manager (OLM v0) — addon

## Summary

OLM v0 ("classic") manages the install/upgrade lifecycle of operators via
CatalogSource/Subscription/CSV. Release **v0.32.0**. Note: **0.32.0 is an OLM release
version, not a published Helm chart** — OLM v0 is normally installed via release manifests /
`operator-sdk olm install`, so the inventory's "chart 0.32.0" is the release, not a chart.

## Context

- Class: upstream addon (in-house packaging); catalog row in [[CONCEPT-ADDON_CATALOG]].
- OLM v0 is **legacy/maintenance** — its successor is **OLM v1** (operator-controller).

## Implementation

- OLM **0.32.0**; operator-registry **v1.55.0**; controller-runtime 0.20.1; K8s libs ~0.32.2.
- Installed from release manifests, not a versioned chart (the in-repo `deploy/chart` is a
  `0.0.0-dev` template).

## Configuration

- v0.32.0 adds **NetworkPolicy support for catalog sources** — may require network/RBAC
  adjustments on upgrade.
- `go-jose/v4` is pinned to mitigate transitive CVE-2025-27144.

## Compatibility

- **Kubernetes range:** not explicitly stated in the v0.32.0 notes (**unverified**); the K8s
  client/apiextensions deps at 0.32.x indicate alignment with **K8s 1.32-era** APIs. Assumed
  workable across 1.29–1.35.
- **Breaking changes:** none documented in v0.32.0; ecosystem-level, plan the eventual move
  to OLM v1.
- **CVEs:** none found in OLM itself (OSV empty); only transitive CVE-2025-27144, mitigated
  by the dependency pin.

## References

- OLM v0.32.0 release notes (above); OLM v1 successor (operator-controller).
- Catalog: [[CONCEPT-ADDON_CATALOG]].
