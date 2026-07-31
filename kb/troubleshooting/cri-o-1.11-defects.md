---
id: TROUBLE-CRI_O_1_11_DEFECTS
type: troubleshooting
title: "cri-o 1.11: defects fixed in the 1.11 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.11.0 <1.12.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cri-o 1.11 known issues
  - cri-o 1.11 fixed in
  - is this cri-o bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cri-o
sources:
  - type: docs
    path: cri-o/cri-o release notes for the 1.11 line — bug-fix entries
    url: https://github.com/cri-o/cri-o/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cri-o 1.11: defects fixed in the 1.11 line

## Summary

**31 defects** the project fixed across **11 releases** of the 1.11 line, from 1.11.0 to
1.11.14. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.11.0

- 7bf9d667 Fix typo in crictl environment variable export
- f51010b9 Fix Conmon timestamps with non-integer-hour offsets
- 6cf08a75 sandbox_run: fix selinux relabel sharing
- 9bf9c82e container_create: more selinux relabel fixes
- d0e48a80 server: fix race between container create and cadvisor asking for info
- da424091 Fix handling of /dev/shm mounting inside of containers
- a5cf1395 network: Fix manage NetworkNS lifecycle
- 1bf96987 test: Fix race condition in ctr.bats
- 446cd49b Fix accidental positive side-effect of RHEL 7.4- bug

### 1.11.1

- 2d62e7b2 Merge pull request #1659 from chavafg/topic/fix-rc-1.11

### 1.11.2

- c2ac3318 Merge pull request #1708 from runcom/fix-caps-error-invalid-1.11

### 1.11.3

- 1a9742bd Merge pull request #1782 from runcom/selinux-fix-privileged-mounts
- e5361d9f Merge pull request #1774 from runcom/fix-image-pull-shadowing

### 1.11.4

- a1770b64 contrib: test: fix up cri-tools repository
- 0e1be2db Merge pull request #1787 from runcom/fix-1.11-k8s-sigs
- b0e2b041 *: fix for repo move over kubernetes-sigs

### 1.11.8

- f8a5beb8 fix containerd-release moved to release-tool

### 1.11.9

- f12e24eff vendor: update storage for a panic fix
- c22b5ef27 Merge pull request #1889 from runcom/fix-nodev-1.11
- 0a771c14c container_create: fix dev mounts and remove nodev from /dev mounts

### 1.11.10

- 5a0142c07 Merge pull request #1912 from runcom/fix-devmapper-111
- b77e711ea vendor: revendor c/storage to fix a devicemapper bug

### 1.11.11

- 276440dd Merge pull request #1958 from giuseppe/fix-another-segfault-1.11
- 9cd8a431 container_server: fix a segfault when the sandbox is not found
- 9272787a Merge pull request #1953 from giuseppe/fix-segfault-on-network-failure-1.11
- acd0b9a9 container: fix potential segfault on setup failure

### 1.11.13

- 62131eab Merge pull request #2184 from openSUSE/release-1.11-oob-log-fix
- 6abfdc01 Fix possible out of bounds access during log parsing
- 62e69f48 Merge pull request #2147 from giuseppe/race-fixes-1.11
- 2a42ce59 container_create: fix race with sandbox being stopped

### 1.11.14

- 9ac5d3fda Merge pull request #2216 from giuseppe/fix-fd-leak


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.11.14**, the newest release recorded here for this line.

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
