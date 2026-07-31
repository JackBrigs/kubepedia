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
  - what breaks upgrading helm
tags:
  - upgrade
  - breaking-change
  - helm
sources:
  - type: docs
    path: helm/helm release notes — entries marked breaking / action required
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm: declared breaking changes by release

## Summary

**3 behaviour changes** the project itself marked as breaking or action-required, across
1 releases from 2.5.0 to 2.5.0. These are not defects: they work as designed and still break
a configuration that worked yesterday. An upgrade crossing any of them needs a decision, not just a
rollout.

## Problem

The upgrade itself usually succeeds. The damage shows up afterwards — a setting silently ignored, a
default flipped, an API version withdrawn, a variable that must now be set explicitly.

## Context

### 2.5.0

- `helm install` and `helm update` no longer download remote charts to the current working directroy. `helm fetch` continues to work as it always has
- Since `--set` now accepts array indices, `values.yaml` keys of the (literal) form `"foo[0]"` will no longer work
- A new field, `Force`, was added to the `UpdateReleaseRequest` and `RollbackReleaseRequset` gRPC calls. This will not break existing gRPC clients, but could break forks of Tiller that override existing gRPC calls


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

- Upstream releases of `helm/helm`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/helm.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
