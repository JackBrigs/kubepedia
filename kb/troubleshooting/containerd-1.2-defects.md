---
id: TROUBLE-CONTAINERD_1_2_DEFECTS
type: troubleshooting
title: "containerd 1.2: defects fixed in the 1.2 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.2.0 <1.3.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - containerd 1.2 known issues
  - containerd 1.2 fixed in
  - is this containerd bug already fixed
tags:
  - troubleshooting
  - upgrade
  - containerd
sources:
  - type: docs
    path: containerd/containerd release notes for the 1.2 line — bug-fix entries
    url: https://github.com/containerd/containerd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# containerd 1.2: defects fixed in the 1.2 line

## Summary

**89 defects** the project fixed across **15 releases** of the 1.2 line, from 1.2.0 to
1.2.14. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.2.0

- Fixed an issue that a container can't be stopped when container processes are accidentally moved out of the container cgroups
- Fix stress test for image config opt requirements
- Fixes containerd-shim-runhcs State on exec id
- Fixes containerd-shim-runhcs Delete on exec id
- Fix panic when bufio Reader called in 2 goroutines
- Fix race in lcow snapshot scratch.vhdx creation
- typo: fix misspells in comments of containers/contaienrs.go
- fix delete running bundle dir when run t start cmd again
- fix when --config provided, don't need Image/RootFS
- Set default log formatting to use RFC3339Nano with fixed width
- update containerd/console to fix race: lock Cond before Signal
- Fix the formatting directives error during compilation
- Fix creation of DirectIO overwriting fifo config
- Bump continuity to fix copy files > 2^32 bytes
- Fix incorrect use of OCI runtime specs-go cgroup dev types
- console_linux: Fix race: lock Cond before Signal
- Fix reading from and writing to console on windows
- Fix an issue that container/sandbox can't be stopped
- Fix tarball ownership and containerd binary path for containerd

### 1.2.1

- Fix race in process state when pausing containers
- Fix a bug that containers sharing pod pid namespace can't be stopped
- fix pipe in broken may cause shim lock forever for runtime v1
- fix pipe in broken may cause shim lock forever for runtime v2

### 1.2.2

- Fix rare deadlock on FIFO creation with timeout
- Fix a bug that a container can't be stopped or inspected when its corresponding image is deleted
- Fix a bug that the cri plugin handles containerd events outside of `k8s.io` namespace
- Fix CI due to Golang 1.10.6 / 1.11.3 regressions (workaround)

### 1.2.3

