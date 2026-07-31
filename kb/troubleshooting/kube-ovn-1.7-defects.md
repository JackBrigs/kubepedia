---
id: TROUBLE-KUBE_OVN_1_7_DEFECTS
type: troubleshooting
title: "kube-ovn 1.7: defects fixed in the 1.7 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.7.0 <1.8.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kube-ovn 1.7 known issues
  - kube-ovn 1.7 fixed in
  - is this kube-ovn bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kube-ovn
sources:
  - type: docs
    path: kubeovn/kube-ovn release notes for the 1.7 line — bug-fix entries
    url: https://github.com/kubeovn/kube-ovn/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kube-ovn 1.7: defects fixed in the 1.7 line

## Summary

**20 defects** the project fixed across **4 releases** of the 1.7 line, from 1.7.0 to
1.7.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.7.0

- Restart ovn-controller to force ovn-ic flows update
- Update usingips check when update finalizer for subnet
- Livenessprobe fail if ovn nb/ovn sb not running
- Pod terminating not recycle ip when controller not ready

### 1.7.1

- Fix lsp may lost when server pressure is high
- Delete process of ip crd delete in cni delete request
- Ignore update pod nic annotation when not nil
- Clean up gateway chassis list for external gw
- Do not delete statefulset pod when update pod
- Add master check when a node adding to a cluster and config sb/nb address
- Add node internal ip into ovn-ic advertise blacklist
- Add field defaultNetworkType in configmap ovn-config
- Enable tx offload again as upstream already fix it

### 1.7.2

- fix ipsets, subnets using underlay networking should not be included in ipsets
- if the string of ip is empty,program will die
- avoid Pod IP to be the same with node internal IP

### 1.7.3

- fix nat-outgoing/policy-routing on pod startup
- re-check ns annotation to avoid annotations lost
- append externalIds for pod and node when upgrade
- init node with wrong ipamkey and lead conflict


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.7.3**, the newest release recorded here for this line.

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
