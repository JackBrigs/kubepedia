---
id: TROUBLE-SKOPEO_1_11_DEFECTS
type: troubleshooting
title: "skopeo 1.11: defects fixed in the 1.11 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.11.0 <1.12.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - skopeo 1.11 known issues
  - skopeo 1.11 fixed in
  - is this skopeo bug already fixed
tags:
  - troubleshooting
  - upgrade
  - skopeo
sources:
  - type: docs
    path: containers/skopeo release notes for the 1.11 line — bug-fix entries
    url: https://github.com/containers/skopeo/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# skopeo 1.11: defects fixed in the 1.11 line

## Summary

**14 defects** the project fixed across **1 releases** of the 1.11 line, from 1.11.0 to
1.11.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.11.0

- fix(deps): update module github.com/stretchr/testify to v1.8.1 by @renovate in https://github.com/containers/skopeo/pull/1789
- fix(deps): update module golang.org/x/term to v0.1.0 by @renovate in https://github.com/containers/skopeo/pull/1791
- fix(deps): update module github.com/spf13/cobra to v1.6.1 by @renovate in https://github.com/containers/skopeo/pull/1800
- fix(deps): update module golang.org/x/term to v0.2.0 by @renovate in https://github.com/containers/skopeo/pull/1804
- fix(deps): update module github.com/containers/storage to v1.44.0 by @renovate in https://github.com/containers/skopeo/pull/1809
- [skip-ci] GHA/Cirrus-cron: Fix execution order by @cevich in https://github.com/containers/skopeo/pull/1820
- fix(deps): update module golang.org/x/term to v0.3.0 by @renovate in https://github.com/containers/skopeo/pull/1818
- proxy: Fix leak of blobs from containers-storage by @cgwalters in https://github.com/containers/skopeo/pull/1837
- fix(deps): update module golang.org/x/term to v0.4.0 by @renovate in https://github.com/containers/skopeo/pull/1839
- fix(deps): update module github.com/containers/storage to v1.45.0 by @renovate in https://github.com/containers/skopeo/pull/1853
- fix(deps): update module github.com/containers/storage to v1.45.1 by @renovate in https://github.com/containers/skopeo/pull/1857
- Cirrus: Fix c/image CI testing by @cevich in https://github.com/containers/skopeo/pull/1862
- Fix storage.conf overrides in test-system in CI, update c/storage by @mtrmac in https://github.com/containers/skopeo/pull/1864
- Fix `make test-system` when run as an unprivileged user (containerized) by @mtrmac in https://github.com/containers/skopeo/pull/1868


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.11.0**, the newest release recorded here for this line.

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
