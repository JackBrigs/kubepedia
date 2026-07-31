---
id: TROUBLE-HELM_3_9_DEFECTS
type: troubleshooting
title: "helm 3.9: defects fixed in the 3.9 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.9.0 <3.10.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 3.9 known issues
  - helm 3.9 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 3.9 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 3.9: defects fixed in the 3.9 line

## Summary

**26 defects** the project fixed across **4 releases** of the 3.9 line, from 3.9.0 to
3.9.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.9.0

- 3.9.1 will contain only bug fixes and will be released on June 8, 2022
- Fix --untardir reference in --destination description 41ccf7b5aba9677573952ba4b4a47be5f0170525 (Simon Alling)
- Fix confusing test failure message 56e52d139c27b43397c567ecc31aea1ce0e73b5d (Simon Alling)
- fix: "... has no deployed releases" error when release history contains only failed releases and history limit reached da8e7d25329f9539cf034588d5638099fd69fda9 (Timofey Kirillov)
- repo: fix repo merge unit test 7a08426869abd4c0bcfe09081c337bdb2bab909a (Markus Lehtonen)
- fix: run 'go mod tidy' for go 1.17 45af381aa4890a1306d56c5b5082390eb3bb248e (Theo Chupp)
- maint: fix syntax error in deploy.sh 75fa221b75326f7ef1815281534b4887dc122c9e (Josh Dolitsky)
- linting issue fixed cfeb431e3c52d59f2bd1853f66bab042f208e989 (Sourik Ghosh)
- Avoid querying for OCI tags can explicit version provided in chart dependencies 01ff5bb00de47709f3c386b28077141df4d1032a (Andrew Block)
- fix: remove deadcode e97c436a8679fa8d5b62e8582249faf0c79e170f (Tomas Pizarro Moreno)
- fix: helm package tests 0963617b9b0100f8b84cde0037be02abe9628b23 (Tomas Pizarro Moreno)
- fix: helm package with dependency update for charts with OCI dependencies e02aeab0e9babe9b16f31362746b5e70790f6e7f (Tomas Pizarro Moreno)
- fix: support empty args with --post-renderer-args 1a7a73b47bd1b0475422211dbacd0d22c99e2394 (guofutan)
- fix: fix args name in postrender/exec_test.go and error if order in postRendererArgsSlice 04e79e936d59d953339cc5b283327bb4b6a64f2d (guofutan)
- fix: change postRendererArgs to Slice Type and use args... d12170b3f20f287268283f2809da751a14f2d743 (guofutan)
- fix: keep the API: postrender.NewExec and Add NewExecWithArgs 44423fb2ca59547968b1028427b5ea0c3176d5a8 (guofutan)
- fix: keep the API: postrender.NewExec and Add NewExecWithArgs 1aab7eb3a1046731d55c14b302bd35fcc4da1140 (guofutan)
- Fix install memory/goroutine leak 5059ae843ef6b504fe55f914953e249a14ff5838 (Neven Miculinic)
- fix(rollback): fix helm rollback doesn't have meta.helm.sh annotations 94dc605968758a63067eceb4978d2347194d2c5b (cndoit18)
- Make validation errors easier to fix 65ec3d6fd6e88f100216edbde789ed8417d1a87f (Damien Nozay)
- fix tarFromLocalDir saving file dependencies in dest path adfb52eda508b80a854da34dd7978d480d46e345 (Matthew Fisher)
- Fix value precedence c4952c9c8c5fce29635b9795b6070f616a31615c (Aram Zegerius)

### 3.9.1

- 3.9.2 will contain only bug fixes will be on August 10, 2022
- fix: improve logging & safety of statefulSetReady 06f449dd762e54f5d6c1245c1ec306182d1a16d7 (Dominic Evans)

### 3.9.2

- 3.9.3 will contain only bug fixes will be on August 10, 2022

### 3.9.3

- fixes #11142 missing array length check on release c801d8876a6fc9c9a5bfa15f31892e16cd30c7bd (Arvid E. Picciani)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.9.3**, the newest release recorded here for this line.

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
