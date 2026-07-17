---
id: TROUBLE-ENVOY_GATEWAY_BACKEND_TLS_SNI
type: troubleshooting
title: "Envoy Gateway 1.6 upgrade: upstream TLS breaks (SNI/SAN)"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.6.0 <=1.8.2"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - envoy gateway backend tls broke
  - envoy gateway sni san required
  - envoy gateway 1.6 alpn
  - gateway api crd 1.4.0 upgrade
tags:
  - troubleshooting
  - envoy
  - gateway-api
  - tls
  - upgrade
sources:
  - type: docs
    path: Envoy Gateway v1.6.0 release notes
    url: https://gateway.envoyproxy.io/news/releases/notes/v1.6.0/
    note: "backend TLS SNI/SAN + ALPN defaults; OIDC token refresh; CRD v1.3→v1.4"
relations:
  - type: see_also
    target: CONCEPT-ADDON_ENVOY_GATEWAY
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# Envoy Gateway 1.6 upgrade: upstream TLS breaks (SNI/SAN)

## Summary

After upgrading Envoy Gateway to **1.6.0**, upstream (backend) TLS connections start failing,
or the chart upgrade fails on CRDs. 1.6.0 changed backend-TLS SNI/ALPN defaults and bumped the
Gateway API CRDs — apply the CRDs and set the upstream SAN/SNI correctly. Also move to
**≥1.6.2** (RCE fix).

## Problem

- Backend TLS handshake failures to upstreams after the upgrade (cert/SNI errors).
- Chart upgrade fails because Gateway API CRDs are the old version.
- OIDC sessions behave differently (unexpected token refresh).

## Context

- Applies to Envoy Gateway **1.6.0–1.8.2** (owner spans 1.4.1→1.6.0 —
  [[CONCEPT-ADDON_ENVOY_GATEWAY]]). v1.6.0 implements **Gateway API v1.4.0**.

## Diagnostics

- **Backend TLS without SNI now auto-derives the upstream SNI from the Host header and
  requires a DNS SAN matching that SNI** — add the matching SAN to the upstream cert, or set
  SNI explicitly.
- **`ALPNProtocols` now defaults to `[h2, http/1.1]`** when unset — pin it if the upstream
  can't negotiate h2.
- **Gateway API CRD bump v1.3.0 → v1.4.0** must be applied **before/with** the chart upgrade;
  the `gateway-helm` chart does **not** install the Gateway API CRDs.
- **OIDC** now auto-refreshes tokens when a refresh token is issued — restore the old
  behaviour with `refreshToken: false` if needed.

## Known Issues

- **v1.6.0 is affected by RCE CVE-2026-22771** (EnvoyExtensionPolicy Lua) — fixed **1.6.2**.
  Bundled Envoy 1.36.4 also has fixes in 1.36.5/1.36.9. Upgrade to EG ≥1.6.2.

## References

- Envoy Gateway v1.6.0 release notes (above); addon: [[CONCEPT-ADDON_ENVOY_GATEWAY]]; horizon:
  [[CONCEPT-UPGRADE_HORIZON]].
