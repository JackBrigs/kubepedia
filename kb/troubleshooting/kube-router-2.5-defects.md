---
id: TROUBLE-KUBE_ROUTER_2_5_DEFECTS
type: troubleshooting
title: "kube-router 2.5: defects fixed in the 2.5 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.5.0 <2.6.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kube-router 2.5 known issues
  - kube-router 2.5 fixed in
  - is this kube-router bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kube-router
sources:
  - type: docs
    path: cloudnativelabs/kube-router release notes for the 2.5 line — bug-fix entries
    url: https://github.com/cloudnativelabs/kube-router/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kube-router 2.5: defects fixed in the 2.5 line

## Summary

**6 defects** the project fixed across **1 releases** of the 2.5 line, from 2.5.0 to
2.5.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.5.0

- d8430e21 - fix(lint): remove nolint for error messages `<Aaron U'Ren>`
- 760fcd5c - fix(lint): remove non-constant format string (govet) `<Aaron U'Ren>`
- 48b631c4 - fix(lint): remove unnecessary variable initializations (copyloopvar) `<Aaron U'Ren>`
- 858fdf65 - fix(lint): prevent against integer overflow errors `<Aaron U'Ren>`
- aa7cffb6 - fix(NSC): only set rp_filter to 2 if it is 1 `<Dmitry Sharshakov>`
- 6ce2c6db - fix(NRC): find all node IPs for NAT exclusion `<Aaron U'Ren>`


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.5.0**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `cloudnativelabs/kube-router`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/kube-router.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
