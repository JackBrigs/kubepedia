---
id: CONCEPT-K8S_ANONYMOUS_AUTH_ENDPOINTS
type: concept
title: "Anonymous auth restricted to configured endpoints (GA 1.34) — hardening knob"
status: active
kubespray_version: ">=v2.31.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - AnonymousAuthConfigurableEndpoints
  - restrict anonymous access healthz
  - anonymous auth specific paths
  - apiserver anonymous endpoints config
tags:
  - kubernetes
  - auth
  - apiserver
  - security
sources:
  - type: code
    path: keps/sig-auth/4633-anonymous-auth-configurable-endpoints
    url: https://github.com/kubernetes/enhancements/tree/master/keps/sig-auth/4633-anonymous-auth-configurable-endpoints
    note: "kep.yaml: alpha 1.31, beta 1.32, stable 1.34"
relations:
  - type: see_also
    target: CONCEPT-INSECURE_DEFAULTS
  - type: see_also
    target: PRACTICE-CLUSTER_HARDENING
  - type: see_also
    target: CONCEPT-K8S_STRUCTURED_AUTHN
---

# Anonymous auth restricted to configured endpoints (GA 1.34) — hardening knob

## Summary

The API server can now allow **anonymous access to only specific paths** (e.g. `/healthz`, `/livez`,
`/readyz`) instead of the all-or-nothing `--anonymous-auth=true|false`.
`AnonymousAuthConfigurableEndpoints` reached **GA in 1.34** (Kubespray v2.31.0). This closes a common
hardening gap: you can keep health endpoints reachable for load balancers while **denying anonymous
access everywhere else** — previously enabling health checks meant enabling anonymous auth globally.

## Context

- Milestone (`keps/sig-auth/4633-...` kep.yaml): alpha **1.31**, beta **1.32**, stable **1.34**.
- **How:** set `anonymous` config in the **structured authentication config**
  ([[CONCEPT-K8S_STRUCTURED_AUTHN]]) with an explicit list of allowed paths; requests to other paths
  from unauthenticated clients are rejected.
- **Why it matters for hardening:** the hardening overlay wants `remove_anonymous_access`
  ([[CONCEPT-INSECURE_DEFAULTS]], [[PRACTICE-CLUSTER_HARDENING]]) but LB health checks often hit the
  apiserver anonymously — this lets you scope anonymous to just the health paths and lock the rest,
  removing the trade-off.
- **Operator note:** opt-in config, not a silent change; the GA means it's available across v2.31.0 to
  tighten a previously blunt setting.

## References

- `keps/sig-auth/4633-anonymous-auth-configurable-endpoints` (kep.yaml GA 1.34). Insecure defaults
  [[CONCEPT-INSECURE_DEFAULTS]]; hardening [[PRACTICE-CLUSTER_HARDENING]]; structured authn
  [[CONCEPT-K8S_STRUCTURED_AUTHN]].
