---
id: TROUBLE-CRI_O_1_8_DEFECTS
type: troubleshooting
title: "cri-o 1.8: defects fixed in the 1.8 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.8.0 <1.9.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cri-o 1.8 known issues
  - cri-o 1.8 fixed in
  - is this cri-o bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cri-o
sources:
  - type: docs
    path: cri-o/cri-o release notes for the 1.8 line — bug-fix entries
    url: https://github.com/cri-o/cri-o/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cri-o 1.8: defects fixed in the 1.8 line

## Summary

**28 defects** the project fixed across **5 releases** of the 1.8 line, from 1.8.0 to
1.8.5. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.8.0

- 71d2131c8 Merge pull request #1138 from runcom/fix-image-policy
- d49fb788d Fix Local modifications exist in repository
- 6b6d634cf Merge pull request #1115 from mountkin/fix-makefile
- d5ffe3475 fix "docker run" command in Makefile
- b85fe5ab9 Fix conmon and runc paths for kpod tests
- dbaf500c0 Merge pull request #1094 from runcom/makefile-fixes
- c54658cb7 Merge pull request #1083 from lsm5/unitfile-fixes
- 499b2fa18 Fix a copy/paste error in libpod initializers
- 863e137bd Merge pull request #1039 from runcom/fix-process-exec
- 9191a994f fixes runc install path on Dockerfile
- d7d2ce7ce Merge pull request #1044 from runcom/fix-host-pid
- da725f3e5 fix host pid handling for containers and share uts ns
- 3be3936d7 Merge pull request #1041 from runcom/fix-e2e
- c04f585a5 Merge pull request #1021 from runcom/fix-crio-versioning
- eafb7f710 Merge pull request #1014 from runcom/oci-kill-all-fix
- a11b1f953 Fixed logic flaw in the secrets mounts
- e07ba4b2d version: fix version handling and kube info
- c6f5a290d oci: fixes to properly handle container stop action
- ab68c553d CI: use a fixed runc version, not master

### 1.8.2

- fe8c42344cdff05aee6b05ef49053e53618e317b image_pull: fix image resolver
- d6ebe5d48 Merge pull request #1174 from runcom/fix-cve-1.8

### 1.8.3

- 187876571 Merge pull request #1191 from runcom/fix-apparmor-1.8
- b2ea67f50 container_create: fix apparmor from container config
- 171e31287 Merge pull request #1180 from runcom/fix-image-pull

### 1.8.4

- 6cc35bf46 Merge pull request #1209 from runcom/fix-exec-1.8
- 765421be0 container_exec: fix terminal true process json

### 1.8.5

- 278bb8568 Merge pull request #1311 from runcom/fix-listen-1.8
- ff1544999 cmd/crio: fix listen address dir creation


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.8.5**, the newest release recorded here for this line.

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
