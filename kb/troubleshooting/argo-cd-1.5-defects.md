---
id: TROUBLE-ARGO_CD_1_5_DEFECTS
type: troubleshooting
title: "argo-cd 1.5: defects fixed in the 1.5 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.5.0 <1.6.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - argo-cd 1.5 known issues
  - argo-cd 1.5 fixed in
  - is this argo-cd bug already fixed
tags:
  - troubleshooting
  - upgrade
  - argo-cd
sources:
  - type: docs
    path: argoproj/argo-cd release notes for the 1.5 line — bug-fix entries
    url: https://github.com/argoproj/argo-cd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# argo-cd 1.5: defects fixed in the 1.5 line

## Summary

**52 defects** the project fixed across **7 releases** of the 1.5 line, from 1.5.0 to
1.5.8. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.5.0

- Fixed bug that prevents automatically update Helm chart when new version is published (#3193)
- feat: Disable Admin Login (fixes #3019) (#3179)
- fix: app reconciliation fails with panic: index out of (#3233)
- fix: upgrade argoproj/pkg version to fix leaked sensitive information in logs (#3230)
- fix: set MaxCallSendMsgSize to MaxGRPCMessageSize for the GRPC caller (#3117)
- fix: dex proxy should forward request to dex preserving the basehref (#3165)
- fix: set default login redirect to baseHRef (#3164)
- fix: don't double-prepend basehref to redirect URLs (fixes #3137)
- fix: ui referring to /api/version using absolute path (#3092)
- fix: Unhang UI on long app info items by using more sane URL match pattern (#3159)
- fix: Allow multiple hostnames per SSH known hosts entry and also allow IPv6 (#2814) (#3074)
- fix: argocd-util backup produced truncated backups. import app status (#3096)
- fix: upgrade redis-ha chart and enable haproxy (#3147)
- fix: make dex server deployment init container resilient to restarts (#3136)
- fix: redact secret values of manifests stored in git (#3088)
- fix: HTTP|HTTPS|NO_PROXY env variable reading #3055 (#3063)
- fix: Correct usage text for repo add command regarding insecure repos (#3068)
- fix: Ensure SSH private key is written out with a final newline character (#2890) (#3064)
- fix: Handle SSH URLs in 'git@server:org/repo' notation correctly (#3062)
- fix sso condition when several sso connectors has been configured (#3057)
- fix: Fix bug where the same pointer is used. (#3059)
- fix: Opening in new tab bad key binding on Linux (#3020)
- fix: K8s secrets for repository credential templates are not deleted when credential template is deleted (#3028)
- fix: SSH credential template not working #3016
- fix: Unable to parse kubectl pre-release version strings (#3034)
- fix: Jsonnet TLA parameters of same type are overwritten (#3022)
- fix: Replace aws-iam-authenticator to support IRSA (#3010)
- fix: SSH repo URL with a user different from `git` is not matched correctly when resolving a webhook (#2988)
- fix: JWT invalid => Password for superuser has changed since token issued (#2108)

### 1.5.1

- fix: return 401 error code if username does not exist (#3369)
- fix: Do not panic while running hooks with short revision (#3368)
- fix: Increase HAProxy check interval to prevent intermittent failures (#3356)

### 1.5.3

- fix: 'argocd sync' does not take into account IgnoreExtraneous annotation (#3486)
- fix: CLI renders flipped diff results (#3480)
- fix: GetApplicationSyncWindows API should not validate project permissions (#3456)
- fix: argocd-util kubeconfig should use RawRestConfig to export config (#3447)
- fix: javascript error on accounts list page (#3453)
- fix: support both <group>/<kind> as well as <kind> as a resource override key (#3433)
- fix: Updating to jsonnet v1.15.0 fix issue #3277 (#3431)
- fix for helm repo add with flag --insecure-skip-server-verification (#3420)
- fix: app diff --local support for helm repo. #3151 (#3407)
- fix: Syncing apps incorrectly states "app synced", but this is not true (#3286)
- fix: for jsonnet when it is located in nested subdirectory and uses import (#3372)
- fix: Update 4.5.3 redis-ha helm manifest (#3370)
- fix: return 401 error code if username does not exist (#3369)
- fix: Do not panic while running hooks with short revision (#3368)

### 1.5.5

- fix: enable redis retries; add redis request duration metric (#3547)
- fix: when --rootpath is on, 404 is returned when URL contains encoded URI (#3564)

### 1.5.6

- fix: Prevent possible nil pointer dereference when getting Helm client (#3613)
- fix: avoid deadlock in settings manager (#3637)

### 1.5.7

- fix: application with EnvoyFilter causes high memory/CPU usage (#3719)

### 1.5.8

- fix: html encode login error/description before rendering it (#3773)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.5.8**, the newest release recorded here for this line.

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
