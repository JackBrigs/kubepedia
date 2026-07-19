---
id: CONCEPT-ADDON_ENVOY_GATEWAY
type: concept
title: "Envoy Gateway (eg) — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.30 <=1.33"
component_version: "1.6.0"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - envoy gateway
  - eg
  - gateway-helm
  - gateway api envoy
tags:
  - addons
  - networking
  - gateway-api
  - envoy
sources:
  - type: docs
    path: Envoy Gateway compatibility matrix
    url: https://gateway.envoyproxy.io/news/releases/matrix/
    note: "EG v1.6.x → K8s 1.30–1.33, Gateway API v1.4.0, Envoy 1.36.4"
  - type: docs
    path: EG v1.6.0 release notes
    url: https://gateway.envoyproxy.io/news/releases/notes/v1.6.0/
    note: "breaking changes; CRD bump v1.3.0→v1.4.0"
  - type: docs
    path: advisory GHSA-xrwg-mqj6-6m22
    url: https://github.com/envoyproxy/gateway/security/advisories/GHSA-xrwg-mqj6-6m22
    note: "CVE-2026-22771 RCE, fixed 1.6.2"
relations:
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
  - type: see_also
    target: CONCEPT-ADDON_INGRESS2GATEWAY
---

# Envoy Gateway (eg) — addon

## Summary

Envoy Gateway (`gateway-helm` chart) is a Gateway API implementation over Envoy Proxy. The
inventory spans **v1.4.1 → v1.6.0**; v1.6.0 implements **Gateway API v1.4.0** and bundles
**Envoy 1.36.4**. **Security-critical:** v1.6.0 is vulnerable to an RCE — upgrade to ≥1.6.2.

## Context

- Class: upstream addon; catalog row in [[CONCEPT-ADDON_CATALOG]].
- Gateway API version tracks the EG version: v1.4.x/v1.5.x → Gateway API v1.3.0; **v1.6.0 →
  v1.4.0**; patch v1.6.1 → v1.4.1.

## Implementation

- Chart→app: `gateway-helm` v1.6.0 → EG 1.6.0, Envoy `distroless-v1.36.4`.
- Chart `kubeVersion`: **none** (the tag Chart.yaml is a release template).
- **Gateway API CRDs are NOT installed by the chart** — apply them separately (they hit
  annotation-size limits if bundled).

## Configuration

- **CRD bump v1.3.0 → v1.4.0** must be applied before/with the chart upgrade to v1.6.0.
- **Backend TLS breaking changes in 1.6.0:** `ALPNProtocols` now defaults to
  `[h2, http/1.1]` when unset; TLS without SNI auto-derives upstream SNI from the Host header
  and **requires a DNS SAN matching that SNI** — can break existing upstream TLS. OIDC now
  auto-refreshes tokens when a refresh token is issued (restore old behaviour with
  `refreshToken: false`).

## Compatibility

- **Kubernetes range:** **v1.30–v1.33** for EG v1.6.x (per the matrix). 1.29/1.34/1.35 are
  not listed (**unverified**).
- **CVEs:** **CVE-2026-22771 / GHSA-xrwg-mqj6-6m22** — RCE via EnvoyExtensionPolicy Lua
  (CVSS 8.8), **v1.6.0 affected, fixed 1.6.2**. Bundled Envoy 1.36.4: CVE-2026-26308 (RBAC
  bypass, fixed Envoy 1.36.5) + a batch fixed in Envoy 1.36.9. Move to EG ≥1.6.2.

## Upstream issues & upgrade notes (mined 2026-07-19)

**Future upgrade context** beyond pinned **1.6.0** (from upstream releases):
- **1.8.1:** bumps **Envoy to 1.38.1**; fixes the unary interceptor and **fail-open authentication in `GatewayNamespaceMode`** (a security-relevant fix — verify your auth posture if on GatewayNamespaceMode).
- 1.7.x/1.8.x are otherwise maintenance; no breaking API changes flagged in this window.

## References

- Compatibility matrix, v1.6.0 release notes, advisory GHSA-xrwg-mqj6-6m22 (above).
- Catalog: [[CONCEPT-ADDON_CATALOG]]; migration tool: [[CONCEPT-ADDON_INGRESS2GATEWAY]].
