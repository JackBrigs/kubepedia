---
id: TROUBLE-SCHEDULER_PLUGINS_0_31_DEFECTS
type: troubleshooting
title: "scheduler-plugins 0.31: defects fixed in the 0.31 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.31.0 <0.32.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - scheduler-plugins 0.31 known issues
  - scheduler-plugins 0.31 fixed in
  - is this scheduler-plugins bug already fixed
tags:
  - troubleshooting
  - upgrade
  - scheduler-plugins
sources:
  - type: docs
    path: kubernetes-sigs/scheduler-plugins release notes for the 0.31 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/scheduler-plugins/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# scheduler-plugins 0.31: defects fixed in the 0.31 line

## Summary

**5 defects** the project fixed across **1 releases** of the 0.31 line, from 0.31.8 to
0.31.8. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.31.8

- bug(preemption): fix SelectVictimsOnNode method consistent with default scheduler by @googs1025 in https://github.com/kubernetes-sigs/scheduler-plugins/pull/838
- fix(util): fix the problem of pod overhead not being calculated by @googs1025 in https://github.com/kubernetes-sigs/scheduler-plugins/pull/840
- fix(QOSSort): refine queue sorting logic by adding inqueue timestamp by @googs1025 in https://github.com/kubernetes-sigs/scheduler-plugins/pull/855
- flake: fix qos sort plugin flaky integration test by @googs1025 in https://github.com/kubernetes-sigs/scheduler-plugins/pull/861
- clientutil: fix a typo by @Huang-Wei in https://github.com/kubernetes-sigs/scheduler-plugins/pull/899


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.31.8**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `kubernetes-sigs/scheduler-plugins`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/scheduler-plugins.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
