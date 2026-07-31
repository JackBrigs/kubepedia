---
id: TROUBLE-METALLB_0_9_DEFECTS
type: troubleshooting
title: "metallb 0.9: defects fixed in the 0.9 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.9.0 <0.10.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - metallb 0.9 known issues
  - metallb 0.9 fixed in
  - is this metallb bug already fixed
tags:
  - troubleshooting
  - upgrade
  - metallb
sources:
  - type: docs
    path: metallb/metallb release notes for the 0.9 line — bug-fix entries
    url: https://github.com/metallb/metallb/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# metallb 0.9: defects fixed in the 0.9 line

## Summary

**6 defects** the project fixed across **4 releases** of the 0.9 line, from 0.9.2 to
0.9.6. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.9.2

- Fix layer2 not sending ARP messages when IP changes ([#520](https://github.com/metallb/metallb/pull/520)). Fixes [#471](https://github.com/metallb/metallb/issues/471)
- Fix to properly expose `address_total` Prometheus metric ([#518](https://github.com/metallb/metallb/pull/518))

### 0.9.3

- Fix manifests to use container image version `v0.9.3` instead of `main`. Users of `v0.9.2` are encouraged to upgrade, as [manifests included in that release](https://raw.githubusercontent.com/metallb/metallb/v0.9.2/manifests/metallb.yaml) use an incorrect container image version. Those two images happen to match now but, as development continues on `main` branch, they will differ

### 0.9.4

- Fix wrong behavior of the addresses_in_use_total metric under certain conditions ([#627](https://github.com/metallb/metallb/pull/627))
- Layer 2: Fix Memberlist convergence following a network partition ([#662](https://github.com/metallb/metallb/pull/662))

### 0.9.6

- Fix nodeAssigned event on k8s >= 1.20 ([#812](https://github.com/metallb/metallb/pull/812))


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.9.6**, the newest release recorded here for this line.

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
