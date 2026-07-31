---
id: TROUBLE-SKOPEO_1_19_DEFECTS
type: troubleshooting
title: "skopeo 1.19: defects fixed in the 1.19 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.19.0 <1.20.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - skopeo 1.19 known issues
  - skopeo 1.19 fixed in
  - is this skopeo bug already fixed
tags:
  - troubleshooting
  - upgrade
  - skopeo
sources:
  - type: docs
    path: containers/skopeo release notes for the 1.19 line — bug-fix entries
    url: https://github.com/containers/skopeo/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# skopeo 1.19: defects fixed in the 1.19 line

## Summary

**16 defects** the project fixed across **1 releases** of the 1.19 line, from 1.19.0 to
1.19.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.19.0

- fix(deps): update module github.com/spf13/cobra to v1.9.1 by @renovate in https://github.com/containers/skopeo/pull/2523
- fix(deps): update module github.com/containers/image/v5 to v5.34.1 by @renovate in https://github.com/containers/skopeo/pull/2528
- fix(deps): update module github.com/containers/common to v0.62.1 by @renovate in https://github.com/containers/skopeo/pull/2534
- fix(deps): update module github.com/opencontainers/image-spec to v1.1.1 by @renovate in https://github.com/containers/skopeo/pull/2535
- fix(deps): update module github.com/containers/storage to v1.57.2 by @renovate in https://github.com/containers/skopeo/pull/2538
- fix(deps): update module github.com/containers/image/v5 to v5.34.2 by @renovate in https://github.com/containers/skopeo/pull/2540
- fix(deps): update module github.com/containers/common to v0.62.2 by @renovate in https://github.com/containers/skopeo/pull/2546
- fix(deps): update module golang.org/x/term to v0.30.0 by @renovate in https://github.com/containers/skopeo/pull/2553
- fix(deps): update module github.com/containers/common to v0.62.3 by @renovate in https://github.com/containers/skopeo/pull/2560
- chore: fix some function names in comment by @luozexuan in https://github.com/containers/skopeo/pull/2562
- fix(deps): update module golang.org/x/term to v0.31.0 by @renovate in https://github.com/containers/skopeo/pull/2569
- Add golangci-lint run --tests=false, fix found issues by @kolyshkin in https://github.com/containers/skopeo/pull/2565
- fix(deps): update module github.com/containers/storage to v1.58.0 by @renovate in https://github.com/containers/skopeo/pull/2580
- fix(deps): update module golang.org/x/term to v0.32.0 by @renovate in https://github.com/containers/skopeo/pull/2593
- fix(deps): update module github.com/containers/image/v5 to v5.35.0 by @renovate in https://github.com/containers/skopeo/pull/2607
- fix(deps): update module github.com/containers/common to v0.63.0 by @renovate in https://github.com/containers/skopeo/pull/2608


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.19.0**, the newest release recorded here for this line.

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
