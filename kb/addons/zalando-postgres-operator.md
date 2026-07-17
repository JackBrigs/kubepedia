---
id: CONCEPT-ADDON_ZALANDO_POSTGRES_OPERATOR
type: concept
title: "Zalando postgres-operator — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "1.14.0"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - zalando-postgres-operator
  - postgres-operator
  - spilo
tags:
  - addons
  - data
  - postgresql
sources:
  - type: code
    path: charts/postgres-operator/Chart.yaml
    url: https://raw.githubusercontent.com/zalando/postgres-operator/v1.14.0/charts/postgres-operator/Chart.yaml
    note: "no kubeVersion; appVersion 1.14.0"
  - type: docs
    path: postgres-operator v1.14.0 release
    url: https://github.com/zalando/postgres-operator/releases/tag/v1.14.0
    note: "PG13–17, PG12 dropped, Patroni 4, log-message change"
relations:
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
---

# Zalando postgres-operator — addon

## Summary

The Zalando **postgres-operator** manages HA PostgreSQL clusters (Spilo/Patroni) via a
`postgresql` CRD. Chart/app **1.14.0**, default Spilo `spilo-17:4.0-p2`, managing
**PostgreSQL 13–17** (PG17 added, **PG12 dropped**).

## Context

- Class: upstream addon; catalog row in [[CONCEPT-ADDON_CATALOG]].

## Implementation

- Chart→app: 1.14.0. Chart `kubeVersion`: **none** (field absent). Compatible with **Patroni
  4**; built with Go 1.23.4. Defaults: `minimal_major_version` 13, `target_major_version` 17.

## Configuration

- Before upgrading, ensure no **PostgreSQL 12** clusters remain — PG12 is dropped and such
  clusters must be upgraded first.
- Note the changed SYNC/UPDATE **log message format** in 1.14.0 — it can break log
  parsing/alerting rules.

## Compatibility

- **Kubernetes range:** **unverified** — upstream publishes no explicit K8s compat matrix and
  the chart declares no `kubeVersion`. Assumed workable across 1.29–1.35; validate on the
  target minor.
- **Known issues:** failed major-version upgrades (now annotation-tracked to skip retries)
  and switchover-candidate search (retry logic added) are the recurring modes fixed in 1.14.0.
- **CVEs:** none found for `github.com/zalando/postgres-operator` (OSV empty). Transitive Go
  deps / the Spilo (PostgreSQL) image are out of scope here.

## References

- `Chart.yaml`, v1.14.0 release notes, operator_parameters doc (above).
- Catalog: [[CONCEPT-ADDON_CATALOG]].
