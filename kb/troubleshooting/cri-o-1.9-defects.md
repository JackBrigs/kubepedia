---
id: TROUBLE-CRI_O_1_9_DEFECTS
type: troubleshooting
title: "cri-o 1.9: defects fixed in the 1.9 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.9.0 <1.10.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cri-o 1.9 known issues
  - cri-o 1.9 fixed in
  - is this cri-o bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cri-o
sources:
  - type: docs
    path: cri-o/cri-o release notes for the 1.9 line — bug-fix entries
    url: https://github.com/cri-o/cri-o/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cri-o 1.9: defects fixed in the 1.9 line

## Summary

**23 defects** the project fixed across **9 releases** of the 1.9 line, from 1.9.0 to
1.9.16. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.9.0

- e572043a6 Merge pull request #1213 from runcom/fix-deps-1.9
- a85ea609d Merge pull request #1207 from runcom/fix-exec-termianl
- afeab27a3 container_exec: fix terminal true process json
- 989d275e7 Merge pull request #1170 from alexandrst88/fix-tutorial
- 2cae11ba3 Merge pull request #1189 from runcom/fix-apparmor-master
- c8aad704d container_create: fix apparmor from container config
- b2a78eba2 Merge pull request #1185 from runcom/fix-runtime-deps
- 4a32d0ff3 Merge pull request #1183 from runcom/fix-image-pull-master
- 070b8bfdc Merge pull request #1176 from runcom/fix-e2e-1.0
- 7508cdeac Merge pull request #1173 from runcom/fix-cve
- 67e2d28c8 Merge pull request #1171 from WeiZhang555/fix-readme
- 21252ed22 Merge pull request #1151 from mdshuai/fix-test-typo

### 1.9.2

- 01631617a sandbox: fix sandbox logPath when crio restarts

### 1.9.4

- b79bd2d1 Merge pull request #1338 from nalind/fix-runasuser-1.9-cache

### 1.9.5

- b79bd2d1 Merge pull request #1338 from nalind/fix-runasuser-1.9-cache

### 1.9.7

- a68f7b55 Merge pull request #1357 from runcom/netns-fixes

### 1.9.11

- 475af0a1 test: Fix race condition in ctr.bats

### 1.9.13

- a4d6f38a4 Merge pull request #1540 from runcom/status-fix-1.9

### 1.9.14

- 88f17a22 Merge pull request #1618 from runcom/fix-race-cadvisor-create-19
- 93351e93 server: fix race between container create and cadvisor asking for info

### 1.9.16

- 7155a7596 Merge pull request #2182 from openSUSE/release-1.9-oob-log-fix
- 1b650eb8f Fix possible out of bounds access during log parsing
- dbf5c04e1 container_create: fix race with sandbox being stopped


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.9.16**, the newest release recorded here for this line.

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
