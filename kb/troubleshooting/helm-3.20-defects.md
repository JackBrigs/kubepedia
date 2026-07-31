---
id: TROUBLE-HELM_3_20_DEFECTS
type: troubleshooting
title: "helm 3.20: defects fixed in the 3.20 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.20.0 <3.21.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 3.20 known issues
  - helm 3.20 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 3.20 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 3.20: defects fixed in the 3.20 line

## Summary

**18 defects** the project fixed across **3 releases** of the 3.20 line, from 3.20.0 to
3.20.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.20.0

- v3 backport: Fixed a bug where helm uninstall with --keep-history did not suspend previous deployed releases https://github.com/helm/helm/pull/12564
- fix(rollback): `errors.Is` instead of string comp 0cd9a60723d2fde199a625582ff068f5a253886c (Hidde Beydals)
- fix(uninstall): supersede deployed releases 8bb0b372268b45b260593061450f1c9dca9ddbb8 (Hidde Beydals)
- Fix `helm pull` untar dir check with repo urls e5e101cced707693ff7fd26880fd8c537c4297f0 (Luna Stadler)
- [backport] fix: get-helm-3 script use helm3-latest-version bd337b46bcce12bd903dc41c73340940fdcf8dab (George Jenkins)
- Fix deprecation warning 9a366b447452e78b092b1a5267d7efc9bbe74f11 (Benoit Tigeot)
- Avoid "panic: interface conversion: interface {} is nil" 2fe49f99ce39e9a33c77b664a8b9cef6117c1c3b (Benoit Tigeot)
- fix: set repo authorizer in registry.Client.Resolve() ffbc53723a47fe0b47551c35963ef8b7f7523832 (Eric Stroczynski)
- fix null merge f0b699eabba56ef3057561779dc30fafc5c07064 (Ben Foster)

### 3.20.1

- Backport of #31644: Fixed a bug where user-provided nil value was not preserved when chart has an empty map or no default for a key
- Backport of #31601: Fixed a bug where OCI references with tag+digest failed with "invalid byte" error
- fix pulling charts from OCI indices 911f2e908ae40b01ca95b857e94b8894043f64fd (Pedro Tôrres)
- Fix import 45c12f71407b6054a37d3e425d5293ee79a1ab37 (Evans Mungai)
- Fix lint warning 09f5129d49a14c9336cea6f33adf5f52889915ef (Evans Mungai)
- fix(values): preserve nil values when chart default is empty map 5417bfaa84871feae9c8171f192e2f9796475054 (Evans Mungai)

### 3.20.2

- 4.1.5 and 3.20.3 are the next patch (bug fix) releases and will be on April 8, 2026
- fix: Chart dot-name path bug 8fb76d6ab555577e98e23b7500009537a471feee (George Jenkins)
- fix: pin codeql-action/upload-sarif to commit SHA in scorecards workflow 3a8927e275c50cecde273872dad2a5576bd46375 (Terry Howe)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.20.2**, the newest release recorded here for this line.

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
