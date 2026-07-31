---
id: TROUBLE-CONTAINERD_1_4_DEFECTS
type: troubleshooting
title: "containerd 1.4: defects fixed in the 1.4 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.4.0 <1.5.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - containerd 1.4 known issues
  - containerd 1.4 fixed in
  - is this containerd bug already fixed
tags:
  - troubleshooting
  - upgrade
  - containerd
sources:
  - type: docs
    path: containerd/containerd release notes for the 1.4 line — bug-fix entries
    url: https://github.com/containerd/containerd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# containerd 1.4: defects fixed in the 1.4 line

## Summary

**69 defects** the project fixed across **10 releases** of the 1.4 line, from 1.4.0 to
1.4.12. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.4.0

- **Create image record after blob download to fix concurrent download issue** [#3972](https://github.com/containerd/containerd/pull/3972)
- **Fix privileged supported** [cri#1356](https://github.com/containerd/cri/pull/1356)
- Add KUBE_CONTAINER_RUNTIME_NAME to fix fluentd support
- Fix for kube-up.sh and update several documments
- Update to later version of critools with timing fix
- [events/exchange_test] Fix deadlock in TestExchangeFilters
- Fix deprecation warnings in CRI tests due to missing unix:// scheme
- unpacker: Fix data race and possible data corruption
- snapshots/devmapper: fix race windown causing IO hangup
- vendor: update go-events to fix alignment for 32bit systems
- man: move ctr.1, containerd-config to section 8, and fix generation
- Update btrfs dependencies in docs for debian buster and ubuntu 19.10 * Fixes: #4090
- Fix incorrect comment from copy/paste of starting script
- Fix startup_delay within default configuration
- fix: eventfd leak for v2 runtime with v1 cgroups
- v2: Fix missing ns when openShimLog on windows
- Fix delete error code on the containerd daemon side
- Fixed io.weight conversation + systemd io.weight controll added
- Fixed memory convertion for `reservation` from high to low
- v2: fix nil panic on statting disabled controllers
- Set GO111MODULE=on to fix Go 1.11/1.12 builds
- Fix sameFile() to recognize empty files as the same
- Specify version = 2 & fix wrong key in registry.md (GCR example)
- config: fix TOML tag for TolerateMissingHugePagesCgroupController
- Increase port-forward timeout to 1s to fix e2e test
- fix incomplete host device for PrivilegedWithoutHostDevices
- update selinux dependency to fix test failures
- Fix store error serialization to gRPC status codes
- Fix containerd build, use `libbtrfs-dev` when available
- Update cri-tools to fix all image reference test failure
- fix: support empty auth config for anonymous registry
- Fix "modules disabled inside GOPATH/src by GO111MODULE=auto"
- ttrpc: fix the issue of marshaling on nil will crash the server

### 1.4.1

- Fix error deleting v2 bundle directory when removing rootfs returns `ErrNotExist` [containerd/containerd#4472](https://github.com/containerd/containerd/pull/4472)
- Fix metrics monitoring of v2 runtime tasks [containerd/containerd#4486](https://github.com/containerd/containerd/pull/4486)
- Fix incorrect stat for Windows containers [containerd/containerd#4468](https://github.com/containerd/containerd/pull/4468)
- Fix devmapper device deletion on rollback [containerd/containerd#4437](https://github.com/containerd/containerd/pull/4437)
- BUILDING.md: fix description about static builds

### 1.4.2

- Fix bug limiting the number of layers by default [containerd/cri#1602](https://github.com/containerd/cri/pull/1602)
- Fix selinux shared memory issue by relabeling /dev/shm [containerd/cri#1605](https://github.com/containerd/cri/pull/1605)
- Fix unknown state preventing removal of containers [containerd/containerd#4656](https://github.com/containerd/containerd/pull/4656)
- Fix nil pointer error when restoring checkpoint [containerd/containerd#4754](https://github.com/containerd/containerd/pull/4754)
- Fix integer overflow on Windows [containerd/containerd#4589](https://github.com/containerd/containerd/pull/4589)
- Fix lcow snapshotter to read trailing tar data [containerd/containerd#4628](https://github.com/containerd/containerd/pull/4628)
- Update cri version to pickup unknown state fix
- Fix Windows service panic file to not be read-only
- Update btrfs vendor for chkptr fix for Go >= 1.14
- fix: always set unknown to false when handling exit event

### 1.4.4

- **Fix container create in CRI to prevent possible environment variable leak between containers** [#1628](https://github.com/containerd/cri/pull/1628)
- **Fix incorrect usage calculation** [#5019](https://github.com/containerd/containerd/pull/5019)
- Fix usage calculation to account for sparse files
- cri/config: fix range iterator issue in ValidatePluginConfig

### 1.4.5

- **Fix leaking socket path in runc shim v2** [#5195](https://github.com/containerd/containerd/pull/5195)
- **Fix cleanup logic in new container in runc shim v2** [#5206](https://github.com/containerd/containerd/pull/5206)
- **Fix registry mirror authorization logic in CRI plugin** [#5446](https://github.com/containerd/containerd/pull/5446)
- runtime/v2/runc: fix the defer cleanup of the NewContainer
- Fix advisory link in release notes for containerd 1.4.4

### 1.4.7

- **Fix invalid validation error checking** [#5565](https://github.com/containerd/containerd/pull/5565)
- **Fix error on image pull resume** [#5560](https://github.com/containerd/containerd/pull/5560)
- **Fix symlink resolution for disk mounts on Windows** [#5411](https://github.com/containerd/containerd/pull/5411)
- [release/1.4] Fix missing Body.Close() calls on push to docker remote

### 1.4.9

- **Fix user agent used for fetching registry authentication tokens** [#5761](https://github.com/containerd/containerd/pull/5761)
- remotes/docker/pusher.go: Fix missing Close()
- remotes/docker/fetcher.go: Fix missing Close()
- [release/1.4] Fix incorrect UA used for registry authentication

### 1.4.10

- **Fix panic in metadata content writer on copy error** [#6043](https://github.com/containerd/containerd/pull/6043)
- Fix panic in metadata content writer on copy error

### 1.4.11

- **Fix insufficiently restricted permissions on container root and plugin directories** [GHSA-c2h3-6mxw-7mvq](https://github.com/containerd/containerd/security/advisories/GHSA-c2h3-6mxw-7mvq)

### 1.4.12

- [release/1.4] Fix containerd fails to pull OCI image with non-`http(s)://` urls ([#6239](https://github.com/containerd/containerd/pull/6239)) [`e9f59a95e`](https://github.com/containerd/containerd/commit/e9f59a95ed5131d2a907fb26d4be2841e1787d28) Fix containerd fails to pull OCI image with non-`http(s)://` urls


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.4.12**, the newest release recorded here for this line.

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
