---
id: TROUBLE-NODE_FEATURE_DISCOVERY_0_16_DEFECTS
type: troubleshooting
title: "node-feature-discovery 0.16: defects fixed in the 0.16 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.16.0 <0.17.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - node-feature-discovery 0.16 known issues
  - node-feature-discovery 0.16 fixed in
  - is this node-feature-discovery bug already fixed
tags:
  - troubleshooting
  - upgrade
  - node-feature-discovery
sources:
  - type: docs
    path: kubernetes-sigs/node-feature-discovery release notes for the 0.16 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/node-feature-discovery/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# node-feature-discovery 0.16: defects fixed in the 0.16 line

## Summary

**7 defects** the project fixed across **3 releases** of the 0.16 line, from 0.16.0 to
0.16.8. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.16.0

- Prevent `nfd-worker` erroring when reading attributes from paravirtual devices (#1557)
- source/cpu: fix build tags on rdt discovery (#1594)
- nfd-master: fix memory leak in nfd api-controller (#1615)
- helm: fix invalid name of host-swaps volume (#1635)
- hack/init-buildx.sh: fix broken patter matching (#1683)

### 0.16.1

- [release-0.16] Fix the problem with starting the master with empty cache by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/node-feature-discovery/pull/1740

### 0.16.8

- Fix nfd-master memory leak on non-leader instances when leader election is enabled (#2136)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.16.8**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `kubernetes-sigs/node-feature-discovery`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/node-feature-discovery.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
