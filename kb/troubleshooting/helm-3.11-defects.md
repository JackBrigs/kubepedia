---
id: TROUBLE-HELM_3_11_DEFECTS
type: troubleshooting
title: "helm 3.11: defects fixed in the 3.11 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.11.0 <3.12.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 3.11 known issues
  - helm 3.11 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 3.11 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 3.11: defects fixed in the 3.11 line

## Summary

**21 defects** the project fixed across **4 releases** of the 3.11 line, from 3.11.0 to
3.11.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.11.0

- 3.11.1 is the next patch/bug fix release and will be on February 08, 2023
- Fix improper use of Table request/response to k8s API 472c5736ab01133de504a826bd9ee12cbe4e7904 (Matt Farina)
- Fix after CR 3d81ea22ac74e667b98a26eb80a5d427d75f7009 (Jakub Warczarek)
- Fix User-Agent header in requests made by Helm 2fa7b3d1b7a289690ccc2c820b3329c6b07a1458 (Jakub Warczarek)
- fix adopted resource not replaced 3181c7ddadd2271d67a457522abc13410929b64c (Vaibhav Sharma)
- Resolve conflicts for go.mod and go.sum 6c76abb3df72df415dd54b9a09ce26fcee8fad95 (Soujanya Mangipudi)
- Fix backwards compatibility b6fef6c4665130644acf7742040ebd46f9cc957c (Martin Hickey)
- fix a few function names on comments 09d3f31358882970d02018bd84bcbcd28b47f986 (cui fliter)
- Fix code style ae828ce0ee0f0ad48482cc9fd773c28b137dd23d (Martin Hickey)
- fix: add cases.NoLower option for we can get same effect to strings.Title f0037e5ef6bb118dbcd6e26497014b97436888d6 (wujunwei)
- avoid adding new public function cd76fcd80557490d2f2ee1204b1bdbf78c738ec9 (CI)
- fix tests 32a41fcfac9ca1b4f4997a6660bacba9a01a9d45 (CI)
- fix: clean up temp files in FindChartInAuthAndTLSAndPassRepoURL (#11171) 24fa3d910d774b9d7f40f1fc8002bc1fb55565ca (CI)
- Fix URL with encoded path support for ChartDownloader d9e5bbc09d4d44660fe20df41ce3b567f0336f85 (Mathieu Parent)

### 3.11.1

- 3.11.2 is the next patch/bug fix release and will be on March 08, 2023

### 3.11.2

- 3.11.3 is the next patch/bug fix release and will be on April 12, 2023
- fix template --output-dir issue d44881ddc096444f210e1f4c3e39f95f80723753 (yxxhero)

### 3.11.3

- Fix goroutine leak in perform 548366cb6c91301e595c9093ffd0ec119ca9dad0 (willzgli)
- Fix goroutine leak in action install 4a3a2683536b4d46639dc7460846e44f426e5e01 (Matt Farina)
- Fix 32bit-x86 typo in testsuite 272f6b9d80e35d68efb4e45942aa4d746e2df0f3 (Dirk Müller)
- Fixes Readiness Check for statefulsets using partitioned rolling update. (#11774) 7994bb4d357a3846263dfb22b97da867159253fe (Aman Nijhawan)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.11.3**, the newest release recorded here for this line.

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
