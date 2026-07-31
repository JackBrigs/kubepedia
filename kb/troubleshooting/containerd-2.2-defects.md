---
id: TROUBLE-CONTAINERD_2_2_DEFECTS
type: troubleshooting
title: "containerd 2.2: defects fixed in the 2.2 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.2.0 <2.3.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - containerd 2.2 known issues
  - containerd 2.2 fixed in
  - is this containerd bug already fixed
tags:
  - troubleshooting
  - upgrade
  - containerd
sources:
  - type: docs
    path: containerd/containerd release notes for the 2.2 line — bug-fix entries
    url: https://github.com/containerd/containerd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# containerd 2.2: defects fixed in the 2.2 line

## Summary

**42 defects** the project fixed across **6 releases** of the 2.2 line, from 2.2.0 to
2.2.6. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.2.0

- **Fix pidfd leak in UnshareAfterEnterUserns**

### 2.2.1

- **Fix image defaults on Darwin to usable configuration**
- **Fix possible panic from WithMediaTypeKeyPrefix**
- **Fix parsing of hugetlb.<size>.events files** ([containerd/cgroups#379](https://github.com/containerd/cgroups/pull/379))
- Fix image defaults on Darwin to usable configuration ([#12544](https://github.com/containerd/containerd/pull/12544)) [`d154e234b`](https://github.com/containerd/containerd/commit/d154e234b29c5bed4f14a72d605e92e4728415a2) Update the ctr pull defaults when using the transfer service [`09364216d`](https://github.com/containerd/containerd/commit/09364216de92aab056118507da59fabf642d88ac) Fix transfer unpack defaults on darwin [`2055d3c62`](https://github.com/containerd/containerd/commit/2055d3c62e85350642c4b031c35a63b22e2ec6f7) Update default differs on darwin [`9da97686d`](https://github.com/containerd/containerd/commit/9da97686d151da046d5512bb9f7f1d67ea4c8393) Use default writable size in erofs snapshotter for non-Linux hosts [`eeb0f889a`](https://github.com/containerd/containerd/commit/eeb0f889aed826b58a3033a5a5b14dff6ccd1979) Update default erofs block size on macOS during erofs diff
- Redact all query parameters in CRI error logs ([#12546](https://github.com/containerd/containerd/pull/12546)) [`c707f771a`](https://github.com/containerd/containerd/commit/c707f771a872f9dd22ad8f2f827317a800e4a74f) fix: redact all query parameters in CRI error logs
- Fix possible panic from WithMediaTypeKeyPrefix ([#12516](https://github.com/containerd/containerd/pull/12516)) [`8b73c2de3`](https://github.com/containerd/containerd/commit/8b73c2de310e95fe3a143473b511fcf99d03692f) remotes: fix possible panic from WithMediaTypeKeyPrefix
- Fix parsing of hugetlb.<size>.events files ([containerd/cgroups#379](https://github.com/containerd/cgroups/pull/379)) [`2ad7a12`](https://github.com/containerd/cgroups/commit/2ad7a1241827ef1bc4f964fe8a5248b073f2db82) hugetlb: correctly parse hugetlb.<size>.events files
- Fix wasm example ([containerd/nri#237](https://github.com/containerd/nri/pull/237)) [`44b2861`](https://github.com/containerd/nri/commit/44b2861a26c8e392229cd8b27a20cf689925f176) Fix wasm example
- Makefile: build proto files unconditionally ([containerd/nri#229](https://github.com/containerd/nri/pull/229)) [`d99f960`](https://github.com/containerd/nri/commit/d99f96028e5226c004f94a3394be82190980c4bd) Fix dockerized proto build [`9623748`](https://github.com/containerd/nri/commit/9623748f543343bfe6b2312df47a7ed9000d47fe) Makefile: build proto files unconditionally [`25d9391`](https://github.com/containerd/nri/commit/25d9391690a7158d851364ef011e1f56fd607a70) build: ensure we use correct version of protoc and its deps
- plugins/logger: fix default event subscription mask. ([containerd/nri#158](https://github.com/containerd/nri/pull/158)) [`33b1db1`](https://github.com/containerd/nri/commit/33b1db1add2e9a603f7c47e1efa95d386f4af560) logger: fix default event subscription mask
- ci: bump golangci-lint to v2.4 ([containerd/nri#225](https://github.com/containerd/nri/pull/225)) [`9787127`](https://github.com/containerd/nri/commit/9787127c0f3e69726b968e12b29dae31e35e250b) Bump golangci-lint to v2.4 [`1a50ff5`](https://github.com/containerd/nri/commit/1a50ff585624f01763fd20aafaeaa92aa8b27c46) Add nolint directives [`00fa1a1`](https://github.com/containerd/nri/commit/00fa1a124e605590d3ceea1e687600785ae6518d) Add and fix comments for exported types [`ac21da7`](https://github.com/containerd/nri/commit/ac21da7be8f991a8699cef41acba8783dee5351e) pkg/api/seccomp: add comments for exported functions [`3aff986`](https://github.com/containerd/nri/commit/3aff986af5f8abefda8552edae991608782df46c) pkg/runtime-tools/generate: remove embedded field "Generator" [`c0c4bb6`](https://github.com/containerd/nri/commit/c0c4bb648ae46207f47d5b18bf447f7d5b32e26b) pkg/api/validate: add comments for exported methods [`c0ba9da`](https://github.com/containerd/nri/commit/c0ba9da712934c860a64af54d96b5cfc74672ff5) adaptation/builtin: add comment for exported symbols
- ci: update actions, test against go1.23, fix linting, and update golangci-lint ([containerd/zfs#88](https://github.com/containerd/zfs/pull/88)) [`662ad3c`](https://github.com/containerd/zfs/commit/662ad3cefa596775e20a44a1c6b1037b0a0d539d) gha: update golangci/golangci-lint-action@v9, golangci-lint v2.7 [`b0b2584`](https://github.com/containerd/zfs/commit/b0b25847ac875af99d62e9d4f83b2875a2f39df9) remove nolint comments [`7c4274b`](https://github.com/containerd/zfs/commit/7c4274bfa0a0df14d66fabb51269bfdfbf4e0b06) fix error capitalization [`24ce1b9`](https://github.com/containerd/zfs/commit/24ce1b93f0579fe5ecaec4bd55290ff7e2f456db) fix inconsistent receiver name [`c8545c3`](https://github.com/containerd/zfs/commit/c8545c33c3c9f4d881c45a22688be49f4ff1502a) gha: update actions/checkout@v6 [`d23ec04`](https://github.com/containerd/zfs/commit/d23ec046338e9a5761083cef373be2bab1551995) gha: update actions/setup-go@v6 [`bb45f6e`](https://github.com/containerd/zfs/commit/bb45f6e4d3965616dcaae6eaab9342af0e4c1cad) gha: update containerd/project-checks@v1.2.2 [`65bc451`](https://github.com/containerd/zfs/commit/65bc451f6abab9d7133abd7c227be227ad6b1f0d) gha: test against go1.23

### 2.2.2

- Fix migrated CRI image config when using legacy registry mirrors
- Fix CNI issue where DEL is never executed after a restart
- Fix nil pointer dereference in container spec memory metrics when memory constraints are not fully configured
- Fix unintended dropping of mount flags for read-only bind-mounts in user namespaces
- Fix AppArmor bug disallowing unix domain sockets on newer kernels
- Fix `ctr image mount` failing with "no such device"
- Fix migrated CRI image config when using legacy registry mirrors ([#12987](https://github.com/containerd/containerd/pull/12987)) [`a20dead7c`](https://github.com/containerd/containerd/commit/a20dead7cc644291433b2da4b1efa2f70c8a144f) set default config_path in plugin init
- Fix CNI issue where DEL is never executed after a restart ([#12926](https://github.com/containerd/containerd/pull/12926)) [`54101116f`](https://github.com/containerd/containerd/commit/54101116fcdf18e21c8d202f86ed93c34a5932af) add integration test for cni result nil [`d44c4384e`](https://github.com/containerd/containerd/commit/d44c4384ec9f7adef9a4598e05f12e0850338fd8) address comment [`f1835270b`](https://github.com/containerd/containerd/commit/f1835270b0b800e4c1ba13391cd4a75617810615) fix issue where cni del is never executed
- Fix AppArmor bug disallowing unix domain sockets on newer kernels ([#12897](https://github.com/containerd/containerd/pull/12897)) [`6c05047b4`](https://github.com/containerd/containerd/commit/6c05047b4ba86d2fb857429c6272bb66679e7dee) apparmor: explicitly set abi/3.0
- integration: Fix TestImageLoad() failure on CI ([#12906](https://github.com/containerd/containerd/pull/12906)) [`09b876a81`](https://github.com/containerd/containerd/commit/09b876a8198818ab7d59e9037e6592889faea861) integration: Fix TestImageLoad() failure on CI
- cri: Fix image volumes with user namespaces ([#12885](https://github.com/containerd/containerd/pull/12885)) [`172ba65b6`](https://github.com/containerd/containerd/commit/172ba65b6a89479865832a7101f10e1b3a323d78) cri: Fix image volumes with user namespaces
- Fix `ctr image mount` failing with "no such device" ([#12831](https://github.com/containerd/containerd/pull/12831)) [`1d7908273`](https://github.com/containerd/containerd/commit/1d79082735d46fe24ded00a55ea6e3a33954593e) core/mount/manager: fix bind mount missing rbind option [`3d509bcd3`](https://github.com/containerd/containerd/commit/3d509bcd335b15cece69ebfa117681d2715df930) core/mount/manager: add tests for WithTemporary option
- Harden error handling to strip potentially-sensitive registry parameters ([#12804](https://github.com/containerd/containerd/pull/12804)) [`cb3ae2119`](https://github.com/containerd/containerd/commit/cb3ae211952909a5c4d9fcb274e029286057fc34) fix: sanitize error before gRPC return to prevent credential leak in pod events
- Fix regression for pulling encrypted images ([#12712](https://github.com/containerd/containerd/pull/12712)) [`8a7409e2e`](https://github.com/containerd/containerd/commit/8a7409e2e71fd9486db3504ab804d4419e45af41) Reinstate image decryption

### 2.2.3

- Handle absolute symlinks in rootfs user lookup to fix regressions when using Go 1.24
- Enable mount manager in diff walking to fix layer extraction errors with some snapshotters (e.g., EROFS)
- Apply absolute symlink resolution to /etc/group in OCI spec to fix lookups on NixOS-style systems
- Fix bug that caused whiteouts to be ignored when parallel unpack was used
- Fix vagrant on CI ([#13066](https://github.com/containerd/containerd/pull/13066)) [`77c6886df`](https://github.com/containerd/containerd/commit/77c6886df6510bf1ac9326436e7b371a28eb5678) Ignore NOCHANGE error
- Fix TOCTOU race bug in tar extraction ([#12971](https://github.com/containerd/containerd/pull/12971)) [`fbed68b8f`](https://github.com/containerd/containerd/commit/fbed68b8fb97b778b0caf68167cb0c4ab4af27df) Fix TOCTOU race bug in tar extraction
- fix(oci): apply absolute symlink resolution to /etc/group ([#13019](https://github.com/containerd/containerd/pull/13019)) [`ee4179e52`](https://github.com/containerd/containerd/commit/ee4179e5212c09e7bc4c429bf5b77eabb2b84662) fix(oci): apply absolute symlink resolution to /etc/group
- fix(oci): handle absolute symlinks in rootfs user lookup ([#13015](https://github.com/containerd/containerd/pull/13015)) [`fd061b848`](https://github.com/containerd/containerd/commit/fd061b84887177b969e8f8e2499e780341cde0ae) test(oci): use fstest and mock fs for better symlink coverage [`5d44d2c22`](https://github.com/containerd/containerd/commit/5d44d2c220d6296156c1c4fe3a500958667a3708) fix(oci): handle absolute symlinks in rootfs user lookup

### 2.2.4

- Fix handling of out-of-range USER values in OCI spec to avoid unexpected username/group lookups
- Fix bugs in sandbox service affecting sandbox creation configuration and event publishing
- Disable overlay "rebase" capability when running in a user namespace to fix layer extraction failures
- sandbox: forward Create fields, fix event topics ([#13266](https://github.com/containerd/containerd/pull/13266)) [`caa29a741`](https://github.com/containerd/containerd/commit/caa29a741321999d2296fc3d89f190b15ce40495) sandbox: forward Create fields, fix event topics

### 2.2.6

- Fix nil pointer dereference in NRI GetIPs during pod sandbox teardown or container exit
- Fix nil pointer dereference in NRI GetIPs ([#13696](https://github.com/containerd/containerd/pull/13696)) [`d3e1a2be9`](https://github.com/containerd/containerd/commit/d3e1a2be92e527bf40ea4746b616bd782e108380) Fix nil pointer dereference in NRI GetIPs
- fix: avoid content storage pollution by limiting the fallback on ref resolution ([#13620](https://github.com/containerd/containerd/pull/13620)) [`36c4275ee`](https://github.com/containerd/containerd/commit/36c4275eed174bdf40df60a5dea2c32191a1e946) fix:avoid content storage pollution by limiting the fallback on ref resolution


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.2.6**, the newest release recorded here for this line.

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
