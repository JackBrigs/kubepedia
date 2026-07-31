---
id: TROUBLE-ARGO_CD_2_1_DEFECTS
type: troubleshooting
title: "argo-cd 2.1: defects fixed in the 2.1 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.1.0 <2.2.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - argo-cd 2.1 known issues
  - argo-cd 2.1 fixed in
  - is this argo-cd bug already fixed
tags:
  - troubleshooting
  - upgrade
  - argo-cd
sources:
  - type: docs
    path: argoproj/argo-cd release notes for the 2.1 line — bug-fix entries
    url: https://github.com/argoproj/argo-cd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# argo-cd 2.1: defects fixed in the 2.1 line

## Summary

**26 defects** the project fixed across **13 releases** of the 2.1 line, from 2.1.1 to
2.1.14. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.1.1

- fix(ui): Add State to props passed to Extensions (#7045)
- fix: keep uid_entrypoint.sh for backward compatibility (#7047)

### 2.1.2

- fix: cluster filter popping out of box (#7135)
- fix: gracefully shutdown metrics server when dex config changes (#7138)
- fix: upgrade gitops engine version to v0.4.1 (#7088)
- fix: repository name already exists when multiple helm dependencies (#7096)

### 2.1.3

- fix: core-install.yaml always refers to latest argocd image (#7321)
- fix: handle applicationset backup forbidden error (#7306)
- fix: Argo CD should not use cached git/helm revision during app creation/update validation (#7244)

### 2.1.4

- fix: Operation has completed with phase: Running (#7482)
- fix: Application status panel shows Syncing instead of Deleting (#7486)
- fix(ui): Add Error Boundary around Extensions and comply with new Extensions API (#7215)

### 2.1.5

- fix: Invalid memory address or nil pointer dereference in processRequestedAppOperation (#7501)

### 2.1.6

- fix: don't use revision caching during app creation (#7508)
- fix: supporting OCI dependencies. Fixes #6062 (#6994)

### 2.1.7

- fix: env vars to tune cluster cache were broken (#7779)
- fix: upgraded gitops engine to v0.4.2 (fixes #7561)

### 2.1.8

- fix: env vars to tune cluster cache were broken (#7779)
- fix: upgraded gitops engine to v0.4.2 (fixes #7561)

### 2.1.9

- fix: Prevent value files outside repository root

### 2.1.10

- fix: Resolve symlinked value files correctly (#8387)

### 2.1.11

- fix: prevent file traversal using helm file values param and application details api (#8606)
- fix!: enforce app create/update privileges when getting repo details (#8558)
- feat: support custom helm values file schemes (#8535)

### 2.1.12

- fix: correct jsonnet paths resolution (#8721)

### 2.1.14

- fix: application resource APIs must enforce project restrictions


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.1.14**, the newest release recorded here for this line.

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
