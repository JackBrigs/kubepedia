---
id: TROUBLE-KATA_CONTAINERS_3_12_DEFECTS
type: troubleshooting
title: "kata-containers 3.12: defects fixed in the 3.12 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.12.0 <3.13.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kata-containers 3.12 known issues
  - kata-containers 3.12 fixed in
  - is this kata-containers bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kata-containers
sources:
  - type: docs
    path: kata-containers/kata-containers release notes for the 3.12 line — bug-fix entries
    url: https://github.com/kata-containers/kata-containers/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kata-containers 3.12: defects fixed in the 3.12 line

## Summary

**13 defects** the project fixed across **1 releases** of the 3.12 line, from 3.12.0 to
3.12.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.12.0

- osbuilder: Fix build dependency of ubuntu rootfs with Docker by @coolljt0725 in https://github.com/kata-containers/kata-containers/pull/10377
- docs: Fix several build failures when I tried the procedures in "Kata Containers with AMD SEV-SNP VMs" by @kimullaa in https://github.com/kata-containers/kata-containers/pull/10386
- ci: Fix error on self-hosted machines by @zvonkok in https://github.com/kata-containers/kata-containers/pull/10516
- runtime-rs: fix vfio device name combination issue by @Apokleos in https://github.com/kata-containers/kata-containers/pull/10577
- agent: fix startup when guest_components_procs is set to none by @squarti in https://github.com/kata-containers/kata-containers/pull/10583
- ci: Fix variant for confidential targets by @zvonkok in https://github.com/kata-containers/kata-containers/pull/10590
- ci: Fix Docker publishing for CSI driver by @sprt in https://github.com/kata-containers/kata-containers/pull/10609
- ci: Fix Docker publishing for CSI driver, 2nd try by @sprt in https://github.com/kata-containers/kata-containers/pull/10612
- workflows: Fix remove artifact name filter by @stevenhorsman in https://github.com/kata-containers/kata-containers/pull/10615
- runtime-rs: Fix the issues with stderr fifo by @justxuewei in https://github.com/kata-containers/kata-containers/pull/10638
- runtime-rs & agent: Fix the issues with bind volumes by @justxuewei in https://github.com/kata-containers/kata-containers/pull/10643
- kata-ctl: fix outdated comments by @liubogithub in https://github.com/kata-containers/kata-containers/pull/10655
- qemu: Fix aarch64 build by @zvonkok in https://github.com/kata-containers/kata-containers/pull/10669


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.12.0**, the newest release recorded here for this line.

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
