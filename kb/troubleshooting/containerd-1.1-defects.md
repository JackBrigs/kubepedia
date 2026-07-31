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

**33 defects** the project fixed across **6 releases** of the 1.1 line, from 1.1.0 to
1.1.7. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.1.0

- Fix label being put on snapshot instead of content
- services/content: fix reading a blob which is smaller than the read buffer
- Update cgroups vendor for license headers/bug fix
- archive: fix logic for skipping mknod when running in userns
- Fix duplicate directories entries on metadata change
- Fix race condition in IO test (TestNewAttach)

### 1.1.1

- Fixes for working set memory calculation, privileged container creation and
- Fix a bug that container running as non-root will get capabilities added by user. This is fixed to keep the behavior consistent with Docker
- Fix startup panic when overlayfs fails to load, now cri plugin will just fail
- Fix for a size validation bug with some registries which impacts the CRI plugin and clients
- Bump continuity to fix copy files > 2^32 bytes

### 1.1.4

- Fix an issue that container/sandbox can't be stopped

### 1.1.5

- Fix a bug that containerd-shim may hang when many exec processes simultaneously
- Fix a bug that IPAM IP leaks after node reboot
- Ignore modprobe failures in systemd ExecStartPre. This fixes containerd start
- fix pipe in broken may cause shim lock forever for runtime v1

### 1.1.6

- containerd/cri#991 Remove container lifecycle image dependency (fixes containerd/cri#990)
- containerd/cri#1016 Specify platform for image pull (fixes containerd/cri#1015)
- containerd/cri#1027 Fix the log ending newline handling (fixes containerd/cri#1026)
- containerd/cri#1042 Set /etc/hostname (fixes containerd/cri#1041)
- containerd/cri#1045 Fix env performance issue (fixes containerd/cri#1044)
- Fix CI due to Golang 1.10.6 / 1.11.3 regressions (workaround)
- fix pid reuse attack when kill a exec process

### 1.1.7

- Fix an issue that non-existent parent directory in image layers is created with permission `0700`. [#3017](https://github.com/containerd/containerd/issues/3017)
- Fix an issue that snapshots of the base image can be deleted by mistake, when images built on top of it are deleted. [#3088](https://github.com/containerd/containerd/pull/3088)
- Fix a bug that container output can be incomplete when stdout and stderr are pointed to the same file. [#3156](https://github.com/containerd/containerd/issues/3156)
- cri: fix a bug that pod can't get started when the same volume is defined differently in the image and the pod spec. [cri#1059](https://github.com/containerd/cri/issues/1059)
- cri: fix a bug that causes container start failure after in-place upgrade containerd to 1.2.4+ or 1.1.6+. [cri#1082](https://github.com/containerd/cri/issues/1082)
- cri: fix a bug that containers being gracefully stopped are SIGKILLed when kubelet is restarted. [cri#1098](https://github.com/containerd/cri/issues/1098)
- cri: Fix a bug that pod UTS namespace is used for host network. [cri#1111](https://github.com/containerd/cri/pull/1111)
- Fix the formatting directives error during compilation
- Fix incorrect use of OCI runtime specs-go cgroup dev types
- Fix /etc/hostname backward compatibility issue for in-place upgrade


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.1.7**, the newest release recorded here for this line.

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
