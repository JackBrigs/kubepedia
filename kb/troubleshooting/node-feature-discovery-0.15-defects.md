---
id: TROUBLE-NODE_FEATURE_DISCOVERY_0_15_DEFECTS
type: troubleshooting
title: "node-feature-discovery 0.15: defects fixed in the 0.15 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.15.0 <0.16.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - node-feature-discovery 0.15 known issues
  - node-feature-discovery 0.15 fixed in
  - is this node-feature-discovery bug already fixed
tags:
  - troubleshooting
  - upgrade
  - node-feature-discovery
sources:
  - type: docs
    path: kubernetes-sigs/node-feature-discovery release notes for the 0.15 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/node-feature-discovery/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# node-feature-discovery 0.15: defects fixed in the 0.15 line

## Summary

**20 defects** the project fixed across **3 releases** of the 0.15 line, from 0.15.0 to
0.15.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.15.0

- deployment/helm: fix namespace of nfd-worker role and rolebinding (#1364)
- deployment/helm: fix handling of enableNodeFeatureApi parameter (#1365)
- nfd-master: fix filtering of extended resources (#1378)
- Fix serviceaccount handling for nfd-gc to be consistent with others (#1392)
- test/e2e: fix source/custom nodename test (#1421)
- Fix pkg name for test/utils/deployment (#1418)
- nfd-master: fix retry of node updates (#1425)
- test/e2e: fix broken feature-annotations test (#1440)
- docs: fix documentation on SEV security features (#1447)
- apis/nfd: fix incorrect comments of matching functions (#1467)
- apis/nfd: fix logging of rule expression processing (#1458)
- docs: fix small typo in customization guide (#1469)
- apis/nfd: fix multiple matcher terms targeting the same feature (#1468)
- Makefile: fix e2e-testing of the full image (#1500)
- chore(nfd-worker): fix minor typo in wrong label value format error (#1506)
- docs: fix name of prometheus kustomize overlay (#1517)
- docs: fix wording and nfd version in master config ref (#1520)
- docs: second fix to the prometheus kustomize overlay name (#1518)

### 0.15.2

- fix hook issue by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/node-feature-discovery/pull/1607

### 0.15.3

- nfd-master: fix memory leak in nfd api-controller by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/node-feature-discovery/pull/1621


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.15.3**, the newest release recorded here for this line.

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
