---
id: TROUBLE-RUNC_1_1_DEFECTS
type: troubleshooting
title: "runc 1.1: defects fixed in the 1.1 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.1.0 <1.2.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - runc 1.1 known issues
  - runc 1.1 fixed in
  - is this runc bug already fixed
tags:
  - troubleshooting
  - upgrade
  - runc
sources:
  - type: docs
    path: opencontainers/runc release notes for the 1.1 line — bug-fix entries
    url: https://github.com/opencontainers/runc/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# runc 1.1: defects fixed in the 1.1 line

## Summary

**15 defects** the project fixed across **7 releases** of the 1.1 line, from 1.1.4 to
1.1.11. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.1.4

- Fix mounting via wrong proc fd. When the user and mount namespaces are used, and the bind mount is followed by the cgroup mount in the spec, the cgroup was mounted using the bind mount's mount fd. (#3511)
- Fix "permission denied" error from `runc run` on `noexec` fs. (#3541)
- Fix failed exec after `systemctl daemon-reload`. Due to a regression in v1.1.3, the `DeviceAllow=char-pts rwm` rule was no longer added and was causing an error `open /dev/pts/0: operation not permitted: unknown` when systemd was reloaded. (#3554)

### 1.1.5

- Fix the inability to use `/dev/null` when inside a container. (#3620)
- Fix changing the ownership of host's `/dev/null` caused by fd redirection (a regression in 1.1.1). (#3674, #3731)
- Fix rare runc exec/enter unshare error on older kernels, including CentOS < 7.7. (#3776)

### 1.1.7

- When used with systemd v240+, systemd cgroup drivers no longer skip `DeviceAllow` rules if the device does not exist (a regression introduced in runc 1.1.3). This fix also reverts the workaround added in runc 1.1.5, removing an extra warning emitted by runc run/start. (#3845, #3708, #3671)

### 1.1.8

- libct: fix a race with systemd removal. (#3877)
- Fix tmpfs mode opts when dir already exists. (#3916)

### 1.1.9

- Fixed losing sticky bit on tmpfs (a regression in 1.1.8). (#3952, #3961)
- intelrdt: fixed ignoring ClosID on some systems. (#3550, #3978)

### 1.1.10

- Fixed permissions of a newly created directories to not depend on the value of umask in tmpcopyup feature implementation. (#3991, #4060)
- libcontainer: cgroup v1 GetStats now ignores missing `kmem.limit_in_bytes` (fixes the compatibility with Linux kernel 6.1+). (#4028)
- Fix a semi-arbitrary cgroup write bug when given a malicious hugetlb configuration. This issue is not a security issue because it requires a malicious `config.json`, which is outside of our threat model. (#4103)

### 1.1.11

- Fix several issues with userns path handling. (#4122, #4124, #4134, #4144)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.1.11**, the newest release recorded here for this line.

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
