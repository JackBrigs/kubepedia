---
id: TROUBLE-KATA_CONTAINERS_3_29_DEFECTS
type: troubleshooting
title: "kata-containers 3.29: defects fixed in the 3.29 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.29.0 <3.30.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kata-containers 3.29 known issues
  - kata-containers 3.29 fixed in
  - is this kata-containers bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kata-containers
sources:
  - type: docs
    path: kata-containers/kata-containers release notes for the 3.29 line — bug-fix entries
    url: https://github.com/kata-containers/kata-containers/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kata-containers 3.29: defects fixed in the 3.29 line

## Summary

**14 defects** the project fixed across **1 releases** of the 3.29 line, from 3.29.0 to
3.29.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.29.0

- Security fixes 23 mar 26 by @stevenhorsman in https://github.com/kata-containers/kata-containers/pull/12704
- gatekeeper: Unrequire NVIDIA GPU SNP tests till auth is fixed by @fidencio in https://github.com/kata-containers/kata-containers/pull/12733
- kata-deploy: Fix kata-deploy pods crashing if containerd restarts by @fidencio in https://github.com/kata-containers/kata-containers/pull/12766
- runtime-rs: Fix FC API fields by @ananos in https://github.com/kata-containers/kata-containers/pull/12767
- runtime-rs: Fix typo in share_fs error message by @YutingNie in https://github.com/kata-containers/kata-containers/pull/12762
- runtime: fix Docker 26+ networking by rescanning after Start by @llink5 in https://github.com/kata-containers/kata-containers/pull/12754
- runtime-rs: fix setting directio via config file by @PiotrProkop in https://github.com/kata-containers/kata-containers/pull/12682
- fix: updated image-rs to v0.18.0 by @pavithiran34 in https://github.com/kata-containers/kata-containers/pull/12782
- kata-deploy: Fix noisy caused by unformatted code by @Apokleos in https://github.com/kata-containers/kata-containers/pull/12791
- runtime: Fix concurrent map read/write panic in Wait() by @fidencio in https://github.com/kata-containers/kata-containers/pull/12826
- runtime-rs: Fix unformatted code in runtime-rs by @Apokleos in https://github.com/kata-containers/kata-containers/pull/12844
- docs: fix nerdctl guest image command by @Xynnn007 in https://github.com/kata-containers/kata-containers/pull/11611
- Confidential tests fixes by @stevenhorsman in https://github.com/kata-containers/kata-containers/pull/12879
- runtime-rs/ch: Fix pod deletion hang and make deletion idempotent by @sprt in https://github.com/kata-containers/kata-containers/pull/12887


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.29.0**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `kata-containers/kata-containers`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/kata-containers.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
