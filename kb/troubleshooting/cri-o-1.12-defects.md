---
id: TROUBLE-CRI_O_1_12_DEFECTS
type: troubleshooting
title: "cri-o 1.12: defects fixed in the 1.12 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.12.0 <1.13.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cri-o 1.12 known issues
  - cri-o 1.12 fixed in
  - is this cri-o bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cri-o
sources:
  - type: docs
    path: cri-o/cri-o release notes for the 1.12 line — bug-fix entries
    url: https://github.com/cri-o/cri-o/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cri-o 1.12: defects fixed in the 1.12 line

## Summary

**22 defects** the project fixed across **6 releases** of the 1.12 line, from 1.12.0 to
1.12.10. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.12.0

- 6fd770281 Fix manpage to correctly state default storage driver
- df9f1761a Merge pull request #1744 from giuseppe/fix-reboot
- 6e03ced47 oci: fix segfault if cgroupfs cannot be configured
- 6ceadd83d Merge pull request #1718 from vrothberg/fix-aa-build
- c541e7c6b Merge pull request #1724 from giuseppe/fix-segfault-conmon
- 3c30a2f1b conmon: fix segfault when --log-level is not specified
- 909d63b2e Merge pull request #1716 from runcom/ipv6-fix
- ec7245bef Merge pull request #1707 from runcom/fix-caps-error-invalid
- 1bf8625a3 Merge pull request #1656 from chavafg/topic/fix-rc

### 1.12.1

- 1c5f9c0a6 vendor: update storage for a panic fix
- fe94f7abd Merge pull request #1888 from runcom/fix-nodev-1.12
- 6ebf9960c container_create: fix dev mounts and remove nodev from /dev mounts
- cbbd61391 fix containerd-release moved to release-tool

### 1.12.2

- fa540c8e8 Merge pull request #1913 from runcom/fix-devmapper-112
- 5d1f5b330 vendor: revendor c/storage to fix a devicemapper bug

### 1.12.4

- e4359798 Merge pull request #1959 from giuseppe/fix-another-segfault-1.12
- 92e62a81 container_server: fix a segfault when the sandbox is not found
- 6dc31736 Merge pull request #1954 from giuseppe/fix-segfault-on-network-failure-1.12
- 68519294 container: fix potential segfault on setup failure

### 1.12.7

- 01d348ab container_create: fix RunAsGroup logic

### 1.12.10

- 4e37578a Merge pull request #2148 from giuseppe/race-fixes-1.12
- f7f31279 container_create: fix race with sandbox being stopped


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.12.10**, the newest release recorded here for this line.

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
