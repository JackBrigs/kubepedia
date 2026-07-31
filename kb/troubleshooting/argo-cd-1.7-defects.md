---
id: TROUBLE-ARGO_CD_1_7_DEFECTS
type: troubleshooting
title: "argo-cd 1.7: defects fixed in the 1.7 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.7.0 <1.8.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - argo-cd 1.7 known issues
  - argo-cd 1.7 fixed in
  - is this argo-cd bug already fixed
tags:
  - troubleshooting
  - upgrade
  - argo-cd
sources:
  - type: docs
    path: argoproj/argo-cd release notes for the 1.7 line — bug-fix entries
    url: https://github.com/argoproj/argo-cd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# argo-cd 1.7: defects fixed in the 1.7 line

## Summary

**35 defects** the project fixed across **8 releases** of the 1.7 line, from 1.7.2 to
1.7.9. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.7.2

- fix: Sync hangs with cert-manager on latest RC (#4105)
- fix: Unable to create project JWT token on K8S v1.15 (#4165)
- fix: Argo CD does not exclude creationTimestamp from diffing (#4157)

### 1.7.3

- fix: application details page crash when app is deleted (#4229)
- fix: api-server unnecessary normalize projects on every start (#4219)
- fix: Re-create already initialized ARGOCD_GNUPGHOME on startup (#4214) (#4223)
- fix: Add openshift as a dex connector type which requires a redirectURI (#4222)
- fix: Replace status.observedAt with redis pub/sub channels for resource tree updates (#1340) (#4208)
- fix: cache inconsistency of child resources (#4053) (#4202)
- fix: do not include kube-api check in application liveness flow (#4163)

### 1.7.4

- fix: automatically stop watch API requests when page is hidden (#4269)
- fix: upgrade gitops-engine dependency (issues #4242, #1881) (#4268)
- fix: application stream API should not return 'ADDED' events if resource version is provided (#4260)
- fix: JS error when using cluster filter in the /application view (#4247)
- fix: improve applications list page client side performance (#4244)

### 1.7.5

- fix: app create with -f should not ignore other options (#4322)
- fix: limit concurrent list requests across all clusters (#4328)
- fix: fix possible deadlock in /v1/api/stream/applications and /v1/api/application APIs (#4315)
- fix: WatchResourceTree does not enforce RBAC (#4311)
- fix: app refresh API should use app resource version (#4303)
- fix: use informer instead of k8s watch to ensure app is refreshed (#4290)

### 1.7.6

- fix: Added cluster authentication to AKS clusters (#4265)
- fix: prevent 'argocd app sync' hangs if sync is completed too quickly (#4373)
- fix: argocd app wait/sync might stuck (#4350)
- fix: failed syncs are not retried soon enough (#4353)

### 1.7.7

- fix: Support transition from a git managed namespace to auto create (#4401)
- fix: reduce memory spikes during cluster cache refresh (#4298)
- fix: No error/warning condition if application destination namespace not monitored by Argo CD (#4329)
- fix: Fix local diff/sync of apps using cluster name (#4201)

### 1.7.8

- fix(logging.go): changing marshaler for JSON logging to use gogo (#4319)
- fix: api-server should not try creating default project it is exists already (#4517)
- fix: JS error on application list page if app has no namespace (#4499)

### 1.7.9

- fix: improve commit verification tolerance (#4825)
- fix: argocd diff --local should not print data of local secrets (#4850)
- fix(ui): stack overflow crash of resource tree view for large applications (#4685)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.7.9**, the newest release recorded here for this line.

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
