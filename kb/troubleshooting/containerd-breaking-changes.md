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
  - what breaks upgrading containerd
tags:
  - upgrade
  - breaking-change
  - containerd
sources:
  - type: docs
    path: containerd/containerd release notes — entries marked breaking / action required
    url: https://github.com/containerd/containerd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# containerd: declared breaking changes by release

## Summary

**5 behaviour changes** the project itself marked as breaking or action-required, across
3 releases from 2.0.0 to 2.3.0. These are not defects: they work as designed and still break
a configuration that worked yesterday. An upgrade crossing any of them needs a decision, not just a
rollout.

## Problem

The upgrade itself usually succeeds. The damage shows up afterwards — a setting silently ignored, a
default flipped, an API version withdrawn, a variable that must now be set explicitly.

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

- Upstream releases of `containerd/containerd`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/containerd.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
