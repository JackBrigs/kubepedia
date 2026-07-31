---
id: TROUBLE-KATA_CONTAINERS_3_4_DEFECTS
type: troubleshooting
title: "kata-containers 3.4: defects fixed in the 3.4 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.4.0 <3.5.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kata-containers 3.4 known issues
  - kata-containers 3.4 fixed in
  - is this kata-containers bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kata-containers
sources:
  - type: docs
    path: kata-containers/kata-containers release notes for the 3.4 line — bug-fix entries
    url: https://github.com/kata-containers/kata-containers/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kata-containers 3.4: defects fixed in the 3.4 line

## Summary

**6 defects** the project fixed across **1 releases** of the 3.4 line, from 3.4.0 to
3.4.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.4.0

- gha: Fix nydus namespace clean up by @GabyCT in https://github.com/kata-containers/kata-containers/pull/9265
- scripts: Fix unbound variables in k8s setup script by @GabyCT in https://github.com/kata-containers/kata-containers/pull/9329
- agent: Fix errors in `make check` by @c3d in https://github.com/kata-containers/kata-containers/pull/9345
- gha: Fix indentation in gha run script by @GabyCT in https://github.com/kata-containers/kata-containers/pull/9450
- agent: Fix the issue with the "test_new_fs_manager" test by @justxuewei in https://github.com/kata-containers/kata-containers/pull/9457
- kata: Remove check for "Fixes" in PR by @zvonkok in https://github.com/kata-containers/kata-containers/pull/9501


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.4.0**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `kata-containers/kata-containers`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/kata-containers.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
