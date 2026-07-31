---
id: TROUBLE-KUBE_OVN_1_6_DEFECTS
type: troubleshooting
title: "kube-ovn 1.6: defects fixed in the 1.6 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.6.0 <1.7.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kube-ovn 1.6 known issues
  - kube-ovn 1.6 fixed in
  - is this kube-ovn bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kube-ovn
sources:
  - type: docs
    path: kubeovn/kube-ovn release notes for the 1.6 line — bug-fix entries
    url: https://github.com/kubeovn/kube-ovn/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kube-ovn 1.6: defects fixed in the 1.6 line

## Summary

**16 defects** the project fixed across **4 releases** of the 1.6 line, from 1.6.0 to
1.6.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.6.0

- Remove not alive pod in networkpolicy portGroup
- Delete Pod when marked with deletionTimestamp
- Use the internal IP when node try to connect to pod
- Do not advertise node switch cidr when enable ovn-ic
- Check if ovn-central ip exists in `NODE_IPS` before start
- Fix the problem of confusion between old and new versions of crd
- Masquerade other nodes to local pod to avoid NodePort triangle traffic

### 1.6.1

- When address is empty, skip route/nat deletion
- Pod terminating not recycle ip when controller not ready
- Set default db addr same with leader node to fix nb and sb error 'bind: Address already in use'

### 1.6.2

- restart ovn-controller to force ovn-ic flows update
- update usingips check when update finalizer for subnet
- livenessprobe fail if ovn nb/ovn sb not running

### 1.6.3

- fix: release ip addresses even if pods not found
- fix: get_leader_ip always return fist node ip
- fix: leader may change during startup, use cluster connection to set options


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.6.3**, the newest release recorded here for this line.

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
