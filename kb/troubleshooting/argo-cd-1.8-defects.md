---
id: TROUBLE-ARGO_CD_1_8_DEFECTS
type: troubleshooting
title: "argo-cd 1.8: defects fixed in the 1.8 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.8.0 <1.9.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - argo-cd 1.8 known issues
  - argo-cd 1.8 fixed in
  - is this argo-cd bug already fixed
tags:
  - troubleshooting
  - upgrade
  - argo-cd
sources:
  - type: docs
    path: argoproj/argo-cd release notes for the 1.8 line — bug-fix entries
    url: https://github.com/argoproj/argo-cd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# argo-cd 1.8: defects fixed in the 1.8 line

## Summary

**23 defects** the project fixed across **7 releases** of the 1.8 line, from 1.8.1 to
1.8.7. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.8.1

- fix: sync retry is broken for multi-phase syncs (#5017)

### 1.8.2

- fix: remove invalid assumption about OCI helm chart path (#5179)
- fix: Possible nil pointer dereference in repository API (#5128)
- fix: Possible nil pointer dereference in repocreds API (#5130)
- fix: use json serialization to store cache instead of github.com/vmihailenco/msgpack (#4965)
- fix: add liveness probe to restart repo server if it fails to server tls requests (#5110) (#5119)
- fix: Allow correct SSO redirect URL for CLI static client (#5098)
- fix: setting 'revision history limit' errors in UI (#5035)
- fix: add api-server liveness probe that catches bad data in informer (#5026)

### 1.8.3

- fix: make sure JWT token time fields contain only integer values (#5228)

### 1.8.4

- fix: version info should be available if anonymous access is enabled (#5422)
- fix: disable jwt claim audience validation #5381 (#5413)
- fix: /api/version should not return tools version for unauthenticated requests (#5415)
- fix: account tokens should be rejected if required capability is disabled (#5414)
- fix: tokens keep working after account is deactivated (#5402)
- fix: a request which was using a revoked project token, would still be allowed to perform requests allowed by default policy (#5378)

### 1.8.5

- fix: 'argocd app wait --suspended' stuck if operation is in progress (#5511)
- fix: Presync hooks stop working after namespace resource is added in a Helm chart #5522

### 1.8.6

- fix: Properly escape HTML for error message from CLI SSO (#5563)
- fix: API server should not print resource body when resource update fails (#5617)
- fix: fix memory leak in application controller (#5604)

### 1.8.7

- fix: Properly escape HTML for error message from CLI SSO (#5563)
- fix: Empty resource whitelist allowed all resources (#5540) (#5551)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.8.7**, the newest release recorded here for this line.

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
