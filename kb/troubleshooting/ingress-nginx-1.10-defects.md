---
id: TROUBLE-INGRESS_NGINX_1_10_DEFECTS
type: troubleshooting
title: "ingress-nginx 1.10: defects fixed in the 1.10 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.10.0 <1.11.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - ingress-nginx 1.10 known issues
  - ingress-nginx 1.10 fixed in
  - is this ingress-nginx bug already fixed
tags:
  - troubleshooting
  - upgrade
  - ingress-nginx
sources:
  - type: docs
    path: kubernetes/ingress-nginx release notes for the 1.10 line — bug-fix entries
    url: https://github.com/kubernetes/ingress-nginx/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# ingress-nginx 1.10: defects fixed in the 1.10 line

## Summary

**17 defects** the project fixed across **7 releases** of the 1.10 line, from 1.10.0 to
1.10.6. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.10.0

- fix datasource, $exported_namespace variable in grafana nginx dashboard (#9092)

### 1.10.1

- Fix admission controller logging of `admissionTime` and `testedConfigurationSize` (#11114)

### 1.10.2

- fix: Ensure changes in MatchCN annotation are detected (#11528)
- Fix helm install on cloud provider admonition block (#11412)
- fix path in file changed detected message (#11286)
- chore: fix function names in comment (#11281)
- fix: update kube version requirement to 1.21 (#11279)
- Fix admission controller logging of `admissionTime` and `testedConfigurationSize` (#11114)

### 1.10.3

- unskip the ocsp tests and update images to fix cfssl bug (#11615)

### 1.10.4

- Controller: Fix panic in alternative backend merging. (#11793)
- Docs: Fix typo in AWS LB Controller reference (#11724)
- Docs: Fix `from-to-www` redirect description. (#11715)

### 1.10.5

- Metrics: Fix namespace in `nginx_ingress_controller_ssl_expire_time_seconds`. (#11985)

### 1.10.6

- GitHub: Fix `exec` in issue template. (#12389)
- Config: Fix panic on invalid `lua-shared-dict`. (#12282)
- Docs: fix limit-rate-after references (#12280)
- [fix] fix nginx temp configs cleanup (#12224)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.10.6**, the newest release recorded here for this line.

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
