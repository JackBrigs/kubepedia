---
id: CONCEPT-ARGOCD_SOURCE_HYDRATOR
type: concept
title: "Argo CD source hydrator + commit-server — push rendered manifests to Git (2.14, alpha)"
status: active
kubespray_version: ">=v2.28.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: ">=2.14.5 <=2.14.21"
verified_at: "2026-07-18"
confidence: verified
aliases:
  - argocd hydrator
  - argocd commit-server
  - argocd push rendered manifests
  - hydrator.enabled
  - argocd source hydrator
tags:
  - argocd
  - gitops
  - concept
sources:
  - type: docs
    path: docs/operator-manual/argocd-cmd-params-cm.yaml
    url: https://github.com/argoproj/argo-cd/blob/v2.14.5/docs/operator-manual/argocd-cmd-params-cm.yaml
    note: "hydrator.enabled + commit.server (argocd-commit-server:8086), commitserver.* keys added in 2.14"
relations:
  - type: see_also
    target: COMPONENT-ARGOCD
  - type: see_also
    target: UPGRADE-ARGOCD_2_11_TO_2_14
---

# Argo CD source hydrator + commit-server — push rendered manifests to Git (2.14, alpha)

## Summary

Argo CD **2.14** introduced the **source hydrator** — an **alpha** feature that renders (hydrates)
manifests and **pushes the rendered output to Git**, so the repo holds both the source templates and
the fully-resolved manifests (a "rendered manifests" / GitOps-of-GitOps pattern). It ships **off by
default** (`hydrator.enabled: "false"`) and adds a **new component**, the `argocd-commit-server`. This
is the version Kubespray pins from v2.28.0, so the capability is present but inert unless enabled.

## Context

- Introduced in Argo CD **2.14** (`docs/operator-manual/argocd-cmd-params-cm.yaml`@v2.14.5) —
  [[UPGRADE-ARGOCD_2_11_TO_2_14]]. Kubespray ships 2.14.x ([[COMPONENT-ARGOCD]]), disabled by default.
- **Config surface:** `hydrator.enabled` (default `"false"`); the commit-server address
  `commit.server: "argocd-commit-server:8086"`, plus `commitserver.listen.address`,
  `commitserver.log.format/level`, `commitserver.metrics.listen.address`.
- **What it does:** on sync, Argo CD renders manifests and **commits them to a separate branch/repo**,
  so the deployed state is auditable as plain YAML in Git — useful for review/promotion workflows and
  drift visibility.
- **Operator note:** **alpha** — don't rely on it for production promotion yet; enabling it means
  running and securing the extra `argocd-commit-server` (it needs write access to your Git repo). If
  you don't enable it, the new params are harmless defaults.

## References

- Argo CD `docs/operator-manual/argocd-cmd-params-cm.yaml`@v2.14.5 (hydrator + commitserver keys).
  Component [[COMPONENT-ARGOCD]]; upgrade [[UPGRADE-ARGOCD_2_11_TO_2_14]].
