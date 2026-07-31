---
id: TROUBLE-NODE_FEATURE_DISCOVERY_0_14_DEFECTS
type: troubleshooting
title: "node-feature-discovery 0.14: defects fixed in the 0.14 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.14.0 <0.15.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - node-feature-discovery 0.14 known issues
  - node-feature-discovery 0.14 fixed in
  - is this node-feature-discovery bug already fixed
tags:
  - troubleshooting
  - upgrade
  - node-feature-discovery
sources:
  - type: docs
    path: kubernetes-sigs/node-feature-discovery release notes for the 0.14 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/node-feature-discovery/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# node-feature-discovery 0.14: defects fixed in the 0.14 line

## Summary

**16 defects** the project fixed across **4 releases** of the 0.14 line, from 0.14.0 to
0.14.5. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.14.0

- nfd-master: fix a crash when processing NodeFeatureRules (#1173)
- pkg/nfd-master/nfd-master.go: Fix typo (#1171)
- nfd-topology-updater: fix wrong kubelet_internal_checkpoint path and compare basename to full path (#1167)
- helm: fix mount for nfd-master config (#1204)
- nfd-master: fix resync period config option (#1185)
- deployment/helm: fix default for kubeletStateDir parameter (#1207)
- Fixed typo in Header under deployment/kustomize.md (#1222)
- Docs: Fix typo on customization-guide (#1247)
- docs: fix toc of topology-updater and topology-gc reference (#1278)
- Fix Topology Manager policy and scope not being updated after NRT creation (#1256)
- fix empty hugepages in some numa nodes caused no such file or directory errors (#1287)
- nfd_gc_test.go: fix multiple import of same pkg (#1333)

### 0.14.1

- deployment/helm: fix namespace of nfd-worker role and rolebinding (#1370)
- deployment/helm: fix handling of enableNodeFeatureApi parameter (#1371)

### 0.14.3

- nfd-master: fix retry of node updates (#1427)

### 0.14.5

- nfd-master: fix memory leak in nfd api-controller by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/node-feature-discovery/pull/1622


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.14.5**, the newest release recorded here for this line.

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
