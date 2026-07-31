---
id: TROUBLE-INGRESS_NGINX_1_9_DEFECTS
type: troubleshooting
title: "ingress-nginx 1.9: defects fixed in the 1.9 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.9.0 <1.10.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - ingress-nginx 1.9 known issues
  - ingress-nginx 1.9 fixed in
  - is this ingress-nginx bug already fixed
tags:
  - troubleshooting
  - upgrade
  - ingress-nginx
sources:
  - type: docs
    path: kubernetes/ingress-nginx release notes for the 1.9 line — bug-fix entries
    url: https://github.com/kubernetes/ingress-nginx/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# ingress-nginx 1.9: defects fixed in the 1.9 line

## Summary

**11 defects** the project fixed across **3 releases** of the 1.9 line, from 1.9.0 to
1.9.5. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.9.0

- Deployment/DaemonSet: Fix templating & value. (#10240)
- fix: remove curl on base container #9716 (#10306)
- fix: path with special characters warning #10281 #10308 (#10330)
- chore(build): Fix Run make dev-env syntax error (#10294)
- Fix “dev-env” Makefile target to work with kubectl 1.28+ (#10350)
- fix: update action file to auto release plugin #10197 (#10321)
- ci(helm): fix Helm Chart release action 422 error (#10237)

### 1.9.4

- Cherry pick fcgi fix and release v1.9.4 (#10544)

### 1.9.5

- fix: remove tcpproxy copy error handling (#10715)
- fix: adjust unfulfillable validation check for session-cookie-samesite annotation (#10604)
- fix: Validate x-forwarded-prefix annotation with RegexPathWithCapture (#10603)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.9.5**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `kubernetes/ingress-nginx`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/ingress-nginx.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
