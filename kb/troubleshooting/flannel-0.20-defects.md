---
id: TROUBLE-FLANNEL_0_20_DEFECTS
type: troubleshooting
title: "flannel 0.20: defects fixed in the 0.20 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.20.0 <0.21.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - flannel 0.20 known issues
  - flannel 0.20 fixed in
  - is this flannel bug already fixed
tags:
  - troubleshooting
  - upgrade
  - flannel
sources:
  - type: docs
    path: flannel-io/flannel release notes for the 0.20 line — bug-fix entries
    url: https://github.com/flannel-io/flannel/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# flannel 0.20: defects fixed in the 0.20 line

## Summary

**7 defects** the project fixed across **3 releases** of the 0.20 line, from 0.20.0 to
0.20.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.20.0

- Correct workflow trivy.yml and upgrade vulnerable dependencies by @thomasferrandiz in https://github.com/flannel-io/flannel/pull/1643
- Fixes backend configuration documentation by @masstamike in https://github.com/flannel-io/flannel/pull/1645

### 0.20.1

- docs: fix troubleshooting by @satoru-takeuchi in https://github.com/flannel-io/flannel/pull/1664

### 0.20.2

- Fixed IPv4 podCIDR check in case spec.PodCIDR is IPv6 by @rbrtbnfgl in https://github.com/flannel-io/flannel/pull/1672
- fix flannel clusterrole by @xh4n3 in https://github.com/flannel-io/flannel/pull/1677
- Fixed masquerade rule to avoid double NAT bug by @rbrtbnfgl in https://github.com/flannel-io/flannel/pull/1681
- pkg/ip/iface_windows_test.go: fix TestGetInterfaceByIP by @UweErikMartin in https://github.com/flannel-io/flannel/pull/1680


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.20.2**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `flannel-io/flannel`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/flannel.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
