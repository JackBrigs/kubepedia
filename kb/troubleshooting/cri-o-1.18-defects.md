---
id: TROUBLE-CRI_O_1_18_DEFECTS
type: troubleshooting
title: "cri-o 1.18: defects fixed in the 1.18 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.18.0 <1.19.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cri-o 1.18 known issues
  - cri-o 1.18 fixed in
  - is this cri-o bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cri-o
sources:
  - type: docs
    path: cri-o/cri-o release notes for the 1.18 line — bug-fix entries
    url: https://github.com/cri-o/cri-o/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cri-o 1.18: defects fixed in the 1.18 line

## Summary

**21 defects** the project fixed across **7 releases** of the 1.18 line, from 1.18.0 to
1.18.6. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.18.0

- Fix bug in `crio version` output where the linkmode cannot be retrieved because of non absolute paths of the executable ([#3627](https://github.com/cri-o/cri-o/pull/3627), [@saschagrunert](https://github.com/saschagrunert))
- Fixed CRI-O to fail to start when `runc` is no configured runtime and the `runc` binary is not in `$PATH` ([#3367](https://github.com/cri-o/cri-o/pull/3367), [@saschagrunert](https://github.com/saschagrunert))
- Fixed SIGHUP reload for drop-in configuration files ([#3241](https://github.com/cri-o/cri-o/pull/3241), [@saschagrunert](https://github.com/saschagrunert))
- Fixed glibc static binary bug to not resolve DNS correctly ([#3615](https://github.com/cri-o/cri-o/pull/3615), [@saschagrunert](https://github.com/saschagrunert))
- Fix bug resulting in false reports of OOM ([#3423](https://github.com/cri-o/cri-o/pull/3423), [@haircommander](https://github.com/haircommander))

### 1.18.1

- Fix linkmode retrieval on `crio version` for static binaries ([#3734](https://github.com/cri-o/cri-o/pull/3734), [@saschagrunert](https://github.com/saschagrunert))
- Fix a bug where CRI-O could not start a container if CONFIG_CGROUP_HUGETLB was not set in the kernel ([#3721](https://github.com/cri-o/cri-o/pull/3721), [@haircommander](https://github.com/haircommander))
- Fix some `crio version` oddities ([#3688](https://github.com/cri-o/cri-o/pull/3688), [@haircommander](https://github.com/haircommander))

### 1.18.2

- Fixed bug where Pod creation would fail if Uid was not specified in Metadata of sandbox config passed in a run pod sandbox request ([#3829](https://github.com/cri-o/cri-o/pull/3829), [@haircommander](https://github.com/haircommander))

### 1.18.3

- Fixed bug where pod names would sometimes leak on creation, causing the kubelet to fail to recreate (#3950, @haircommander)

### 1.18.4

- Fixed regression where it was not able to run exec any more when compiling CRI-O with newer go versions ([#4192](https://github.com/cri-o/cri-o/pull/4192), [@saschagrunert](https://github.com/saschagrunert))
- Fix a bug where a sudden reboot causes incomplete image writes. This could cause image storage to be corrupted, resulting in an error `layer not known`. ([#3972](https://github.com/cri-o/cri-o/pull/3972), [@giuseppe](https://github.com/giuseppe))
- Fixed a bug where a container creation failure caused that container to leak in the runtime ([#4237](https://github.com/cri-o/cri-o/pull/4237), [@haircommander](https://github.com/haircommander))
- Fixed a bug where exec sync requests (manually or automatically triggered via readiness/liveness probes) overwrite the runtime `info.runtimeSpec.process.args` of the container status (for example via `crictl inspect`). ([#3992](https://github.com/cri-o/cri-o/pull/3992), [@openshift-cherrypick-robot](https://github.com/openshift-cherrypick-robot))
- Fix bug where empty config fields having to do with storage cause `/info` requests to return incorrect information (which causes cadvisor to fail to read imageFs information) ([#4176](https://github.com/cri-o/cri-o/pull/4176), [@openshift-cherrypick-robot](https://github.com/openshift-cherrypick-robot))
- Fixed crio restart behavior to make sure that Pod creation timestamps are restored and the order in the list of pods stays stable across restarts ([#4010](https://github.com/cri-o/cri-o/pull/4010), [@openshift-cherrypick-robot](https://github.com/openshift-cherrypick-robot))

### 1.18.5

- Fixed a bug where crictl only showed pod level stats, not container level stats. (#4043, @haircommander)
- Fix a bug where CollectMode wouldn't be set if the feature was backported to systemd (in RHEL/CentOS 7, for instance) (#4572, @openshift-cherrypick-robot)
- Fix a bug where containers didn't have a finished time set when using the "vm" style runtimes. (#4498, @openshift-cherrypick-robot)
- Fix running privileged systemd containers with bidirectional mounts (#4583, @giuseppe)

### 1.18.6

- Fixed invalid version in `crio version` output


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.18.6**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `cri-o/cri-o`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/cri-o.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
