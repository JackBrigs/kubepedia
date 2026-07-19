---
id: CONCEPT-ADDON_KARMA
type: concept
title: "Karma (Alertmanager UI) — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "0.121"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - karma
  - alertmanager dashboard
  - karma ui
tags:
  - addons
  - observability
  - alerting
  - ui
sources:
  - type: code
    path: charts/karma/Chart.yaml (wiremind)
    url: https://raw.githubusercontent.com/wiremind/wiremind-helm-charts/karma-2.11.0/charts/karma/Chart.yaml
    note: "kubeVersion >=1.19-0; app karma v0.121"
  - type: docs
    path: karma v0.121 release
    url: https://github.com/prymitive/karma/releases/tag/v0.121
    note: "additive (receivers keep_re/strip_re)"
relations:
  - type: see_also
    target: TROUBLE-KARMA
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
  - type: see_also
    target: CONCEPT-ADDON_ALERTMANAGER
---

# Karma (Alertmanager UI) — addon

## Summary

Karma is an Alertmanager dashboard (aggregates alerts across multiple Alertmanager
instances). Chart **2.11.0** (published by **wiremind**, not the app author) → app **karma
v0.121**. Fronted by **oauth2-proxy 8.3.1** — which ships an app version with unpatched
auth-bypass CVEs (see Compatibility).

## Context

- Class: upstream addon; catalog row in [[CONCEPT-ADDON_CATALOG]]. Pairs with
  [[CONCEPT-ADDON_ALERTMANAGER]].

## Implementation

- Chart→app (chart≠app): `karma-2.11.0` (wiremind) → karma **v0.121**. Chart `kubeVersion`:
  **`>=1.19-0`**. Karma is a stateless UI with no K8s API dependency.

## Configuration

- v0.121 is additive (new `receivers:keep_re`/`strip_re`); no chart-level changelog published.
- Point karma at the Alertmanager cluster URIs; auth is delegated to the oauth2-proxy in front.

## Compatibility

- **Kubernetes range:** only the chart gate `>=1.19-0` (admits 1.29–1.35); no version matrix
  (stateless UI). Beyond the gate: **unverified**.
- **karma CVEs:** none found (zero published advisories).
- **oauth2-proxy 8.3.1 → app 7.12.0 auth-bypass CVEs** (fixed only in app 7.15.2 — chart 8.3.1
  is behind): GHSA-7x63-xv5r-3p2x (Critical, `X-Forwarded-Uri` bypass), GHSA-5hvv-m4w4-gf6v
  (Critical, health-check UA bypass), GHSA-pxq7-h93f-9jrg (High, fragment confusion in
  `skip_auth_routes`). Chart 8.0.0 also switched the Redis subchart to `dandydeveloper/redis-ha`
  (session-store migration). Upgrade oauth2-proxy app to ≥7.15.2.

## Upstream issues & upgrade notes (mined 2026-07-19)

**Upstream (Karma):** actively maintained; latest **0.131** (the pin 0.121 is a few patches behind). No breaking changes in this window — Karma is a stateless read-only Alertmanager dashboard, so upgrades are low-risk. Reachability/OAuth remain the operational concerns ([[TROUBLE-KARMA]]).

## Older-version CVEs & security history (mined 2026-07-19)

Karma has no notable CVE record; it's a read-only dashboard, so older-version exposure is limited to base-image/Go CVEs and any UI (XSS-class) fixes. Low security surface — upgrading (latest 0.131) is low-urgency from a CVE standpoint; the OAuth proxy in front is the real access-control boundary.

## References

- karma Chart.yaml (wiremind), karma v0.121 release, oauth2-proxy advisories (above).
- Catalog: [[CONCEPT-ADDON_CATALOG]]; Alertmanager: [[CONCEPT-ADDON_ALERTMANAGER]].
