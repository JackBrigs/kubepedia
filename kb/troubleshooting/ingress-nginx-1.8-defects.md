---
id: TROUBLE-INGRESS_NGINX_1_8_DEFECTS
type: troubleshooting
title: "ingress-nginx 1.8: defects fixed in the 1.8 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.8.0 <1.9.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - ingress-nginx 1.8 known issues
  - ingress-nginx 1.8 fixed in
  - is this ingress-nginx bug already fixed
tags:
  - troubleshooting
  - upgrade
  - ingress-nginx
sources:
  - type: docs
    path: kubernetes/ingress-nginx release notes for the 1.8 line — bug-fix entries
    url: https://github.com/kubernetes/ingress-nginx/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# ingress-nginx 1.8: defects fixed in the 1.8 line

## Summary

**6 defects** the project fixed across **2 releases** of the 1.8 line, from 1.8.0 to
1.8.1. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.8.0

- helm: Fix opentelemetry module installation for daemonset (#9792)
- Correct annotations in monitoring docs (#9976)
- fix: avoid builds and tests for changes to markdown (#9962)

### 1.8.1

- Fix mirror-target values without path separator and port (#9889)
- fix: add canary to sidebar in examples (#10068)
- fix broken kubernetes.io/user-guide/ docs links (#10055)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.8.1**, the newest release recorded here for this line.

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
