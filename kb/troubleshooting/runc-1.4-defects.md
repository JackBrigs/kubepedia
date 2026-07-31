---
id: TROUBLE-RUNC_1_4_DEFECTS
type: troubleshooting
title: "runc 1.4: defects fixed in the 1.4 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.4.0 <1.5.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - runc 1.4 known issues
  - runc 1.4 fixed in
  - is this runc bug already fixed
tags:
  - troubleshooting
  - upgrade
  - runc
sources:
  - type: docs
    path: opencontainers/runc release notes for the 1.4 line — bug-fix entries
    url: https://github.com/opencontainers/runc/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# runc 1.4: defects fixed in the 1.4 line

## Summary

**17 defects** the project fixed across **4 releases** of the 1.4 line, from 1.4.0 to
1.4.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.4.0

- cgroups: provide iocost statistics for cgroupv2. (opencontainers/cgroups#43)
- cgroups: retry DBus connection when it fails with EAGAIN. (opencontainers/cgroups#45)
- cgroups: improve `cpuacct.usage_all` resilience when parsing data from patched kernels (such as the Tencent kernels). (opencontainers/cgroups#46, opencontainers/cgroups#50)
- libct: close child fds on `prepareCgroupFD` error. (#4936)
- Fix various file descriptor leaks and add additional tests to detect them as comprehensively as possible. (#5007, #5021, #5034)

### 1.4.1

- libct: fix panic in `initSystemdProps` when processing certain systemd properties in the OCI spec. (#5161, #5133)
- libct: fix several file descriptor leaks on error paths. (#5168, #5009)
- Remove unnecessary `crypto/tls` dependency by open-coding the systemd socket activation logic, allowing us to more easily avoid false positive CVE warnings. (#5093, #5057)
- Remove legacy `os.Is*` error usage, improving error type detection to make our error fallback paths more robust. (#5162, #5061)
- Go 1.26 has started enforcing a restriction of `os/exec.Cmd` which caused issues with our usage of `CLONE_INTO_CGROUP` (on newer kernels). This has now been resolved. (#5116, #5091)
- Recursive `atime`-related mount flags (`rrelatime` et al.) are now applied properly. (#5114, #5098)
- Fix a regression in `runc exec` due to `CLONE_INTO_CGROUP` in the (inadvisable) scenario where a container is configured without cgroup namespaces and with `/sys/fs/cgroup` mounted `rw`. (#5117, #5101)
- On machines with more than 1024 CPU cores, our logic for resetting the CPU affinity will now correctly reset the affinity onto _all_ available cores (not just the first 1024). (#5149, #5025)
- PR #4757 caused a regression that resulted in spurious `cannot start a container that has stopped` errors when running `runc create` and has thus been reverted. (#5157, #5153, #5151, #4645, #4757)

### 1.4.2

- A regression in runc v1.3.0 which can result in a stuck `runc exec` or `runc run` when the container process runs for a short time. (#5208, #5210, #5216)
- Mount sources that need to be open on the host are now closed earlier during container start, reducing the total amount of used file descriptors and helping to avoid hitting the open files limit when handling many such mounts. (#5177, #5201)

### 1.4.3

- Various integration test improvements. (#5222, #5237, #5226, #5229, #5239, #5249, #5269, #5287, #5295, #5304)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.4.3**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `opencontainers/runc`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/runc.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
