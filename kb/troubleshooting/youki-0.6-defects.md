---
id: TROUBLE-YOUKI_0_6_DEFECTS
type: troubleshooting
title: "youki 0.6: defects fixed in the 0.6 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.6.0 <0.7.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - youki 0.6 known issues
  - youki 0.6 fixed in
  - is this youki bug already fixed
tags:
  - troubleshooting
  - upgrade
  - youki
sources:
  - type: docs
    path: youki-dev/youki release notes for the 0.6 line — bug-fix entries
    url: https://github.com/youki-dev/youki/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# youki 0.6: defects fixed in the 0.6 line

## Summary

**25 defects** the project fixed across **1 releases** of the 0.6 line, from 0.6.0 to
0.6.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.6.0

- Implement mount destination validation to ensure absolute paths in OCI Runtime Spec by @nayuta723 in https://github.com/youki-dev/youki/pull/3315
- Fix default filemode for device creation by @you-matsuura in https://github.com/youki-dev/youki/pull/3276
- fix(3293) Ambient capabilities are not applied as expected by @tommady in https://github.com/youki-dev/youki/pull/3294
- fix(libcgroups): set `sz` field in `bpf_prog_load_opts` by @sou1118 in https://github.com/youki-dev/youki/pull/3340
- Fix recursive mount_setattr handling for rec_attr and improve mounts_recursive tests by @saku3 in https://github.com/youki-dev/youki/pull/3345
- fix(libcgroups): pass `full_path` to Devices controller instead of `cgroup_path` by @sou1118 in https://github.com/youki-dev/youki/pull/3355
- Align with runc: use user's HOME when HOME is empty string by @bells17 in https://github.com/youki-dev/youki/pull/3269
- Refactor checkpoint by @nayuta723 in https://github.com/youki-dev/youki/pull/3365
- Fix typos in documentation by @oglok in https://github.com/youki-dev/youki/pull/3343
- (chore) Fix broken links in user document by @donkomura in https://github.com/youki-dev/youki/pull/3361
- Fixed minor spelling errors in libcontainer documentation. by @CheatCodeSam in https://github.com/youki-dev/youki/pull/3305
- Add poststart hook test by @fspv in https://github.com/youki-dev/youki/pull/3292
- Replace once_cell with stdlib OnceLock/LazyLock by @yan-ace62 in https://github.com/youki-dev/youki/pull/3323
- Add poststart_fail hook test by @fspv in https://github.com/youki-dev/youki/pull/3313
- Added new test "kill no effect" by @oneplus1000 in https://github.com/youki-dev/youki/pull/3332
- Pass State directly to `run_hooks` instead of Container reference by @IrvingMg in https://github.com/youki-dev/youki/pull/3360
- Batch running the test groups in test_framework by @donkomura in https://github.com/youki-dev/youki/pull/3372
- refact mount_recursive test by @saku3 in https://github.com/youki-dev/youki/pull/3383
- Add test poststop hook by @donkomura in https://github.com/youki-dev/youki/pull/3395
- Add prestart hook test by @fspv in https://github.com/youki-dev/youki/pull/3382
- Add create_runtime hook test by @fspv in https://github.com/youki-dev/youki/pull/3396
- Sync the state to confirm hooks execution by @donkomura in https://github.com/youki-dev/youki/pull/3385
- Include container status to IncorrectStatus error messaging by @CarloQuick in https://github.com/youki-dev/youki/pull/3411
- Add prestart_fail hook test by @fspv in https://github.com/youki-dev/youki/pull/3406
- prepare v0.6.0 by @saku3 in https://github.com/youki-dev/youki/pull/3424


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.6.0**, the newest release recorded here for this line.

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
