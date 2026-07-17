---
id: TROUBLE-ARGOCD_APP_OUTOFSYNC
type: troubleshooting
title: "ArgoCD Application stuck OutOfSync / Progressing / sync fails"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - argocd out of sync
  - argocd sync failed
  - application stuck progressing
  - argocd comparison error
  - argocd degraded health
  - argocd rbac sync error
tags:
  - troubleshooting
  - gitops
  - argocd
  - deployment
sources:
  - type: docs
    path: Argo CD — Sync / Health / Troubleshooting
    url: https://argo-cd.readthedocs.io/en/stable/operator-manual/health/
    note: "sync status vs health status; sync fails on RBAC/webhook/CRD ordering (verified)"
relations:
  - type: see_also
    target: CONCEPT-GITOPS
  - type: see_also
    target: TROUBLE-RBAC_FORBIDDEN
  - type: see_also
    target: TROUBLE-ADMISSION_WEBHOOK_BLOCKING
---

# ArgoCD Application stuck OutOfSync / Progressing / sync fails

## Summary

An ArgoCD Application has **two** independent statuses — **Sync** (does the cluster match
Git?) and **Health** (are the resources healthy?). "Stuck" usually means either the sync
**failed to apply** (RBAC/webhook/CRD ordering) or the applied resources never became
**Healthy** (the workload itself is broken). Read both statuses — they point at different
fixes.

## Problem

`kubectl -n argocd get application <app>` (or the UI) shows `OutOfSync`,
`SyncFailed`, or `Progressing`/`Degraded` that never settles; the sync operation errors or
loops.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0` with ArgoCD ([[CONCEPT-GITOPS]],
  [[COMPONENT-ARGOCD]]).
- ArgoCD applies manifests **as its own ServiceAccount** and then evaluates health — a
  failure at either step surfaces as "not synced".

## Diagnostics

- **`argocd app get <app>`** (or UI) — separate **Sync** vs **Health**; the operation
  message names the failing resource and error.
- **Sync failure text** routes it: `forbidden` → RBAC; `failed calling webhook` →
  admission; `no matches for kind` / `CRD not found` → ordering.
- **Diff:** `argocd app diff <app>` — what ArgoCD thinks differs (drift, or a field a
  controller mutates causing perpetual OutOfSync).
- **Resource health:** for a `Degraded`/`Progressing` app, inspect the actual workload pods
  ([[TROUBLE-CRASHLOOPBACKOFF]] / [[TROUBLE-POD_PENDING_UNSCHEDULABLE]]).

## Known Issues

- **`SyncFailed: forbidden`** — the ArgoCD application-controller SA lacks RBAC to create
  that resource/kind. Grant it (least-privilege) — [[TROUBLE-RBAC_FORBIDDEN]].
- **`failed calling webhook`** — an admission webhook rejects/blocks the applied objects
  ([[TROUBLE-ADMISSION_WEBHOOK_BLOCKING]]).
- **CRD ordering (`no matches for kind`)** — the CR is applied before its CRD exists. Use
  **sync waves** / `Replace=true` / apply the CRD first, or enable
  `ServerSideApply`.
- **Perpetual OutOfSync (never converges)** — a controller/webhook mutates a field ArgoCD
  keeps trying to revert. Add `ignoreDifferences` for that field, or use server-side apply.
- **Stuck `Progressing`** — the resources applied but never went Healthy: the **workload**
  is failing (image/config/probe) — fix that, not ArgoCD.
- **`ComparisonError` / repo errors** — ArgoCD can't fetch/render the repo (auth, path,
  Helm/Kustomize error); check the repo credentials and the render.

**Gotchas:**

- **Sync ≠ Health.** `Synced` but `Degraded` = manifests applied, app broken (workload
  problem). `OutOfSync` but `Healthy` = drift not yet applied. Don't conflate them.
- **Auto-sync + selfHeal** will fight manual `kubectl` edits — expected, not a bug.
- Deleting an app with `prune`/finalizers can hang if child resources have finalizers
  ([[TROUBLE-NAMESPACE_STUCK_TERMINATING]] is the analogous finalizer trap).

## References

- Argo CD health/sync docs. GitOps: [[CONCEPT-GITOPS]]; RBAC: [[TROUBLE-RBAC_FORBIDDEN]];
  webhooks: [[TROUBLE-ADMISSION_WEBHOOK_BLOCKING]].
