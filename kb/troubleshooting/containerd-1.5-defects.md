---
id: TROUBLE-CONTAINERD_1_5_DEFECTS
type: troubleshooting
title: "containerd 1.5: defects fixed in the 1.5 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.5.0 <1.6.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - containerd 1.5 known issues
  - containerd 1.5 fixed in
  - is this containerd bug already fixed
tags:
  - troubleshooting
  - upgrade
  - containerd
sources:
  - type: docs
    path: containerd/containerd release notes for the 1.5 line — bug-fix entries
    url: https://github.com/containerd/containerd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# containerd 1.5: defects fixed in the 1.5 line

## Summary

**110 defects** the project fixed across **16 releases** of the 1.5 line, from 1.5.0 to
1.5.18. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.5.0

- Fix PushHandler cannot push image that contains duplicated blobs
- Fix backword-compatibility issue of non-versioned config file
- Update go-winio to fix compile error on armv7
- runtime/v2/runc: fix the defer cleanup of the NewContainer
- rootfs: fix the error handling of the createInitLayer
- Fix unsupported files exporting functions for apparmor and seccomp
- Fix error checking when resolving shim binary path
- cio.copyIO: fix pipes potentially not being closed (Windows)
- cri/config: fix range iterator issue in ValidatePluginConfig
- Fix Windows service panic file to not be read-only
- Fix package name in cri runtimeoptions protobuf
- Update btrfs vendor for chkptr fix for Go >= 1.14
- ctr: fix the incorrect image unmount error hint
- fix: always set unknown to false when handling exit event
- fix no-pivot not working in io.containerd.runtime.v1.linux
- fix `make test` failure of missing sha256 package
- cr: fix checkpoint from image getting skipped
- BUILDING.md: fix description about static builds
- Specify version = 2 & fix wrong key in registry.md (GCR example)
- config: fix TOML tag for TolerateMissingHugePagesCgroupController
- Increase port-forward timeout to 1s to fix e2e test
- vendor: update go-events to fix alignment for 32bit systems
- fix incomplete host device for PrivilegedWithoutHostDevices
- update selinux dependency to fix test failures
- Fix store error serialization to gRPC status codes
- Fix containerd build, use `libbtrfs-dev` when available
- Update cri-tools to fix all image reference test failure
- fix: support empty auth config for anonymous registry
- Update containerd to fix panic caused by race condition
- Fix /etc/hostname backward compatibility issue for in-place upgrade
- Fix the issue that pod or container config file without metadata will crash containerd
- Fix an issue that container/sandbox can't be stopped
- Bump continuity to fix copy files > 2^32 bytes
- Fix tarball ownership and containerd binary path for containerd
- Add KUBE_CONTAINER_RUNTIME_NAME to fix fluentd support
- Fix for kube-up.sh and update several documments
- Fix a log line and also set containerd log level to debug in node e2e
- Fix one line of log, we are writing not reading
- Update containerd to include the gcr private registry fix
- Add toml config file for cri-containerd fix #182
- Checkpoint and restart recovery fix part of #120
- Update docker and cri-o to include the sirupsen fix
- Fix a race that fake execution client sends event to closed channel
- v2: ebpf: replace deprecated prog.Attach/prog.Detach and fix closer
- Fix ptsname() for big-endian architectures (again)
- Fix actions to follow the model from other repos
- Fix usage calculation to account for sparse files
- Temporarily disable EXC0002 until GoDoc is fixed in this repo
- Fix a regression of windows build issue of undefined symbol
- README: fix JSON syntax-error, and reformat JSON examples
- fix bug, failed to assert net error due to error wrap

### 1.5.1

