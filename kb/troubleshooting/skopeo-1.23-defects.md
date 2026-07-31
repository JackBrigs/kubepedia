---
id: TROUBLE-SKOPEO_1_23_DEFECTS
type: troubleshooting
title: "skopeo 1.23: defects fixed in the 1.23 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.23.0 <1.24.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - skopeo 1.23 known issues
  - skopeo 1.23 fixed in
  - is this skopeo bug already fixed
tags:
  - troubleshooting
  - upgrade
  - skopeo
sources:
  - type: docs
    path: containers/skopeo release notes for the 1.23 line — bug-fix entries
    url: https://github.com/containers/skopeo/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# skopeo 1.23: defects fixed in the 1.23 line

## Summary

**16 defects** the project fixed across **1 releases** of the 1.23 line, from 1.23.0 to
1.23.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.23.0

- fix(deps): update github.com/opencontainers/image-spec digest to 26647a4 by @renovate[bot] in https://github.com/containers/skopeo/pull/2736
- fix(deps): update common, image, and storage deps to afd10d8 by @renovate[bot] in https://github.com/containers/skopeo/pull/2765
- fix(deps): update common, image, and storage deps to b0f86df by @renovate[bot] in https://github.com/containers/skopeo/pull/2774
- fix(deps): update common, image, and storage deps to e7626b7 by @renovate[bot] in https://github.com/containers/skopeo/pull/2786
- fix(deps): update common, image, and storage deps to b2572af by @renovate[bot] in https://github.com/containers/skopeo/pull/2790
- fix(deps): update common, image, and storage deps to b5801a6 by @renovate[bot] in https://github.com/containers/skopeo/pull/2792
- fix(deps): update common, image, and storage deps to 0e2aefd by @renovate[bot] in https://github.com/containers/skopeo/pull/2794
- Packit: fix downstream post-modifications action by @lsm5 in https://github.com/containers/skopeo/pull/2810
- fix(deps): update common, image, and storage deps to 854aaaf by @renovate[bot] in https://github.com/containers/skopeo/pull/2812
- fix(deps): update github.com/opencontainers/image-spec digest to a4c6ade by @renovate[bot] in https://github.com/containers/skopeo/pull/2813
- fix(deps): update common, image, and storage deps to d48bc74 by @renovate[bot] in https://github.com/containers/skopeo/pull/2819
- Fix misc. warnings by @mtrmac in https://github.com/containers/skopeo/pull/2823
- fix(deps): update common, image, and storage deps to ddaabae by @renovate[bot] in https://github.com/containers/skopeo/pull/2825
- fix(deps): update common, image, and storage deps to 94ad023 by @renovate[bot] in https://github.com/containers/skopeo/pull/2831
- fix(deps): update common, image, and storage deps to 8af7873 by @renovate[bot] in https://github.com/containers/skopeo/pull/2835
- fix(deps): update go.podman.io/storage digest to f0ddf1a by @renovate[bot] in https://github.com/containers/skopeo/pull/2837


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.23.0**, the newest release recorded here for this line.

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
