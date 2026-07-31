---
id: TROUBLE-HELM_3_0_DEFECTS
type: troubleshooting
title: "helm 3.0: defects fixed in the 3.0 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.0.0 <3.1.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 3.0 known issues
  - helm 3.0 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 3.0 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 3.0: defects fixed in the 3.0 line

## Summary

**26 defects** the project fixed across **3 releases** of the 3.0 line, from 3.0.1 to
3.0.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.0.1

- chart_downloader: fix lint issue. 7c22ef9ce89e0ebeb7125ba2ebf7d421f3e82ffa (Andreas Stenius)
- fix(plugin): Avoid crash on missing flag 530c5a55835fe572b08c91ac4c8d978f9fd9610a (Marc Khouzam)
- fix "Chart.lock is out of sync with Chart.yaml" (#7119) 5c9befa75d77a4bb37c3ac9f3d35e651087c1a46 (海的澜色)
- fix stack overflow error (#7114) eea01af8f972dffec6fef3d6337c72259060d683 (海的澜色)
- fix: ignore pax header files in chart validation 767c9aeacee89570b7c7436fb88a47293c9699ba (chloel)
- fix(cli): helm list was ignoring some errors 00465540402994561171c37af8743eb9a19e28a6 (Marc Khouzam)
- fix: change error message to contain correct field name af1c07015d8aa2d134589d8a306a1740a6632db6 (Daniel Strobusch)
- fix(plugin): Avoid duplication of flag list 80e6ce6b2d701cbe70afd49614a1d458aef25201 (Marc Khouzam)
- fix(plugin): Add missing -n known flag 27b0442252af557ec86c127a339af1f3ed9d0610 (Marc Khouzam)
- fix(cli): IsReachable check for "get values" da496234a85938721a1704e55fb74e53d4ba363b (Marc Khouzam)
- fix(lint): Remove requirement that directory name and chart name match 73074769a4c639e83e0d43ebff4a7bd53eec0f44 (Scott Morgan)
- fix(lint): Remove requirement that directory name and chart name match 5c4125f88a839c4ead411ce8a3002a0f79ac1998 (Scott Morgan)

### 3.0.2

- fix(kube): Port use of watcher with retries to wait for resources (#7217) 19e47ee3283ae98139d98460de796c1be1e3975f (Martin Hickey)
- fix(cmd): Add message about deprecated chart (#6889) b88a28a25feb55829649ef14c43fb27f6fda79bf (kvendingoldo)
- fix(*): Helm v3 handling of APIVersion v1 charts dependencies (#7009) 8c283e8706ce19c0f19226344854906596414fcf (Paul "TBBle" Hampson)
- fix: stop discovery errors from halting chart rendering. 7f6da66ae80862eeea0de3acce32ad9453692674 (Matt Butcher)

### 3.0.3

- Signed-off-by: Ahmad Kazemi <ahmad.kazemi@recordpoint.com> log.Printf replaced to fix the log issue. bba7bc1c88ec045199b66fe88b1468a6a17102a3 (Ahmad Kazemi)
- fix(package): remove --set, --values, etc. flags cde43f8d9e4d9318c29c5e1f16c4cfd67a356f53 (Matthew Fisher)
- fix(chartutil): remove empty lines and a space from rendered chart templates (#7455) ee8c924115cf55b1446ff4be9e9609a105d45c75 (Shota Nakamura)
- fix(helm): improve handling of corrupted storage d3836d6f74bfe6ada6d992868561159b66396cd3 (Cristian Klein)
- Fix: helm3 - kind sorter incorrectly compares unknown and namespace 86839f249031c348412409565b05f7ca5b3e3eab (Bradley Skuse)
- Fix a typo "update" -> "updates" (#7346) d2cf1284ee75954ffedaba8af5d8339b68e72368 (Hu Shuai)
- fix(cmd): Fixes logging on action conf init error (#6909) 64e57d92b649a67f222bff23582b5d665b639791 (Jorge I. Gasca)
- fix(comp): tail cannot open +2 for reading 50a647728f78925802abfa4d06bb41a4c52ade05 (Frank Lin PIAT)
- Add back fix for CRD patch creation 4771f256cdaac056a6553af42cfa3ffac5b7896c (Adrian Gonzalez-Martin)
- Port PR #4161 Fix incorrect timestamp when helm package to Helmv3 d72867582536615c311e39578dcdf65421ed9de4 (Romain Grenet)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.0.3**, the newest release recorded here for this line.

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
