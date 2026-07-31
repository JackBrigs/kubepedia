---
id: TROUBLE-CILIUM_1_9_DEFECTS
type: troubleshooting
title: "cilium 1.9: defects fixed in the 1.9 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.9.0 <1.10.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cilium 1.9 known issues
  - cilium 1.9 fixed in
  - is this cilium bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cilium
sources:
  - type: docs
    path: cilium/cilium release notes for the 1.9 line — bug-fix entries
    url: https://github.com/cilium/cilium/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cilium 1.9: defects fixed in the 1.9 line

## Summary

**11 defects** the project fixed across **3 releases** of the 1.9 line, from 1.9.0 to
1.9.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.9.0

- Fixed an issue that could cause some allowed HTTP header values to not show up in logs
- Include error text instead of error type in traces when the transport returns an error
- Fixed an issue that could cause an HTTP/2 request to hang when the TCP connection becomes unresponsive
- Block key and SAS authentication for non TLS protected endpoints
- Passing a `nil` credential value will no longer cause a panic. Instead, the authentication is skipped
- Calling `Error` on a zero-value `azcore.ResponseError` will no longer panic
- Fixed an issue in `fake.PagerResponder[T]` that would cause a trailing error to be omitted when iterating over pages
- Context values created by `azcore` will no longer flow across disjoint HTTP requests
- **Feature**: Adds support for `SourceIdentity` to `stscreds.AssumeRoleProvider` [#1588](https://github.com/aws/aws-sdk-go-v2/pull/1588). Fixes [#1575](https://github.com/aws/aws-sdk-go-v2/issues/1575)

### 1.9.1

- The `retry-after-ms` and `x-ms-retry-after-ms` headers weren't being checked during retries

### 1.9.2

- `runtime.MarshalAsByteArray` and `runtime.MarshalAsJSON` will preserve the preexisting value of the `Content-Type` header


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.9.2**, the newest release recorded here for this line.

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
