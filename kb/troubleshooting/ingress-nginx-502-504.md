---
id: TROUBLE-INGRESS_NGINX_502_504
type: troubleshooting
title: "ingress-nginx: 502 Bad Gateway / 504 Gateway Timeout"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: ">=1.11.0 <=1.15.1"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - ingress 502 bad gateway
  - ingress 504 gateway timeout
  - ingress-nginx upstream error
  - nginx no endpoints
tags:
  - troubleshooting
  - ingress-nginx
  - ingress
  - networking
sources:
  - type: docs
    path: ingress-nginx troubleshooting
    url: https://kubernetes.github.io/ingress-nginx/troubleshooting/
    note: "upstream, endpoints, timeouts, TLS"
relations:
  - type: see_also
    target: CONCEPT-ADDON_INGRESS_NGINX
  - type: see_also
    target: TROUBLE-SERVICE_NO_ENDPOINTS
---

# ingress-nginx: 502 Bad Gateway / 504 Gateway Timeout

## Summary

The Ingress returns **502** (upstream unreachable/error) or **504** (upstream too slow). The
controller is fine; the problem is the **backend**: no endpoints, wrong port, backend errors,
protocol/TLS mismatch, or timeouts too low for a slow app.

## Problem

- Clients get 502/504 from the ingress for a specific host/path.
- Intermittent 502s under load.

## Context

- Applies to controller **1.11–1.15** (owner deploys 1.12.0 — [[CONCEPT-ADDON_INGRESS_NGINX]]).

## Diagnostics

- **502 — upstream unreachable/error:**
  - **No endpoints:** the target Service has no ready pods (readiness failing / selector
    mismatch) — [[TROUBLE-SERVICE_NO_ENDPOINTS]].
  - **Wrong port:** the Ingress `servicePort` / Service `targetPort` doesn't match the
    container port.
  - **Protocol/TLS:** backend expects HTTPS but the annotation says HTTP (or vice-versa) —
    set `nginx.ingress.kubernetes.io/backend-protocol` correctly.
- **504 — upstream too slow:** raise proxy timeouts
  (`nginx.ingress.kubernetes.io/proxy-read-timeout` / `-send-timeout`) if the app legitimately
  needs longer; otherwise the backend is overloaded/stuck.
- **Controller logs:** `kubectl -n <ns> logs <controller-pod>` shows the upstream address and
  the exact error per request.
- **Large requests/headers:** buffer-size/body-size annotations may be needed.

## Known Issues

- 1.12.0 tightened **annotation validation** (High) — snippet annotations may be silently
  dropped ([[TROUBLE-INGRESS_NGINX_ANNOTATION_REJECTED]]); and 1.12.0 is IngressNightmare-
  affected (patch to 1.12.1).

## References

- ingress-nginx troubleshooting (above); addon: [[CONCEPT-ADDON_INGRESS_NGINX]]; endpoints:
  [[TROUBLE-SERVICE_NO_ENDPOINTS]].
