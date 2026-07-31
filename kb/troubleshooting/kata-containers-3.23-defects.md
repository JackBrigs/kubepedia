---
id: TROUBLE-KATA_CONTAINERS_3_23_DEFECTS
type: troubleshooting
title: "kata-containers 3.23: defects fixed in the 3.23 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.23.0 <3.24.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kata-containers 3.23 known issues
  - kata-containers 3.23 fixed in
  - is this kata-containers bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kata-containers
sources:
  - type: docs
    path: kata-containers/kata-containers release notes for the 3.23 line — bug-fix entries
    url: https://github.com/kata-containers/kata-containers/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kata-containers 3.23: defects fixed in the 3.23 line

## Summary

**6 defects** the project fixed across **1 releases** of the 3.23 line, from 3.23.0 to
3.23.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.23.0

- dragonball: Bump kvm-ioctls to fix security issue by @spectator333 in https://github.com/kata-containers/kata-containers/pull/11867
- runtime-rs: some remote hypervisor fixes by @pmores in https://github.com/kata-containers/kata-containers/pull/11857
- runtime-rs: Fix several incorrect settings with guest empty dir. by @Apokleos in https://github.com/kata-containers/kata-containers/pull/12067
- runtime-rs: fix the issue of hot-unplug memory smaller by @lifupan in https://github.com/kata-containers/kata-containers/pull/12038
- runtime-rs: fix the issue of wrong vcpu number by @lifupan in https://github.com/kata-containers/kata-containers/pull/12095
- runtime: fix the issue of update interface error by @lifupan in https://github.com/kata-containers/kata-containers/pull/12044


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.23.0**, the newest release recorded here for this line.

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
