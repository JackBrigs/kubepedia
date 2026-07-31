---
id: TROUBLE-NERDCTL_1_3_DEFECTS
type: troubleshooting
title: "nerdctl 1.3: defects fixed in the 1.3 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.3.0 <1.4.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - nerdctl 1.3 known issues
  - nerdctl 1.3 fixed in
  - is this nerdctl bug already fixed
tags:
  - troubleshooting
  - upgrade
  - nerdctl
sources:
  - type: docs
    path: containerd/nerdctl release notes for the 1.3 line — bug-fix entries
    url: https://github.com/containerd/nerdctl/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# nerdctl 1.3: defects fixed in the 1.3 line

## Summary

**5 defects** the project fixed across **2 releases** of the 1.3 line, from 1.3.0 to
1.3.1. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.3.0

- Fix operation not permitted with `systemd-homed` for rootless mode (#2056 , thanks to @AkihiroSuda )
- `nerdctl top`: Fix the top command on Windows (#2038 , thanks to @dardelean)
- `nerdctl help`: Fix show hidden commands (#2125 , thanks to @yuchanns)

### 1.3.1

- `nerdctl run`: Fix #2164 `sudo nerdctl run -p <container port> <image> always defaults to 49153 host port` (#2169, thanks to @vsiravar) Make tty behavior compatible to Docker (#2167, thanks to @ktock)
- `nerdctl push`: Fix cosign regression in nerdctl v1.3.0 (#2172, thanks to @ningziwen)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.3.1**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `containerd/nerdctl`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/nerdctl.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
