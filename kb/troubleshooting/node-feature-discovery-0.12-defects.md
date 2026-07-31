---
id: TROUBLE-NODE_FEATURE_DISCOVERY_0_12_DEFECTS
type: troubleshooting
title: "node-feature-discovery 0.12: defects fixed in the 0.12 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.12.0 <0.13.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - node-feature-discovery 0.12 known issues
  - node-feature-discovery 0.12 fixed in
  - is this node-feature-discovery bug already fixed
tags:
  - troubleshooting
  - upgrade
  - node-feature-discovery
sources:
  - type: docs
    path: kubernetes-sigs/node-feature-discovery release notes for the 0.12 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/node-feature-discovery/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# node-feature-discovery 0.12: defects fixed in the 0.12 line

## Summary

**20 defects** the project fixed across **3 releases** of the 0.12 line, from 0.12.0 to
0.12.4. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.12.0

- docs: remove fixed release tag in developer guide (#798)
- docs: fix operator deployment instructions (#811)
- docs: small typo fix in cpuid feature list (#824)
- github: small fix in new-release issue template (#822)
- test/e2e: fix checking of nfd-master annotation (#839)
- source/fake: fix name of fake flag feature (#843)
- nfd-master: fix incorrect log messages in crd controller (#860)
- nfd-master: more fixes to log messages (#861)
- Fix templates for NodeFeatureRule with MatchAny (#865)
- docs: fix incorrect shell snippet for removing labels (#892)
- test/e2e: fix segfault in case no e2e config file is specified (#891)
- apis/nfd: fix NodeFeatureRule templating (#935)
- test/e2e: fix topologu-updater cmdline args (#960)
- e2e: topologyupdater: fix and stabilize tests (#961)
- helm: fix mount name of topology-updater config (#979)
- nfd-master: fix creation of the -enable-nodefeature-api flag (#992)
- test/e2e: fix mistake in ginkgo focus (#1000)

### 0.12.2

- source/cpu: fix build flags of cpuid detection (#1104)
- deployment: fixes for mounting kubelet config (#1105)

### 0.12.4

- nfd-master: fix a crash when processing NodeFeatureRules (#1176)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.12.4**, the newest release recorded here for this line.

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
