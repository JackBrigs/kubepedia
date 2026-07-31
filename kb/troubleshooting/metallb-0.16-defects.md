---
id: TROUBLE-METALLB_0_16_DEFECTS
type: troubleshooting
title: "metallb 0.16: defects fixed in the 0.16 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.16.0 <0.17.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - metallb 0.16 known issues
  - metallb 0.16 fixed in
  - is this metallb bug already fixed
tags:
  - troubleshooting
  - upgrade
  - metallb
sources:
  - type: docs
    path: metallb/metallb release notes for the 0.16 line — bug-fix entries
    url: https://github.com/metallb/metallb/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# metallb 0.16: defects fixed in the 0.16 line

## Summary

**9 defects** the project fixed across **2 releases** of the 0.16 line, from 0.16.0 to
0.16.1. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.16.0

- Allocation: fix the AllocationFailed event to indicate when the pool doesn't have any IPs left. (#2891, @oribon)
- Fix ConfigurationState to be updated when the resource is recreated. (#2953, @oribon)
- Fix L2 speaker election ignoring service selectors, making sure only the relevant L2Advertisements for the service are considered. (#3014, @oribon)
- Fix never changing session down metric with peer address in native mode. All the other events are generated with address:port, here we restore to the original format with the address only. (#2879, @fedepaol)
- Fixes invalid maximum value in CRD validation of ASNs in Kubernetes v1.36.0 (#3035, @PseudoResonance)
- L2Status controller: fix a scenario where two speakers try to modify the same status resource (#2938, @oribon)

### 0.16.1

- Fix helm chart rendering issue when default values are provided. (#3058, @fedepaol)
- Fixed BGPPeer v1beta2 schema: `localASN` now correctly declares `format: int64` (was `int32`, which cannot represent the declared `Maximum=4294967295`). (#3054, @lexfrei)
- Fixed controller health probes and the health bind address is now configurable and defaults to all interfaces (#3062, @Jakob3xD)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.16.1**, the newest release recorded here for this line.

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
