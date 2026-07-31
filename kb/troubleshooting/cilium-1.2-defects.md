---
id: TROUBLE-CILIUM_1_2_DEFECTS
type: troubleshooting
title: "cilium 1.2: defects fixed in the 1.2 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.2.0 <1.3.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cilium 1.2 known issues
  - cilium 1.2 fixed in
  - is this cilium bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cilium
sources:
  - type: docs
    path: cilium/cilium release notes for the 1.2 line — bug-fix entries
    url: https://github.com/cilium/cilium/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cilium 1.2: defects fixed in the 1.2 line

## Summary

**9 defects** the project fixed across **2 releases** of the 1.2 line, from 1.2.0 to
1.2.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.2.0

- Fixed an issue in `runtime.SetMultipartFormData` to properly handle slices of `io.ReadSeekCloser`
- Failure to poll the state of an LRO will now return an `*azcore.ResponseError` for poller types that require this behavior
- Fixed a bug in `runtime.NewPipeline` that would cause pipeline-specified allowed headers and query parameters to be lost
- This version includes all fixes and features from 1.2.0-beta.*

### 1.2.3

- #46: Fixed 0.x.x and 0.0.x in constraints being treated as *
- #34: Fixed issue where hyphen range was not working with pre-release parsing
- #24: Fixed edge case issue where constraint "> 0" does not handle "0.0.1-alpha" properly
- Issue #21: Per the SemVer spec (section 9) a pre-release is unstable and might not satisfy the intended compatibility. The change here ignores pre-releases on constraint checks (e.g., ~ or ^) when a pre-release is not part of the constraint. For example, `^1.2.3` will ignore pre-releases while `^1.2.3-alpha` will include them
- Fixed #1: * constraint failing on valid versions


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.2.3**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `cilium/cilium`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/cilium.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
