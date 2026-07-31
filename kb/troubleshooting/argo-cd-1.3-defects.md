---
id: TROUBLE-ARGO_CD_1_3_DEFECTS
type: troubleshooting
title: "argo-cd 1.3: defects fixed in the 1.3 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.3.0 <1.4.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - argo-cd 1.3 known issues
  - argo-cd 1.3 fixed in
  - is this argo-cd bug already fixed
tags:
  - troubleshooting
  - upgrade
  - argo-cd
sources:
  - type: docs
    path: argoproj/argo-cd release notes for the 1.3 line — bug-fix entries
    url: https://github.com/argoproj/argo-cd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# argo-cd 1.3: defects fixed in the 1.3 line

## Summary

**60 defects** the project fixed across **3 releases** of the 1.3 line, from 1.3.0 to
1.3.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.3.0

- failed parsing on parameters with comma (#1660)
- StatefulSet with OnDelete Update Strategy stuck progressing (#1881)
- Error message "Unable to load data: key is missing" is confusing (#1944)
- Multiple parallel app syncs causes OOM (#2022)
- Unknown error when setting params with argocd app set on helm app (#2046)
- Endpoint is no longer shown as a child of services (#2060)
- SSH known hosts entry cannot be deleted if contains shell pattern in name (#2099)
- Application 404s on names with periods (#2114)
- Adding certs for hostnames ending with a dot (.) is not possible (#2116)
- v1.2.0-rc1 nil pointer dereference when syncing (#2146)
- 1.2.0-rc1 - Authentication Required error in Repo Server (#2152)
- v1.2.0-rc1 Applications List View doesn't work (#2174)
- Manual sync does not trigger Presync hooks (#2185)
- SyncError app condition disappears during app reconciliation (#2192)
- argocd app wait\sync prints 'Unknown' for resources without health (#2198)
- 1.2.0-rc2 Warning during secret diffing (#2206)
- SSO redirect url is incorrect if configured Argo CD URL has trailing slash (#2212)
- Application summary diff page shows hooks (#2215)
- An app with a single resource and Sync hook remains progressing (#2216)
- v1.2.0-rc2 does not retrieve http(s) based git repository behind the proxy (#2243)
- Intermittent "git ls-remote" request failures should not fail app reconciliation (#2245)
- Result of ListApps operation for Git repo is cached incorrectly (#2263)
- Controller panics due to nil pointer error (#2290)
- The Helm --kube-version support does not work on GKE: (#2303)
- Fixes bug that prevents you creating repos via UI/CLI. (#2308)
- The 'helm.repositories' settings is dropped without migration path (#2316)
- Badge response does not contain cache control header (#2317)
- Inconsistent sync result from UI and CLI (#2321)
- Failed edit application with plugin type requiring environment (#2330)
- End-to-End tests not working with Kubernetes v1.16 (#2371)
- Creating an application from Helm repository should select "Helm" as source type (#2378)
- The parameters of ValidateAccess GRPC method should not be logged (#2386)
- Maintenance window meaning is confusing (#2398)
- UI bug when targetRevision is omitted (#2407)
- Too many vulnerabilities in Docker image (#2425)
- proj windows commands not consistent with other commands (#2443)
- Custom resource actions cannot be executed from the UI (#2448)
- Application controller sometimes accidentally removes duplicated/excluded resource warning condition (#2453)
- Logic that checks sync windows state in the cli is incorrect (#2455)
- UI don't allow to create window with `* * * * *` schedule (#2475)
- Helm Hook is executed twice if annotated with both pre-install and pre-upgrade annotations (#2480)
- Impossible to edit chart name using App details page (#2484)
- ArgoCD does not provide CSRF protection (#2496)
- ArgoCD failing to install CRDs in master from Helm Charts (#2497)
- Timestamp in Helm package file name causes error in Application with Helm source (#2549)
- Attempting to create a repo with password but not username panics (#2567)
- UI incorrectly mark resources as `Required Pruning` (#2577)
- argocd app diff prints only first difference (#2616)
- Cluster list page fails if any cluster is not reachable (#2620)
- Repository type should be mandatory for repo add command in CLI (#2622)
- Repo server executes unnecessary ls-remotes (#2626)
- Application list page incorrectly filter apps by label selector (#2633)
- Custom actions are disabled in Argo CD UI (#2635)
- Failure of `argocd version` in the self-building container image (#2645)
- Application list page is not updated automatically anymore (#2655)
- Regression: Cannot return Kustomize version for 3.1.0 (#2662)
- API server does not allow creating role with action `action/*` (#2670)
- Application controller `kubectl-parallelism-limit` flag is broken (#2673)

### 1.3.1

- #2767 Fix bug whereby retry does not work for CLI

### 1.3.2

- #2797 Fix directory traversal edge case and enhance tests


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.3.2**, the newest release recorded here for this line.

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
