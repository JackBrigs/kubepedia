---
id: CONCEPT-ADDON_ALERTMANAGER
type: concept
title: "Alertmanager (prometheus-community chart) — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "0.25.0"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - alertmanager
  - prometheus alertmanager
  - alertmanager 0.28.0
tags:
  - addons
  - observability
  - alerting
sources:
  - type: code
    path: charts/alertmanager/Chart.yaml
    url: https://raw.githubusercontent.com/prometheus-community/helm-charts/alertmanager-0.28.0/charts/alertmanager/Chart.yaml
    note: "kubeVersion >=1.16.0-0; appVersion v0.25.0"
relations:
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
  - type: see_also
    target: CONCEPT-OBSERVABILITY_STACK
  - type: see_also
    target: TROUBLE-ALERTMANAGER_NOTIFICATIONS
---

# Alertmanager (prometheus-community chart) — addon

## Summary

Standalone Alertmanager via the prometheus-community `alertmanager` chart **0.28.0**. **The
chart pins an old app: `appVersion v0.25.0`** — which carries a High-severity stored-XSS
CVE. Verify the effective `image.tag`; if it is the default 0.25.0, override it upward.

## Context

- Class: upstream addon; catalog row in [[CONCEPT-ADDON_CATALOG]]. Complements the metrics
  stack [[CONCEPT-ADDON_VM_K8S_STACK]] / [[CONCEPT-OBSERVABILITY_STACK]].

## Implementation

- Chart→app: `alertmanager-0.28.0` → **v0.25.0** (raw `Chart.yaml`). A deployer overriding
  `image.tag` runs a different app version — check the running image.
- Chart `kubeVersion`: **`>=1.16.0-0`** (README also says "Kubernetes 1.14+").

## Configuration

- **Override `image.tag` to ≥ v0.25.1** (better, a current 0.27/0.28 app) to clear the XSS
  below — the chart default is stale.
- Standard Alertmanager clustering/gossip and receiver secrets apply.

## Compatibility

- **Kubernetes range:** no explicit compat matrix; effectively unbounded upper. Covers
  1.29–1.35 via the chart floor.
- **CVE (app v0.25.0):** **CVE-2023-40577 / GHSA-v86x-5fm3-5p7j** — stored XSS via
  `/api/v1/alerts`, High (CVSS 7.5), fixed in **v0.25.1**. Era Go-stdlib/base-image CVEs
  (e.g. CVE-2023-24538) may also flag on the old image — verify the build's base image.

## References

- `Chart.yaml` (above); advisory GHSA-v86x-5fm3-5p7j.
- Catalog: [[CONCEPT-ADDON_CATALOG]].
