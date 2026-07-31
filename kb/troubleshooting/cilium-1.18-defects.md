---
id: TROUBLE-CILIUM_1_18_DEFECTS
type: troubleshooting
title: "cilium 1.18: defects fixed in the 1.18 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.18.0 <1.19.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cilium 1.18 known issues
  - cilium 1.18 fixed in
  - is this cilium bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cilium
sources:
  - type: docs
    path: cilium/cilium release notes for the 1.18 line — bug-fix entries
    url: https://github.com/cilium/cilium/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cilium 1.18: defects fixed in the 1.18 line

## Summary

**11 defects** the project fixed across **10 releases** of the 1.18 line, from 1.18.0 to
1.18.45. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.18.0

- **Announcement**: When using the SSOTokenProvider, a previous implementation incorrectly compensated for invalid SSOTokenProvider configurations in the shared profile. This has been fixed via PR #1903 and tracked in issue #1846

### 1.18.1

- Fixed incorrect request/response logging try info when logging a request that's being retried

### 1.18.2

- Fixed a case in which `BearerTokenPolicy` didn't ensure an authentication error is non-retriable

### 1.18.5

- **Bug Fix**: Unify logic between shared config and in finding home directory

### 1.18.18

- **Bug Fix**: Allow RoleARN to be set as functional option on STS WebIdentityRoleOptions. Fixes aws/aws-sdk-go-v2#2015

### 1.18.19

- **Bug Fix**: Modernize non codegen files with go fix

### 1.18.20

- **Bug Fix**: Replace usages of the old ioutil/ package throughout the SDK

### 1.18.28

- **Dependency Update**: Update to smithy-go v1.27.1 to fix several union-related deserialization bugs in schema-serde-enabled services

### 1.18.42

- **Bug Fix**: Fixed a bug where merging `max_attempts` or `duration_seconds` fields across shared config files with invalid values would silently default them to 0
- **Bug Fix**: Move type assertion of config values out of the parsing stage, which resolves an issue where the contents of a profile would silently be dropped with certain numeric formats

### 1.18.45

- **Bug Fix**: Fail to load config if an explicitly provided profile doesn't exist


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.18.45**, the newest release recorded here for this line.

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
