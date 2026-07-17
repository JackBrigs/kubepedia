---
id: CONCEPT-ADDON_GIGAPIPE
type: concept
title: "Gigapipe / qryn (read + write) — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "4.1.6"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - gigapipe
  - gigapipe-read
  - gigapipe-write
  - qryn
  - cloki
tags:
  - addons
  - observability
  - logs
  - clickhouse
sources:
  - type: code
    path: gigapipe-helm values.yaml / Chart.yaml
    url: https://raw.githubusercontent.com/metrico/gigapipe-helm/main/Chart.yaml
    note: "chart 0.3.0, appVersion v4.1.6; MODE=reader/writer split; no kubeVersion"
  - type: docs
    path: qryn/gigapipe repo
    url: https://github.com/metrico/gigapipe
    note: "ClickHouse-backed; latest app v4.3.1"
relations:
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
  - type: see_also
    target: CONCEPT-OBSERVABILITY_STACK
---

# Gigapipe / qryn (read + write) — addon

## Summary

`gigapipe-read` and `gigapipe-write` are the same **qryn / Gigapipe** (Metrico) stateless
observability backend (logs/metrics/traces over **ClickHouse**), run as `MODE=reader` and
`MODE=writer` against one ClickHouse cluster. Chart 0.3.0 → app **v4.1.6** (latest upstream
is v4.3.1). ClickHouse is a required external dependency.

## Context

- Class: upstream addon; `gigapipe-read`/`gigapipe-write` rows in [[CONCEPT-ADDON_CATALOG]].
  One doc covers both (same image, different `MODE`). Complements
  [[CONCEPT-OBSERVABILITY_STACK]].
- Identity: qryn (formerly cLoki), commercialized as Gigapipe; repo renamed
  `metrico/qryn` → `metrico/gigapipe`.

## Implementation

- Chart `metrico/gigapipe-helm` 0.3.0 → app **v4.1.6** (chart lags; latest app v4.3.1).
  `MODE` env: `all`/`writer`/`reader`/`init_only`. Chart `kubeVersion`: **none**.
- **ClickHouse** is the backing store; upstream baseline **ClickHouse 22.6.2.12+**.

## Configuration

- **Init pass required:** schema/table creation via init / `MODE=init_only` before
  reader/writer start; `CLUSTER_NAME` and storage policy must match across reader and writer.
- Replication is a **manual** migration (convert to `Replicated*` engines + coordinate
  ZooKeeper/Keeper) — not automatic on upgrade.
- Avoid ClickHouse passwords with special chars or >32 chars (breaks auth).

## Compatibility

- **Kubernetes range:** no upstream K8s range (**unverified**); standard `apps/v1`
  Deployments, so unconstrained across 1.29–1.35.
- **CVEs:** qryn/gigapipe itself none found. **ClickHouse** (required backing store) carries
  CVE-2025-1385 / GHSA-5phv-x8x4-83x5 (library-bridge RCE, High; fixed 24.3.18.6 / 24.8.14.27
  / 25.1.5.5), CVE-2024-6873 (native-interface heap overflow/DoS), CVE-2024-23689 — keep
  ClickHouse patched.

## References

- gigapipe-helm Chart.yaml/values, qryn repo + wiki (above); ClickHouse advisories.
- Catalog: [[CONCEPT-ADDON_CATALOG]]; observability hub: [[CONCEPT-OBSERVABILITY_STACK]].
