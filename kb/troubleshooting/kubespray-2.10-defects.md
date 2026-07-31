---
id: TROUBLE-KUBESPRAY_2_10_DEFECTS
type: troubleshooting
title: "kubespray 2.10: defects fixed in the 2.10 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.10.0 <2.11.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kubespray 2.10 known issues
  - kubespray 2.10 fixed in
  - is this kubespray bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kubespray
sources:
  - type: docs
    path: kubernetes-sigs/kubespray release notes for the 2.10 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/kubespray/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kubespray 2.10: defects fixed in the 2.10 line

## Summary

**5 defects** the project fixed across **2 releases** of the 2.10 line, from 2.10.0 to
2.10.4. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.10.0

- Non-master nodes can no longer set reserved labels (see kubernetes/kubernetes/#68267)
- Kube-router inter-node communication does not work
- Calico KDD does currently not work (see #4727)

### 2.10.4

- Fix double tolerations in `dns-autoscaler.yml` bug
- fix start CoreDNS when init secondary master (#4867)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.10.4**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `kubernetes-sigs/kubespray`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/kubespray.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
