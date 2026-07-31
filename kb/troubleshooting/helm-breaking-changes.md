---
id: TROUBLE-HELM_BREAKING_CHANGES
type: troubleshooting
title: "helm: declared breaking changes by release"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.5.0 <=2.5.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm breaking changes
  - helm upgrade broke
  - helm action required upgrade
tags:
  - upgrade
  - breaking-change
  - helm
sources:
  - type: docs
    path: helm/helm release notes — "breaking changes" / "action required" entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py, short and duplicate lines filtered out"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm: declared breaking changes by release

## Summary

**3 behaviour changes** the project itself marked as breaking or action-required, across
1 releases from 2.5.0 to 2.5.0. Read this before planning
an upgrade that crosses any of these versions: unlike defects, these are changes that work as
designed and still break a working configuration.

## Problem

An upgrade across a breaking change usually succeeds — the failure appears afterwards, in behaviour:
a setting silently ignored, a default flipped, an API version withdrawn.

## Context

### 2.5.0

- `helm install` and `helm update` no longer download remote charts to the current working directroy. `helm fetch` continues to work as it always has.
- Since `--set` now accepts array indices, `values.yaml` keys of the (literal) form `"foo[0]"` will no longer work.
- A new field, `Force`, was added to the `UpdateReleaseRequest` and `RollbackReleaseRequset` gRPC calls. This will not break existing gRPC clients, but could break forks of Tiller that override existing gRPC calls.

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

- Upstream releases of `helm/helm`, read 2026-07-31 via `scripts/upstream_issues.py`;
  raw extraction in `reports/upstream/helm.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
