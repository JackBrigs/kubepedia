---
id: CONCEPT-ADDON_KUBERNETES_DASHBOARD
type: concept
title: "kubernetes-dashboard (+ oauth2-proxy) — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "7.6.1"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - kubernetes-dashboard
  - dashboard addon
  - oauth2-proxy
tags:
  - addons
  - dashboard
  - ui
  - security
sources:
  - type: code
    path: charts/kubernetes-dashboard/Chart.yaml
    url: https://raw.githubusercontent.com/kubernetes/dashboard/kubernetes-dashboard-7.6.1/charts/kubernetes-dashboard/Chart.yaml
    note: "kubeVersion >=1.21.0-0; umbrella chart (no single appVersion)"
  - type: docs
    path: dashboard 7.0.0 release notes
    url: https://github.com/kubernetes/dashboard/releases/tag/kubernetes-dashboard-7.0.0
    note: "7.x rearchitecture (Kong, mandatory auth)"
relations:
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
  - type: see_also
    target: CONCEPT-ADDON_HEADLAMP
---

# kubernetes-dashboard (+ oauth2-proxy) — addon

## Summary

The official Kubernetes Dashboard, chart **7.6.1**, fronted by **oauth2-proxy** (chart
8.1.1). **Two security-relevant facts:** the upstream `kubernetes/dashboard` repo is now
**archived/retired** (last push 2026-01-21) — no longer actively maintained; and the
deployed oauth2-proxy chart 8.1.1 ships app **v7.12.0**, which has **multiple auth-bypass
CVEs**. Consider migrating to [[CONCEPT-ADDON_HEADLAMP]] and upgrading oauth2-proxy.

## Context

- Class: upstream addon; catalog row in [[CONCEPT-ADDON_CATALOG]].
- 7.x is an umbrella chart (multiple images + Kong gateway), not a single-container app.

## Implementation

- Chart 7.6.1 image tags: `dashboard-auth 1.1.3`, `dashboard-api 1.8.1`, `dashboard-web
  1.4.0`, `dashboard-metrics-scraper 1.1.1`; **Kong 2.38.0** dependency (DBless, required).
- Chart `kubeVersion`: **`>=1.21.0-0`**.
- **oauth2-proxy chart 8.1.1 → app v7.12.0** (chart≠app — verify the effective image).

## Configuration

- **7.0 rearchitecture (applies to 7.6.1):** Kong API gateway is a **required** dependency;
  token auth is **mandatory** (JWE→JWT, login can no longer be skipped;
  `clusterReadOnlyRole` / skip-login removed); cert-manager, nginx, metrics-server are
  **disabled by default** (wire TLS/ingress yourself); the plugin system was removed.
- A misconfigured/failed **Kong** pod takes the whole UI down.

## Compatibility

- **Kubernetes range:** chart floor `>=1.21`; 7.0 notes list 1.29 as fully supported, no
  explicit upper bound — treat **≥1.29** as the safe floor for 1.29–1.35.
- **oauth2-proxy v7.12.0 auth-bypass CVEs** (fronts an auth-mandatory Dashboard — upgrade to
  **≥7.15.2**): GHSA-vjrc-mh2v-45x6 (header smuggling via underscore, fixed 7.13.0);
  GHSA-7x63-xv5r-3p2x (`X-Forwarded-Uri` spoofing), GHSA-pxq7-h93f-9jrg (fragment confusion
  in `skip_auth_routes`), GHSA-c5c4-8r6x-56w3 (email-domain bypass), GHSA-5hvv-m4w4-gf6v
  (health-check User-Agent bypass) — all fixed **7.15.2**.
- **Dashboard CVEs:** none found via OSV, but the split 7.x images are poorly indexed —
  "none found, coverage-limited," not proven clean.

## References

- `Chart.yaml`, 7.0.0 release notes, oauth2-proxy advisories (above).
- Catalog: [[CONCEPT-ADDON_CATALOG]]; maintained alternative: [[CONCEPT-ADDON_HEADLAMP]].
