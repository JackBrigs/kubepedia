---
id: TROUBLE-SKOPEO_1_15_DEFECTS
type: troubleshooting
title: "skopeo 1.15: defects fixed in the 1.15 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.15.0 <1.16.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - skopeo 1.15 known issues
  - skopeo 1.15 fixed in
  - is this skopeo bug already fixed
tags:
  - troubleshooting
  - upgrade
  - skopeo
sources:
  - type: docs
    path: containers/skopeo release notes for the 1.15 line — bug-fix entries
    url: https://github.com/containers/skopeo/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# skopeo 1.15: defects fixed in the 1.15 line

## Summary

**13 defects** the project fixed across **1 releases** of the 1.15 line, from 1.15.0 to
1.15.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.15.0

- fix(deps): update module github.com/opencontainers/image-spec to v1.1.0-rc6 by @renovate in https://github.com/containers/skopeo/pull/2201
- fix(deps): update module github.com/containers/storage to v1.52.0 by @renovate in https://github.com/containers/skopeo/pull/2196
- fix(deps): update module github.com/containers/common to v0.57.3 by @renovate in https://github.com/containers/skopeo/pull/2208
- fix(deps): update golang.org/x/exp digest to 1b97071 by @renovate in https://github.com/containers/skopeo/pull/2211
- fix(deps): update module github.com/containers/common to v0.57.4 by @renovate in https://github.com/containers/skopeo/pull/2212
- fix(deps): update module github.com/opencontainers/image-spec to v1.1.0 by @renovate in https://github.com/containers/skopeo/pull/2231
- Avoid a warning by gopls / VSCode by @mtrmac in https://github.com/containers/skopeo/pull/2237
- fix(deps): update github.com/containers/image/v5 digest to faa4f4f by @renovate in https://github.com/containers/skopeo/pull/2239
- fix(deps): update module golang.org/x/term to v0.18.0 by @renovate in https://github.com/containers/skopeo/pull/2244
- fix(deps): update module github.com/containers/storage to v1.53.0 by @renovate in https://github.com/containers/skopeo/pull/2243
- fix(deps): update module github.com/containers/image/v5 to v5.30.0 by @renovate in https://github.com/containers/skopeo/pull/2248
- fix(deps): update module github.com/containers/common to v0.58.0 by @renovate in https://github.com/containers/skopeo/pull/2250
- fix(deps): update module github.com/containers/ocicrypt to v1.1.10 by @renovate in https://github.com/containers/skopeo/pull/2254


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.15.0**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `containers/skopeo`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/skopeo.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
