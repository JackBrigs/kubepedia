---
id: TROUBLE-ARGO_CD_2_0_DEFECTS
type: troubleshooting
title: "argo-cd 2.0: defects fixed in the 2.0 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.0.0 <2.1.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - argo-cd 2.0 known issues
  - argo-cd 2.0 fixed in
  - is this argo-cd bug already fixed
tags:
  - troubleshooting
  - upgrade
  - argo-cd
sources:
  - type: docs
    path: argoproj/argo-cd release notes for the 2.0 line — bug-fix entries
    url: https://github.com/argoproj/argo-cd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# argo-cd 2.0: defects fixed in the 2.0 line

## Summary

**27 defects** the project fixed across **5 releases** of the 2.0 line, from 2.0.1 to
2.0.5. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.0.1

- fix: spark application check fails on missing section (#6036)
- fix: Adding explicit bind to redis and sentinel for IPv4 clusters #5957 (#6005)
- fix: fix: use correct field for evaluating whether or not GitHub Enterprise is selected (#5987)

### 2.0.2

- fix: enable access to metrics port in embedded network policies (#6277)
- fix: display log streaming error in logs viewer (#6100) (#6273)
- fix: Don't count errored or completed neighbor pods toward resource consumption (#6259)
- fix: Enable kex algo diffie-hellman-group-exchange-sha256 for go-git ssh (#6256)
- fix: copy github app key from repocreds (#6140, #6197)
- fix(ui): UI crashes after reinstalling ArgoCD (#6218)
- fix: add network policies to restrict traffic flow between argocd components (#6156)
- fix: Revert "feat: Add health checks for kubernetes-external-secrets (#5435)"
- chore: Allow ingress traffic to argocd-server by default (#6179)

### 2.0.3

- fix: add missing --container flag to 'argocd app logs' command (#6320)
- fix: grpc web proxy must ensure to read full header (#6319)
- fix: controller should refresh app before running sync operation (#6294)

### 2.0.4

- fix: typo in networkPolicy definition in manifests (#6532)
- fix: allows access to dex metrics from any pod (#6420)
- fix: add client side retry to prevent 'transport is closing' errors (#6402)
- fix: Update documentation Argocd app CRD health with app of apps (#6281)
- fix(ui): Crash on application pod view (#6384)
- chore: pin mkdocs version to fix docs build (#6421)

### 2.0.5

- fix: allow argocd-notification ingress to repo-server (#6746)
- fix: argocd-server crashes due to nil pointer dereference (#6757)
- fix: WebUI failure when loading pod view 't.parentRefs is undefined' (#6490) (#6535)
- fix: prevent 'cannot read property "filter" of undefined' during nodes filtering (#6453)
- fix: download Pod Logs button not honouring argocd-server rootpath (#6548) (#6627)
- fix: upgrade gitops engine to fix workflow health check


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.0.5**, the newest release recorded here for this line.

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
