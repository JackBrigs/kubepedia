---
id: TROUBLE-KUBE_OVN_0_4_DEFECTS
type: troubleshooting
title: "kube-ovn 0.4: defects fixed in the 0.4 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.4.0 <0.5.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kube-ovn 0.4 known issues
  - kube-ovn 0.4 fixed in
  - is this kube-ovn bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kube-ovn
sources:
  - type: docs
    path: kubeovn/kube-ovn release notes for the 0.4 line — bug-fix entries
    url: https://github.com/kubeovn/kube-ovn/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kube-ovn 0.4: defects fixed in the 0.4 line

## Summary

**6 defects** the project fixed across **2 releases** of the 0.4 line, from 0.4.0 to
0.4.1. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.4.0

- Reuse node annotations when kube-ovn-controller restart

### 0.4.1

- manual static ip allocation and automatic allocation should use different ip validation
- json: cannot unmarshal string into Go value of type request.PodResponse
- use ovsdb-client to get leader info to avoid log rotation
- use default-gw as default-exclude-ips and expose args to docs
- to cleanup all created resources, not only kube-ovn namespace


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.4.1**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `kubeovn/kube-ovn`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/kube-ovn.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
