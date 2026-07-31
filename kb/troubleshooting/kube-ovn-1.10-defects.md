---
id: TROUBLE-KUBE_OVN_1_10_DEFECTS
type: troubleshooting
title: "kube-ovn 1.10: defects fixed in the 1.10 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.10.0 <1.11.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kube-ovn 1.10 known issues
  - kube-ovn 1.10 fixed in
  - is this kube-ovn bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kube-ovn
sources:
  - type: docs
    path: kubeovn/kube-ovn release notes for the 1.10 line — bug-fix entries
    url: https://github.com/kubeovn/kube-ovn/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kube-ovn 1.10: defects fixed in the 1.10 line

## Summary

**10 defects** the project fixed across **1 releases** of the 1.10 line, from 1.10.0 to
1.10.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.10.0

- keep vm's and statefulset's ips when user specified subnet
- ovs trace flow always ends with controller action
- fix: workqueue_depth should show count not rate
- fix routes for packets from Pods to other nodes
- ignore all link local unicast addresses/routes
- fix: do not recreate port for terminating pods
- fix: The underlay physical gateway config by external-gw-addr when use snat&eip
- add missing link scope routes in vpc-nat-gateway
- skip ping gateway for pods during live migration
- don't check conflict for migration pod with only static mac


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.10.0**, the newest release recorded here for this line.

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
