---
id: TROUBLE-KUBERNETES_DASHBOARD
type: troubleshooting
title: "Kubernetes Dashboard: login/access issues and the retired-upstream caveat (oauth2-proxy, RBAC)"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "7.6.1"
verified_at: "2026-07-19"
confidence: confirmed
aliases:
  - kubernetes dashboard login
  - dashboard token
  - dashboard oauth2-proxy
  - dashboard retired
tags:
  - troubleshooting
  - ui
  - dashboard
  - security
sources:
  - type: external
    path: kubernetes_dashboard
    url: https://github.com/kubernetes/dashboard
    note: "dashboard 7.x fronted by oauth2-proxy; access bounded by RBAC; upstream repo archived/retired"
relations:
  - type: see_also
    target: CONCEPT-ADDON_KUBERNETES_DASHBOARD
  - type: see_also
    target: CONCEPT-SECURITY_INDEX
  - type: see_also
    target: CONCEPT-ADDON_HEADLAMP
---

# Kubernetes Dashboard: login/access issues and the retired-upstream caveat (oauth2-proxy, RBAC)

## Summary

The Kubernetes Dashboard (chart `7.6.1`, behind **oauth2-proxy**) shows resources **as the logged-in identity**, so access problems are RBAC/auth, not UI bugs. Two caveats: the upstream repo is **archived/retired** (consider [[CONCEPT-ADDON_HEADLAMP]]), and a dashboard is a **high-value target** — never expose it unauthenticated ([[CONCEPT-SECURITY_INDEX]]).

## Problem

- Can't log in, or the UI loads but shows **forbidden**/empty for namespaces.

## Context

- Dashboard `7.6.1` ([[CONCEPT-ADDON_KUBERNETES_DASHBOARD]]); 7.x requires the Kong/oauth2-proxy front, not the old bearer-token-only flow.
- **RBAC:** the viewer identity must have read RBAC; the UI mirrors it exactly.
- **Security:** the archived upstream means no new fixes — treat exposure conservatively.

## Diagnostics

```bash
kubectl -n kubernetes-dashboard logs deploy/kubernetes-dashboard-web | tail
kubectl auth can-i list pods --as=<user> -A
kubectl -n kubernetes-dashboard get deploy,svc | grep oauth2
```

## Known Issues

- **Access — fix:** grant the identity the needed RBAC; confirm oauth2-proxy is configured (issuer/client) and healthy.
- **Retirement — plan:** migrate to a maintained UI (Headlamp) since the dashboard repo is archived ([[CONCEPT-ADDON_HEADLAMP]]).

## References

Upstream project (see `sources`). Catalog entry [[CONCEPT-ADDON_KUBERNETES_DASHBOARD]].
