---
id: TROUBLE-SKOPEO_1_16_DEFECTS
type: troubleshooting
title: "skopeo 1.16: defects fixed in the 1.16 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.16.0 <1.17.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - skopeo 1.16 known issues
  - skopeo 1.16 fixed in
  - is this skopeo bug already fixed
tags:
  - troubleshooting
  - upgrade
  - skopeo
sources:
  - type: docs
    path: containers/skopeo release notes for the 1.16 line — bug-fix entries
    url: https://github.com/containers/skopeo/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# skopeo 1.16: defects fixed in the 1.16 line

## Summary

**24 defects** the project fixed across **1 releases** of the 1.16 line, from 1.16.0 to
1.16.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.16.0

- fix(deps): update module github.com/containers/common to v0.58.1 by @renovate in https://github.com/containers/skopeo/pull/2275
- fix(deps): update module golang.org/x/term to v0.19.0 by @renovate in https://github.com/containers/skopeo/pull/2281
- [skip-ci] Fix issue/pr lock workflow by @cevich in https://github.com/containers/skopeo/pull/2289
- fix(deps): update module github.com/containers/common to v0.58.2 by @renovate in https://github.com/containers/skopeo/pull/2300
- chore: fix function names by @writegr in https://github.com/containers/skopeo/pull/2304
- fix(deps): update module golang.org/x/exp to v0.0.0-20240416160154-fe59bbe5cc7f by @renovate in https://github.com/containers/skopeo/pull/2313
- fix summaries for `standalone-sign` and `standalone-verify` by @ktdreyer in https://github.com/containers/skopeo/pull/2315
- fix(deps): update module golang.org/x/term to v0.20.0 by @renovate in https://github.com/containers/skopeo/pull/2318
- fix(deps): update module golang.org/x/exp to v0.0.0-20240506185415-9bf2ced13842 by @renovate in https://github.com/containers/skopeo/pull/2319
- fix(deps): update module github.com/containers/common to v0.58.3 by @renovate in https://github.com/containers/skopeo/pull/2324
- fix(deps): update module github.com/containers/image/v5 to v5.31.0 by @renovate in https://github.com/containers/skopeo/pull/2334
- fix(deps): update module github.com/containers/common to v0.59.0 by @renovate in https://github.com/containers/skopeo/pull/2336
- fix(deps): update golang.org/x/exp digest to fd00a4e by @renovate in https://github.com/containers/skopeo/pull/2345
- fix(deps): update module github.com/containers/common to v0.59.1 by @renovate in https://github.com/containers/skopeo/pull/2347
- fix(deps): update module golang.org/x/term to v0.21.0 by @renovate in https://github.com/containers/skopeo/pull/2348
- fix(deps): update module github.com/spf13/cobra to v1.8.1 by @renovate in https://github.com/containers/skopeo/pull/2355
- fix(deps): update module github.com/containers/image/v5 to v5.31.1 by @renovate in https://github.com/containers/skopeo/pull/2363
- fix(deps): update golang.org/x/exp digest to 7f521ea by @renovate in https://github.com/containers/skopeo/pull/2372
- fix(deps): update module github.com/containers/ocicrypt to v1.2.0 by @renovate in https://github.com/containers/skopeo/pull/2373
- fix(deps): update module golang.org/x/term to v0.22.0 by @renovate in https://github.com/containers/skopeo/pull/2374
- fix(deps): update module github.com/containers/common to v0.59.2 by @renovate in https://github.com/containers/skopeo/pull/2379
- fix(deps): update module github.com/containers/storage to v1.55.0 by @renovate in https://github.com/containers/skopeo/pull/2384
- fix(deps): update module github.com/containers/image/v5 to v5.32.0 by @renovate in https://github.com/containers/skopeo/pull/2383
- fix(deps): update module github.com/containers/common to v0.60.0 by @renovate in https://github.com/containers/skopeo/pull/2386


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.16.0**, the newest release recorded here for this line.

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
