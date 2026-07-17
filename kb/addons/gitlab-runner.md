---
id: CONCEPT-ADDON_GITLAB_RUNNER
type: concept
title: "GitLab Runner — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "18.4.0"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - gitlab-runner
  - gitlab-com-runner
  - gitlab ci runner
tags:
  - addons
  - ci
  - gitlab
sources:
  - type: code
    path: Chart.yaml (v0.81.0)
    url: https://gitlab.com/gitlab-org/charts/gitlab-runner/-/raw/v0.81.0/Chart.yaml
    note: "no kubeVersion; app 18.4.0"
  - type: docs
    path: GitLab Runner Kubernetes install
    url: https://docs.gitlab.com/runner/install/kubernetes/
    note: "install + support policy"
relations:
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
---

# GitLab Runner — addon

## Summary

GitLab Runner deployed via the official chart. Two instances are in the inventory:
`gitlab-runner` chart **0.81.0** (app **18.4.0**) and `gitlab-com-runner` chart **0.63.0**
(app **16.10.0**). The 16.10 → 18.x span crosses the **registration-token deprecation** — the
single most important migration item here.

## Context

- Class: upstream addon; catalog row in [[CONCEPT-ADDON_CATALOG]].
- Runs CI jobs as pods via the Kubernetes executor; RBAC + a namespace for job pods are
  required.

## Implementation

- Chart→app: `0.81.0` → **18.4.0**; `0.63.0` → **16.10.0** (raw `Chart.yaml`).
- Chart `kubeVersion`: **none** in either version.
- HTTPS is the chart default since 0.65.0.

## Configuration

- **Registration architecture change (16.10 → 18.x):** the new authentication-token
  ("Next Token") flow replaces the legacy **registration-token** workflow, which is
  deprecated and disabled by default from GitLab **17.0** — plan the migration when moving
  the old `gitlab-com-runner` (16.10.0) forward.
- **ExternalSecret API:** chart 0.81.0 bumped it to `v1`; if you use external-secrets, its
  operator must support the `v1` CRD (old `v1beta1` may break).
- The legacy Kubernetes execution strategy
  (`FF_USE_LEGACY_KUBERNETES_EXECUTION_STRATEGY`) is being removed in 18.x.

## Compatibility

- **Kubernetes range:** no precise per-minor matrix published (**unverified**); docs state
  only a floor and a rolling support policy (a new K8s minor ~3 months after release,
  ≥3 production-ready minors). Functions across 1.29–1.35.
- **Known issues:** an "Upgrade recommended" banner can persist after upgrading; Kubernetes
  executor pod/attach, image-pull and RBAC failures are the common runtime modes.
- **CVEs:** none found for the Runner Go module `gitlab.com/gitlab-org/gitlab-runner` at
  18.4.0 (OSV empty). **Do not conflate** with GitLab **server** 18.4.x security patches —
  those are a different product.

## References

- `Chart.yaml` (0.81.0/0.63.0), Kubernetes install + executor troubleshooting docs (above).
- Catalog: [[CONCEPT-ADDON_CATALOG]].
