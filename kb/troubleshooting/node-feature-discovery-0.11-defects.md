---
id: TROUBLE-NODE_FEATURE_DISCOVERY_0_11_DEFECTS
type: troubleshooting
title: "node-feature-discovery 0.11: defects fixed in the 0.11 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.11.0 <0.12.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - node-feature-discovery 0.11 known issues
  - node-feature-discovery 0.11 fixed in
  - is this node-feature-discovery bug already fixed
tags:
  - troubleshooting
  - upgrade
  - node-feature-discovery
sources:
  - type: docs
    path: kubernetes-sigs/node-feature-discovery release notes for the 0.11 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/node-feature-discovery/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# node-feature-discovery 0.11: defects fixed in the 0.11 line

## Summary

**8 defects** the project fixed across **3 releases** of the 0.11 line, from 0.11.0 to
0.11.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.11.0

- scripts/update-gh-pages: fix symlink to stable version (#724)
- docs: fix operator deployment instructions (#726)
- scripts/prepare-release: fix upating of readme (#755)
- docs: re-fix operator deployment instructions (#762)

### 0.11.2

- docs: fix operator deployment instructions (#813)
- docs: small typo fix in cpuid feature list (#826)
- Fix templates for NodeFeatureRule with MatchAny (#872)

### 0.11.3

- docs: fix incorrect shell snippet for removing labels (#893)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.11.3**, the newest release recorded here for this line.

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
