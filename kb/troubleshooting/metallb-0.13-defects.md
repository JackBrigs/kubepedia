---
id: TROUBLE-METALLB_0_13_DEFECTS
type: troubleshooting
title: "metallb 0.13: defects fixed in the 0.13 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.13.0 <0.14.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - metallb 0.13 known issues
  - metallb 0.13 fixed in
  - is this metallb bug already fixed
tags:
  - troubleshooting
  - upgrade
  - metallb
sources:
  - type: docs
    path: metallb/metallb release notes for the 0.13 line — bug-fix entries
    url: https://github.com/metallb/metallb/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# metallb 0.13: defects fixed in the 0.13 line

## Summary

**6 defects** the project fixed across **4 releases** of the 0.13 line, from 0.13.2 to
0.13.11. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.13.2

- Logging: Avoid printing microseconds, fix the calling site for each log ([PR #1351](https://github.com/metallb/metallb/pull/1351))
- IPV6 / FRR: fix single hop ebgp next hop tracking ([PR #1367](https://github.com/metallb/metallb/pull/1367))
- A race condition happening when the speaker container was slower than the frr one was fixed ([PR 1463](https://github.com/metallb/metallb/pull/1463))

### 0.13.3

- Fix images on ARM broken in 0.13.2 ([PR 1478](https://github.com/metallb/metallb/pull/1478))

### 0.13.7

- Fix service monitor relabelings in Helm charts ([PR 1650](https://github.com/metallb/metallb/pull/1650))

### 0.13.11

- Fix kustomize v5 deprecations ([PR 1986](https://github.com/metallb/metallb/pull/1986), [Issue 1985](https://github.com/metallb/metallb/issues/1985))


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.13.11**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `metallb/metallb`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/metallb.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
