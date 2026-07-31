---
id: TROUBLE-KUBE_OVN_1_9_DEFECTS
type: troubleshooting
title: "kube-ovn 1.9: defects fixed in the 1.9 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.9.0 <1.10.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kube-ovn 1.9 known issues
  - kube-ovn 1.9 fixed in
  - is this kube-ovn bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kube-ovn
sources:
  - type: docs
    path: kubeovn/kube-ovn release notes for the 1.9 line — bug-fix entries
    url: https://github.com/kubeovn/kube-ovn/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kube-ovn 1.9: defects fixed in the 1.9 line

## Summary

**28 defects** the project fixed across **4 releases** of the 1.9 line, from 1.9.0 to
1.9.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.9.0

- fix nat-outgoing/policy-routing on pod startup
- re-check ns annotation to avoid annotations lost
- append externalIds for pod and node when upgrade
- init node with wrong ipamkey and lead conflict
- In netpol egress rules, except rule should be set to "!=" and should not be "=="
- fix trace command in dual stack underlay networking
- fix pinger and monitor in underlay networking
- change inspection logic from manually adding lsp to just reading pod queue
- fix: ensure all kube-ovn components deleted before annotate pods
- fix: check allocated annotation in update handler
- fix read-only pointer in vlan and provider-network
- fix: no need to set address for ls to lr port
- when update subnet's except ip,we should filter repeat ip
- when netpol is added to a workload, the workload's POD can be accessed using service
- fix: do not reuse released ip after subnet updated
- use different ip crd with provider suffix for pod multus nic
- move chassis judge to the end of node processing
- append check for centralized subnet nat process
- modify pod's process of update for use multus cni as default cni

### 1.9.1

- continue of deletion for del pod failed when can't found vpc or subnet
- replace ecmp dp_hash with hash by src_ip (#1289)
- skip ping gateway for pods during live migration

### 1.9.2

- ignore all link local unicast addresses/routes
- fix: do not recreate port for terminating pods
- fix: The underlay physical gateway config by external-gw-addr when use snat&eip
- add missing link scope routes in vpc-nat-gateway

### 1.9.3

- delete ipam record and static route when gc lsp
- fix: ovs trace flow always ends with controller action


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.9.3**, the newest release recorded here for this line.

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
