---
id: TROUBLE-COREDNS_1_11_DEFECTS
type: troubleshooting
title: "coredns 1.11: defects fixed in the 1.11 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.11.0 <1.12.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - coredns 1.11 known issues
  - coredns 1.11 fixed in
  - is this coredns bug already fixed
tags:
  - troubleshooting
  - upgrade
  - coredns
sources:
  - type: docs
    path: coredns/coredns release notes for the 1.11 line — bug-fix entries
    url: https://github.com/coredns/coredns/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# coredns 1.11: defects fixed in the 1.11 line

## Summary

**12 defects** the project fixed across **4 releases** of the 1.11 line, from 1.11.0 to
1.11.4. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.11.0

- Plus many bug fixes, and some security improvements
- plugin/clouddns: fix answers limited to one response (https://github.com/coredns/coredns/pull/5986)
- plugin/forward: fix forward metrics for backwards compatibility (https://github.com/coredns/coredns/pull/6178)
- plugin/kubernetes: fix headless/endpoint query panics when endpoints are disabled (https://github.com/coredns/coredns/pull/6137)
- plugin/kubernetes: fix ports panic (https://github.com/coredns/coredns/pull/6179)
- prevent fail counter of a proxy overflows (https://github.com/coredns/coredns/pull/5990)
- prevent panics when using DoHWriter (https://github.com/coredns/coredns/pull/6120)

### 1.11.1

- plugin/cache: fix keepttl parsing (https://github.com/coredns/coredns/pull/6250)

### 1.11.3

- plugin/rewrite: fix multi request concurrency issue in cname rewrite (https://github.com/coredns/coredns/pull/6407)
- plugin/cache: fix keepttl parsing (https://github.com/coredns/coredns/pull/6250)

### 1.11.4

- plugin/etcd: fix etcd connection leakage during reload (https://github.com/coredns/coredns/pull/6646)
- plugin/file: Fix zone parser error handling (https://github.com/coredns/coredns/pull/6680)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.11.4**, the newest release recorded here for this line.

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
