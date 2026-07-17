---
id: CONCEPT-ADDON_PYRRA
type: concept
title: "Pyrra (SLO controller) — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "0.9.4"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - pyrra
  - slo controller
  - pyrra 1.1.0
tags:
  - addons
  - observability
  - slo
sources:
  - type: code
    path: charts/pyrra/Chart.yaml
    url: https://raw.githubusercontent.com/pyrra-dev/helm-charts/pyrra-1.1.0/charts/pyrra/Chart.yaml
    note: "no kubeVersion; appVersion v0.9.4 (chart repo is pyrra-dev/helm-charts)"
relations:
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
---

# Pyrra (SLO controller) — addon

## Summary

Pyrra manages SLOs (`ServiceLevelObjective` CRD) and generates Prometheus recording/alerting
rules from them. Chart **1.1.0** → app **v0.9.4** (not v0.8.1 as the inventory lists — verify
the running image). The chart lives in a **separate repo** (`pyrra-dev/helm-charts`).

## Context

- Class: upstream addon; catalog row in [[CONCEPT-ADDON_CATALOG]]. Pairs with the
  metrics/alerting stack ([[CONCEPT-ADDON_VM_K8S_STACK]] / [[CONCEPT-ADDON_ALERTMANAGER]]).

## Implementation

- Chart→app: `pyrra-1.1.0` → **v0.9.4** (raw `Chart.yaml`). **Version-mapping caveat:** the
  inventory's `v0.8.1` does not match chart 1.1.0.
- Chart `kubeVersion`: **none** (field absent). CRD-based controller; K8s compat governed by
  the vendored client-go / controller-runtime.

## Configuration

- Provide a working Prometheus/VM datasource; Pyrra's generated rules must be scrapeable by
  the same stack that serves its UI queries.

## Compatibility

- **Kubernetes range:** no explicit matrix (**unverified**). No K8s API deprecation affects
  its manifests across 1.29–1.35.
- **Breaking changes:** none flagged for the v0.9.x line in release notes (**unverified**
  beyond that).
- **CVEs:** none found (OSV empty for `github.com/pyrra-dev/pyrra` at both 0.9.4 and 0.8.1).

## References

- `Chart.yaml` (pyrra-dev/helm-charts); v0.9.0 release notes.
- Catalog: [[CONCEPT-ADDON_CATALOG]].
