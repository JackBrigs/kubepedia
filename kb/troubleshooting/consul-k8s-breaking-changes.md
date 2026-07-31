---
id: TROUBLE-CONSUL_K8S_BREAKING_CHANGES
type: troubleshooting
title: "consul-k8s: declared breaking changes by release"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.5.0 <=0.5.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - consul-k8s breaking changes
  - consul-k8s upgrade broke
  - consul-k8s action required upgrade
tags:
  - upgrade
  - breaking-change
  - consul-k8s
sources:
  - type: docs
    path: hashicorp/consul-k8s release notes — "breaking changes" / "action required" entries
    url: https://github.com/hashicorp/consul-k8s/releases
    note: "machine-extracted by scripts/upstream_issues.py, short and duplicate lines filtered out"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# consul-k8s: declared breaking changes by release

## Summary

**3 behaviour changes** the project itself marked as breaking or action-required, across
1 releases from 0.5.0 to 0.5.0. Read this before planning
an upgrade that crosses any of these versions: unlike defects, these are changes that work as
designed and still break a working configuration.

## Problem

An upgrade across a breaking change usually succeeds — the failure appears afterwards, in behaviour:
a setting silently ignored, a default flipped, an API version withdrawn.

## Context

### 0.5.0

- The v1alpha1 API version was deprecated and removed.
- The `NamedAddress` value for `Gateway`'s `spec.addresses[].type` field has
- Implementations are now expected to use `500` instead of `503` responses when

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

- Upstream releases of `hashicorp/consul-k8s`, read 2026-07-31 via `scripts/upstream_issues.py`;
  raw extraction in `reports/upstream/consul-k8s.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
