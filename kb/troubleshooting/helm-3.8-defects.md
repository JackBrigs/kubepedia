---
id: TROUBLE-HELM_3_8_DEFECTS
type: troubleshooting
title: "helm 3.8: defects fixed in the 3.8 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.8.0 <3.9.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 3.8 known issues
  - helm 3.8 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 3.8 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 3.8: defects fixed in the 3.8 line

## Summary

**32 defects** the project fixed across **3 releases** of the 3.8 line, from 3.8.0 to
3.8.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.8.0

- 3.8.1 will contain only bug fixes and be released on March 09, 2022
- Fix panic with OCI for install, upgrade, and show 548ec55cf9ee54f8563c2848b9f9fd33b8753936 (Matt Farina)
- Fix linting ba4020770ec21286dbf9cb4b6c6c82b42ee8d4d3 (Scott Rigby)
- Fixed bad commit 9c3b0008896d840237617bae8cc9823b77b536d4 (Andrew Block)
- Fix import 4c8a3faaa28e67316297d68fcb1cca0a54a8ae56 (Scott Rigby)
- Fix Trim to TrimPrefix 1fabbabae9fd0c76fccf2a6658de867d8cf96ab9 (Scott Rigby)
- Add OCI tag verions to the Dependency object before Resolve. TODO: fix HTTP HTTPS error for local registries e3f2fb42357fbe67257b0eeacd82cb6cba98c7c1 (Scott Rigby)
- Fix typo. Thanks buildbot. Also comments at 80 chars 157ac85ab72827062b963a99ab7990c31804c5dd (Scott Rigby)
- Fix memory leak in upgrade action ad3d2cc8efc12e2aa7a0144ed4a11169193646e3 (Jerome Küttner)
- fix(pkg/kube): statefulSetReady: handle partition cases correctly c3310bb72496e97237008f5f9fafa52f5d7d69a9 (Bhavin Gandhi)
- Fix specifying of Kubernetes version from build scripts 7838fb769d00f53c858d994a873f42c2960a7d25 (Matt Farina)
- fix: added resource info into the validation error 7f68bfa1fa9146b0fcc0cb6b30a50f6df40cc7ff (Timofey Kirillov)
- fix a SIGSEGV similar to issue 1347 fe6f348490f32d5dab3173e037626b8f12cd431c (Brandon Cole)
- Fix a golint issue caused by typo 9b7a45a384dff68c96e0811e267cebfbe6b6ac2f (Guangwen Feng)
- fix(helm): process dependencies import-values 1931b0702dd7f0d19a66ddd9b882d62e7622943d (Stuart Drennan)
- docs: fix typo Charts.yaml 5753f61ae35c2507b3116d84662d45f51cfa2099 (Alexey Igrychev)
- Fix default registry config path of oci protocol provider 52cbc2f49c0f2e1675783f04b1426166419da46c (Kai Takac)
- Make validation errors easier to fix 9fa373e8be0a6f4f3d25be91a6c7be874f7714ac (Damien Nozay)
- fix tarFromLocalDir saving file dependencies in dest path d2dd32470b312095e8c7399146bc684b89ffeaa6 (Matthew Fisher)
- fix(install): if subcharts are disabled, the CRD for subcharts should not be installed da15d96a680111a09f0436b19afb07fd9895fa02 (cndoit18)

### 3.8.1

- 3.8.2 will contain only bug fixes and will be released on April 13, 2022
- fix: remove deadcode 952d034ed0d4e48f64e894ecc96712a2b5a6ad8f (Tomas Pizarro Moreno)
- fix: helm package tests 02028a27a88d2a800a6ffc95163246987e5754dc (Tomas Pizarro Moreno)
- fix: helm package with dependency update for charts with OCI dependencies bc3d14cbc5399fcce1aa739a15a7a02416cf6133 (Tomas Pizarro Moreno)
- Fix typo Unset the env var before func return in Unit Test 9499df01bbc5eff5a463045977918f714d79a0c5 (Kay Yan)
- maint: fix syntax error in deploy.sh 7663ffa87b5294152152c9a1b0d8b424dcd51952 (Josh Dolitsky)
- linting issue fixed 803ecb837a5f842f57f3a9a86788e468469d9fcc (Sourik Ghosh)
- Avoid querying for OCI tags can explicit version provided in chart dependencies 3aacde171ef8504c431e783c25a01de0d1776801 (Andrew Block)
- Fix install memory/goroutine leak 4827ca1f167937f9599ad2486e43ce3914192f43 (Neven Miculinic)

### 3.8.2

- Make validation errors easier to fix 7df8251760085ba247fce49415e2be20e6f08ab7 (Damien Nozay)
- fix tarFromLocalDir saving file dependencies in dest path bd77989fb14b017880fde4bf842c7fa459b13f0a (Matthew Fisher)
- Fix value precedence 5d017e11f1f47345a3559bf70f63d81a7edc981a (Aram Zegerius)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.8.2**, the newest release recorded here for this line.

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
