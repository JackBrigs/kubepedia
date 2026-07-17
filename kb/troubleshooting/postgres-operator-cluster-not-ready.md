---
id: TROUBLE-POSTGRES_OPERATOR_CLUSTER_NOT_READY
type: troubleshooting
title: "Zalando postgres-operator: cluster not ready / failover issues"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: ">=1.13.0 <=1.15.1"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - postgresql cluster not coming up
  - spilo pod crashloop
  - patroni no leader
  - postgres-operator failover stuck
tags:
  - troubleshooting
  - postgresql
  - zalando
  - data
sources:
  - type: docs
    path: postgres-operator quickstart/troubleshooting
    url: https://github.com/zalando/postgres-operator/blob/master/docs/quickstart.md
    note: "Spilo/Patroni cluster, roles, failover"
relations:
  - type: see_also
    target: CONCEPT-ADDON_ZALANDO_POSTGRES_OPERATOR
---

# Zalando postgres-operator: cluster not ready / failover issues

## Summary

A `postgresql` cluster stays not-ready, a Spilo pod crashloops, or failover doesn't elect a
new primary. Spilo runs **Patroni** for HA; the block is usually storage/permissions on the
data dir, Patroni leader election, or a blocked major-version upgrade.

## Problem

- `postgresql` resource never reaches `Running`; pods `0/1` or `CrashLoopBackOff`.
- No primary after a node failure (all replicas, no leader).
- Connections refused / read-only.

## Context

- Applies to postgres-operator **1.13–1.15** (owner runs 1.14.0 —
  [[CONCEPT-ADDON_ZALANDO_POSTGRES_OPERATOR]]). Manages PostgreSQL 13–17 (PG12 dropped in
  1.14).

## Diagnostics

1. `kubectl logs <spilo-pod>` — Patroni output. `patronictl list` (exec) shows member roles
   and lag.
2. **Data dir / PVC:** permission-denied on the mnesia/pgdata mount, or a `Pending` PVC (no
   StorageClass) keeps the pod down — check the PVC and `fsGroup`/security context.
3. **No leader / failover stuck:** Patroni needs its DCS (Kubernetes endpoints/configmaps) and
   RBAC; check the operator and pod RBAC. A network partition or all-replica lag can block
   promotion.
4. **Major-version upgrade blocked:** a failed major upgrade is now annotation-tracked to skip
   retries — inspect the cluster annotations/events; ensure no PG12 clusters remain (dropped).
5. **Operator health:** `kubectl logs deploy/postgres-operator` for reconcile errors.

## Known Issues

- 1.14.0 changed SYNC/UPDATE **log message format** — log-based alerting may need updating.
- The Spilo (PostgreSQL) image carries its own CVE stream — track image updates separately
  from the operator.

## References

- postgres-operator docs (above); addon: [[CONCEPT-ADDON_ZALANDO_POSTGRES_OPERATOR]].
