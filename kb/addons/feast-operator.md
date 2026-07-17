---
id: CONCEPT-ADDON_FEAST_OPERATOR
type: concept
title: "Feast Operator (feature store) — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "0.64.0"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - feast-operator
  - feast feature store
tags:
  - addons
  - ml
  - feature-store
  - feast
sources:
  - type: docs
    path: feast-operator README
    url: https://github.com/feast-dev/feast/blob/master/infra/feast-operator/README.md
    note: "kustomize install; requires Server-Side Apply"
  - type: docs
    path: Feast v0.64.0 release
    url: https://github.com/feast-dev/feast/releases/tag/v0.64.0
    note: "registry RBAC hardening; selector migration job removed"
relations:
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
---

# Feast Operator (feature store) — addon

## Summary

The Feast Operator manages Feast (ML feature store) `FeatureStore` resources. It ships from
the `feast-dev/feast` monorepo (no separate operator tag) — latest Feast **v0.64.0**.
Installed via **kustomize with Server-Side Apply** (plain `kubectl apply` fails).

## Context

- Class: upstream addon; catalog row in [[CONCEPT-ADDON_CATALOG]].

## Implementation

- Versioned with Feast; latest **v0.64.0** (2026-06-13). Install:
  `kubectl apply --server-side --force-conflicts -f .../dist/install.yaml`.
- No Helm chart / no `kubeVersion`; the README's "v1.11.3+" is an operator-sdk scaffold
  minimum, not a tested support floor.

## Configuration

- **Server-Side Apply is required** — the combined v1alpha1+v1 CRD exceeds the client-side
  annotation limit, so plain `kubectl apply` fails (the most common install error).
- v0.64.0 hardened **registry RBAC** (permission checks on Commit/Refresh RPCs, proto dump
  removed) — review remote-registry RBAC before upgrading. The selector migration job was
  removed, so clusters skipping intermediate versions may miss that migration.

## Compatibility

- **Kubernetes range:** no explicit tested range upstream (**unverified**); the only
  documented platform baseline is via Red Hat OpenShift AI (OpenShift 4.14+ / RHOAI 2.20+).
- **CVEs:** these target the Feast **Feature Server** component (direct operator-control-plane
  applicability **unverified**), several Critical/High: CVE-2026-23537 (`/save-document`,
  Critical), CVE-2026-56121 (unsafe deserialization → unauth access, Critical),
  CVE-2026-23538 (`/ws/chat` unauth WebSocket DoS, High), CVE-2026-23536, CVE-2025-11157,
  CVE-2024-11602. Do not expose the Feature Server unauthenticated.

## References

- feast-operator README, Feast v0.64.0 release, GHSA advisories (above).
- Catalog: [[CONCEPT-ADDON_CATALOG]].
