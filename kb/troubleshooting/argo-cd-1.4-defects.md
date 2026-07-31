---
id: TROUBLE-ARGO_CD_1_4_DEFECTS
type: troubleshooting
title: "argo-cd 1.4: defects fixed in the 1.4 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.4.0 <1.5.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - argo-cd 1.4 known issues
  - argo-cd 1.4 fixed in
  - is this argo-cd bug already fixed
tags:
  - troubleshooting
  - upgrade
  - argo-cd
sources:
  - type: docs
    path: argoproj/argo-cd release notes for the 1.4 line — bug-fix entries
    url: https://github.com/argoproj/argo-cd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# argo-cd 1.4: defects fixed in the 1.4 line

## Summary

**30 defects** the project fixed across **3 releases** of the 1.4 line, from 1.4.0 to
1.4.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.4.0

- fix: Adds support for /api/v1/account* via HTTP. Fixes #2664 (#2701)
- fix: Allow '@'-character in SSH usernames when connecting a repository (#2612)
- fix: Allow dot in project policy. Closes #2724 (#2755)
- fix: Allow you to sync local Helm apps. Fixes #2741 (#2747)
- fix: Allows Helm parameters that contains arrays or maps. (#2525)
- fix: application-controller doesn't deal with rm/add same cluster gracefully (x509 unknown) (#2389)
- fix: diff local ignore kustomize build options (#2942)
- fix: Ensures that Helm charts are correctly resolved before sync. Fixes #2758 (#2760)
- fix: Fix 'Open application' link when using basehref (#2729)
- fix: fix a bug with cluster add when token secret is not first in list. (#2744)
- fix: fix bug where manifests are not cached. Fixes #2770 (#2771)
- fix: Fixes bug whereby retry does not work for CLI. Fixes #2767 (#2768)
- fix: git contention leads applications into Unknown state (#2877)
- fix: Issue #1944 - Gracefully handle missing cached app state (#2464)
- fix: Issue #2668 - Delete a specified context (#2669)
- fix: Issue #2683 - Make sure app update don't fail due to concurrent modification (#2852)
- fix: Issue #2721 Optimize helm repo querying (#2816)
- fix: Issue #2853 - Improve application env variables/labels editing (#2856)
- fix: Issue 2848 - Application Deployment history panel shows incorrect info for recent releases (#2849)
- fix: Make BeforeHookCreation the default. Fixes #2754 (#2759)
- fix: No error on `argocd app create` in CLI if `--revision` is omitted #2665
- fix: Only delete resources during app delete cascade if permitted to (fixes #2693) (#2695)
- fix: prevent user from seeing/deleting resources not permitted in project (#2908) (#2910)
- fix: self-heal should retry syncing an application after specified delay
- fix: stop logging dex config secrets #(2904) (#2937)
- fix: stop using jsondiffpatch on clientside to render resource difference (#2869)
- fix: UI should re-trigger SSO login if SSO JWT token expires (#2891)
- fix: update argocd-util import was not working properly (#2939)

### 1.4.1

- fix: impossible to config RBAC if group name includes ',' (#3013)

### 1.4.2

- fix: correctly replace cache in namespace isolation mode (#3023)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.4.2**, the newest release recorded here for this line.

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
