---
id: TROUBLE-ARGO_CD_1_2_DEFECTS
type: troubleshooting
title: "argo-cd 1.2: defects fixed in the 1.2 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.2.0 <1.3.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - argo-cd 1.2 known issues
  - argo-cd 1.2 fixed in
  - is this argo-cd bug already fixed
tags:
  - troubleshooting
  - upgrade
  - argo-cd
sources:
  - type: docs
    path: argoproj/argo-cd release notes for the 1.2 line — bug-fix entries
    url: https://github.com/argoproj/argo-cd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# argo-cd 1.2: defects fixed in the 1.2 line

## Summary

**18 defects** the project fixed across **2 releases** of the 1.2 line, from 1.2.0 to
1.2.1. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.2.0

- Do not panic if the type is not api.Status (an error scenario) (#2105)
- Make sure endpoint is shown as a child of service (#2060)
- Word-wraps app info in the table and list views. (#2004)
- Project source/destination removal should consider wildcards (#1780)
- Repo whitelisting in UI does not support wildcards (#2000)
- Wait for CRD creation during sync process (#1940)
- Added a button to select out of sync items in the sync panel (#1902)
- Proper handling of an excluded resource in an application (#1621)
- Stop repeating logs on stopped container (#1614)
- Fix git repo url parsing on application list view (#2174)
- Fix nil pointer dereference error during app reconciliation (#2146)
- Fix history api fallback implementation to support app names with dots (#2114)
- Fixes some code issues related to Kustomize build options. (#2146)
- Adds checks around valid paths for apps (#2133)
- Endpoint incorrectly considered top level managed resource (#2060)
- Allow adding certs for hostnames ending on a dot (#2116)

### 1.2.1

- Fix degraded proxy support for http(s) git repository (#2243)
- Fix nil pointer dereference in application controller (#2290)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.2.1**, the newest release recorded here for this line.

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
