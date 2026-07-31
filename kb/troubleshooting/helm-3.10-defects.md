---
id: TROUBLE-HELM_3_10_DEFECTS
type: troubleshooting
title: "helm 3.10: defects fixed in the 3.10 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.10.0 <3.11.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 3.10 known issues
  - helm 3.10 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 3.10 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 3.10: defects fixed in the 3.10 line

## Summary

**18 defects** the project fixed across **4 releases** of the 3.10 line, from 3.10.0 to
3.10.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.10.0

- 3.10.1 will contain only bug fixes and be released on October 12, 2022
- fix special string in the filename ece46c1d3a44e5f90cca0cbb96ae302dc47885cb (d-d-up)
- fixes #11142 missing array length check on release b9f347a574851d01f058663d7b65a108b9f980bc (Arvid E. Picciani)
- fix: use `go install` instead of `go get` aa6e82bac8db0b50766c03276dd0fed1bba6208c (Matthew Fisher)
- fix: improve logging & safety of statefulSetReady 7c74f1dd027709156c3345e1965693f04b8dd9ac (Dominic Evans)
- Fixed helm uninstall not deleting the resource. fe00c9296d50acc490dd08cd95eb014d37409716 (Mayank Thakur)
- Fix UT d8c0e01132705b427d27835f9d3e2e8bb3e4da22 (stan-sz)
- fix --registry-config issue 9f199b6517c21394bca555983c70fc232d65014c (yxxhero)
- fix(helm): ignore file-not-found error for `helm repo list -o json` 94779dc99f266adde81882412ee944072da3b136 (Teo Klestrup Röijezon)

### 3.10.1

- 3.10.2 will contain only bug fixes and be released on November 9, 2022
- avoid adding new public function 75a1369794499daa7223271996781cadaf2c1adf (CI)
- fix tests 959acd8a1da38d33b5069f083a040fa237c04bfd (CI)
- fix: clean up temp files in FindChartInAuthAndTLSAndPassRepoURL (#11171) f6830f7b0ab91909454fbdc476b4e760d6525abc (CI)
- Fix URL with encoded path support for ChartDownloader 4e075315f81311372568d73f2c929577d10c0de2 (Mathieu Parent)
- fix: add cases.NoLower option for we can get same effect to strings.Title 48444319694a4b6110541ef7bfea9a8627c1aa39 (wujunwei)

### 3.10.2

- 3.10.3 will contain only bug fixes and be released on December 14, 2022
- fix a few function names on comments 50f003e5ee8704ec937a756c646870227d7c8b58 (cui fliter)

### 3.10.3

- Fix backwards compatibility 835b7334cfe2e5e27870ab3ed4135f136eecc704 (Martin Hickey)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.10.3**, the newest release recorded here for this line.

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
