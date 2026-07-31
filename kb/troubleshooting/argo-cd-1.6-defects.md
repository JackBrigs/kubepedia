---
id: TROUBLE-ARGO_CD_1_6_DEFECTS
type: troubleshooting
title: "argo-cd 1.6: defects fixed in the 1.6 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.6.0 <1.7.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - argo-cd 1.6 known issues
  - argo-cd 1.6 fixed in
  - is this argo-cd bug already fixed
tags:
  - troubleshooting
  - upgrade
  - argo-cd
sources:
  - type: docs
    path: argoproj/argo-cd release notes for the 1.6 line — bug-fix entries
    url: https://github.com/argoproj/argo-cd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# argo-cd 1.6: defects fixed in the 1.6 line

## Summary

**16 defects** the project fixed across **3 releases** of the 1.6 line, from 1.6.0 to
1.6.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.6.0

- fix: settings manager should invalidate cache after updating repositories/repository credentials (#3672)
- fix: Allow unsetting the last remaining values file (#3644) (#3645)
- fix: Read cert data from kubeconfig during cluster addition and use if present (#3655) (#3667)
- fix: Allow underscores in hostnames in certificate module (#3596)
- fix: apply scopes from argocd-rbac-cm to project jwt group searches (#3508)
- fix: fix nil pointer dereference error after cluster deletion (#3634)
- fix: Prevent possible nil pointer dereference when getting Helm client (#3613)
- fix: Allow CLI version command to succeed without server connection (#3049) (#3550)
- fix: use 'git show-ref' to both retrieve and store generated manifests (#3578)
- fix: enable redis retries; add redis request duration metric (#3575)
- fix: Disable keep-alive for HTTPS connection to Git (#3531)

### 1.6.1

- fix: User unable to generate project token even if account has appropriate permissions (#3804)

### 1.6.2

- fix: use glob matcher in casbin built-in model (#3966)
- fix: Normalize Helm chart path when chart name contains a slash (#3987)
- fix: allow duplicates when using generateName (#3878)
- fix: nil pointer dereference while syncing an app (#3915)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.6.2**, the newest release recorded here for this line.

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
