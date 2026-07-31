---
id: TROUBLE-CRI_O_1_16_DEFECTS
type: troubleshooting
title: "cri-o 1.16: defects fixed in the 1.16 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.16.0 <1.17.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cri-o 1.16 known issues
  - cri-o 1.16 fixed in
  - is this cri-o bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cri-o
sources:
  - type: docs
    path: cri-o/cri-o release notes for the 1.16 line — bug-fix entries
    url: https://github.com/cri-o/cri-o/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cri-o 1.16: defects fixed in the 1.16 line

## Summary

**20 defects** the project fixed across **1 releases** of the 1.16 line, from 1.16.0 to
1.16.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.16.0

- 7deb5e656 fix specfile for hack/build-rpms.sh
- 7f50ff083 Fix server restore to not remove podman containers
- 62bf91528 fix selinux label on volume mount directory creation
- 6a4d9f935 Fix invalid log_dir position in crio.conf
- e8e8d7252 Fix possible segmentation fault on restore when runtime_type changes
- 13a874dc4 cleanup: fix typo words in config.go
- 01d71e2f1 Fix hostport mapping for IPv6 addresses
- a677466e3 crio-wipe: Fix int compare in lib.bash
- c6ebf8427 main.go: flag help message error fix
- 8f47f37ac Fix documentation for IP based sandbox methods
- 49521cc19 Fix parse of memory.limit_in_bytes on 32-bit machines
- 96d782cce Fix documentation between crio.8.md and source
- 8d994c4a9 Fix `signature_policy` value in man page
- 4f5f0e78e Fix `no_pivot` boolean style in man page
- e33303c5c Fix `ctr_stop_timeout` value in man page
- 6f0e47f5c Fix wrong `file_locking_path` in man page
- 098a0bdd0 Fix `default_mounts_file` documentation
- bc47270e2 Fix git-vars target for shells which do not default to bash
- af0c1b274 Fix invalid CRIO_ROOT for integration tests
- 0db55c324 Fix seccomp checks for integration tests


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.16.0**, the newest release recorded here for this line.

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
