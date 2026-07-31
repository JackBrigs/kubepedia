---
id: TROUBLE-KATA_CONTAINERS_3_15_DEFECTS
type: troubleshooting
title: "kata-containers 3.15: defects fixed in the 3.15 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.15.0 <3.16.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kata-containers 3.15 known issues
  - kata-containers 3.15 fixed in
  - is this kata-containers bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kata-containers
sources:
  - type: docs
    path: kata-containers/kata-containers release notes for the 3.15 line — bug-fix entries
    url: https://github.com/kata-containers/kata-containers/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kata-containers 3.15: defects fixed in the 3.15 line

## Summary

**13 defects** the project fixed across **1 releases** of the 3.15 line, from 3.15.0 to
3.15.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.15.0

- minor build fixes by @mythi in https://github.com/kata-containers/kata-containers/pull/10881
- agent: Fix race condition with cgroup watchers by @sprt in https://github.com/kata-containers/kata-containers/pull/10911
- gpu: IOMMUFD fix by @zvonkok in https://github.com/kata-containers/kata-containers/pull/10931
- agent: Fix non-guest-pull build by @fidencio in https://github.com/kata-containers/kata-containers/pull/10934
- kata-deploy: k0s: Fix drop-in path by @fidencio in https://github.com/kata-containers/kata-containers/pull/10960
- Fix virtio-net-ccw by @Jakob-Naucke in https://github.com/kata-containers/kata-containers/pull/10817
- gpu: fix init symlinks by @zvonkok in https://github.com/kata-containers/kata-containers/pull/10965
- Shell check errors fix by @stevenhorsman in https://github.com/kata-containers/kata-containers/pull/10958
- Rework and fix metrics issues by @stevenhorsman in https://github.com/kata-containers/kata-containers/pull/10954
- agent: Fix default linux device permissions by @zvonkok in https://github.com/kata-containers/kata-containers/pull/10976
- agent: fix permisssion according to runc by @zvonkok in https://github.com/kata-containers/kata-containers/pull/10982
- kata-types: Fix bugs related to annotations in kata-types by @Apokleos in https://github.com/kata-containers/kata-containers/pull/10937
- runtime-rs: Fix log_level's comments in configuration-dragonball.toml.in by @teawater in https://github.com/kata-containers/kata-containers/pull/10975


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.15.0**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `kata-containers/kata-containers`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/kata-containers.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
