---
id: TROUBLE-FLANNEL_0_27_DEFECTS
type: troubleshooting
title: "flannel 0.27: defects fixed in the 0.27 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.27.0 <0.28.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - flannel 0.27 known issues
  - flannel 0.27 fixed in
  - is this flannel bug already fixed
tags:
  - troubleshooting
  - upgrade
  - flannel
sources:
  - type: docs
    path: flannel-io/flannel release notes for the 0.27 line — bug-fix entries
    url: https://github.com/flannel-io/flannel/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# flannel 0.27: defects fixed in the 0.27 line

## Summary

**5 defects** the project fixed across **3 releases** of the 0.27 line, from 0.27.0 to
0.27.4. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.27.0

- test: fix e2e tests in CI workflows and don't run the workflows on "push" events by @thomasferrandiz in https://github.com/flannel-io/flannel/pull/2240
- fix: clean-up rules when starting instead of shutting down by @thomasferrandiz in https://github.com/flannel-io/flannel/pull/2239

### 0.27.1

- Fix deadlock in startup for large clusters by @sudheerv in https://github.com/flannel-io/flannel/pull/2251

### 0.27.4

- Fix: recreate VXLAN device (flannel.*) when external interface is deleted and re-added by @pratikjagrut in https://github.com/flannel-io/flannel/pull/2272
- Fix interface IP address lookup in dual-stack mode by @np-13 in https://github.com/flannel-io/flannel/pull/2283


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.27.4**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `flannel-io/flannel`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/flannel.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
