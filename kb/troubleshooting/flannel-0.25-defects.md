---
id: TROUBLE-FLANNEL_0_25_DEFECTS
type: troubleshooting
title: "flannel 0.25: defects fixed in the 0.25 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.25.0 <0.26.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - flannel 0.25 known issues
  - flannel 0.25 fixed in
  - is this flannel bug already fixed
tags:
  - troubleshooting
  - upgrade
  - flannel
sources:
  - type: docs
    path: flannel-io/flannel release notes for the 0.25 line — bug-fix entries
    url: https://github.com/flannel-io/flannel/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# flannel 0.25: defects fixed in the 0.25 line

## Summary

**9 defects** the project fixed across **8 releases** of the 0.25 line, from 0.25.0 to
0.25.7. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.25.0

- chore: fix typo by @pavedroad in https://github.com/flannel-io/flannel/pull/1903

### 0.25.1

- chore: fix typo in comment by @looklose in https://github.com/flannel-io/flannel/pull/1934

### 0.25.2

- Bug fixes by @thomasferrandiz in https://github.com/flannel-io/flannel/pull/1947
- Fixed IPv6 0 initialization by @rbrtbnfgl in https://github.com/flannel-io/flannel/pull/1969

### 0.25.3

- Bump knftables 0.0.16 and fix e2e test by @thomasferrandiz in https://github.com/flannel-io/flannel/pull/1986

### 0.25.4

- Fix bug in the logic polling the interface by @manuelbuil in https://github.com/flannel-io/flannel/pull/1996

### 0.25.5

- Fix bug in hostgw-windows by @manuelbuil in https://github.com/flannel-io/flannel/pull/1998

### 0.25.6

- Fixed values file on flannel chart by @rbrtbnfgl in https://github.com/flannel-io/flannel/pull/2036

### 0.25.7

- Fixed IPv6 chosen in case of public-ipv6 configured by @rbrtbnfgl in https://github.com/flannel-io/flannel/pull/2072


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.25.7**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `flannel-io/flannel`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/flannel.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
