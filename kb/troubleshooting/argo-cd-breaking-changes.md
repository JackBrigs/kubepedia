---
id: TROUBLE-ARGO_CD_BREAKING_CHANGES
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
  - what breaks upgrading argo-cd
tags:
  - upgrade
  - breaking-change
  - argo-cd
sources:
  - type: docs
    path: argoproj/argo-cd release notes — entries marked breaking / action required
    url: https://github.com/argoproj/argo-cd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# argo-cd: declared breaking changes by release

## Summary

**8 behaviour changes** the project itself marked as breaking or action-required, across
3 releases from 0.11.0 to 1.2.0. These are not defects: they work as designed and still break
a configuration that worked yesterday. An upgrade crossing any of them needs a decision, not just a
rollout.

## Problem

The upgrade itself usually succeeds. The damage shows up afterwards — a setting silently ignored, a
default flipped, an API version withdrawn, a variable that must now be set explicitly.

## Context

### 0.11.0

- Argo CD's resource names were renamed for consistency. For example, the application-controller deployment was renamed to argocd-application-controller. When upgrading from v0.10 to v0.11, the older resources should be pruned to avoid inconsistent state and controller in-fighting
- As a consequence to moving to recommended kubernetes labels, when upgrading from v0.10 to v0.11, all applications will immediately be OutOfSync due to the change in tracking labels. This will correct itself with another sync of the application. However, since Pods will be recreated, please take this into consideration, especially if your applications are configured with auto-sync
- There was significant reworking of the `app.status` fields to reduce the payload size, simplify the datastructure and remove fields which were no longer used by the controller. No breaking changes were made in `app.spec`
- An older Argo CD CLI (v0.10 and below) will not be compatible with Argo CD v0.11. To keep CI pipelines in sync with the API server, it is recommended to have pipelines download the CLI directly from the API server https://${ARGOCD_SERVER}/download/argocd-linux-amd64 during the CI pipeline

### 1.0.0

- Remove deprecated componentParameterOverrides field #1372

### 1.2.0

- Kustomize v1 support is removed. All kustomize charts are built using the same Kustomize version
- Kustomize v2.0.3 upgraded to v3.1.0 . We've noticed one backward incompatible change: https://github.com/kubernetes-sigs/kustomize/issues/42 . Starting v2.1.0 namespace prefix feature works with CRD ( which might cause renaming of generated resource definitions)
- Argo CD config maps must be annotated with `app.kubernetes.io/part-of: argocd` label. Make sure to apply updated `install.yaml` manifest in addition to changing image version


## Diagnostics

```bash
# which version is actually deployed
kubectl get nodes -o wide
helm list -A
```

Cross the list above against the range you are moving through, not only the target version.

## Known Issues

Entries are verbatim from upstream release notes and filtered mechanically: lines shorter than
45 characters and duplicates are dropped, because section headings and list fragments reach the
extractor looking like entries. If a release you care about appears empty here, read its notes
upstream before concluding that nothing changed.

## References

- Upstream releases of `argoproj/argo-cd`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/argo-cd.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
