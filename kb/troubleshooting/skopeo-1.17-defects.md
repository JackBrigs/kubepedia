---
id: TROUBLE-SKOPEO_1_17_DEFECTS
type: troubleshooting
title: "skopeo 1.17: defects fixed in the 1.17 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.17.0 <1.18.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - skopeo 1.17 known issues
  - skopeo 1.17 fixed in
  - is this skopeo bug already fixed
tags:
  - troubleshooting
  - upgrade
  - skopeo
sources:
  - type: docs
    path: containers/skopeo release notes for the 1.17 line — bug-fix entries
    url: https://github.com/containers/skopeo/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# skopeo 1.17: defects fixed in the 1.17 line

## Summary

**16 defects** the project fixed across **1 releases** of the 1.17 line, from 1.17.0 to
1.17.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.17.0

- fix(deps): update module golang.org/x/term to v0.23.0 by @renovate in https://github.com/containers/skopeo/pull/2390
- fix(deps): update module github.com/containers/image/v5 to v5.32.1 by @renovate in https://github.com/containers/skopeo/pull/2394
- fix(deps): update module github.com/containers/common to v0.60.1 by @renovate in https://github.com/containers/skopeo/pull/2396
- fix(deps): update module github.com/containers/image/v5 to v5.32.2 by @renovate in https://github.com/containers/skopeo/pull/2403
- fix(deps): update module github.com/containers/common to v0.60.2 by @renovate in https://github.com/containers/skopeo/pull/2405
- fix(deps): update module github.com/masterminds/semver/v3 to v3.3.0 by @renovate in https://github.com/containers/skopeo/pull/2410
- fix(deps): update golang.org/x/exp digest to 9b4947d by @renovate in https://github.com/containers/skopeo/pull/2415
- fix(deps): update module golang.org/x/term to v0.24.0 by @renovate in https://github.com/containers/skopeo/pull/2418
- fix(deps): update module github.com/containers/common to v0.60.3 by @renovate in https://github.com/containers/skopeo/pull/2425
- fix(deps): update golang.org/x/exp digest to 701f63a by @renovate in https://github.com/containers/skopeo/pull/2429
- fix(deps): update module github.com/containers/common to v0.60.4 by @renovate in https://github.com/containers/skopeo/pull/2430
- fix(deps): update module golang.org/x/term to v0.25.0 by @renovate in https://github.com/containers/skopeo/pull/2431
- Fix format string inconsistency causing a build failure by @mtrmac in https://github.com/containers/skopeo/pull/2440
- fix(deps): update module github.com/containers/storage to v1.55.1 by @renovate in https://github.com/containers/skopeo/pull/2444
- fix(deps): update golang.org/x/exp digest to f66d83c by @renovate in https://github.com/containers/skopeo/pull/2447
- fix(deps): update module github.com/containers/image/v5 to v5.33.0 by @renovate in https://github.com/containers/skopeo/pull/2453


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.17.0**, the newest release recorded here for this line.

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
