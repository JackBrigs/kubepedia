---
id: TROUBLE-INGRESS_NGINX_1_11_DEFECTS
type: troubleshooting
title: "ingress-nginx 1.11: defects fixed in the 1.11 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.11.0 <1.12.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - ingress-nginx 1.11 known issues
  - ingress-nginx 1.11 fixed in
  - is this ingress-nginx bug already fixed
tags:
  - troubleshooting
  - upgrade
  - ingress-nginx
sources:
  - type: docs
    path: kubernetes/ingress-nginx release notes for the 1.11 line — bug-fix entries
    url: https://github.com/kubernetes/ingress-nginx/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# ingress-nginx 1.11: defects fixed in the 1.11 line

## Summary

**17 defects** the project fixed across **7 releases** of the 1.11 line, from 1.11.0 to
1.11.7. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.11.0

- fix: Ensure changes in MatchCN annotation are detected (#11529)
- Chart: Fix `IngressClass` annotations. (#11416)
- Fix helm install on cloud provider admonition block (#11394)
- fix path in file changed detected message (#11271)
- fix: update kube version requirement to 1.21 (#11275)
- Fix admission controller logging of `admissionTime` and `testedConfigurationSize` (#11089)
- [mTLS] Fix acme verification when mTLS and Client CN verification is enabled (#11062)

### 1.11.1

- unskip the ocsp tests and update images to fix cfssl bug (#11616)
- fix: Ensure changes in MatchCN annotation are detected (#11529)

### 1.11.2

- Controller: Fix panic in alternative backend merging. (#11794)

### 1.11.3

- Metrics: Fix namespace in `nginx_ingress_controller_ssl_expire_time_seconds`. (#11986)

### 1.11.4

- GitHub: Fix `exec` in issue template. (#12388)
- Config: Fix panic on invalid `lua-shared-dict`. (#12284)
- [fix] fix nginx temp configs cleanup (#12223)

### 1.11.5

- fix DNS issues with unresolvable backends with ExternalName (#12952)

### 1.11.7

- Lua: Fix `ExternalName` services without endpoints. (#13430)
- Fix 🐛: Markdown requires nested content inside a list item to be indented (#13391)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.11.7**, the newest release recorded here for this line.

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
