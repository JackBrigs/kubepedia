---
id: TROUBLE-INGRESS_NGINX_1_14_DEFECTS
type: troubleshooting
title: "ingress-nginx 1.14: defects fixed in the 1.14 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.14.0 <1.15.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - ingress-nginx 1.14 known issues
  - ingress-nginx 1.14 fixed in
  - is this ingress-nginx bug already fixed
tags:
  - troubleshooting
  - upgrade
  - ingress-nginx
sources:
  - type: docs
    path: kubernetes/ingress-nginx release notes for the 1.14 line — bug-fix entries
    url: https://github.com/kubernetes/ingress-nginx/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# ingress-nginx 1.14: defects fixed in the 1.14 line

## Summary

**11 defects** the project fixed across **3 releases** of the 1.14 line, from 1.14.0 to
1.14.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.14.0

- Controller: Fix `limit_req_zone` sorting. (#14005)
- Metrics: Fix `nginx_ingress_controller_config_last_reload_successful`. (#13830)
- Docs: Bump mkdocs to v9.6.16, fix links. (#13741)
- Docs: Fix default config values and links. (#13737)
- Controller: Fix nil pointer in path validation. (#13679)
- Controller: Fix SSL session ticket path. (#13665)
- Docs: Fix links and formatting in user guide. (#13654)
- Config/Annotations: Fix `proxy-busy-buffers-size`. (#13610)

### 1.14.1

- Controller: Fix host/path overlap detection for multiple rules. (#14132)

### 1.14.3

- Controller: Fix sync for when host clock jumps to future. (#14451)
- Util: Fix panic for empty `cpu.max` file. (#14448)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.14.3**, the newest release recorded here for this line.

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
