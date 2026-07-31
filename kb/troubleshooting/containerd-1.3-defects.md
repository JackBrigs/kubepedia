---
id: TROUBLE-CONTAINERD_1_3_DEFECTS
type: troubleshooting
title: "containerd 1.3: defects fixed in the 1.3 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.3.0 <1.4.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - containerd 1.3 known issues
  - containerd 1.3 fixed in
  - is this containerd bug already fixed
tags:
  - troubleshooting
  - upgrade
  - containerd
sources:
  - type: docs
    path: containerd/containerd release notes for the 1.3 line — bug-fix entries
    url: https://github.com/containerd/containerd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# containerd 1.3: defects fixed in the 1.3 line

## Summary

**61 defects** the project fixed across **9 releases** of the 1.3 line, from 1.3.0 to
1.3.10. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.3.0

- Updated cni plugins to v0.7.6 to fix a race condition in the `bridge` plugin. (https://github.com/containerd/containerd/issues/3507)
- **Fix garbage collection scheduling on reference removal.** Ensures removal of leases or containers triggers the next scheduled garbage collection
- Fix all media types in Accept header to match RFC
- Update cri test to fix image reference test and fix gcs deploy
- travis: fix Xenial tests not being run on master
- Fix potential panic for task in unknown state
- Fix potential containerd panic during graceful shutdown
- Made fixes and optimizations to encryption GC
- Fix metadata content store to call writer digest after commit
- Fix backwards compat with v2 containerd configs
- Fix seccomp contributed profile for clone syscall
- fix parseInfoFile does not handle spaces in filenames
- Fix issue with NewFIFOSetInDir with Terminal true
- Fix a bug in shim log on Windows that can cause 100% CPU utilization
- Fix runhcs shim bug in Create with "len(Rootfs) == 0"
- Fix spurious ttrpc client shutdown error log on success
- Fix CI due to Golang 1.10.6 / 1.11.3 regressions (workaround)
- fix: should get runtime name from container info
- fix pipe in broken may cause shim lock forever for runtime v1
- fix pipe in broken may cause shim lock forever for runtime v2
- fix container cmd args may parsed as ctr args
- fix: fix failed to get container-shim relation with io.containerd.runc.v1
- Fix mingw version back to working version with Golang
- fixed an issue with invalid soft memory limits
- Fix copy_file_range usage for files > 2GB on 32-bit archs
- Backport fix for default path env for CRI created OCI config
- fix: support empty auth config for anonymous registry
- Update containerd to fix panic caused by race condition
- Fix /etc/hostname backward compatibility issue for in-place upgrade
- Fix the issue that pod or container config file without metadata will crash containerd
- Fix Method of judging command execution failure

### 1.3.1

- Fix deadlock on image pull and unpack after a registry error [containerd/containerd#3816](https://github.com/containerd/containerd/issues/3816)
- Add local-fs.target to service file to fix corrupt image after unexpected host reboot. Reported in [containerd/containerd#3671](https://github.com/containerd/containerd/issues/3671), and fixed by [containerd/containerd#3745](https://github.com/containerd/containerd/pull/3745)
- Fix large output of processes with TTY getting occasionally truncated. Reported in [containerd/containerd#3738](https://github.com/containerd/containerd/issues/3738) and fixed by [containerd/containerd#3754](https://github.com/containerd/containerd/pull/3754)
- Fix direct unpack when running in user namespace. Reported in [containerd/containerd#3762](https://github.com/containerd/containerd/issues/3762), and fixed by [containerd/containerd#3779](https://github.com/containerd/containerd/pull/3779)
- CRI fixes: Fix shim delete error code to avoid unnecessary retries in the CRI plugin. Discovered in [containerd/cri#1309](https://github.com/containerd/cri/issues/1309), and fixed by [containerd/containerd#3733](https://github.com/containerd/containerd/pull/3733) and [containerd/containerd#3740](https://github.com/containerd/containerd/pull/3740)
- Fix delete error code on the containerd daemon side

### 1.3.2

- Fix containerd pid race condition [containerd/containerd#3857](https://github.com/containerd/containerd/pull/3857)
- Fix containerd build, use `libbtrfs-dev` when available

### 1.3.3

- Fix eventfd leak [containerd/containerd#3961](https://github.com/containerd/containerd/pull/3961)
- Fix API filters to properly handle and return parse errors [containerd/containerd#3950](https://github.com/containerd/containerd/pull/3950)
- fix: eventfd leak for v2 runtime with v1 cgroups

### 1.3.4

- Correct logic of FIFO cleanup [containerd/containerd#4150](https://github.com/containerd/containerd/pull/4150)
- Man page fixes [containerd/containerd#4144](https://github.com/containerd/containerd/pull/4144)
- vendor: update go-events to fix alignment for 32bit systems
- man: move ctr.1, containerd-config to section 8, and fix generation
- Fix incorrect comment from copy/paste of starting script

### 1.3.5

- Fix image usage calculation error [containerd/containerd#4276](https://github.com/containerd/containerd/pull/4276)

### 1.3.7

- Update to later version of critools with timing fix

### 1.3.8

- Fix metrics monitoring of v2 runtime tasks [containerd/containerd#4486](https://github.com/containerd/containerd/pull/4486)
- Fix nil pointer error when restoring checkpoint [containerd/containerd#4754](https://github.com/containerd/containerd/pull/4754)
- Fix devmapper device deletion on rollback [containerd/containerd#4437](https://github.com/containerd/containerd/pull/4437)
- Fix integer overflow on Windows [containerd/containerd#4589](https://github.com/containerd/containerd/pull/4589)
- Fix release.yml script for GH Actions changes to env/path
- Add KUBE_CONTAINER_RUNTIME_NAME to fix fluentd support
- Fix for kube-up.sh and update several documments

### 1.3.10

- **Fix container create in CRI to prevent possible environment variable leak between containers** [#1629](https://github.com/containerd/cri/pull/1629)
- **Fix incorrect usage calculation** [#5126](https://github.com/containerd/containerd/pull/5126)
- v2: Fix missing ns when openShimLog on windows
- Fix usage calculation to account for sparse files
- Fix sameFile() to recognize empty files as the same


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.3.10**, the newest release recorded here for this line.

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
