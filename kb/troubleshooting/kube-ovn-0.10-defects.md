---
id: TROUBLE-KUBE_OVN_0_10_DEFECTS
type: troubleshooting
title: "kube-ovn 0.10: defects fixed in the 0.10 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.10.0 <0.11.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kube-ovn 0.10 known issues
  - kube-ovn 0.10 fixed in
  - is this kube-ovn bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kube-ovn
sources:
  - type: docs
    path: kubeovn/kube-ovn release notes for the 0.10 line — bug-fix entries
    url: https://github.com/kubeovn/kube-ovn/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kube-ovn 0.10: defects fixed in the 0.10 line

## Summary

**13 defects** the project fixed across **3 releases** of the 0.10 line, from 0.10.0 to
0.10.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.10.0

- When all ip in subnet is used create lsp will panic with index out of range err
- Mount /var/run/netns into kube-ovn-cniserver for kind
- Use ep.subset.port.name to infer target port number
- When delete node recycle related ip/route resource
- Block subnet deletion when there is any ip in use
- GC logical_switch_port form listing pods and nodes
- PodSelector in networkpolicy should only consider pods in the same ns

### 0.10.1

- If cidr block not ends with zero, reformat it to avoid add route failure
- Resync iptables to prevent rules deleted by other software
- Set ovn-openflow-probe-interval to prevent ovn-controller consumes all cpu
- Do not return not found error when first add node

### 0.10.2

- requeue subnet add event when conflict with exist subnet
- periodically recompute ovn-controller to avoid inconsistency


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.10.2**, the newest release recorded here for this line.

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
