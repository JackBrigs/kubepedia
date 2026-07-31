---
id: TROUBLE-HELM_2_0_DEFECTS
type: troubleshooting
title: "helm 2.0: defects fixed in the 2.0 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.0.0 <2.1.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 2.0 known issues
  - helm 2.0 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 2.0 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 2.0: defects fixed in the 2.0 line

## Summary

**5 defects** the project fixed across **2 releases** of the 2.0 line, from 2.0.1 to
2.0.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.0.1

- An important bug in `helm delete` has been fixed. For this reason, we recommend updating
- The parser for `--set` has been fixed, and now handles backslash escaping of characters like `.` and `=`
- A 2.0.2 release is planned, and this release will contain only bug fixes

### 2.0.2

- A substantial bug with `helm upgrade -f` has been fixed
- An updated Sprig library (2.7.0) has been included because it contains a substantial bug fix for `quote`


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.0.2**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `helm/helm`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/helm.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
