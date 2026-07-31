---
id: TROUBLE-YOUKI_0_7_DEFECTS
type: troubleshooting
title: "youki 0.7: defects fixed in the 0.7 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.7.0 <0.8.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - youki 0.7 known issues
  - youki 0.7 fixed in
  - is this youki bug already fixed
tags:
  - troubleshooting
  - upgrade
  - youki
sources:
  - type: docs
    path: youki-dev/youki release notes for the 0.7 line — bug-fix entries
    url: https://github.com/youki-dev/youki/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# youki 0.7: defects fixed in the 0.7 line

## Summary

**43 defects** the project fixed across **1 releases** of the 0.7 line, from 0.7.0 to
0.7.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.7.0

- fix(3207, 3209) Difference between the exec command in runc and youki by @tommady in https://github.com/youki-dev/youki/pull/3210
- fix(checkpoint): delete container state after checkpoint without --leave-running by @nayuta723 in https://github.com/youki-dev/youki/pull/3501
- fix(libcgroups): add /run/systemd/private fallback for dbus system connection by @nayuta723 in https://github.com/youki-dev/youki/pull/3557
- fix(libcgroups): `pids-limit` is set to 0, change it to 1 by @moz-sec in https://github.com/youki-dev/youki/pull/3634
- fix duplicate mount entries on exec by @saku3 in https://github.com/youki-dev/youki/pull/3432
- fix: inherit config.json env vars in exec processes by @KevinKickass in https://github.com/youki-dev/youki/pull/3439
- Checking source file type with `is_dir()` in bind mount implementation by @logica0419 in https://github.com/youki-dev/youki/pull/3484
- fix(libcgroups): Set MemorySwapMax to 0 when memory::limit == memory::swap by @souk4711 in https://github.com/youki-dev/youki/pull/3488
- seccomp: fix multi-condition rule handling and follow runc for duplicate arg comparators by @saku3 in https://github.com/youki-dev/youki/pull/3489
- fix: validate process.terminal field against --console-socket option by @nayuta723 in https://github.com/youki-dev/youki/pull/3528
- fix: preserve mount flags for readonly remount of rootfs in init by @YawKar in https://github.com/youki-dev/youki/pull/3536
- fix: ratime and rnostrictatime mount options failing with EINVAL by @kechigon in https://github.com/youki-dev/youki/pull/3467
- fix(channel): split intermediate and init readiness channels by @uran0sH in https://github.com/youki-dev/youki/pull/3504
- fix: respect bundle option in youki spec command by @YawKar in https://github.com/youki-dev/youki/pull/3543
- fix(libcgroups): return typed error when systemd is not available by @SAY-5 in https://github.com/youki-dev/youki/pull/3546
- fix youki spec command overwrites the existing config.json by @tommady in https://github.com/youki-dev/youki/pull/3555
- fix: drop bounding caps by default if unset by @YawKar in https://github.com/youki-dev/youki/pull/3554
- Use process env for StartContainer hooks when without explicit hook env by @bells17 in https://github.com/youki-dev/youki/pull/3470
- fix: validation differences between youki and runc by @tommady in https://github.com/youki-dev/youki/pull/3556
- fix(libcontainer): consider gid_mappings when looking up id-map binaries by @tkshsbcue in https://github.com/youki-dev/youki/pull/3624
- fix(libcontainer): Bind mount detection should be based on bind/rbind options, not type == "bind" by @tommady in https://github.com/youki-dev/youki/pull/3611
- fix(libcontainer): scope pivot_root rslave to the old root only by @saku3 in https://github.com/youki-dev/youki/pull/3621
- fix: youki spec state vs runc spec state generated config differences by @tommady in https://github.com/youki-dev/youki/pull/3645
- fix(checkpoint): remove unimplemented options from help output by @nayuta723 in https://github.com/youki-dev/youki/pull/3455
- Disable colors in logs by @stepancheg in https://github.com/youki-dev/youki/pull/3433
- [Bug]: Duplicate error and chain printing by @CarloQuick in https://github.com/youki-dev/youki/pull/3419
- Fix logging for dropping capabilities by @stepancheg in https://github.com/youki-dev/youki/pull/3436
- contest: add checkpoint/restore integration tests by @nayuta723 in https://github.com/youki-dev/youki/pull/3448
- Deduplicate e2e test hook helpers by @fspv in https://github.com/youki-dev/youki/pull/3412
- Add poststop_fail hook test by @fspv in https://github.com/youki-dev/youki/pull/3407
- fix: use correct fedora version number and deprecate riskv64 from lima-setup.sh by @gat786 in https://github.com/youki-dev/youki/pull/3497
- [Refactor] Use `&&` operator in if-let conditions by @logica0419 in https://github.com/youki-dev/youki/pull/3531
- Add checkpoint/restore integration tests to contest by @tommady in https://github.com/youki-dev/youki/pull/3493
- fix: parse info parameters exactly by @immanuwell in https://github.com/youki-dev/youki/pull/3541
- add aarch64 bundle for integration test by @saku3 in https://github.com/youki-dev/youki/pull/3530
- Skip namespaces that are not specified for the init process by @saku3 in https://github.com/youki-dev/youki/pull/3551
- fix(wasmedge): replace unwrap with proper error propagation in exec by @immanuwell in https://github.com/youki-dev/youki/pull/3570
- feat(contest): add reason for TestResult::Skipped by @donkomura in https://github.com/youki-dev/youki/pull/3588
- fix(utils): reject network device names exceeding the kernel limit according to the kernel reference by @Scanf-s in https://github.com/youki-dev/youki/pull/3608
- fix(contest): avoid flaky MAC race in checkpoint netdevice test by @donkomura in https://github.com/youki-dev/youki/pull/3640
- add killsig test by @YamasouA in https://github.com/youki-dev/youki/pull/3612
- prepare v0.7.0 by @nayuta723 in https://github.com/youki-dev/youki/pull/3655
- bump version to 0.7.0 and fix version-up regex in justfile by @nayuta723 in https://github.com/youki-dev/youki/pull/3665


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.7.0**, the newest release recorded here for this line.

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
