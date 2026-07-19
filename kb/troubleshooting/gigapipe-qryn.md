---
id: TROUBLE-GIGAPIPE
type: troubleshooting
title: "Gigapipe/qryn: reads return nothing / writes rejected — ClickHouse backend, reader/writer split"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "4.1.6"
verified_at: "2026-07-19"
confidence: confirmed
aliases:
  - qryn no data
  - gigapipe clickhouse connection
  - gigapipe reader writer
  - qryn write failing
tags:
  - troubleshooting
  - observability
  - qryn
  - clickhouse
sources:
  - type: external
    path: gigapipe
    url: https://github.com/metrico/qryn
    note: "qryn/Gigapipe is stateless over ClickHouse; reader and writer are separate MODEs sharing the same DB"
relations:
  - type: see_also
    target: CONCEPT-ADDON_GIGAPIPE
  - type: see_also
    target: CONCEPT-OBSERVABILITY_STACK
---

# Gigapipe/qryn: reads return nothing / writes rejected — ClickHouse backend, reader/writer split

## Summary

Gigapipe/qryn is a **stateless** logs/metrics/traces backend over **ClickHouse**, run split into `MODE=reader` and `MODE=writer`. Both are only as healthy as their **ClickHouse** connection and must point at the **same** database — the usual failures are a ClickHouse the pods can't reach/auth, or a reader/writer schema mismatch.

## Problem

- Queries return **no data** though ingestion looks fine, or writes are **rejected** / dropped.

## Context

- Gigapipe `4.1.6` ([[CONCEPT-ADDON_GIGAPIPE]]); part of the observability layer ([[CONCEPT-OBSERVABILITY_STACK]]).
- **Stateless over ClickHouse:** all state is in ClickHouse; if reader and writer point at different DBs/tables, the reader sees nothing the writer wrote.
- **ClickHouse health:** wrong DSN/creds, or an overloaded/misconfigured ClickHouse, breaks both read and write.

## Diagnostics

```bash
kubectl -n <ns> logs deploy/gigapipe-writer | tail   # ClickHouse errors on insert
kubectl -n <ns> logs deploy/gigapipe-reader | tail
# check both share the same CLICKHOUSE_* env / DSN
kubectl -n <ns> get deploy gigapipe-reader gigapipe-writer -o yaml | grep -i clickhouse
```

## Known Issues

- **No data — fix:** ensure reader and writer use the **same** ClickHouse DB/tables and that the writer's inserts succeed (check its logs).
- **ClickHouse — fix:** correct the DSN/credentials; verify ClickHouse is reachable and healthy; create the schema if missing.

## References

Upstream project (see `sources`). Catalog entry [[CONCEPT-ADDON_GIGAPIPE]].
