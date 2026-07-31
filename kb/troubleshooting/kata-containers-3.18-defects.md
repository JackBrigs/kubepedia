---
id: TROUBLE-KATA_CONTAINERS_3_18_DEFECTS
type: troubleshooting
title: "kata-containers 3.18: defects fixed in the 3.18 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.18.0 <3.19.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kata-containers 3.18 known issues
  - kata-containers 3.18 fixed in
  - is this kata-containers bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kata-containers
sources:
  - type: docs
    path: kata-containers/kata-containers release notes for the 3.18 line — bug-fix entries
    url: https://github.com/kata-containers/kata-containers/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kata-containers 3.18: defects fixed in the 3.18 line

## Summary

**16 defects** the project fixed across **1 releases** of the 3.18 line, from 3.18.0 to
3.18.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.18.0

- osbuilder: lib.sh: Fix indent by @Rtoax in https://github.com/kata-containers/kata-containers/pull/11267
- runtime-rs: fix vfio pci address domain 0001 problem by @sampleyang in https://github.com/kata-containers/kata-containers/pull/11254
- Drop outdated erofs patches for 6.1.y kernels & fix a dragonball vsock issue by @hsiangkao in https://github.com/kata-containers/kata-containers/pull/10964
- runtime-rs: fix the issue of delete cgroup failed by @lifupan in https://github.com/kata-containers/kata-containers/pull/11301
- genpolicy: fix svc_name regex by @katexochen in https://github.com/kata-containers/kata-containers/pull/11314
- runtime: fix cgroupv2 deletion when sandbox_cgroup_only=false by @Champ-Goblem in https://github.com/kata-containers/kata-containers/pull/11324
- Fix | Support initdata for SNP by @Xynnn007 in https://github.com/kata-containers/kata-containers/pull/11329
- ci: fix artifact name of RISC-V tarball by @burgerdev in https://github.com/kata-containers/kata-containers/pull/11387
- ci: Fix Mariner rootfs build failure by @sprt in https://github.com/kata-containers/kata-containers/pull/11396
- Revert "ci: Fix Mariner rootfs build failure" by @sprt in https://github.com/kata-containers/kata-containers/pull/11398
- protocols: Fix the noise caused by non-formatted codes in protocols by @Apokleos in https://github.com/kata-containers/kata-containers/pull/11345
- genpolicy: fix rules syntax issues, rego v1 compatibility; ci: checks for rego parsing by @katexochen in https://github.com/kata-containers/kata-containers/pull/11412
- Fix logging on virtiofs shutdown by @pawelbeza in https://github.com/kata-containers/kata-containers/pull/11359
- gpu: Fix module signing by @zvonkok in https://github.com/kata-containers/kata-containers/pull/11337
- workflows: Fix permissions by @stevenhorsman in https://github.com/kata-containers/kata-containers/pull/11435
- release: Fix helm push typo by @stevenhorsman in https://github.com/kata-containers/kata-containers/pull/11438


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.18.0**, the newest release recorded here for this line.

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
