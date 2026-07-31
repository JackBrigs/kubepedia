---
id: TROUBLE-CRI_O_1_0_DEFECTS
type: troubleshooting
title: "cri-o 1.0: defects fixed in the 1.0 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.0.0 <1.1.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cri-o 1.0 known issues
  - cri-o 1.0 fixed in
  - is this cri-o bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cri-o
sources:
  - type: docs
    path: cri-o/cri-o release notes for the 1.0 line — bug-fix entries
    url: https://github.com/cri-o/cri-o/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cri-o 1.0: defects fixed in the 1.0 line

## Summary

**19 defects** the project fixed across **8 releases** of the 1.0 line, from 1.0.1 to
1.0.9. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.0.1

- d8aaba71 Merge pull request #1045 from runcom/fix-host-pid-v1
- 3a504024 Merge pull request #1040 from runcom/fix-process-exec-v1
- a45c16d7 fix host pid handling for containers and share uts ns
- a2ab0a5e Merge pull request #1047 from runcom/fix-e2e-v1
- 5f826acf Merge pull request #1033 from runcom/fix-stop-1.0
- 9b797f0c oci: fixes to properly handle container stop action
- bb737b91 Merge pull request #1022 from runcom/fix-version-rel-1
- 7efdae80 version: fix version handling and kube info

### 1.0.2

- c31d1d15 Merge pull request #1093 from runcom/makefile-fixes-v1
- 1544488a Merge pull request #1084 from lsm5/release-1.0-unitfile-fixes

### 1.0.3

- 66586603b Merge pull request #1121 from runcom/carry-logs-fix-v1
- d54ad9465 Merge pull request #1099 from runcom/makefile-fixes-v1

### 1.0.4

- 8a39d94a0 Merge pull request #1134 from runcom/fix-cve-2017-14992

### 1.0.6

- dd571523ecde501ede49a9d6dd5e39efcee9ec20 image_pull: fix image resolver
- 3078f5906 Merge pull request #1175 from runcom/fix-cve-1.0

### 1.0.7

- c30571b43 Merge pull request #1182 from runcom/fix-image-pull-v1

### 1.0.8

- 111988640 Merge pull request #1210 from runcom/fix-exec-1.7
- 327d8b327 container_exec: fix terminal true process json

### 1.0.9

- 0f7d5d583 cmd/crio: fix listen address dir creation


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.0.9**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `cri-o/cri-o`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/cri-o.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
