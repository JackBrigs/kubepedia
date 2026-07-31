---
id: TROUBLE-NODE_FEATURE_DISCOVERY_0_10_DEFECTS
type: troubleshooting
title: "node-feature-discovery 0.10: defects fixed in the 0.10 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.10.0 <0.11.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - node-feature-discovery 0.10 known issues
  - node-feature-discovery 0.10 fixed in
  - is this node-feature-discovery bug already fixed
tags:
  - troubleshooting
  - upgrade
  - node-feature-discovery
sources:
  - type: docs
    path: kubernetes-sigs/node-feature-discovery release notes for the 0.10 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/node-feature-discovery/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# node-feature-discovery 0.10: defects fixed in the 0.10 line

## Summary

**13 defects** the project fixed across **2 releases** of the 0.10 line, from 0.10.0 to
0.10.1. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.10.0

- fix kustomize sample overlay enabling cert-manager (#710)
- Fix the typo in deployment-and-usage.md (#575)
- Fix broken link for worker-conf example (#590)
- deployment: fix formatting of the worker conf sample (#599)
- topology-updater:fix klog initialization (#625)
- pkg/resourcemonitor: fix typo in comment (#641)
- Topology-updater introduction typo fix (#645)
- More topology updater documentation typo fixes (#648)
- images: fix invalid k8s-staging-test-infra/gcb-docker-gcloud tag (#686)
- source/usb: fix fallback to default label format (#694)
- Fix kustomization template to work with cert-manager (#710)
- docs: small fix in block and net features in customization guide (#715)

### 0.10.1

- [release-0.10] scripts/update-gh-pages: fix symlink to stable version (#746)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.10.1**, the newest release recorded here for this line.

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
