---
id: CONCEPT-ADDON_FLAGGER
type: concept
title: "Flagger (progressive delivery) — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "1.40.0"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - flagger
  - progressive delivery
  - canary controller
tags:
  - addons
  - progressive-delivery
  - flagger
sources:
  - type: code
    path: charts/flagger/Chart.yaml
    url: https://raw.githubusercontent.com/fluxcd/flagger/v1.40.0/charts/flagger/Chart.yaml
    note: "kubeVersion >=1.19.0-0; appVersion 1.40.0"
  - type: docs
    path: flagger CHANGELOG
    url: https://raw.githubusercontent.com/fluxcd/flagger/v1.40.0/CHANGELOG.md
    note: "1.40.0 features; built against K8s client 1.31"
relations:
  - type: see_also
    target: TROUBLE-FLAGGER_CANARY
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
---

# Flagger (progressive delivery) — addon

## Summary

Flagger (`fluxcd/flagger` chart+app **1.40.0**) automates canary / blue-green / A-B rollouts
driven by metrics, working with a service mesh or Gateway API. 1.40.0 (2024-12-17) adds a
Splunk Observability metrics provider and AWS Gateway API Controller compatibility.

## Context

- Class: upstream addon; catalog row in [[CONCEPT-ADDON_CATALOG]].
- Works with the ingress/mesh layer (this platform runs Envoy Gateway / ingress-nginx), so
  its traffic-shifting depends on the chosen provider.

## Implementation

- Chart tracks app: `flagger v1.40.0`. Chart `kubeVersion`: **`>=1.19.0-0`** (open upper
  bound). Built against Kubernetes client libraries **1.31.x**.
- 1.40.0: Splunk Observability provider (PR #1733); AWS Gateway API Controller compat —
  preserves/injects HTTPRoute annotations (PR #1746); Go dep bumps to fix various CVEs.
- Cross-version (since 1.39.0): new webhook field `.spec.analysis.webhooks[].disableTLS`;
  built with Go 1.23.

## Configuration

- Pick the metrics provider (Prometheus/VM, Splunk, etc.) and mesh/gateway provider
  explicitly; canary analysis fails if the metric queries return no data.
- Gateway API users: unsorted header filters previously triggered unnecessary canary
  restarts (fixed 1.39.0, PR #1713) — stay ≥1.39.0.

## Compatibility

- **Kubernetes range:** no explicit upstream matrix (**unverified**); docs state no minimum
  version. Client libs at 1.31.x → safe across 1.29–1.35.
- **CVEs:** none found directly against `github.com/fluxcd/flagger` (OSV empty). Flux GHSAs
  found are for other Flux components, not the Flagger operator; one transitive dep advisory
  (CVE-2023-48713, `knative.dev/serving`) appears in the tree but is not Flagger code.

## Upstream issues & upgrade notes (mined 2026-07-19)

**Upstream:** releases 1.41–1.43 are patch/feature (CHANGELOG-only; no breaking flagged) beyond the pinned 1.40.0.

**Open upstream issues (as of 2026-07-19):** `skipAnalysis` is a non-pointer bool → **false may not serialize**, desyncing the Canary (#1660, a real API bug); AWS ALB ingress support still open (#659); no GitOps rollback-commit-back (#682); no "keep old version for instant rollback" (#453). Know these before designing canary flows.

## Older-version CVEs & security history (mined 2026-07-19)

Flagger publishes **no GitHub security advisories** in this window — no version-specific CVEs to flag for older releases. Historical exposure is limited to transitive dependency/base-image CVEs in older images; upgrading for those is optional-not-urgent from a Flagger-code standpoint.

## References

- `Chart.yaml`, CHANGELOG, PRs #1733/#1746/#1713 (above).
- Catalog: [[CONCEPT-ADDON_CATALOG]].
