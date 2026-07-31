---
id: TROUBLE-CNI_PLUGINS_1_2_DEFECTS
type: troubleshooting
title: "cni-plugins 1.2: defects fixed in the 1.2 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.2.0 <1.3.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cni-plugins 1.2 known issues
  - cni-plugins 1.2 fixed in
  - is this cni-plugins bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cni-plugins
sources:
  - type: docs
    path: containernetworking/plugins release notes for the 1.2 line — bug-fix entries
    url: https://github.com/containernetworking/plugins/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cni-plugins 1.2: defects fixed in the 1.2 line

## Summary

**5 defects** the project fixed across **1 releases** of the 1.2 line, from 1.2.0 to
1.2.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.2.0

- ([#809](https://github.com/containernetworking/plugins/pull/809)). bridge: refresh host-veth mac after port add
- ([#802](https://github.com/containernetworking/plugins/pull/802)). Add IPv6 support for AddDefaultRoute
- ([#779](https://github.com/containernetworking/plugins/pull/779)). Fix path substitution to enable setting sysctls on vlan interfaces
- ([#782](https://github.com/containernetworking/plugins/pull/782)). host-local: fix bug on getting NextIP of addresses with first byte
- ([#709](https://github.com/containernetworking/plugins/pull/709)). dhcp: Fix client id in renew/release


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.2.0**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `containernetworking/plugins`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/cni-plugins.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
