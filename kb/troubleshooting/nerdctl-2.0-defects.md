---
id: TROUBLE-NERDCTL_2_0_DEFECTS
type: troubleshooting
title: "nerdctl 2.0: defects fixed in the 2.0 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.0.0 <2.1.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - nerdctl 2.0 known issues
  - nerdctl 2.0 fixed in
  - is this nerdctl bug already fixed
tags:
  - troubleshooting
  - upgrade
  - nerdctl
sources:
  - type: docs
    path: containerd/nerdctl release notes for the 2.0 line — bug-fix entries
    url: https://github.com/containerd/nerdctl/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# nerdctl 2.0: defects fixed in the 2.0 line

## Summary

**9 defects** the project fixed across **4 releases** of the 2.0 line, from 2.0.1 to
2.0.5. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.0.1

- Network: Fix permissions for `/etc/{resolv.conf, hosts}` with umask 0077 (#3708, thanks to @apostasie)
- Compose: Fix the support for `devices` (#3683, thanks to @ryfow)

### 2.0.2

- `nerdctl pull`: Fixed `hosts.toml` resolution for `index.docker.io` (#3720, thanks to @apostasie)
- Rootless: Fix an issue about bypass4netns on restarting the host (#3724, thanks to @apostasie)

### 2.0.4

- CI: Lots of fixes, refactoring, and the introduction of the [Tigron testing framework](https://github.com/containerd/nerdctl/tree/v2.0.4/mod/tigron) (several PRs, thanks to @apostasie)

### 2.0.5

- `nerdctl run` Add `--cpu-rt-period` and `--cpu-rt-runtime` flags (#4078, thanks to @swagatbora90) Fix double carriage returns with pty (#4054, thanks to @apostasie)
- `nerdctl inspect` Add `env` and `user` properties (#4007, thanks to @Shubhranshu153) Fix incompatibility with Docker (array vs stream of array) (#3961, thanks to @weiyuhang2011)
- `nerdctl compose` Fix `env_file` with profile (#4073, thanks to @yankay)
- `nerdctl system prune` Fix parsing `BUILDKIT_HOST` (#4115, thanks to @Shubhranshu153)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.0.5**, the newest release recorded here for this line.

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
