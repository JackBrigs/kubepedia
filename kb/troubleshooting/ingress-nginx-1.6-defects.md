---
id: TROUBLE-INGRESS_NGINX_1_6_DEFECTS
type: troubleshooting
title: "ingress-nginx 1.6: defects fixed in the 1.6 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.6.0 <1.7.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - ingress-nginx 1.6 known issues
  - ingress-nginx 1.6 fixed in
  - is this ingress-nginx bug already fixed
tags:
  - troubleshooting
  - upgrade
  - ingress-nginx
sources:
  - type: docs
    path: kubernetes/ingress-nginx release notes for the 1.6 line — bug-fix entries
    url: https://github.com/kubernetes/ingress-nginx/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# ingress-nginx 1.6: defects fixed in the 1.6 line

## Summary

**9 defects** the project fixed across **1 releases** of the 1.6 line, from 1.6.4 to
1.6.4. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.6.4

- Fix incorrect annotation name in upstream hashing configuration (#9617)
- fix(grafana-dashboard): remove hardcoded namespace references (#9523)
- Fix indentation on serviceAccount annotation (#9129)
- avoid builds and tests for non-code changes (#9392)
- [user-guide configmap] fix doc for global-auth-snippet (#9372)
- fix: missing CORS headers when auth fails (#9251)
- Fix styling in canary annotation docs. (#9259)
- fix(hpa): deprecated api version, bump to v2 (#9348)
- Fixed indentation in commented-out autoscaling (#9225)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.6.4**, the newest release recorded here for this line.

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