- **Fix registry mirror authorization logic in CRI plugin** [#5446](https://github.com/containerd/containerd/pull/5446)
- **Fix regression in cri-cni-release to include cri tools** [#5462](https://github.com/containerd/containerd/pull/5462)
- Fix different registry hosts referencing the same auth config

### 1.5.3

- **Fix invalid validation error checking** [#5565](https://github.com/containerd/containerd/pull/5565)
- **Fix error on image pull resume** [#5560](https://github.com/containerd/containerd/pull/5560)
- **Fix User Agent sent to registry authentication server** [#5533](https://github.com/containerd/containerd/pull/5533)
- **Fix symlink resolution for disk mounts on Windows** [#5411](https://github.com/containerd/containerd/pull/5411)
- Fix missing Body.Close() calls on push to docker remote
- Fix incorrect UA used for registry authentication

### 1.5.5

- remotes/docker/pusher.go: Fix missing Close()
- remotes/docker/fetcher.go: Fix missing Close()

### 1.5.6

- **Update hcsshim to v0.8.21 to fix layer issue on Windows Server 2019** [#5942](https://github.com/containerd/containerd/pull/5942)
- **Add support for 'clone3' syscall to fix issue with certain images when seccomp is enabled** [#5982](https://github.com/containerd/containerd/pull/5982)
- **Fix panic in metadata content writer on copy error** [#6043](https://github.com/containerd/containerd/pull/6043)
- Fix panic in metadata content writer on copy error
- Fix content copy to not ignore unexpected EOF

### 1.5.7

- **Fix insufficiently restricted permissions on container root and plugin directories** [GHSA-c2h3-6mxw-7mvq](https://github.com/containerd/containerd/security/advisories/GHSA-c2h3-6mxw-7mvq)

### 1.5.8

- [release/1.5] Fix containerd fails to pull OCI image with non-`http(s)://` urls ([#6238](https://github.com/containerd/containerd/pull/6238)) [`01428ec40`](https://github.com/containerd/containerd/commit/01428ec4095d23727d227e5602690a2ad356d02f) Fix containerd fails to pull OCI image with non-`http(s)://` urls
- [release/1.5] Use deactivatelayer to recover layers that we cannot rename ([#6133](https://github.com/containerd/containerd/pull/6133)) [`16762f3e5`](https://github.com/containerd/containerd/commit/16762f3e5c26688dd7482b9b880f1b46e4185661) Fix spelling mistake in Windows snapshotter [`6094bc770`](https://github.com/containerd/containerd/commit/6094bc77050820c5433c2281d9f3e2a0883eb580) Use DeactivateLayer to recover layers that we cannot rename
- [release/1.5] Fix pull fails on unexpected EOF ([#6117](https://github.com/containerd/containerd/pull/6117)) [`aa7c9d9da`](https://github.com/containerd/containerd/commit/aa7c9d9daf5876311c4a77bb445c51225ba19956) Fix pull fails on unexpected EOF

### 1.5.9

- **Fix unprivileged pod using 'hostPath' bypassing SELinux labels** ([GHSA-mvff-h3cj-wj9c](https://github.com/containerd/containerd/security/advisories/GHSA-mvff-h3cj-wj9c))
- **Fix setting the "container_kvm_t" SELinux label**
- [release/1.5] seutil: Fix setting the "container_kvm_t" label ([#6381](https://github.com/containerd/containerd/pull/6381)) [`da5749b67`](https://github.com/containerd/containerd/commit/da5749b670823abd3fa03298c2e89cd22c8bfb6d) seutil: Fix setting the "container_kvm_t" label

### 1.5.11

- **Fix the inheritable capability defaults** ([GHSA-c9cp-9c75-9v8c](https://github.com/containerd/containerd/security/advisories/GHSA-c9cp-9c75-9v8c))
- [release/1.5] fix critools installation ([#6718](https://github.com/containerd/containerd/pull/6718)) Update get to install for cri tools
- Github Security Advisory [GHSA-c9cp-9c75-9v8c](https://github.com/containerd/containerd/security/advisories/GHSA-c9cp-9c75-9v8c) Fix the Inheritable capability defaults

### 1.5.12

- **Fix inotify fd leak when cgroup is deleted**
- **Fix deadlock from abandoned transactions in native snapshotter**
- [release/1.5] fix #6054 MaxConcurrentDownloads is not effect when Unpack is true ([#6774](https://github.com/containerd/containerd/pull/6774)) [`4dbd0c851`](https://github.com/containerd/containerd/commit/4dbd0c851b9b0cb0d8b02c44d72c311a25a2512a) fix #6054 MaxConcurrentDownloads is not effect when Unpack is true
- [release/1.5 backport] native: fix deadlock from leaving transactions open ([#6726](https://github.com/containerd/containerd/pull/6726)) [`603ef55e0`](https://github.com/containerd/containerd/commit/603ef55e0e696b382ad08d83168d608f54f1b6e2) native: fix deadlock from leaving transactions open
- v2: Fix inotify fd leak when cgroup is deleted ([#212](https://github.com/containerd/cgroups/pull/212)) [`a7d6888`](https://github.com/containerd/cgroups/commit/a7d6888aa30218c8aff15d979eb3f6aec0b7979c) v2: add test case for Manager.EventChan() behavior [`cf1f978`](https://github.com/containerd/cgroups/commit/cf1f978b93bf784118d3ab7dec6a47b8204918c2) v2: flip error handling for readKVStat("memory.events") to reduce indentation [`6a46df2`](https://github.com/containerd/cgroups/commit/6a46df25065d551a8d998495c34263354c84f2c1) v2: manager: factor out memory.events parsing [`35b5b55`](https://github.com/containerd/cgroups/commit/35b5b55c686080de64facf127d6d6a5ca9a0fe6b) v2: Fix inotify leak when cgroup is deleted
- fix Implicit memory aliasing in for loop ([#214](https://github.com/containerd/cgroups/pull/214)) [`182c3af`](https://github.com/containerd/cgroups/commit/182c3afa53b8cccce0611cca9dee46410c4f82f7) fix Implicit memory aliasing in for loop
- Fix potential dirfd leak. ([#210](https://github.com/containerd/cgroups/pull/210)) [`17fece8`](https://github.com/containerd/cgroups/commit/17fece81870ef8aa1a31f05210b8f425e37038a0) Fix potential dirfd leak

### 1.5.13

- **Fix ExecSync handler to cap console output size** ([GHSA-5ffw-gxpp-mxpf](https://github.com/containerd/containerd/security/advisories/GHSA-5ffw-gxpp-mxpf))

### 1.5.14

- **Fix WWW-Authenticate parsing to allow empty quoted string**
- **Fix createTarFile: make xattr EPERM non-fatal**
- **Fix dockerPusher to handle abort correctly**
- **Fix CRI: PodSandboxStatus should tolerate missing task**
- **Fix io.containerd.runc.v1: Stats() shouldn't assume s.container is non-nil**
- [release/1.5] cherry-pick: remotes: fix dockerPusher to handle abort correctly ([#7467](https://github.com/containerd/containerd/pull/7467)) [`2fe813d36`](https://github.com/containerd/containerd/commit/2fe813d368ffc5e1224e0748b30d6d240b858250) remotes: fix dockerPusher to handle abort correctly
- [release 1.5 backport] Fix cleanup in critest ([#7275](https://github.com/containerd/containerd/pull/7275)) [`c2ace6ebc`](https://github.com/containerd/containerd/commit/c2ace6ebc8bf3cda5faee1c4861670257f238bed) Fix cleanup in critest
- [release/1.5] Fix WWW-Authenticate parsing ([#7132](https://github.com/containerd/containerd/pull/7132)) [`8ae864ae9`](https://github.com/containerd/containerd/commit/8ae864ae9871d8f7d16c5f21cd9d54e5fcaabd97) [release/1.5] Fix WWW-Authenticate parsing
- [release/1.5] ctr: fix label args used in NewContainer ([#7071](https://github.com/containerd/containerd/pull/7071)) [`febb0e82d`](https://github.com/containerd/containerd/commit/febb0e82d6c6a8974fc2b3bdfa80a92895106fa6) ctr: fix label args used in NewContainer

### 1.5.15

- **Fix CNI leaks by changing pod network setup order in CRI plugin**
- **Fix lease labels unexpectedly overwriting expiration**
- [release/1.5] cherry-pick: Fix order of operations when setting lease labels ([#7746](https://github.com/containerd/containerd/pull/7746)) Fix order of operations when setting lease labels
- [release/1.5] retry request on writer reset ([#7479](https://github.com/containerd/containerd/pull/7479)) fix pusher concurrent close channel retry request on writer reset
- [release/1.5] feat: support import image for specific platform ([#7595](https://github.com/containerd/containerd/pull/7595)) fix: wrong flag type feat: support import image for specific platform
- Fix wrapping errors ([#196](https://github.com/containerd/continuity/pull/196)) fs: fix wrapping nil err fmt.Errorf: use %w, not %v to wrap errors
- fix fmt.Errorf("%w", err) on err == nil ([#187](https://github.com/containerd/continuity/pull/187)) fix fmt.Errorf("%w", err) on err == nil
- Fix darwin issues ([#186](https://github.com/containerd/continuity/pull/186)) update AUTHORS darwin: use utimensat syscall instead of utimes fix darwin usage of du command

### 1.5.16

- **Fix goroutine leak during Exec in CRI plugin** ([GHSA-2qjp-425j-52j9](https://github.com/containerd/containerd/security/advisories/GHSA-2qjp-425j-52j9))
- Github Security Advisory [GHSA-2qjp-425j-52j9](https://github.com/containerd/containerd/security/advisories/GHSA-2qjp-425j-52j9) Prepare release notes for v1.5.16 CRI stream server: Fix goroutine leak in Exec

### 1.5.17

- **Fix no CNI info for pod sandbox on restart**
- [release/1.5] CRI: Fix no CNI info for pod sandbox on restart ([#7849](https://github.com/containerd/containerd/pull/7849)) [`23c2a863e`](https://github.com/containerd/containerd/commit/23c2a863e338c6e1ddb2bb56d1b2e35f118f5284) CRI: Fix no CNI info for pod sandbox on restart

### 1.5.18

- **Fix supplementary groups not being set up properly** ([GHSA-hmfx-3pcx-653p](https://github.com/containerd/containerd/security/advisories/GHSA-hmfx-3pcx-653p))
- **Fix OCI image importer memory exhaustion** ([GHSA-259w-8hf6-59c2](https://github.com/containerd/containerd/security/advisories/GHSA-259w-8hf6-59c2))
- Github Security Advisory [GHSA-hmfx-3pcx-653p](https://github.com/containerd/containerd/security/advisories/GHSA-hmfx-3pcx-653p) [`a62c38bf2`](https://github.com/containerd/containerd/commit/a62c38bf2173faa813018939710fc8491e4f7dba) oci: fix additional GIDs [`3b89da580`](https://github.com/containerd/containerd/commit/3b89da580b76471d6c03cb1fc6c14db6aa23d3db) oci: fix loop iterator aliasing [`b07ec6b25`](https://github.com/containerd/containerd/commit/b07ec6b251bd51f06bc72ef408f31e3f6e6e87f9) oci: skip checking gid for WithAppendAdditionalGroups [`356672cb5`](https://github.com/containerd/containerd/commit/356672cb56fd5a0eed11e5089ac824c7ab09ffac) refactor: reduce duplicate code [`6a7b7617c`](https://github.com/containerd/containerd/commit/6a7b7617cfbd90009a2e05e0e5eff4ef92028d7b) add WithAdditionalGIDs test [`832bcf300`](https://github.com/containerd/containerd/commit/832bcf300b1ec29c9b08326aab2d4eafee58dd85) add WithAppendAdditionalGroups helper
- [release/1.5] Fix retry logic within devmapper device deactivation ([#8089](https://github.com/containerd/containerd/pull/8089)) [`0d16d045d`](https://github.com/containerd/containerd/commit/0d16d045dfd0d800a00dc362736b815f6cc96de8) Fix retry logic within devmapper device deactivation


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.5.18**, the newest release recorded here for this line.

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
