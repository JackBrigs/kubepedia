---
id: TROUBLE-INGRESS_NGINX_1_13_DEFECTS
type: troubleshooting
title: "ingress-nginx 1.13: defects fixed in the 1.13 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.13.0 <1.14.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - ingress-nginx 1.13 known issues
  - ingress-nginx 1.13 fixed in
  - is this ingress-nginx bug already fixed
tags:
  - troubleshooting
  - upgrade
  - ingress-nginx
sources:
  - type: docs
    path: kubernetes/ingress-nginx release notes for the 1.13 line — bug-fix entries
    url: https://github.com/kubernetes/ingress-nginx/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# ingress-nginx 1.13: defects fixed in the 1.13 line

## Summary

**16 defects** the project fixed across **6 releases** of the 1.13 line, from 1.13.0 to
1.13.7. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.13.0

- Docs: Fix function names in comments. (#13517)
- Lua: Fix `ExternalName` services without endpoints. (#13154)
- Fix 🐛: Markdown requires nested content inside a list item to be indented (#13388)
- Docs: Fix link in installation instructions. (#13190)
- fix DNS issues with unresolvable backends with ExternalName (#10989)

### 1.13.1

- Docs: Bump mkdocs to v9.6.16, fix links. (#13743)
- Docs: Fix default config values and links. (#13738)
- Controller: Fix nil pointer in path validation. (#13681)
- Controller: Fix SSL session ticket path. (#13667)
- Docs: Fix links and formatting in user guide. (#13661)
- Config/Annotations: Fix `proxy-busy-buffers-size`. (#13638)

### 1.13.2

- Metrics: Fix `nginx_ingress_controller_config_last_reload_successful`. (#13860)

### 1.13.4

- Controller: Fix `limit_req_zone` sorting. (#14006)

### 1.13.5

- Controller: Fix host/path overlap detection for multiple rules. (#14131)

### 1.13.7

- Controller: Fix sync for when host clock jumps to future. (#14450)
- Util: Fix panic for empty `cpu.max` file. (#14449)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.13.7**, the newest release recorded here for this line.

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
