---
id: TROUBLE-COREDNS_1_13_DEFECTS
type: troubleshooting
title: "coredns 1.13: defects fixed in the 1.13 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.13.0 <1.14.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - coredns 1.13 known issues
  - coredns 1.13 fixed in
  - is this coredns bug already fixed
tags:
  - troubleshooting
  - upgrade
  - coredns
sources:
  - type: docs
    path: coredns/coredns release notes for the 1.13 line — bug-fix entries
    url: https://github.com/coredns/coredns/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# coredns 1.13: defects fixed in the 1.13 line

## Summary

**7 defects** the project fixed across **2 releases** of the 1.13 line, from 1.13.0 to
1.13.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.13.0

- core: Fix Corefile infinite loop on unclosed braces (https://github.com/coredns/coredns/pull/7571)
- core: Fix Corefile related import cycle issue (https://github.com/coredns/coredns/pull/7567)
- plugin/file: Fix data race in tree Elem.Name (https://github.com/coredns/coredns/pull/7574)

### 1.13.2

- core: Fix usage of sync.Pool to save an alloc (https://github.com/coredns/coredns/pull/7701)
- core: Fix data race with sync.RWMutex for uniq (https://github.com/coredns/coredns/pull/7707)
- plugin/kubernetes: Fix kubernetes plugin logging (https://github.com/coredns/coredns/pull/7727)
- plugin/secondary: Fix reload causing secondary plugin goroutine to leak (https://github.com/coredns/coredns/pull/7694)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.13.2**, the newest release recorded here for this line.

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
