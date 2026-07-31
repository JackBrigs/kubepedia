---
id: TROUBLE-SKOPEO_1_18_DEFECTS
type: troubleshooting
title: "skopeo 1.18: defects fixed in the 1.18 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.18.0 <1.19.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - skopeo 1.18 known issues
  - skopeo 1.18 fixed in
  - is this skopeo bug already fixed
tags:
  - troubleshooting
  - upgrade
  - skopeo
sources:
  - type: docs
    path: containers/skopeo release notes for the 1.18 line — bug-fix entries
    url: https://github.com/containers/skopeo/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# skopeo 1.18: defects fixed in the 1.18 line

## Summary

**18 defects** the project fixed across **1 releases** of the 1.18 line, from 1.18.0 to
1.18.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.18.0

- fix(deps): update module github.com/moby/sys/capability to v0.4.0 by @renovate in https://github.com/containers/skopeo/pull/2457
- fix(deps): update module github.com/masterminds/semver/v3 to v3.3.1 by @renovate in https://github.com/containers/skopeo/pull/2462
- fix(deps): update module github.com/stretchr/testify to v1.10.0 by @renovate in https://github.com/containers/skopeo/pull/2464
- fix(deps): update golang.org/x/exp digest to 2d47ceb by @renovate in https://github.com/containers/skopeo/pull/2467
- Fix handling of errorShouldDisplayUsage by @mtrmac in https://github.com/containers/skopeo/pull/2469
- fix(deps): update module golang.org/x/term to v0.27.0 by @renovate in https://github.com/containers/skopeo/pull/2471
- fix(deps): update module github.com/containers/ocicrypt to v1.2.1 by @renovate in https://github.com/containers/skopeo/pull/2475
- fix(deps): update golang.org/x/exp digest to b2144cd by @renovate in https://github.com/containers/skopeo/pull/2482
- fix(deps): update module golang.org/x/term to v0.28.0 by @renovate in https://github.com/containers/skopeo/pull/2487
- fix(deps): update module github.com/containers/storage to v1.56.1 by @renovate in https://github.com/containers/skopeo/pull/2494
- fix(deps): update module github.com/containers/image/v5 to v5.33.1 by @renovate in https://github.com/containers/skopeo/pull/2495
- fix(deps): update module github.com/containers/common to v0.61.1 by @renovate in https://github.com/containers/skopeo/pull/2498
- fix(deps): update module github.com/containers/storage to v1.57.0 by @renovate in https://github.com/containers/skopeo/pull/2506
- fix(deps): update module github.com/containers/storage to v1.57.1 by @renovate in https://github.com/containers/skopeo/pull/2507
- fix(deps): update module github.com/containers/image/v5 to v5.34.0 by @renovate in https://github.com/containers/skopeo/pull/2508
- fix(deps): update module github.com/spf13/pflag to v1.0.6 by @renovate in https://github.com/containers/skopeo/pull/2505
- fix(deps): update module github.com/containers/common to v0.62.0 by @renovate in https://github.com/containers/skopeo/pull/2509
- fix(deps): update module golang.org/x/term to v0.29.0 by @renovate in https://github.com/containers/skopeo/pull/2511


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.18.0**, the newest release recorded here for this line.

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
