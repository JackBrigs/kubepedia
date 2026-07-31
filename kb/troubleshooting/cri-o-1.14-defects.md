---
id: TROUBLE-CRI_O_1_14_DEFECTS
type: troubleshooting
title: "cri-o 1.14: defects fixed in the 1.14 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.14.0 <1.15.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cri-o 1.14 known issues
  - cri-o 1.14 fixed in
  - is this cri-o bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cri-o
sources:
  - type: docs
    path: cri-o/cri-o release notes for the 1.14 line — bug-fix entries
    url: https://github.com/cri-o/cri-o/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cri-o 1.14: defects fixed in the 1.14 line

## Summary

**35 defects** the project fixed across **7 releases** of the 1.14 line, from 1.14.0 to
1.14.12. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.14.0

- Switched to golangci-lint with many additional linters enabled alongwith fixes
- 4d51ce85 Merge pull request #2158 from openSUSE/integration-fix
- 8cbd6890 Merge pull request #2042 from openSUSE/apparmor-test-fix
- 323f6940 Fix apparmor related integration tests
- 31b32698 Merge pull request #2045 from openSUSE/network-test-fix
- be2df39d Merge pull request #2039 from runcom/vndr-fix
- 650fae1c Merge pull request #2006 from fntlnz/fix/makefile-unused-variable
- 2d0c697f Merge pull request #1983 from openSUSE/filesystem-fix
- df8f28a3 Merge pull request #1940 from vikaschoudhary16/fix-permissions
- fd6ca608 Merge pull request #1984 from openSUSE/utils-fix
- 4379cb44 Fix segfault for invalid paths in GetDiskUsageStats()
- 95ad2104 Merge pull request #1981 from runcom/dockertransport-fix
- 12ec0b28 Merge pull request #1957 from giuseppe/fix-race-stop-pod-sandbox
- df052eb1 Merge pull request #1956 from giuseppe/fix-network-cleanup
- f4cb1772 Merge pull request #1955 from giuseppe/fix-another-segfault
- 6703d85f container_create: fix race with sandbox being stopped
- d6b2efb4 container_server: fix a segfault when the sandbox is not found
- e428dc09 Merge pull request #1944 from giuseppe/fix-segfault-on-network-failure
- 2319849d container: fix potential segfault on setup failure
- c60178b7 Usernamespaces: Fix permissions on runDirPath and BundlePath

### 1.14.1

- 3ddde3dee Merge pull request #2301 from openSUSE/release-1.14-travis-fix
- ecb8f669f Merge pull request #2253 from openSUSE/release-1.14-netns-nil-fix
- 2b87faf32 Merge pull request #2216 from giuseppe/fix-fd-leak
- efb108aae Merge pull request #2187 from openSUSE/release-1.14-oob-log-fix
- b58326d23 Fix possible out of bounds access during log parsing
- 5923bd29c Merge pull request #2169 from giuseppe/fix-segfault-with-manage_network_ns_lifecycle
- 281d80cbf sandbox: fix segfault with manage_network_ns_lifecycle

### 1.14.4

- a548864fb Fix runtime panic when having concurrent writes to runtime impl map

### 1.14.5

- 9a4bdced4 Fix up machine os content version and cri-o version in spec

### 1.14.10

- b58b525ba Fix parse of memory.limit_in_bytes on 32-bit machines
- 7f23249ef Fix container image used for integration tests

### 1.14.11

- a4fe91585 fix golangci-lint install for go 1.10
- 372500603 Update vendor code for cni and ocicni and libpod, fix build errors
- 62b536f56 crio-wipe: Fix int compare in lib.bash

### 1.14.12

- 74985cbcb Fix integration tests by adjusting image digest


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.14.12**, the newest release recorded here for this line.

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
