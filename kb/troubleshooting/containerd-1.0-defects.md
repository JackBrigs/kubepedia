---
id: TROUBLE-CONTAINERD_1_0_DEFECTS
type: troubleshooting
title: "containerd 1.0: defects fixed in the 1.0 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.0.0 <1.1.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - containerd 1.0 known issues
  - containerd 1.0 fixed in
  - is this containerd bug already fixed
tags:
  - troubleshooting
  - upgrade
  - containerd
sources:
  - type: docs
    path: containerd/containerd release notes for the 1.0 line — bug-fix entries
    url: https://github.com/containerd/containerd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# containerd 1.0: defects fixed in the 1.0 line

## Summary

**25 defects** the project fixed across **4 releases** of the 1.0 line, from 1.0.0 to
1.0.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.0.0

- 68d4dfe4 Merge pull request #1870 from dnephin/fix-error-messages
- a6fad51e Merge pull request #1869 from Ace-Tang/cio-docs-fix
- aca8e159 docs: fix usage of cio package in docs
- fe4e30cb Merge pull request #1859 from dmcgowan/fix-snapshot-logs

### 1.0.1

- dafb45d7 Merge pull request #2005 from AkihiroSuda/fix-user-1.0
- 0a2c2a26 Merge pull request #2003 from dmcgowan/cherry-pick-fix-whiteout-rootpath-1.0
- 8b6cbcc7 vendor: update ttrpc for shutdown fix
- edc72bbc Merge pull request #1980 from dmcgowan/cherry-pick-fix-1723
- eeef202b Fix parent directories not included in tar
- 6c7abf7c Merge pull request #1918 from crosbymichael/cherry-pull-fix

### 1.0.2

- bed74e242e Fixes missing whiteout parent directories
- 7193749fb0 Merge pull request #2102 from dnephin/fix-vendor-validation
- b9640ad1d9 Fix vendor.conf now that it is validated
- 5c21576e40 Fix duplicate directories entries on metadata change
- 383a6dea31 Merge pull request #2034 from estesp/cherrypick-npe-fix

### 1.0.3

- 8386ef28 Fix typo in CreateUnixSocket error message
- 62aad0e4 Merge pull request #2247 from estesp/fix-typeurl-typo
- 2f27d47c Fix typo in metadata test typeurl string
- 386b4e93 Merge pull request #2240 from dmcgowan/backport-fix-uncompressed-label
- 457c658e Fix label being put on snapshot instead of content
- abef3899 services/content: fix reading a blob which is smaller than the read buffer
- a609ec46 Merge pull request #2224 from dmcgowan/backport-archive-gc-fixes
- 3d34cc01 Fixes a default config bug of gc scheduler
- 5f0a37cf Update cgroups vendor for licenses/bug fix
- a3372da0 archive: fix logic for skipping mknod when running in userns


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.0.3**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `containerd/containerd`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/containerd.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
