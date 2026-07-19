---
id: TROUBLE-FEAST_OPERATOR
type: troubleshooting
title: "Feast Operator: FeatureStore not reconciling — install needs Server-Side Apply, online/offline store, registry"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: ">=0.64.0"
verified_at: "2026-07-19"
confidence: confirmed
aliases:
  - feast operator install fails
  - featurestore not ready
  - feast kubectl apply fails
  - feast server-side apply
  - feast online store connection
tags: [troubleshooting, ml, feast, operator]
sources:
  - type: external
    path: Feast operator
    url: https://github.com/feast-dev/feast/tree/v0.64.0/infra/feast-operator
    note: "install via kustomize with Server-Side Apply (plain apply fails on large CRDs); FeatureStore reconcile"
relations:
  - type: see_also
    target: CONCEPT-ADDON_FEAST_OPERATOR
---

# Feast Operator: FeatureStore not reconciling — install needs Server-Side Apply, online/offline store, registry

## Summary

The Feast Operator manages `FeatureStore` resources. The **#1 install trap** is that it must be applied
with **Server-Side Apply** — a plain `kubectl apply` fails on the large CRDs (annotation-size limit).
After install, a `FeatureStore` that won't become ready is usually an **online/offline store** or
**registry** connection problem. Feast `v0.64.0`.

## Problem

- `kubectl apply` of the operator manifests fails (`metadata.annotations: Too long`), or a `FeatureStore`
  stays not-ready with the operator reconcile erroring.

## Context

- Feast Operator `0.64.0` ([[CONCEPT-ADDON_FEAST_OPERATOR]]); ships from the feast monorepo (no separate
  operator tag), installed via **kustomize + Server-Side Apply**.
- **Plain apply fails:** the CRDs exceed the client-side-apply annotation limit; you must use
  `kubectl apply --server-side` (or `kubectl apply -k ... --server-side`).
- **Store connectivity:** a FeatureStore references an **online store** (e.g. Redis) and **offline
  store** + **registry**; wrong endpoints/creds leave it not-ready.

## Diagnostics

```bash
kubectl -n feast-operator-system logs deploy/feast-operator-controller-manager | tail
kubectl get featurestore -A ; kubectl describe featurestore <name> -n <ns>
kubectl get crd | grep feast
```

## Known Issues

- **Install fails — fix:** apply with **`--server-side`**:
  `kubectl apply -k <feast-operator-kustomize> --server-side --force-conflicts`.
- **FeatureStore not ready — fix:** `describe` for the failing store; fix the online (Redis)/offline/
  registry connection strings and secrets.
- **Upgrades:** keep applying server-side to avoid field-manager conflicts on the big CRDs.

## References

- Feast operator (v0.64.0). Addon [[CONCEPT-ADDON_FEAST_OPERATOR]].
