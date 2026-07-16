---
id: API-FLOWCONTROL_APISERVER
type: api
title: flowcontrol.apiserver.k8s.io (FlowSchema, PriorityLevelConfiguration)
status: active
kubespray_version: null
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - flowcontrol.apiserver.k8s.io
  - FlowSchema
  - PriorityLevelConfiguration
tags:
  - kubernetes
  - api
  - apiserver
sources:
  - type: docs
    path: kubernetes.io deprecation guide
    url: https://kubernetes.io/docs/reference/using-api/deprecation-guide/#flowcontrol-resources-v132
    note: "v1beta3 removed in v1.32; use v1"
relations:
  - type: see_also
    target: CONCEPT-K8S_API_REMOVALS
---

# flowcontrol.apiserver.k8s.io (FlowSchema, PriorityLevelConfiguration)

## Summary

The API Priority and Fairness resources `FlowSchema` and
`PriorityLevelConfiguration` live under `flowcontrol.apiserver.k8s.io`. The
`v1beta3` version is **removed in Kubernetes v1.32**; use `v1` (GA since v1.29).

## Implementation

- Removed version: `flowcontrol.apiserver.k8s.io/v1beta3` (removed in `1.32`).
- Replacement: `flowcontrol.apiserver.k8s.io/v1` (available since `1.29`).
- The resources (`FlowSchema`, `PriorityLevelConfiguration`) are unchanged in
  purpose; only the API version changes.

## Compatibility

- Kubernetes `1.31`: `v1beta3` still served (alongside `v1`).
- Kubernetes `1.32`–`1.35`: `v1beta3` removed; only `v1` is served.
- Behavioral note in `v1`: `spec.limited.nominalConcurrencyShares` defaults to 30
  only when unspecified; an explicit `0` is left as `0` (not coerced to 30).

## Upgrade Notes

- Before upgrading a cluster to `1.32`, update any manifests/tools that reference
  `flowcontrol.apiserver.k8s.io/v1beta3` to `/v1`. Custom APF configuration is the
  main place this appears; most clusters use the built-in defaults and are
  unaffected.
- In the Kubespray range, this boundary is crossed when moving to a release that
  installs `1.32`+ (`v2.30.0` min is `1.32.0`).

## References

- Kubernetes API deprecation guide (kubernetes.io), Flow Control v1.32 section —
  verified 2026-07-16.
