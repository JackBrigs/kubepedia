---
id: TROUBLE-NODE_FEATURE_DISCOVERY_0_13_DEFECTS
type: troubleshooting
title: "node-feature-discovery 0.13: defects fixed in the 0.13 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.13.0 <0.14.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - node-feature-discovery 0.13 known issues
  - node-feature-discovery 0.13 fixed in
  - is this node-feature-discovery bug already fixed
tags:
  - troubleshooting
  - upgrade
  - node-feature-discovery
sources:
  - type: docs
    path: kubernetes-sigs/node-feature-discovery release notes for the 0.13 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/node-feature-discovery/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# node-feature-discovery 0.13: defects fixed in the 0.13 line

## Summary

**11 defects** the project fixed across **6 releases** of the 0.13 line, from 0.13.0 to
0.13.5. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.13.0

- source/cpu: fix build flags of cpuid detection (#1063)
- deployment: fixes for mounting kubelet config (#1080)
- hack/prepare-release.sh: fix name of one e2e test file (#1151)

### 0.13.1

- nfd-master: fix -prune by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/node-feature-discovery/pull/1165
- nfd-master: fix a crash when processing NodeFeatureRules by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/node-feature-discovery/pull/1174
- nfd-topology-updater: fix wrong kubelet_internal_checkpoint path and compare basename to full path by @k8s-infra-cherrypick-robot in https://github.com/kubernetes-sigs/node-feature-discovery/pull/1183

### 0.13.2

- helm: fix mount for nfd-master config (#1205)
- deployment/helm: fix default for kubeletStateDir parameter (#1209)

### 0.13.3

- nfd-master: fix node updates on config change by @marquiz in https://github.com/kubernetes-sigs/node-feature-discovery/pull/1259

### 0.13.4

- fix empty hugepages in some numa nodes caused no such file or directory errors (#1298)

### 0.13.5

- deployment/helm: fix namespace of nfd-worker role and rolebinding (#1369)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.13.5**, the newest release recorded here for this line.

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
