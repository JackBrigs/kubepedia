---
id: TROUBLE-CONTAINERD_BREAKING_CHANGES
type: troubleshooting
title: "containerd: declared breaking changes by release"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.0.0 <=2.3.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - containerd breaking changes
  - containerd upgrade broke
  - containerd action required upgrade
tags:
  - upgrade
  - breaking-change
  - containerd
sources:
  - type: docs
    path: containerd/containerd release notes — "breaking changes" / "action required" entries
    url: https://github.com/containerd/containerd/releases
    note: "machine-extracted by scripts/upstream_issues.py, short and duplicate lines filtered out"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# containerd: declared breaking changes by release

## Summary

**5 behaviour changes** the project itself marked as breaking or action-required, across
3 releases from 2.0.0 to 2.3.0. Read this before planning
an upgrade that crosses any of these versions: unlike defects, these are changes that work as
designed and still break a working configuration.

## Problem

An upgrade across a breaking change usually succeeds — the failure appears afterwards, in behaviour:
a setting silently ignored, a default flipped, an API version withdrawn.

## Context

### 2.0.0

- Update RuntimeDefault seccomp profile to disallow io_uring related syscalls
- Remove `LimitNOFILE` from `containerd.service`
- Remove `io.containerd.runtime.v1.linux` and `io.containerd.runc.v1`

### 2.1.0

- Update FreeBSD defaults and re-organize platform defaults

### 2.3.0

- Accumulate owners for OCI hook adjustments, disallowing commas in plugin names ([containerd/nri#264](https://github.com/containerd/nri/pull/264))

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

- Upstream releases of `containerd/containerd`, read 2026-07-31 via `scripts/upstream_issues.py`;
  raw extraction in `reports/upstream/containerd.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
