---
id: TROUBLE-ARGO_CD_2_2_DEFECTS
type: troubleshooting
title: "argo-cd 2.2: defects fixed in the 2.2 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.2.0 <2.3.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - argo-cd 2.2 known issues
  - argo-cd 2.2 fixed in
  - is this argo-cd bug already fixed
tags:
  - troubleshooting
  - upgrade
  - argo-cd
sources:
  - type: docs
    path: argoproj/argo-cd release notes for the 2.2 line — bug-fix entries
    url: https://github.com/argoproj/argo-cd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# argo-cd 2.2: defects fixed in the 2.2 line

## Summary

**27 defects** the project fixed across **11 releases** of the 2.2 line, from 2.2.0 to
2.2.12. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.2.0

- Argo CD API server caches RBAC checks that significantly improves the GET /api/v1/applications API performance (#7587)
- Health check support for KubeVirt (#7176), Cassandra (#7017), Openshift Route (#7112), DeploymentConfig (#7114), Confluent (#6957) and SparkApplication (#7434) CRDs
- Persistent banner (#7312) with custom positioning (#7462)
- Cluster name support in project destinations (#7198)
- around 30 more features and a total of 84 bug fixes

### 2.2.1

- fix: Resource details page crashes when resource is not deployed and hide managed fields is selected (#7971)
- fix: Issue with headless installation (#7958)

### 2.2.2

- fix: Issue with project scoped resources (#8048)
- fix: Default value for retry validation #8055 (#8064)
- fix: Sync window panel is crashed if resource name not contain letters (#8053)
- fix: Upgrade github.com/argoproj/gitops-engine to v0.5.2
- fix: Opening app details shows UI error on some apps (#8016) (#8019)
- fix: Correctly handle project field during partial cluster update (#7994)
- fix: Cluster API does not support updating labels and annotations (#7901)

### 2.2.3

- fix: Application exist panic when execute api call (#8188)
- fix: Route health check stuck in 'Progressing' (#8170)

### 2.2.4

- fix: Prevent value files outside repository root

### 2.2.5

- fix: Resolve symlinked value files correctly (#8387)

### 2.2.6

- fix: prevent file traversal using helm file values param and application details api (#8606)
- fix!: enforce app create/update privileges when getting repo details (#8558)
- feat: support custom helm values file schemes (#8535)

### 2.2.7

- fix: correct jsonnet paths resolution (#8721)

### 2.2.8

- fix: application resource APIs must enforce project restrictions

### 2.2.11

- fix: webhook typo in case of error in GetManifests (#9671)

### 2.2.12

- fix: create serviceaccount token for v1.24 clusters (#9546)
- fix: upgrade moment from 2.29.2 to 2.29.3 (#9330)
- chore: upgrade moment to latest version to fix CVE (#9005)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.2.12**, the newest release recorded here for this line.

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
