---
id: TROUBLE-KARMA
type: troubleshooting
title: "Karma: no alerts shown — can't reach Alertmanager instances / OAuth in front"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "0.121"
verified_at: "2026-07-19"
confidence: confirmed
aliases:
  - karma no alerts
  - karma alertmanager unreachable
  - karma oauth
  - karma dashboard empty
tags:
  - troubleshooting
  - observability
  - karma
  - alerting
sources:
  - type: external
    path: karma
    url: https://github.com/prymitive/karma
    note: "Karma aggregates alerts from one or more Alertmanager URLs; empty = it can't reach them"
relations:
  - type: see_also
    target: CONCEPT-ADDON_KARMA
  - type: see_also
    target: CONCEPT-ADDON_ALERTMANAGER
  - type: see_also
    target: TROUBLE-ALERTMANAGER_NOTIFICATIONS
---

# Karma: no alerts shown — can't reach Alertmanager instances / OAuth in front

## Summary

Karma is a read-only dashboard that **aggregates alerts across Alertmanager instances** ([[CONCEPT-ADDON_ALERTMANAGER]]). An empty Karma means it **can't reach** the configured Alertmanager URL(s), or the **OAuth proxy** in front is blocking. Karma itself holds no alert state. App `v0.121`.

## Problem

- Karma UI is empty / shows an Alertmanager as down, even though alerts are firing.

## Context

- Karma `v0.121` ([[CONCEPT-ADDON_KARMA]]), typically behind oauth2-proxy.
- **Upstream reachability:** Karma polls each Alertmanager's API; a wrong URL, network policy, or a down AM ([[TROUBLE-ALERTMANAGER_NOTIFICATIONS]]) yields no alerts.
- **OAuth:** the fronting proxy can block the UI or the upstream calls if misconfigured.

## Diagnostics

```bash
kubectl -n <ns> logs deploy/karma | tail        # 'error fetching' <am-url>
kubectl -n <ns> get cm karma -o yaml | grep -i uri   # configured AM URLs
```

## Known Issues

- **No alerts — fix:** correct the Alertmanager URI(s) in Karma's config and ensure network reachability; verify the AM itself is healthy.
- **OAuth — fix:** fix the proxy so it neither blocks the UI nor the upstream Alertmanager calls.

## References

Upstream project (see `sources`). Catalog entry [[CONCEPT-ADDON_KARMA]].
