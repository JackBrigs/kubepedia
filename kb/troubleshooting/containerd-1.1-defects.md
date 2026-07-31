---
id: TROUBLE-CONTAINERD_1_1_DEFECTS
type: troubleshooting
title: "containerd 1.1: defects fixed in the 1.1 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.1.0 <1.2.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - containerd 1.1 known issues
  - containerd 1.1 fixed in
  - is this containerd bug already fixed
tags:
  - troubleshooting
  - upgrade
  - containerd
sources:
  - type: docs
    path: containerd/containerd release notes for the 1.1 line — bug-fix entries
    url: https://github.com/containerd/containerd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# containerd 1.1: defects fixed in the 1.1 line

## Summary

**90 defects** the project fixed across **8 releases** of the 1.1 line, from 1.1.0 to
1.1.8. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.1.0

- 1381f8fddc Merge pull request #2301 from HusterWan/zr/fix-misspell
- e9114e3257 Merge pull request #2294 from fermayo/fix-cli-help
- 6c02c5cf0a Merge pull request #2272 from dmcgowan/fix-platform-pull-test
- 1a9f9e65b9 Merge pull request #2258 from mlaventure/fix-stupid-typo
- 81feacd393 Fix typo in CreateUnixSocket error message
- 79963209f6 Merge pull request #2239 from estesp/fix-test-typeurl
- dd1085c922 Fix typo in metadata test typeurl string
- fec0a1ba89 Merge pull request #2237 from dmcgowan/fix-pull-uncompressed-label
- d608e3d9dc Fix label being put on snapshot instead of content
- 7b323b1402 services/content: fix reading a blob which is smaller than the read buffer
- 804249cdcf Merge pull request #2214 from miaoyq/fixes-config-bug
- 9304193b8c Merge pull request #2219 from dmcgowan/fix-lock-on-schema1-configs
- d465f858a0 Fixes a default config bug of gc scheduler
- 3c1ef1a714 Merge pull request #2212 from dmcgowan/fix-overlay-cleanup-race
- 94cf25f7db overlay: fix cleanup directory deletion race
- edf7f410fb Merge pull request #2199 from estesp/vndr-cgroups-fix-licenses
- e38b2bbc3f Update cgroups vendor for license headers/bug fix
- 142ecddd0d Merge pull request #2180 from AkihiroSuda/fix-ctr-c-create-unix
- 125fdeff8a linux: fix runtime-root propagation
- b3a4e63c69 Merge pull request #2173 from AkihiroSuda/fix-shim-runtime-root
- fffc111ba8 archive: fix logic for skipping mknod when running in userns
- 25c403415a Merge pull request #2151 from Random-Liu/fix-load-task
- efb813f18b Merge pull request #2126 from dmcgowan/fix-2119
- f12ba2407e Merge pull request #2111 from Random-Liu/fix-trace-level
- aa49e704e2 Merge pull request #2095 from dmcgowan/fix-whiteout-parent-directories
- 13733b6a65 Merge pull request #2100 from kunalkushwaha/testsuite-typo-fix
- d778dd15d8 Fixes missing whiteout parent directories
- 254807da5b Merge pull request #2092 from dnephin/fix-vendor-validation
- 2448ae6976 Merge pull request #2054 from dmcgowan/fix-duplicate-tar-file
- dfadd8ce75 Fix duplicate directories entries on metadata change
- ef485c80ec Merge pull request #2049 from dnephin/fix-errorf-return
- bbb5b2f15e Merge pull request #2001 from dmcgowan/fix-whiteout-rootpath
- 4a6e2975cf Merge pull request #1994 from AkihiroSuda/fix-user
- bf0236b457 Merge pull request #1991 from dnephin/fix-progress-panic
- 87cb12de32 vendor: update ttrpc for shutdown fix
- 1a0c7ee8a0 Merge pull request #1955 from containerd/fix-website
- 00ad7fe408 Fix website rendering via gh-pages
- c07ede497d Merge pull request #1940 from schomatis/fix-io-testnewattach-race
- eda50b1fa6 Fix race condition in IO test (TestNewAttach)
- d4317a1b0d Fix parent directories not included in tar
- f33f49e30f Merge pull request #1924 from crosbymichael/fix-gauge
- 5971d369e0 Merge pull request #1916 from dnephin/fix-pull-after-failure
- cb423f8360 Merge pull request #1907 from Random-Liu/fix-deadlock
- c2cedac2ec Merge pull request #1899 from YaoZengzeng/fix
- 31dabf0c7d Merge pull request #1892 from estesp/fix-release-link
- 0eec9c078a Fix missing libcontainer syscall file

### 1.1.1

- Fixes for working set memory calculation, privileged container creation and
- Fix a bug that container running as non-root will get capabilities added by user. This is fixed to keep the behavior consistent with Docker
- Fix startup panic when overlayfs fails to load, now cri plugin will just fail
- Fix for a size validation bug with some registries which impacts the CRI plugin and clients
- 5d87c67c15 Merge pull request #2416 from dmcgowan/backport-arm-fix
- 2326b62470 Merge pull request #2367 from dmcgowan/1.1-fix-size-validation-error
- 60448fe8b9 Fix invalid length bug with some registries
- 7f5ed29069 Bump continuity to fix copy files > 2^32 bytes
- 01a0741488 Merge pull request #2334 from dmcgowan/fix-missing-return-1.1

