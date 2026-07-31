---
id: TROUBLE-CILIUM_1_4_DEFECTS
type: troubleshooting
title: "cilium 1.4: defects fixed in the 1.4 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.4.0 <1.5.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cilium 1.4 known issues
  - cilium 1.4 fixed in
  - is this cilium bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cilium
sources:
  - type: docs
    path: cilium/cilium release notes for the 1.4 line — bug-fix entries
    url: https://github.com/cilium/cilium/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cilium 1.4: defects fixed in the 1.4 line

## Summary

**9 defects** the project fixed across **5 releases** of the 1.4 line, from 1.4.0 to
1.4.28. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.4.0

- ARM's RP registration policy will no longer swallow unrecognized errors
- Fixed an issue in `runtime.NewPollerFromResumeToken()` when resuming a `Poller` with a custom `PollingHandler`
- Fixed wrong policy copy in `arm/runtime.NewPipeline()`
- `ManagedIdentityCredential` will now retry when IMDS responds 410 or 503

### 1.4.1

- Fixed #64: Fix pre-release precedence issue (thanks @uudashr)
- **Documentation**: Fixes the AssumeRoleProvider's documentation for using custom TokenProviders

### 1.4.2

- #70: Fix the handling of pre-releases and the 0.0.0 release edge case

### 1.4.19

- **Bug Fix**: Modernize non codegen files with go fix

### 1.4.28

- **Dependency Update**: Update to smithy-go v1.27.1 to fix several union-related deserialization bugs in schema-serde-enabled services


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.4.28**, the newest release recorded here for this line.

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
