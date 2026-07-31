---
id: TROUBLE-NERDCTL_2_3_DEFECTS
type: troubleshooting
title: "nerdctl 2.3: defects fixed in the 2.3 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.3.0 <2.4.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - nerdctl 2.3 known issues
  - nerdctl 2.3 fixed in
  - is this nerdctl bug already fixed
tags:
  - troubleshooting
  - upgrade
  - nerdctl
sources:
  - type: docs
    path: containerd/nerdctl release notes for the 2.3 line — bug-fix entries
    url: https://github.com/containerd/nerdctl/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# nerdctl 2.3: defects fixed in the 2.3 line

## Summary

**13 defects** the project fixed across **4 releases** of the 2.3 line, from 2.3.0 to
2.3.4. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.3.0

- `nerdctl container`: Added SELinux support for `nerdctl run` and `nerdctl info` (#4639, thanks to @ningmingxiao) Improved `nerdctl run --gpus` handling by using CDI (#4617, thanks to @elezar) Improved GPU vendor detection for CDI device IDs (#4728, thanks to @shiv-tyagi) Fixed shared IPC namespace handling for `nerdctl run` (#4718, thanks to @weiyuhang2011) Added missing `--ipc` options to `nerdctl run` help text and shell completion (#4731, thanks to @haytok) Added support for `nerdctl cp` with tarballs (#4704, thanks to @sondavidb) Added missing `HostConfig` fields to the Docker-compatible `nerdctl container inspect` response (#4850, thanks to @ayush-panta) Fixed reading logs of stopped containers by waiting for the logger to finish (#4857, thanks to @haytok)
- `nerdctl network`: Added MAC, IPv4, and IPv6 addresses to `nerdctl network inspect` output (#4680, thanks to @coderbirju) Fixed binding containers on different IP addresses to the same port (#4800, thanks to @yankay) Fixed cleanup of port-reserver state and unused iptables chains after container removal (#4801, #4811, #4820, #4835, thanks to @haytok) Fixed freeing reserved ports in rootful mode (#4862, thanks to @unsuman) Ignored missing `/proc/net/tcp6` and `/proc/net/udp6` on IPv6-disabled systems (#4824, thanks to @shouhei)
- `nerdctl compose`: Fixed compose pull policy handling for invalid options (#4686, thanks to @haytok)
- Documentation: Fixed the formatting of the `--security-opt label=<selinuxlabel>` entry in the command reference (#4882, thanks to @ogulcanaydogan)
- Misc: Added `make uninstall` (#4797, thanks to @mvanhorn) Fixed a nil pointer panic in `commonLock` cleanup (#4819, thanks to @fedebram) Corrected usage display to show `[command]` instead of `[flags]` (#4733, thanks to @niveshdandyan) Fixed building newer runc versions (#4653, thanks to @zhangyoufu) Updated the list of unimplemented Docker features (#4747, #4809, thanks to @rohansood10 and @IstvanCsVarga)

### 2.3.1

- `nerdctl network`: Fixed a panic when statting an invalid CNI config path (#4890, thanks to @immanuwell)
- Documentation: Fixed the spelling of the `--sig-proxy` flag in the command reference (#4903, thanks to @MukundaKatta) Removed a stray quote from the `--interactive` flag documentation (#4904, thanks to @MukundaKatta)
- CI and tests: Added zizmor workflow linting and fixed reported workflow issues (#4909, thanks to @omribz156) Continued migrating container tests to Tigron (#4863, #4865, thanks to @opjt)

### 2.3.2

- `nerdctl image`: Added the overlaybd `vsize` option (#4960, thanks to @fourierrr) Fixed `nerdctl load` failures (#4888, thanks to @ningmingxiao)
- `nerdctl network`: Fixed a panic when statting an invalid CNI config path (#4890, thanks to @immanuwell)
- CI and tests: Continued migrating container tests to Tigron (#4897, #4900, #4898, #4916, thanks to @ogulcanaydogan and @opjt) Migrated compose run tests to the `nerdtest` framework (#4845, #4911, thanks to @sathiraumesh and @haytok) Replaced Vagrant with Lima for FreeBSD tests (#4952, thanks to @AkihiroSuda) Fixed syslog test timing and startup behavior (#4898, thanks to @ogulcanaydogan)
- Documentation: Updated the Windows installation section in `README.md` (#4949, thanks to @ofek) Fixed a typo and a missing import in `tools.md` (#4917, thanks to @opjt)

### 2.3.4

- `nerdctl (container|image|network) inspect` Fix format errors (#5019, thanks to @immanuwell)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.3.4**, the newest release recorded here for this line.

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
