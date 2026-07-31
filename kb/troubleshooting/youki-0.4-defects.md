---
id: TROUBLE-YOUKI_0_4_DEFECTS
type: troubleshooting
title: "youki 0.4: defects fixed in the 0.4 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.4.0 <0.5.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - youki 0.4 known issues
  - youki 0.4 fixed in
  - is this youki bug already fixed
tags:
  - troubleshooting
  - upgrade
  - youki
sources:
  - type: docs
    path: youki-dev/youki release notes for the 0.4 line — bug-fix entries
    url: https://github.com/youki-dev/youki/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# youki 0.4: defects fixed in the 0.4 line

## Summary

**14 defects** the project fixed across **2 releases** of the 0.4 line, from 0.4.0 to
0.4.1. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.4.0

- Fix/dbus call issue by @YJDoc2 in https://github.com/containers/youki/pull/2838
- Fix word order in README sentence justifying Rust usage by @andrewimeson in https://github.com/containers/youki/pull/2805
- move macro define youki_version to use before by @lengrongfu in https://github.com/containers/youki/pull/2813
- Use HashMap for envs in container_init_process by @musaprg in https://github.com/containers/youki/pull/2817
- Ignore linter for MOUNT_ATTR__ATIME by @yihuaf in https://github.com/containers/youki/pull/2819
- Fix typos and bump version for typos ci by @Jerrypoi in https://github.com/containers/youki/pull/2839
- Install nightly for running linter inside devcontainer by @musaprg in https://github.com/containers/youki/pull/2845
- Add issue templates by @YJDoc2 in https://github.com/containers/youki/pull/2829
- Fix markdown format in experiment/selinux/README.md by @keisku in https://github.com/containers/youki/pull/2855
- initial progress on supporting OwnedFd by @zahash in https://github.com/containers/youki/pull/2809
- Rust 1.80.0 by @utam0k in https://github.com/containers/youki/pull/2869
- Prepare for v0.4.0 by @utam0k in https://github.com/containers/youki/pull/2880
- Release for v0.4.0 by @github-actions in https://github.com/containers/youki/pull/2791

### 0.4.1

- prepare for version 0.4.1 by @YJDoc2 in https://github.com/containers/youki/pull/2897


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.4.1**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `youki-dev/youki`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/youki.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
