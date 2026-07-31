---
id: TROUBLE-KATA_CONTAINERS_3_19_DEFECTS
type: troubleshooting
title: "kata-containers 3.19: defects fixed in the 3.19 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.19.0 <3.20.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kata-containers 3.19 known issues
  - kata-containers 3.19 fixed in
  - is this kata-containers bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kata-containers
sources:
  - type: docs
    path: kata-containers/kata-containers release notes for the 3.19 line — bug-fix entries
    url: https://github.com/kata-containers/kata-containers/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kata-containers 3.19: defects fixed in the 3.19 line

## Summary

**18 defects** the project fixed across **1 releases** of the 3.19 line, from 3.19.0 to
3.19.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.19.0

- runtime-rs: fix the issue return the wrong volume by @lifupan in https://github.com/kata-containers/kata-containers/pull/11467
- runtime-rs: Fix calculation of odd memory sizes by @fidencio in https://github.com/kata-containers/kata-containers/pull/11470
- runtime-rs: Fix noise with frequently appearing in unstaged changes by @Apokleos in https://github.com/kata-containers/kata-containers/pull/11490
- kata-agent: mount.rs: Fix warning of test by @teawater in https://github.com/kata-containers/kata-containers/pull/11509
- security: ci: Fixes for Zizmor GHA security scanning by @sprt in https://github.com/kata-containers/kata-containers/pull/11475
- runtime-rs: refactor and fix the implementation of guest-pull by @Apokleos in https://github.com/kata-containers/kata-containers/pull/11482
- runtime: Fix rootlessDir not correctly set in rootless VMM mode by @StevenFryto in https://github.com/kata-containers/kata-containers/pull/11527
- gh: Fix released VERSION file by @fidencio in https://github.com/kata-containers/kata-containers/pull/11554
- Rust advisory fixes pre 3.19.0 by @stevenhorsman in https://github.com/kata-containers/kata-containers/pull/11555
- runtime-rs: Fix initdata length field missing when create block by @Apokleos in https://github.com/kata-containers/kata-containers/pull/11557
- gpu: Fix kata deploy.sh by @zvonkok in https://github.com/kata-containers/kata-containers/pull/11335
- runk: Fix build errors by @Tim-Zhang in https://github.com/kata-containers/kata-containers/pull/11575
- agent: fix the issue of parent writer pipe fd leak by @lifupan in https://github.com/kata-containers/kata-containers/pull/11504
- shellcheck: fix kernel/build.sh by @zvonkok in https://github.com/kata-containers/kata-containers/pull/10961
- workflow: Fix osv-scanner action by @stevenhorsman in https://github.com/kata-containers/kata-containers/pull/11581
- runtime-rs: Fix the issue of blocking socket with Tokio by @justxuewei in https://github.com/kata-containers/kata-containers/pull/11578
- kernel: fix enable kernel debug by @zvonkok in https://github.com/kata-containers/kata-containers/pull/11584
- qemu: tdx: Fix binary path for non-gpu TDX by @fidencio in https://github.com/kata-containers/kata-containers/pull/11589


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.19.0**, the newest release recorded here for this line.

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
