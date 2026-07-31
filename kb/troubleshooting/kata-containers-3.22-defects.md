---
id: TROUBLE-KATA_CONTAINERS_3_22_DEFECTS
type: troubleshooting
title: "kata-containers 3.22: defects fixed in the 3.22 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.22.0 <3.23.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kata-containers 3.22 known issues
  - kata-containers 3.22 fixed in
  - is this kata-containers bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kata-containers
sources:
  - type: docs
    path: kata-containers/kata-containers release notes for the 3.22 line — bug-fix entries
    url: https://github.com/kata-containers/kata-containers/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kata-containers 3.22: defects fixed in the 3.22 line

## Summary

**11 defects** the project fixed across **1 releases** of the 3.22 line, from 3.22.0 to
3.22.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.22.0

- agent/rustjail: Fix double free in TTY handling by @sprt in https://github.com/kata-containers/kata-containers/pull/11833
- gha: zizmor: fix "workflow or action definition without a name" error by @sprt in https://github.com/kata-containers/kata-containers/pull/11855
- libs: Fix the test_parse_mount_options failure on ppc64le by @shwetha-s-poojary in https://github.com/kata-containers/kata-containers/pull/11849
- agent/rustjail: Fix potentially uninitialized memory read in unsafe code by @sprt in https://github.com/kata-containers/kata-containers/pull/11872
- gpu: Some fixes regarding the rootfs v580 by @zvonkok in https://github.com/kata-containers/kata-containers/pull/11896
- gha: Fix `docs-url-alive-check` workflow by @sprt in https://github.com/kata-containers/kata-containers/pull/11901
- runtime: fix device typo by @M-Phansa in https://github.com/kata-containers/kata-containers/pull/11894
- runtime: fix "num-queues expects uint64" error with virtio-blk by @spuzirev in https://github.com/kata-containers/kata-containers/pull/11888
- gpu: Fix kernel module signing by @zvonkok in https://github.com/kata-containers/kata-containers/pull/11916
- virtcontainers: fix nydus cleanup on rootfs unmount by @katexochen in https://github.com/kata-containers/kata-containers/pull/11899
- gpu: rootfs fixes by @zvonkok in https://github.com/kata-containers/kata-containers/pull/11966


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.22.0**, the newest release recorded here for this line.

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
