---
id: TROUBLE-DEX_OIDC_LOGIN_FAILS
type: troubleshooting
title: "Dex: OIDC login fails (redirect / connector / issuer)"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: ">=2.42.0 <=2.45.1"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - dex login fails
  - oidc redirect_uri mismatch
  - dex connector error
  - dex issuer mismatch
tags:
  - troubleshooting
  - dex
  - oidc
  - sso
sources:
  - type: docs
    path: Dex documentation
    url: https://dexidp.io/docs/
    note: "issuer, connectors, static clients, redirect URIs"
relations:
  - type: see_also
    target: CONCEPT-ADDON_DEX
---

# Dex: OIDC login fails (redirect / connector / issuer)

## Summary

SSO through Dex fails at login — a redirect error, `redirect_uri` mismatch, or an upstream
connector error. Dex is an OIDC broker; the failure is usually the **client/redirect config**,
the **issuer URL**, or the **upstream connector** (LDAP/SAML/OAuth) credentials.

## Problem

- Login returns `redirect_uri did not match` or `invalid client`.
- Blank page / connector error after choosing an identity provider.
- Tokens rejected by the relying app (issuer/audience mismatch).

## Context

- Applies to Dex **2.42–2.45** (owner runs 2.42.0 — [[CONCEPT-ADDON_DEX]]). Often multiple Dex
  versions run (e.g. bundled with envoy-xds-controller) — keep issuer/config consistent.

## Diagnostics

1. **redirect_uri mismatch:** the app's callback URL must be listed **exactly** in the Dex
   static client's `redirectURIs` (scheme/host/port/path, trailing slash) — add the exact URI.
2. **Issuer URL:** Dex's `issuer` must be the externally-reachable URL the client uses; a
   mismatch makes token `iss` validation fail at the relying party. It must be stable and
   TLS-terminated correctly.
3. **Connector error:** check `kubectl logs` of the Dex pod — LDAP bind failures, SAML
   nil-pointer (fixed in 2.42), or OAuth app secret errors surface here. Verify connector
   credentials/endpoints.
4. **Client secret:** the relying app's client ID/secret must match the Dex `staticClients`
   entry.
5. **TLS/gRPC:** the 2.42 Go/TLS dependency bump can affect TLS to connectors — re-verify CA
   trust after upgrades.

## Known Issues

- Image scanners flag transitive CVE-2024-45338 in the 2.42.0 image (not a Dex-app CVE) — can
  fail CI gates.

## References

- Dex docs (above); addon: [[CONCEPT-ADDON_DEX]].
