---
id: TROUBLE-CILIUM_1_13_DEFECTS
type: troubleshooting
title: "cilium 1.13: defects fixed in the 1.13 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.13.0 <1.14.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cilium 1.13 known issues
  - cilium 1.13 fixed in
  - is this cilium bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cilium
sources:
  - type: docs
    path: cilium/cilium release notes for the 1.13 line — bug-fix entries
    url: https://github.com/cilium/cilium/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cilium 1.13: defects fixed in the 1.13 line

## Summary

**6 defects** the project fixed across **3 releases** of the 1.13 line, from 1.13.0 to
1.13.5. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.13.0

- **Announcement**: When using the SSOTokenProvider, a previous implementation incorrectly compensated for invalid SSOTokenProvider configurations in the shared profile. This has been fixed via PR #1903 and tracked in issue #1846

### 1.13.1

- `AzureCLICredential` quoted arguments incorrectly on Windows
- **Bug Fix**: Fixes LoadDefaultConfig handling of errors returned by passed in functional options. Previously errors returned from the LoadOptions passed into LoadDefaultConfig were incorrectly ignored. [#1562](https://github.com/aws/aws-sdk-go-v2/pull/1562). Thanks to [Pinglei Guo](https://github.com/pingleig) for submitting this PR
- **Bug Fix**: Fixes the SDK's handling of `duration_sections` in the shared credentials file or specified in multiple shared config and shared credentials files under the same profile. [#1568](https://github.com/aws/aws-sdk-go-v2/pull/1568). Thanks to [Amir Szekely](https://github.com/kichik) for help reproduce this bug
- **Bug Fix**: Updates `config` module to use os.UserHomeDir instead of hard coded environment variable for OS. [#1563](https://github.com/aws/aws-sdk-go-v2/pull/1563)

### 1.13.5

- **Bug Fix**: Unify logic between shared config and in finding home directory


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.13.5**, the newest release recorded here for this line.

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
