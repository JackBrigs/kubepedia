---
id: TROUBLE-KATA_CONTAINERS_3_14_DEFECTS
type: troubleshooting
title: "kata-containers 3.14: defects fixed in the 3.14 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.14.0 <3.15.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kata-containers 3.14 known issues
  - kata-containers 3.14 fixed in
  - is this kata-containers bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kata-containers
sources:
  - type: docs
    path: kata-containers/kata-containers release notes for the 3.14 line — bug-fix entries
    url: https://github.com/kata-containers/kata-containers/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kata-containers 3.14: defects fixed in the 3.14 line

## Summary

**5 defects** the project fixed across **1 releases** of the 3.14 line, from 3.14.0 to
3.14.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.14.0

- gpu: Fix rootfs build by @zvonkok in https://github.com/kata-containers/kata-containers/pull/10736
- agent: Update ttrpc to include the fix for connectivity issues by @fidencio in https://github.com/kata-containers/kata-containers/pull/10775
- gpu: Fix arm64 kernel build by @zvonkok in https://github.com/kata-containers/kata-containers/pull/10777
- gpu: Fix arm64 build by @zvonkok in https://github.com/kata-containers/kata-containers/pull/10812
- gpu: Add first target and fix extratarballs by @zvonkok in https://github.com/kata-containers/kata-containers/pull/10791


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.14.0**, the newest release recorded here for this line.

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
