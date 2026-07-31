---
id: TROUBLE-KATA_CONTAINERS_3_8_DEFECTS
type: troubleshooting
title: "kata-containers 3.8: defects fixed in the 3.8 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.8.0 <3.9.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kata-containers 3.8 known issues
  - kata-containers 3.8 fixed in
  - is this kata-containers bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kata-containers
sources:
  - type: docs
    path: kata-containers/kata-containers release notes for the 3.8 line — bug-fix entries
    url: https://github.com/kata-containers/kata-containers/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kata-containers 3.8: defects fixed in the 3.8 line

## Summary

**13 defects** the project fixed across **1 releases** of the 3.8 line, from 3.8.0 to
3.8.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.8.0

- runtime-rs: container: fix the issue of missing cleanup container by @lifupan in https://github.com/kata-containers/kata-containers/pull/10045
- tests: Fix missing log on TDX by @ChengyuZhu6 in https://github.com/kata-containers/kata-containers/pull/10031
- Fix issue while adding multiple networks with nerdctl by @amshinde in https://github.com/kata-containers/kata-containers/pull/9899
- runtime-rs : fix the issue of stop sandbox by @lifupan in https://github.com/kata-containers/kata-containers/pull/10043
- runtime-rs: Fix QEMU backend for runtime-rs by @ananos in https://github.com/kata-containers/kata-containers/pull/10052
- ci: Fix rate limit error by migrating busybox_image by @AdithyaKrishnan in https://github.com/kata-containers/kata-containers/pull/10101
- tests: Fix error with `kubectl debug` by @ChengyuZhu6 in https://github.com/kata-containers/kata-containers/pull/10102
- agent: fix the AllowRequestsFailingPolicy functionality by @danmihai1 in https://github.com/kata-containers/kata-containers/pull/10098
- Fix metrics json results file by @dborquez in https://github.com/kata-containers/kata-containers/pull/10120
- tools: Fix container image build warning by @hex2dec in https://github.com/kata-containers/kata-containers/pull/10137
- osbuilder: fix typo in ubuntu rootfs depends by @deagon in https://github.com/kata-containers/kata-containers/pull/10172
- kata-deploy: fix kata-deploy reset by @beraldoleal in https://github.com/kata-containers/kata-containers/pull/10170
- ci: stdio: Fix typo on getting the containerd version by @fidencio in https://github.com/kata-containers/kata-containers/pull/10181


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.8.0**, the newest release recorded here for this line.

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
