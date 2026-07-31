---
id: TROUBLE-COREDNS_1_12_DEFECTS
type: troubleshooting
title: "coredns 1.12: defects fixed in the 1.12 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.12.0 <1.13.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - coredns 1.12 known issues
  - coredns 1.12 fixed in
  - is this coredns bug already fixed
tags:
  - troubleshooting
  - upgrade
  - coredns
sources:
  - type: docs
    path: coredns/coredns release notes for the 1.12 line — bug-fix entries
    url: https://github.com/coredns/coredns/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# coredns 1.12: defects fixed in the 1.12 line

## Summary

**7 defects** the project fixed across **3 releases** of the 1.12 line, from 1.12.1 to
1.12.4. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.12.1

- plugin/kubernetes: Fix handling of pods having DeletionTimestamp set (https://github.com/coredns/coredns/pull/7119) (#7131)

### 1.12.3

- plugin/cache: Fix data race when refreshing cached messages (https://github.com/coredns/coredns/pull/7398)
- plugin/cache: Fix data race when updating the TTL of cached messages (https://github.com/coredns/coredns/pull/7397)
- plugin/test: Fix TXT record comparison logic for multi-string vs multi-record scenarios (https://github.com/coredns/coredns/pull/7413)

### 1.12.4

- plugin/file: Fix label offset problem in ClosestEncloser (https://github.com/coredns/coredns/pull/7465)
- plugin/grpc: Fix span leak and deadline on error attempt (https://github.com/coredns/coredns/pull/7487)
- plugin/transfer: Fix goroutine leak on axfr err (https://github.com/coredns/coredns/pull/7516)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.12.4**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `coredns/coredns`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/coredns.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