- fix in Tar xattrs to restore compatibility with older container images [#2953](https://github.com/containerd/containerd/pull/2953)
- background `O_NONBLOCK` in OpenFifo to fix uncancelled context timeout issue
- runtime: exec race condition fixed [#2970](https://github.com/containerd/containerd/pull/2970)
- cri: fixed issues with extra newline character in log without an extra newline [#2984](https://github.com/containerd/containerd/pull/2984)
- cri: fixed an issue with pods being ignored after load failures [#2984](https://github.com/containerd/containerd/pull/2984)

### 1.2.4

- cri: Fix env performance issue [#1045](https://github.com/containerd/cri/pull/1045)

### 1.2.5

- Fix an issue that non-existent parent directory in image layers is created with permission
- Fix an issue that snapshots of the base image can be deleted by mistake, when images
- cri: Fix a bug that pod can't get started when the same volume is defined
- cri: Fix a bug that causes container start failure after in-place upgrade containerd
- cgroups updated to dbea6f2bd41658b84b00417ceefa416b97 to fix issues for systemd 420 and
- Fix /etc/hostname backward compatibility issue for in-place upgrade

### 1.2.6

- Fix a bug that custom containerd cgroup path does not work in containerd 1.2.5. [#3143](https://github.com/containerd/containerd/pull/3143)
- Fix a bug in the containerd client that `WithAllCapabilities` applies incomplete capability list. [#3147](https://github.com/containerd/containerd/pull/3147)
- Fix a bug that container output can be incomplete when stdout and stderr are pointed to the same file. [#3118](https://github.com/containerd/containerd/issues/3118)
- Fix a bug that containerd can't properly handle space in mount point path. [3161](https://github.com/containerd/containerd/pull/3161)
- cri: fix a bug that containers being gracefully stopped are SIGKILLed when kubelet is restarted. [cri#1098](https://github.com/containerd/cri/issues/1098)
- cri: Fix a bug that pod UTS namespace is used for host network. [cri#1111](https://github.com/containerd/cri/pull/1111)
- Update runc to v1.0.0-rc7-6-g029124da [#3183](https://github.com/containerd/containerd/pull/3183) to fix potential container start failure on non-SELinux system. [runc#2030](https://github.com/opencontainers/runc/issues/2030)
- fix parseInfoFile does not handle spaces in filenames

### 1.2.7

- Fix a bug that containerd shim leaks goroutine and file descriptor after containerd restarts. [ttrpc#37](https://github.com/containerd/ttrpc/pull/37)
- Fix a bug that a container can't be deleted if first deletion attempt is canceled or timeout. [#3264](https://github.com/containerd/containerd/pull/3264)
- Fix a bug that containerd leaks file descriptor when using v2 containerd shims, e.g. `containerd-shim-runc-v1`. [#3273](https://github.com/containerd/containerd/pull/3273)
- Fix a bug that a container with lingering processes can't terminate when it shares pid namespace with another container. [moby/moby#38978](https://github.com/moby/moby/issues/38978)
- Fix a bug that containerd can't read shim logs after restart. [#3282](https://github.com/containerd/containerd/pull/3282)
- Fix a bug that `shim_debug` option is not honored for existing containerd shims after containerd restarts. [#3283](https://github.com/containerd/containerd/pull/3283)
- cri: Fix a bug that a container can't be stopped when the exit event is not successfully published by the containerd shim. [#3125](https://github.com/containerd/containerd/issues/3125), [#3177](https://github.com/containerd/containerd/issues/3177)
- cri: Fix a bug that exec process is not cleaned up if grpc context is canceled or timeout. [cri#1159](https://github.com/containerd/cri/pull/1159)
- Fix a selinux keyring labeling issue by updating runc to v1.0.0-rc.8 and selinux library to v1.2.2. [opencontainers/selinux#50](https://github.com/opencontainers/selinux/pull/50)

### 1.2.8

- Skip rootfs unmount when no mounts are provided. Fixed by [PR #3148](https://github.com/containerd/containerd/pull/3148) {cherry-picked as [PR #3402](https://github.com/containerd/containerd/pull/3402)}
- Close inherited socket file descriptor. Fixed in [PR #3359](https://github.com/containerd/containerd/pull/3359) {cherry-picked as [PR #3364](https://github.com/containerd/containerd/pull/3364)}
- Call CloseIO when stdin closes in ctr. Fixed by [PR #3462](https://github.com/containerd/containerd/pull/3462) {cherry-picked as [PR 3490](https://github.com/containerd/containerd/pull/3490)}
- Several multi-arch image fixes, including: ARM platform matching, selecting the proper manifest, and limited to best matched manifest to solve discrepancies with multi-arch image operations. Backported [PR #3270](https://github.com/containerd/containerd/pull/3270) as [PR #3404](https://github.com/containerd/containerd/pull/3404), [PR #3484](https://github.com/containerd/containerd/pull/3484) as [PR #3512](https://github.com/containerd/containerd/pull/3512), and added [PR #3421](https://github.com/containerd/containerd/pull/3421)
- Override image's environment config with process config; including backport of fixes and tests for merging/replacing env variables; fix in [PR #3542](https://github.com/containerd/containerd/pull/3542), backported via [PR #3546](https://github.com/containerd/containerd/pull/3546) which included a backport of [PR #2887](https://github.com/containerd/containerd/pull/2887). Additional fix to logic for override re: image `$PATH` cherry-picked in [PR #3565](https://github.com/containerd/containerd/pull/3565)
- Shim hang fix in master via [PR #3540](https://github.com/containerd/containerd/pull/3540) backported to `release/1.2` via [PR #3561](https://github.com/containerd/containerd/pull/3561)
- CRI: Fix a bug that if an image is deleted immediately after being pulled, the image may still exist after the deletion finishes successfully. (https://github.com/containerd/cri/issues/1161)
- CRI: Fix a bug that `runc` and `crictl` binaries shipped in https://storage.googleapis.com/cri-containerd-release are versioned with the containerd version. (https://github.com/containerd/cri/pull/1193)
- CRI: Fix a bug that the images become unusable if 2 images have the same image ID and RepoTag, but different RepoDigests. (https://github.com/containerd/containerd/issues/3401)
- CRI: Fix [ProcMount](https://stupefied-goodall-e282f7.netlify.com/contributors/design-proposals/auth/proc-mount-type/) support (https://github.com/containerd/cri/pull/1216). ***NOTE: To use containerd 1.2.8+ with Kubernetes 1.11 or below, you MUST set `disable_proc_mount=true` in the cri plugin config.*** (https://github.com/containerd/cri/issues/1208)
- CRI: Fix a bug that containerd tries to connect image registry with `https` even if the `http` endpoint is configured. (https://github.com/containerd/cri/issues/1201)

### 1.2.9

- CRI fixes: Fix a bug that the default apparmor profile is mistakenly applied to privileged containers with runtime/default specified. [containerd/cri#1239](https://github.com/containerd/cri/issues/1239) Fix a bug that image can't be pulled if an empty AuthConfig is specified. [containerd/cri#1249](https://github.com/containerd/cri/issues/1249)
- Bug fix: Compute manifest data when not provided (Docker-Content-Digest header missing). [PR #3591](https://github.com/containerd/containerd/pull/3591) {cherry-picked from master [PR #3245](https://github.com/containerd/containerd/pull/3245) with backports of [#2871](https://github.com/containerd/containerd/pull/2871) and [#3335](https://github.com/containerd/containerd/pull/3335) required}
- Bug fix: Use default UNIX env when image has no environment. [PR #3601](https://github.com/containerd/containerd/pull/3601) {cherry-picked from master branch [PR #3599](https://github.com/containerd/containerd/pull/3599)}
- Bug fix: archive: truncate modification time. [PR #3602](https://github.com/containerd/containerd/pull/3602) {cherry-picked from master branch [PR #3589](https://github.com/containerd/containerd/pull/3589)}
- Bug fix: zfs: Datasets don't seem to be cleaned up properly on image removal. Reported in [containerd/zfs#22](https://github.com/containerd/zfs/issues/22) and fixed by [PR containerd/zfs#24](https://github.com/containerd/zfs/pull/24) and re-vendored into containerd `release/1.2` via [PR #3596](https://github.com/containerd/containerd/pull/3596)
- fix: support empty auth config for anonymous registry

### 1.2.10

- CRI fixes: Fix a bug that the default UNIX path is not in the default OCI config via the CRI plugin. Reported in [containerd/cri#1279](https://github.com/containerd/cri/issues/1279) and fixed by [containerd/cri#1283](https://github.com/containerd/cri/pull/1283)
- Backport fix for default UNIX environment in OCI container config
- Fix Method of judging command execution failure

### 1.2.11

- Add local-fs.target to service file to fix corrupt image after unexpected host reboot. Reported in [containerd/containerd#3671](https://github.com/containerd/containerd/issues/3671), and fixed by [containerd/containerd#3746](https://github.com/containerd/containerd/pull/3746)
- CRI fixes: Fix shim delete error code to avoid unnecessary retries in the CRI plugin. Discovered in [containerd/cri#1309](https://github.com/containerd/cri/issues/1309), and fixed by [containerd/containerd#3732](https://github.com/containerd/containerd/pull/3732) and [containerd/containerd#3739](https://github.com/containerd/containerd/pull/3739)
- Fix delete error code on the containerd daemon side

### 1.2.12

- A fix to prevent `SIGSEGV` when starting containerd-shim [containerd/containerd#3960](https://github.com/containerd/containerd/pull/3960)
- Fixes to `exec` [containerd/containerd#3755](https://github.com/containerd/containerd/pull/3755) Prevent `docker exec` hanging if an earlier `docker exec` left a zombie process Prevent High system load/CPU utilization with liveness and readiness probes Prevent Docker healthcheck causing high CPU utilization
- Fix API filters to properly handle and return parse errors [containerd/containerd#3950](https://github.com/containerd/containerd/pull/3950)
- Fix containerd build, use `libbtrfs-dev` when available

### 1.2.13

- Fix container pid race condition [containerd#4025](https://github.com/containerd/containerd/pull/4025)
- Fix incorrect comment from copy/paste of starting script
- fixed an issue with invalid soft memory limits

### 1.2.14

- Fix regression pushing manifests as octet stream [#4268](https://github.com/containerd/containerd/pull/4268)
- Add comment clarifying fix for security issue
- Fix incorrect backport of setting octet-stream


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.2.14**, the newest release recorded here for this line.

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
