---
id: TROUBLE-KATA_CONTAINERS_3_31_DEFECTS
type: troubleshooting
title: "kata-containers 3.31: defects fixed in the 3.31 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.31.0 <3.32.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kata-containers 3.31 known issues
  - kata-containers 3.31 fixed in
  - is this kata-containers bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kata-containers
sources:
  - type: docs
    path: kata-containers/kata-containers release notes for the 3.31 line — bug-fix entries
    url: https://github.com/kata-containers/kata-containers/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kata-containers 3.31: defects fixed in the 3.31 line

## Summary

**7 defects** the project fixed across **1 releases** of the 3.31 line, from 3.31.0 to
3.31.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.31.0

- genpolicy: Fix matching of `..` in paths by @gkurz in https://github.com/kata-containers/kata-containers/pull/12991
- runtime-rs: Fix warnings in rust runtime by @Apokleos in https://github.com/kata-containers/kata-containers/pull/13011
- kata-deploy: Fix containerd debug level path for config schema v4 by @fidencio in https://github.com/kata-containers/kata-containers/pull/13021
- fix: add click 8.3.3 to docs requirements by @pavithiran34 in https://github.com/kata-containers/kata-containers/pull/13037
- kata-ctl: Fix failures when kata-ctl exec with short id by @Apokleos in https://github.com/kata-containers/kata-containers/pull/12437
- Fix #13008: runtime/fc track real firecracker PID instead of jailer PID by @sebwolf-de in https://github.com/kata-containers/kata-containers/pull/13009
- agent-ctl: CLH virtio fs queue size fix by @stevenhorsman in https://github.com/kata-containers/kata-containers/pull/13073


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.31.0**, the newest release recorded here for this line.

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
