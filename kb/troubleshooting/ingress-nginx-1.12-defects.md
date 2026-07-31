---
id: TROUBLE-INGRESS_NGINX_1_12_DEFECTS
type: troubleshooting
title: "ingress-nginx 1.12: defects fixed in the 1.12 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.12.0 <1.13.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - ingress-nginx 1.12 known issues
  - ingress-nginx 1.12 fixed in
  - is this ingress-nginx bug already fixed
tags:
  - troubleshooting
  - upgrade
  - ingress-nginx
sources:
  - type: docs
    path: kubernetes/ingress-nginx release notes for the 1.12 line — bug-fix entries
    url: https://github.com/kubernetes/ingress-nginx/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# ingress-nginx 1.12: defects fixed in the 1.12 line

## Summary

**13 defects** the project fixed across **6 releases** of the 1.12 line, from 1.12.0 to
1.12.8. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.12.0

- GitHub: Fix `exec` in issue template. (#12387)
- Config: Fix panic on invalid `lua-shared-dict`. (#12283)
- [fix] fix nginx temp configs cleanup (#12225)
- Metrics: Fix namespace in `nginx_ingress_controller_ssl_expire_time_seconds`. (#10274)
- Controller: Fix panic in alternative backend merging. (#11789)
- unskip the ocsp tests and update images to fix cfssl bug (#11606)

### 1.12.1

- fix DNS issues with unresolvable backends with ExternalName (#12951)

### 1.12.3

- Lua: Fix `ExternalName` services without endpoints. (#13429)
- Fix 🐛: Markdown requires nested content inside a list item to be indented (#13390)

### 1.12.5

- Controller: Fix nil pointer in path validation. (#13682)
- Controller: Fix SSL session ticket path. (#13668)

### 1.12.6

- Metrics: Fix `nginx_ingress_controller_config_last_reload_successful`. (#13859)

### 1.12.8

- Controller: Fix `limit_req_zone` sorting. (#14007)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.12.8**, the newest release recorded here for this line.

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
