---
id: TROUBLE-ARGOCD_BREAKING_CHANGES
type: troubleshooting
title: "argo-cd: declared breaking changes by release"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.11.0 <=1.2.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - argo-cd breaking changes
  - argo-cd upgrade broke
  - argo-cd action required upgrade
tags:
  - upgrade
  - breaking-change
  - argo-cd
sources:
  - type: docs
    path: argoproj/argo-cd release notes — "breaking changes" / "action required" entries
    url: https://github.com/argoproj/argo-cd/releases
    note: "machine-extracted by scripts/upstream_issues.py, short and duplicate lines filtered out"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# argo-cd: declared breaking changes by release

## Summary

**8 behaviour changes** the project itself marked as breaking or action-required, across
3 releases from 0.11.0 to 1.2.0. Read this before planning
an upgrade that crosses any of these versions: unlike defects, these are changes that work as
designed and still break a working configuration.

## Problem

An upgrade across a breaking change usually succeeds — the failure appears afterwards, in behaviour:
a setting silently ignored, a default flipped, an API version withdrawn.

## Context

### 0.11.0

- Argo CD's resource names were renamed for consistency. For example, the application-controller
- As a consequence to moving to recommended kubernetes labels, when upgrading from v0.10 to v0.11,
- There was significant reworking of the `app.status` fields to reduce the payload size, simplify
- An older Argo CD CLI (v0.10 and below) will not be compatible with Argo CD v0.11. To keep

### 1.0.0

- Remove deprecated componentParameterOverrides field #1372

### 1.2.0

- Kustomize v1 support is removed. All kustomize charts are built using the same Kustomize version
- Kustomize v2.0.3 upgraded to v3.1.0 . We've noticed one backward incompatible change: https://github.com/kubernetes-sigs/kustomize/issues/42 . Starting v2.1.0 namespace prefix feature works with CRD ( which might cause renaming of generated resource definitions)
- Argo CD config maps must be annotated with `app.kubernetes.io/part-of: argocd` label. Make sure to apply updated `install.yaml` manifest in addition to changing image version.

## Diagnostics

Compare the version in use against the list above:

```bash
kubectl get nodes -o wide          # runtime versions, for node components
helm list -A                       # chart-deployed components
```

## Known Issues

Entries are verbatim from upstream release notes and filtered mechanically: lines shorter than 45
characters and duplicates were dropped, because section headings and list fragments come through the
extractor as if they were entries. If a release you care about looks empty here, read its notes
upstream before concluding nothing changed.

## References

- Upstream releases of `argoproj/argo-cd`, read 2026-07-31 via `scripts/upstream_issues.py`;
  raw extraction in `reports/upstream/argo-cd.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