### 1.1.3

- 68380d41dd Fix options ordering in proto api txt files

### 1.1.4

- 013c509a Merge pull request #2654 from estesp/cherrypick-commit-fix
- 0367114b Fix an issue that container/sandbox can't be stopped

### 1.1.5

- Fix a bug that containerd-shim may hang when many exec processes simultaneously
- Fix a bug that IPAM IP leaks after node reboot
- Ignore modprobe failures in systemd ExecStartPre. This fixes containerd start
- [`538c6661e7`](https://github.com/containerd/containerd/commit/538c6661e7e7e1fd833846a90e11ff0d4093da36) fix pipe in broken may cause shim lock forever for runtime v1
- [`deeaac9094`](https://github.com/containerd/containerd/commit/deeaac90942ba0f38313823583b5d36e49b71f39) fix: modify lock location of exec delete

### 1.1.6

- containerd/cri#991 Remove container lifecycle image dependency (fixes containerd/cri#990)
- containerd/cri#1016 Specify platform for image pull (fixes containerd/cri#1015)
- containerd/cri#1027 Fix the log ending newline handling (fixes containerd/cri#1026)
- containerd/cri#1042 Set /etc/hostname (fixes containerd/cri#1041)
- containerd/cri#1045 Fix env performance issue (fixes containerd/cri#1044)
- [`b48afb426e`](https://github.com/containerd/containerd/commit/b48afb426e4c9acecf5abc0d2c62f2ee8fa975b8) fix: SCHILY.xattrs should be SCHILY.xattr
- [`ff8a80e4c1`](https://github.com/containerd/containerd/commit/ff8a80e4c18299f533a2dae92906db6d302b5600) [release/1.1] fix: linter issue
- [`0e93a1e41f`](https://github.com/containerd/containerd/commit/0e93a1e41fbb89c2bb6dca64629471ec375772db) Revert "Fix CI due to Golang 1.10.6 / 1.11.3 regressions (workaround)"
- [`66a3eeb5b7`](https://github.com/containerd/containerd/commit/66a3eeb5b78ef409b7520dae64e17bc3aceb1ebc) Fix CI due to Golang 1.10.6 / 1.11.3 regressions (workaround)
- [`190c910435`](https://github.com/containerd/containerd/commit/190c910435299eecf915d06586b8d4e1412de95a) fix pid reuse attack when kill a exec process
- [`33c860f31d`](https://github.com/containerd/containerd/commit/33c860f31d1346a95f65a54083523060a35085fd) fix race in exec delete and start
- [`b9cb0b21`](https://github.com/containerd/cri/commit/b9cb0b217e0f3e919f17de76afb62d3d40ee2ba4) Fix lint error
- [`0e24a83a`](https://github.com/containerd/cri/commit/0e24a83ad4d4125d3afc0226f934b9625e28cec3) Fix the log ending newline handling
- [`1347be5a`](https://github.com/containerd/cri/commit/1347be5a127ad5f14ab3b7bd87ae19ba5b26b353) Revert "Temporary fix for golang regression #29241."
- [`2b2ca4c4`](https://github.com/containerd/cri/commit/2b2ca4c472915caf3919d64ce34d5db315de9406) Temporary fix for golang regression #29241

### 1.1.7

- Fix an issue that non-existent parent directory in image layers is created with permission `0700`. [#3017](https://github.com/containerd/containerd/issues/3017)
- Fix an issue that snapshots of the base image can be deleted by mistake, when images built on top of it are deleted. [#3088](https://github.com/containerd/containerd/pull/3088)
- Fix a bug that container output can be incomplete when stdout and stderr are pointed to the same file. [#3156](https://github.com/containerd/containerd/issues/3156)
- cri: fix a bug that pod can't get started when the same volume is defined differently in the image and the pod spec. [cri#1059](https://github.com/containerd/cri/issues/1059)
- cri: fix a bug that causes container start failure after in-place upgrade containerd to 1.2.4+ or 1.1.6+. [cri#1082](https://github.com/containerd/cri/issues/1082)
- cri: fix a bug that containers being gracefully stopped are SIGKILLed when kubelet is restarted. [cri#1098](https://github.com/containerd/cri/issues/1098)
- cri: Fix a bug that pod UTS namespace is used for host network. [cri#1111](https://github.com/containerd/cri/pull/1111)
- [`45b8d86585`](https://github.com/containerd/containerd/commit/45b8d86585f43786ac7d0b38ee67dec95e30ebb7) Fix the formatting directives error during compilation
- [`5539584`](https://github.com/containerd/cgroups/commit/5539584069073a678346861117642026f267fba3) Fix incorrect use of OCI runtime specs-go cgroup dev types
- [`134c2f35`](https://github.com/containerd/cri/commit/134c2f35daa7c8a46d39e3d02976ff24e561b544) Fix /etc/hostname backward compatibility issue for in-place upgrade

### 1.1.8

- [`2a82a9d2f4`](https://github.com/containerd/containerd/commit/2a82a9d2f4853df7a4820781a639cc81110a50e6) Merge pull request [#3699](https://github.com/containerd/containerd/pull/3699) from dmcgowan/fix-release-notes-1.1.8
- [`c828c5d082`](https://github.com/containerd/containerd/commit/c828c5d082810c2b4769c9d693232eac1c879ec9) Fix typo in release notes


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.1.8**, the newest release recorded here for this line.

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
