---
id: TROUBLE-HEADLAMP
type: troubleshooting
title: "Headlamp: can't log in / empty cluster view — token/OIDC auth and RBAC of the viewer"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "0.43.0"
verified_at: "2026-07-19"
confidence: confirmed
aliases:
  - headlamp login
  - headlamp empty view
  - headlamp oidc
  - headlamp token
tags:
  - troubleshooting
  - ui
  - headlamp
sources:
  - type: external
    path: headlamp
    url: https://headlamp.dev/docs/latest/
    note: "Headlamp authenticates with a bearer token or OIDC; what you see is bounded by that identity's RBAC"
relations:
  - type: see_also
    target: CONCEPT-ADDON_HEADLAMP
  - type: see_also
    target: CONCEPT-ADDON_KUBERNETES_DASHBOARD
---

# Headlamp: can't log in / empty cluster view — token/OIDC auth and RBAC of the viewer

## Summary

Headlamp is a web UI ([[CONCEPT-ADDON_HEADLAMP]]) that acts **as the logged-in identity** — via a **bearer token** or **OIDC**. A blank/partial cluster view is almost never a Headlamp bug: it's the identity's **RBAC** not granting read on those resources, or an auth/OIDC misconfig.

## Problem

- Login fails, or the UI loads but shows **no/partial resources**.

## Context

- Headlamp `0.43.0`; a modern replacement for the retired kubernetes-dashboard ([[CONCEPT-ADDON_KUBERNETES_DASHBOARD]]).
- **Identity = RBAC:** Headlamp queries the API **as** the token/OIDC user; it can only show what that subject may `get`/`list`. An empty namespace list = missing RBAC, not a UI fault.
- **OIDC:** issuer/client/redirect misconfig blocks login entirely.

## Diagnostics

```bash
# what can the viewer's SA/user actually see?
kubectl auth can-i list pods --as=system:serviceaccount:<ns>:<sa> -A
kubectl -n <ns> logs deploy/headlamp | tail   # OIDC/auth errors
```

## Known Issues

- **Empty view — fix:** grant the viewer identity the needed (Cluster)RoleBinding; the UI reflects RBAC exactly.
- **Login — fix:** correct OIDC issuer/client/redirect, or use a valid ServiceAccount token; ensure the token isn't expired.

## References

Upstream project (see `sources`). Catalog entry [[CONCEPT-ADDON_HEADLAMP]].
