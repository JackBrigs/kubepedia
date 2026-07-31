---
id: TROUBLE-SKOPEO_1_14_DEFECTS
type: troubleshooting
title: "skopeo 1.14: defects fixed in the 1.14 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.14.0 <1.15.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - skopeo 1.14 known issues
  - skopeo 1.14 fixed in
  - is this skopeo bug already fixed
tags:
  - troubleshooting
  - upgrade
  - skopeo
sources:
  - type: docs
    path: containers/skopeo release notes for the 1.14 line — bug-fix entries
    url: https://github.com/containers/skopeo/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# skopeo 1.14: defects fixed in the 1.14 line

## Summary

**9 defects** the project fixed across **3 releases** of the 1.14 line, from 1.14.0 to
1.14.6. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.14.0

- [CI:BUILD] RPM: fix ELN builds by @lsm5 in https://github.com/containers/skopeo/pull/2026
- Follow-up fixes to #2029 by @mtrmac in https://github.com/containers/skopeo/pull/2048
- fix(deps): update github.com/containers/image/v5 digest to 58d5eb6 by @renovate in https://github.com/containers/skopeo/pull/2099
- Fix a man page link by @mtrmac in https://github.com/containers/skopeo/pull/2103
- fix(deps): update github.com/containers/common digest to 745eaa4 by @renovate in https://github.com/containers/skopeo/pull/2119
- Fix ENTRYPOINT documentation, drop others. by @mtrmac in https://github.com/containers/skopeo/pull/2138
- fix(deps): update github.com/containers/common digest to 3e5caa0 by @renovate in https://github.com/containers/skopeo/pull/2143

### 1.14.1

- Fix libsubid detection by @lsm5 in https://github.com/containers/skopeo/pull/2190

### 1.14.6

- [release-1.14] Fixes Listing tags in JFrog Artifactory may fail by @TomSweeneyRedHat in https://github.com/containers/skopeo/pull/2381


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.14.6**, the newest release recorded here for this line.

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
