---
id: TROUBLE-HELM_3_12_DEFECTS
type: troubleshooting
title: "helm 3.12: defects fixed in the 3.12 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.12.0 <3.13.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 3.12 known issues
  - helm 3.12 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 3.12 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 3.12: defects fixed in the 3.12 line

## Summary

**13 defects** the project fixed across **3 releases** of the 3.12 line, from 3.12.0 to
3.12.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.12.0

- 3.12.1 is the next patch/bug fix release and will be on June 14, 2023
- Fix goroutine leak in action install 7c9d636f40e751c775cd1baea5ef2fd4f7139f6e (Matt Farina)
- fix quiet lint does not fail on non-linting errors 853c18002f51cbdc62011bf14b361362dd6a82d0 (Joe Julian)
- Fixes Readiness Check for statefulsets using partitioned rolling update. (#11774) eea2f27babb0fddd9fb1907f4d8531c8f5c73c66 (Aman Nijhawan)
- fix: failed testcase on windows 878e962b23ece82d2fd42fc66f01dcabaa6e8b45 (wujunwei)
- Fix 32bit-x86 typo in testsuite 1fc836935684cd7505b481f2e9f3182ac23814a3 (Dirk Müller)
- Fix goroutine leak in perform 11150cdcc6bb69b62ec88faa523d9ff6727e8be7 (willzgli)
- Fix improper use of Table request/response to k8s API 36e18fa6e16049b5e5ec8ca4f9fefd76e6abd212 (Matt Farina)
- fix template --output-dir issue 1c25a1fadd1f5f11fae9ea85f981ba0947ac97cb (yxxhero)

### 3.12.1

- 3.12.2 is the next patch/bug fix release and will be on July 12, 2023
- fix comment grammar error. 91bb1e34e605a2bfc3fbc4de14921e071af84fd7 (wujunwei)
- fix(search): print repo search result in original case 5b19d8eedb24691a035f1d1f1d42cb0cdde97813 (Höhl, Lukas)

### 3.12.2

- 3.12.3 is the next patch/bug fix release and will be on August 9, 2023


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.12.2**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `helm/helm`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/helm.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
