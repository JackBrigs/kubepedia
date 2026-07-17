---
id: TROUBLE-INGRESS_NGINX_ANNOTATION_REJECTED
type: troubleshooting
title: "ingress-nginx: annotation rejected / Ingress fails after upgrade"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.12.0 <=1.15.1"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - ingress-nginx annotation validation error
  - admission webhook denied ingress
  - annotations-risk-level
  - ingress snippet blocked
tags:
  - troubleshooting
  - ingress-nginx
  - ingress
  - upgrade
sources:
  - type: docs
    path: ingress-nginx controller-v1.12.0 release notes
    url: https://github.com/kubernetes/ingress-nginx/releases/tag/controller-v1.12.0
    note: "annotation validation on by default, risk-level High; snippets/metrics changes"
relations:
  - type: see_also
    target: CONCEPT-ADDON_INGRESS_NGINX
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
  - type: see_also
    target: TROUBLE-ADMISSION_WEBHOOK_BLOCKING
---

# ingress-nginx: annotation rejected / Ingress fails after upgrade

## Summary

After upgrading ingress-nginx to **1.12.0+**, creating/updating an Ingress is rejected by the
admission webhook with an annotation-validation error, or snippet annotations stop working.
1.12 turned annotation validation **on by default** at risk-level **High**. Adjust the
annotation or the risk level.

## Problem

- `admission webhook "validate.nginx.ingress.kubernetes.io" denied the request:
  annotation ... contains invalid value` when applying a previously-accepted Ingress.
- Configuration-snippet / server-snippet annotations no longer take effect.
- Metrics scraping breaks (metric endpoint/metric removed).

## Context

- Applies to controller **1.12.0–1.15.1** (owner deploys 1.12.0 — [[CONCEPT-ADDON_INGRESS_NGINX]]).
- Part of the ingress-nginx hardening after the 2025 IngressNightmare CVEs.

## Diagnostics

- **`--enable-annotation-validation` is on** and `annotations-risk-level` defaults to **High**
  — snippet-type annotations are now high-risk and blocked. Lower the risk level
  (`--annotations-risk-level=Medium`) only if you understand the exposure, or remove the
  offending annotation.
- **`--enable-metrics` is now disabled by default**; the metric
  `ingress_upstream_latency_seconds` was removed — re-enable metrics explicitly if scraped.
- `strict-validate-path-type` is on and `allow-cross-namespace-resources` is off; the Lua
  plugin system and memcached global rate limiting were removed.

## Known Issues

- **Do not stay on 1.12.0** — it is IngressNightmare-affected (**CVE-2025-1974**, 9.8); fixed
  in controller **1.12.1**. Restrict access to the admission webhook until patched
  ([[TROUBLE-ADMISSION_WEBHOOK_BLOCKING]]).

## References

- controller-v1.12.0 release notes (above); addon: [[CONCEPT-ADDON_INGRESS_NGINX]]; horizon:
  [[CONCEPT-UPGRADE_HORIZON]].
