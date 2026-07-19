---
id: TROUBLE-AWX_OPERATOR
type: troubleshooting
title: "AWX Operator: AWX instance stuck deploying — Postgres PVC, migrations, admin secret, resources"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: ">=24.6.1"
verified_at: "2026-07-19"
confidence: confirmed
aliases:
  - awx not coming up
  - awx operator reconcile stuck
  - awx postgres pending
  - awx migration job
  - awx admin password
tags:
  - troubleshooting
  - automation
  - awx
  - operator
sources:
  - type: external
    path: awx-operator
    url: https://github.com/ansible/awx-operator
    note: "operator 2.19.1 -> AWX 24.6.1; Postgres 15 + Redis 7; migration + admin-password secret"
relations:
  - type: see_also
    target: CONCEPT-ADDON_AWX
  - type: see_also
    target: TROUBLE-PVC_PENDING_NO_STORAGECLASS
---

# AWX Operator: AWX instance stuck deploying — Postgres PVC, migrations, admin secret, resources

## Summary

An `AWX` CR never becomes ready — the instance is heavy and DB-bound, so the usual culprits are a **Postgres PVC that won't bind**, stalled **migrations**, a missing **admin-password secret**, or insufficient **resources**. The operator keeps reconciling while the app waits on its database.

## Problem

- After creating an `AWX` CR, the instance never becomes ready: `awx-*` pods `Pending`/`CrashLoop`, the
  operator reconcile loops, or the web UI never serves.

## Context

- AWX Operator `2.19.1` → AWX `24.6.1` ([[CONCEPT-ADDON_AWX]]); defaults to **PostgreSQL 15** + Redis 7.
- **Postgres storage:** the managed Postgres needs a **PVC** that binds; no default StorageClass or a
  `Pending` PVC ([[TROUBLE-PVC_PENDING_NO_STORAGECLASS]]) stalls the whole instance (AWX won't start
  without its DB).
- **Migrations:** the operator runs a **migration** step against Postgres; if Postgres isn't ready or
  creds mismatch, the task/web pods crashloop waiting on the schema.
- **Admin secret:** the initial admin password comes from a Secret (`<name>-admin-password`); a missing
  or mis-referenced secret blocks first login.
- **Resources:** AWX (web + task + ee + postgres + redis) is heavy; insufficient CPU/memory or quota
  leaves pods `Pending`/OOM.

## Diagnostics

```bash
kubectl -n awx logs deploy/awx-operator-controller-manager -c awx-manager | tail
kubectl -n awx get pods,pvc                                  # postgres PVC bound? pods state?
kubectl -n awx describe awx <name>                           # CR conditions
kubectl -n awx get secret <name>-admin-password
```

## Known Issues

- **Postgres PVC — fix:** ensure a default/working StorageClass so the DB PVC binds; the instance can't
  progress until Postgres is `Running`.
- **Migrations/crashloop — fix:** confirm Postgres is up and the DB creds secret matches; the task/web
  pods recover once migrations complete.
- **Admin login — fix:** read the generated `<name>-admin-password` secret (or set your own before
  apply); don't recreate it after first deploy without updating the DB.
- **Resources — fix:** raise requests/limits or free quota; give the node enough headroom for the full
  AWX pod set.
- **External DB alternative:** point the CR at an external Postgres (`postgres_configuration_secret`) to
  avoid the managed-DB PVC dependency in constrained clusters.

## References

- awx-operator upstream. Addon [[CONCEPT-ADDON_AWX]]; storage [[TROUBLE-PVC_PENDING_NO_STORAGECLASS]].
