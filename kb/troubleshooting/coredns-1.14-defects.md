---
id: TROUBLE-COREDNS_1_14_DEFECTS
type: troubleshooting
title: "coredns 1.14: defects fixed in the 1.14 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.14.0 <1.15.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - coredns 1.14 known issues
  - coredns 1.14 fixed in
  - is this coredns bug already fixed
tags:
  - troubleshooting
  - upgrade
  - coredns
sources:
  - type: docs
    path: coredns/coredns release notes for the 1.14 line — bug-fix entries
    url: https://github.com/coredns/coredns/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# coredns 1.14: defects fixed in the 1.14 line

## Summary

**10 defects** the project fixed across **3 releases** of the 1.14 line, from 1.14.0 to
1.14.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.14.0

- core: Fix gosec G115 integer overflow warnings (https://github.com/coredns/coredns/pull/7799)
- plugin/azure: Fix slice init length (https://github.com/coredns/coredns/pull/6901)
- plugin/file: Fix for misleading SOA parser warnings (https://github.com/coredns/coredns/pull/7774)

### 1.14.2

- plugin/forward: Fix parsing error when handling TLS+IPv6 address (https://github.com/coredns/coredns/pull/7848)
- plugin/kubernetes: Fix panic on empty ListenHosts (https://github.com/coredns/coredns/pull/7857)
- plugin/rewrite: Fix cname target rewrite for CNAME chains (https://github.com/coredns/coredns/pull/7853)

### 1.14.3

- plugin/file: Fix data race in xfr.go (https://github.com/coredns/coredns/pull/8039)
- plugin/ready: fix Reset list of readiness plugins (https://github.com/coredns/coredns/pull/8035)
- plugin/transfer: Fix case-sensitive zone handling for AXFR/IXFR (https://github.com/coredns/coredns/pull/7899)
- plugin/transfter: Fix longestMatch to select the most specific zone correctly (https://github.com/coredns/coredns/pull/7949)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.14.3**, the newest release recorded here for this line.

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
