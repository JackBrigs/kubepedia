---
id: CONCEPT-ADDON_ENVOY_XDS_CONTROLLER
type: concept
title: "envoy-xds-controller (exc) — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "0.17.1"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - envoy-xds-controller
  - exc
  - exc-stage
  - exc-test
tags:
  - addons
  - networking
  - envoy
  - xds
sources:
  - type: code
    path: helm/charts/envoy-xds-controller/Chart.yaml
    url: https://raw.githubusercontent.com/kaasops/envoy-xds-controller/main/helm/charts/envoy-xds-controller/Chart.yaml
    note: "chart 0.87.0 → appVersion v0.17.1; no kubeVersion"
  - type: docs
    path: envoy-xds-controller releases
    url: https://github.com/kaasops/envoy-xds-controller/releases
    note: "v0.17.0 refactor; v0.17.1 fixes"
relations:
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
---

# envoy-xds-controller (exc) — addon

## Summary

The kaasops **envoy-xds-controller** serves Envoy xDS config from Kubernetes CRDs. The
inventory runs it in three environments — `exc` chart **0.87.0**, `exc-stage` **0.86.0**,
`exc-test` **0.84.0** (each paired with dex 0.22.1). Chart 0.87.0 → app **v0.17.1**
(chart≠app numbering). The Envoy data-plane image is user-supplied, not pinned by the chart.

## Context

- Class: upstream addon; catalog rows (exc/exc-stage/exc-test) in [[CONCEPT-ADDON_CATALOG]].
  This one doc covers all three deployments.

## Implementation

- Chart→app: `envoy-xds-controller` 0.87.0 → **v0.17.1**.
- Chart `kubeVersion`: **none** (field absent).
- **v0.17.0 is a major refactor:** removed the legacy `resbuilder` + adapters (may break
  custom integrations), added HTTP/2 protocol options. v0.17.1 adds a wildcard-cert fallback
  and fixes spurious xDS snapshot version increments. No published migration guide.

## Configuration

- Supply the Envoy data-plane image explicitly; the chart does not pin it.
- After the 0.17.0 refactor, re-validate any custom resource-builder integrations.

## Compatibility

- **Kubernetes range:** no published matrix (**unverified**); no chart `kubeVersion`.
  Assumed workable across 1.29–1.35 via CRDs, but not tested-declared.
- **CVEs:** none found (no GHSA/CVE for the repo).

## References

- `Chart.yaml`, releases (above).
- Catalog: [[CONCEPT-ADDON_CATALOG]].
