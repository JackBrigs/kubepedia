---
id: TROUBLE-SCHEDULER_PLUGINS_BREAKING_CHANGES
type: troubleshooting
title: "scheduler-plugins: declared breaking changes by release"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.25.7 <=0.25.7"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - scheduler-plugins breaking changes
  - scheduler-plugins upgrade broke
  - scheduler-plugins action required upgrade
tags:
  - upgrade
  - breaking-change
  - scheduler-plugins
sources:
  - type: docs
    path: kubernetes-sigs/scheduler-plugins release notes — "breaking changes" / "action required" entries
    url: https://github.com/kubernetes-sigs/scheduler-plugins/releases
    note: "machine-extracted by scripts/upstream_issues.py, short and duplicate lines filtered out"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# scheduler-plugins: declared breaking changes by release

## Summary

**4 behaviour changes** the project itself marked as breaking or action-required, across
1 releases from 0.25.7 to 0.25.7. Read this before planning
an upgrade that crosses any of these versions: unlike defects, these are changes that work as
designed and still break a working configuration.

## Problem

An upgrade across a breaking change usually succeeds — the failure appears afterwards, in behaviour:
a setting silently ignored, a default flipped, an API version withdrawn.

## Context

### 0.25.7

- The API Group of CRD `PodGroup` and `ElasticQuota` is migrated to `scheduling.x-k8s.io`. The brand new installations don't need to do anything. Users migrating to this release need to do the following steps:
- use `kubectl replace -f <crds>` to ensure new CRDs function well
- migrate the labels - new label is using a style of `*.scheduling.x-k8s.io/<label-name>`, e.g., `scheduling.x-k8s.io/pod-group`
- Helm chart now leverages `--namespace scheduler-plugins --create-namespace` to consolidate both Helm release meta info and chart artifacts in the same namespace. Moreover, it enables users to customize the installation namespace.

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

- Upstream releases of `kubernetes-sigs/scheduler-plugins`, read 2026-07-31 via `scripts/upstream_issues.py`;
  raw extraction in `reports/upstream/scheduler-plugins.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
