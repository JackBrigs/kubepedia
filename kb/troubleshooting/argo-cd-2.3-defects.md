---
id: TROUBLE-ARGO_CD_2_3_DEFECTS
type: troubleshooting
title: "argo-cd 2.3: defects fixed in the 2.3 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.3.0 <2.4.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - argo-cd 2.3 known issues
  - argo-cd 2.3 fixed in
  - is this argo-cd bug already fixed
tags:
  - troubleshooting
  - upgrade
  - argo-cd
sources:
  - type: docs
    path: argoproj/argo-cd release notes for the 2.3 line — bug-fix entries
    url: https://github.com/argoproj/argo-cd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# argo-cd 2.3: defects fixed in the 2.3 line

## Summary

**42 defects** the project fixed across **7 releases** of the 2.3 line, from 2.3.0 to
2.3.7. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.3.0

- The skipCrds flag and ability to ignore missing values files for Helm (#8012, #8003)
- Additional environment variables for Kustomize (#8096)
- Argo CD CLI follows the XDG Base directory standard (#7638)
- Redis is no longer used during SSO login (#8241)
- fix: Add "Restarting MinIO" status to MiniO Tenant health check (#8191)
- fix: Adding pagination to grouped nodes sliding panel#7837 (#7915)
- fix: Allow all resources to add external links (#7923)
- fix: Application exist panic when execute api call (#8188)
- fix: Controller panics if resource manifest has incorrect annotation (#8022)
- fix: Correctly handle project field during partial cluster update (#7994)
- fix: Default value for retry validation #8055 (#8064)
- fix: Fix a possible crash when parsing RBAC (#8165)
- fix: Grouped node list missing resources on Compact resources view #8014 (#8018)
- fix: Issue with headless installation (#7958)
- fix: Issue with project scoped resources (#8048)
- fix: Kubernetes labels normalization for Prometheus (#7925)
- fix: Nested Refresh dropdown does not work on Application Details page #1524 (#7950)
- fix: Network line colors and menu icon alignment (#8059)
- fix: Opening app details shows UI error on some apps (#8016) (#8019)
- fix: Prevent possible nil-pointer deref in normalizer (#8185)
- fix: Prevent possible out-of-bounds access when loading policies (#8186)
- fix: Provide a semantic version parsed version for KUBE_VERSION (#8250)
- fix: Resource details page crashes when resource is not deployed and hide managed fields is selected (#7971)
- fix: Route health check stuck in 'Progressing' (#8170)
- fix: Sync window panel is crashed if resource name not contain letters (#8053)
- fix: Targetervision compatible without prefix refs/heads or refs/tags (#7939)
- fix: Trailing line in Filter Dropdown Menus #7821 (#8001)
- fix(ui): Use consistent case for diff modes (#7945)
- fix: Use gRPC timeout for sidecar CMPs (#8131) (#8236)

### 2.3.1

- fix: Retry checkbox unchecked unexpectedly; Sync up with YAML (#8682) (#8720)
- fix: correct jsonnet paths resolution (#8721)
- fix(ui): Applications page incorrectly resets to tiles view. Fixes #8702 (#8718)

### 2.3.2

- fix: application resource APIs must enforce project restrictions

### 2.3.3

- fix: prevent excessive repo-server disk usage for large repos (#8845) (#8897)
- fix: Set QPS and burst rate for resource ops client (#8915)

### 2.3.4

- fix: fix broken monaco editor collapse icons (#8709)
- fix: allow cli/ui to follow logs (#8987) (#9065)

### 2.3.6

- fix: webhook typo in case of error in GetManifests (#9671)

### 2.3.7

- fix: skip redirect url validation when it's the base href (#10058) (#10116)
- fix: upgrade moment from 2.29.2 to 2.29.3 (#9330)
- fix: use serviceaccount name instead of struct (#9614)
- fix: create serviceaccount token for v1.24 clusters (#9546)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.3.7**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `argoproj/argo-cd`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/argo-cd.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
