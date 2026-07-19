---
id: CONCEPT-ADDON_1PASSWORD_CONNECT
type: concept
title: "1Password Connect — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "1.7.3"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - 1password-connect
  - 1password connect
  - connect 1.17.0
tags:
  - addons
  - secrets
  - 1password
sources:
  - type: code
    path: charts/connect/Chart.yaml
    url: https://raw.githubusercontent.com/1Password/connect-helm-charts/connect-1.17.0/charts/connect/Chart.yaml
    note: "no kubeVersion constraint; appVersion 1.7.3 (tag connect-1.17.0)"
  - type: docs
    path: connect chart CHANGELOG
    url: https://raw.githubusercontent.com/1Password/connect-helm-charts/connect-1.17.0/charts/connect/CHANGELOG.md
    note: "app 1.7.3 unchanged since chart 1.15.1; 1.17.0 adds default resources"
relations:
  - type: see_also
    target: TROUBLE-1PASSWORD_CONNECT
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
---

# 1Password Connect — addon

## Summary

1Password Connect (`connect` chart **1.17.0**, app **1.7.3**) runs the connect-api /
connect-sync pair in-cluster to serve secrets from 1Password vaults (used with the Connect
Operator / external-secrets). The app version **1.7.3** has been unchanged since chart
1.15.1 — chart 1.17.0 is a chart-level-only bump.

## Context

- Class: upstream addon; catalog row in [[CONCEPT-ADDON_CATALOG]].
- Provides secrets to workloads; commonly paired with external-secrets ([[CONCEPT-SECRETS_MANAGEMENT]]).

## Implementation

- Chart→app: `connect-1.17.0` → connect-api/connect-sync **1.7.3** (app carried unchanged
  through 1.15.1 → 1.16.0 → 1.17.0).
- Chart `kubeVersion`: **none** (field absent).
- Chart 1.17.0 changes (app unchanged): **added default resource requests/limits**
  (PRs #209/#211) — pods that previously had no limits now get CPU/mem limits, which can
  change scheduling/OOM behaviour; fixed podDisruptionBudget labels (#213). Incremental,
  no breaking changes from 1.15.x/1.16.x.

## Configuration

- The credentials Secret has a base64-encoding gotcha — a double-encoded credentials file
  yields an "invalid credentials file" startup failure.
- If Prometheus Operator CRDs are absent, disabling `serviceMonitor` is not enough: the
  ClusterRole still declares ServiceMonitor rules, which can fail RBAC/deploy on clusters
  without those CRDs (connect-helm-charts#224).

## Compatibility

- **Kubernetes range:** no published matrix and no chart `kubeVersion` (**unverified** /
  unconstrained for 1.29–1.35). Treat as not officially bounded.
- **CVEs:** none found for Connect 1.7.3 (OSV empty). The only historic CVE-2021-36758
  affects Connect server before 1.2 and does not apply.

## References

- `Chart.yaml` + connect CHANGELOG (above); issue #224.
- Catalog: [[CONCEPT-ADDON_CATALOG]].
