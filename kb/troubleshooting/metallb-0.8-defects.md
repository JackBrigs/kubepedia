---
id: TROUBLE-METALLB_0_8_DEFECTS
type: troubleshooting
title: "metallb 0.8: defects fixed in the 0.8 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.8.0 <0.9.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - metallb 0.8 known issues
  - metallb 0.8 fixed in
  - is this metallb bug already fixed
tags:
  - troubleshooting
  - upgrade
  - metallb
sources:
  - type: docs
    path: metallb/metallb release notes for the 0.8 line — bug-fix entries
    url: https://github.com/metallb/metallb/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# metallb 0.8: defects fixed in the 0.8 line

## Summary

**12 defects** the project fixed across **3 releases** of the 0.8 line, from 0.8.0 to
0.8.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.8.0

- Fix address allocation in cases where no addresses were available at service creation, but the deletion of another service subsequently makes one available
- Fix allocation not updating when the address pool annotation changes. ([#448](https://github.com/metallb/metallb/issues/448))
- Fix periodic crashes due to `glog` trying to write to disk despite explicit instructions to the contrary
- Fix `spec.loadBalancerIP` validation on IPv6 clusters
- Fix BGP Router ID selection on v6 BGP sessions
- Fix handling of IPv6 addresses in the BGP connection establishment logic
- Fix incorrect ARP/NDP responses on bonded interfaces
- Fix ARP/NDP responses sent on interfaces with the NOARP flag

### 0.8.1

- Fix the apiGroup for PodSecurityPolicy, for compatibility with Kubernetes 1.16. ([#458](https://github.com/metallb/metallb/issues/458))
- Fix speaker posting events with an empty string as the announcing node name. ([#456](https://github.com/metallb/metallb/issues/456))
- Fix RBAC permissions on speaker, to allow it to post events to all namespaces. ([#455](https://github.com/metallb/metallb/issues/455))

### 0.8.2

- Fix layer2 node selection when healthy and unhealthy replicas are colocated on a single node


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.8.2**, the newest release recorded here for this line.

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
