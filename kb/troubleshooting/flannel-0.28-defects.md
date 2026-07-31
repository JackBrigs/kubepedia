---
id: TROUBLE-FLANNEL_0_28_DEFECTS
type: troubleshooting
title: "flannel 0.28: defects fixed in the 0.28 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.28.0 <0.29.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - flannel 0.28 known issues
  - flannel 0.28 fixed in
  - is this flannel bug already fixed
tags:
  - troubleshooting
  - upgrade
  - flannel
sources:
  - type: docs
    path: flannel-io/flannel release notes for the 0.28 line — bug-fix entries
    url: https://github.com/flannel-io/flannel/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# flannel 0.28: defects fixed in the 0.28 line

## Summary

**15 defects** the project fixed across **8 releases** of the 0.28 line, from 0.28.0 to
0.28.7. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.28.0

- Added TAG to fix bin version by @rbrtbnfgl in https://github.com/flannel-io/flannel/pull/2297
- fix GHA path in dependabot.yaml by @thomasferrandiz in https://github.com/flannel-io/flannel/pull/2304
- Fix spelling by @fguendling in https://github.com/flannel-io/flannel/pull/2302

### 0.28.1

- Fix blackhole creation test logic in AddBlackholeV4Route and AddBlackholeV6Route by @axeal in https://github.com/flannel-io/flannel/pull/2329

### 0.28.2

- fix extensions code exec by @thomasferrandiz in https://github.com/flannel-io/flannel/pull/2400

### 0.28.3

- fix: honor --stderrthreshold flag when --logtostderr is enabled by @pierluigilenoci in https://github.com/flannel-io/flannel/pull/2405
- vxlan: fix v6 direct route deletion to use v6DirectRoute by @cuiweixie in https://github.com/flannel-io/flannel/pull/2403
- lease: fix LeaseAttrs.String() after json.Marshal errors by @cuiweixie in https://github.com/flannel-io/flannel/pull/2404

### 0.28.4

- fix go version (don't set patch version) by @thomasferrandiz in https://github.com/flannel-io/flannel/pull/2428

### 0.28.5

- fix(vxlan): guard ifaceAddrsV6[0] on IPv4-only setups by @SAY-5 in https://github.com/flannel-io/flannel/pull/2434
- fix: reap orphaned zombie child processes when running as PID 1 by @pratikjagrut in https://github.com/flannel-io/flannel/pull/2438

### 0.28.6

- fix: skip invalid CIDRs in subnet file readers by @immanuwell in https://github.com/flannel-io/flannel/pull/2454
- etcd: bug fixes suggested by Claude by @thomasferrandiz in https://github.com/flannel-io/flannel/pull/2472
- fix: use semver tag type in Docker meta to support release events by @thomasferrandiz with @Copilot in https://github.com/flannel-io/flannel/pull/2483

### 0.28.7

- fix: use install-conf in chart by @thomasferrandiz in https://github.com/flannel-io/flannel/pull/2484


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.28.7**, the newest release recorded here for this line.

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
