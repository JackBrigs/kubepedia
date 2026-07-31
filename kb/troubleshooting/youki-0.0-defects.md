---
id: TROUBLE-YOUKI_0_0_DEFECTS
type: troubleshooting
title: "youki 0.0: defects fixed in the 0.0 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.0.0 <0.1.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - youki 0.0 known issues
  - youki 0.0 fixed in
  - is this youki bug already fixed
tags:
  - troubleshooting
  - upgrade
  - youki
sources:
  - type: docs
    path: youki-dev/youki release notes for the 0.0 line — bug-fix entries
    url: https://github.com/youki-dev/youki/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# youki 0.0: defects fixed in the 0.0 line

## Summary

**106 defects** the project fixed across **5 releases** of the 0.0 line, from 0.0.1 to
0.0.5. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.0.1

- fix a memory subsystem by @utam0k in https://github.com/containers/youki/pull/36
- Fixed spelling mistake in src/rootfs.rs by @PeterYordanov in https://github.com/containers/youki/pull/67
- Change execution path and fix CI by @minakawa-daiki in https://github.com/containers/youki/pull/73
- Fix issues with cgroup v1 and v2 by @Furisto in https://github.com/containers/youki/pull/69
- Fix badges in README by @tsturzl in https://github.com/containers/youki/pull/80
- Fix README link typo by @sasurau4 in https://github.com/containers/youki/pull/88
- Fix README.md Fedora & Centos instructions by @nimrodshn in https://github.com/containers/youki/pull/107
- fix the warnings shown by cargo clippy by @utam0k in https://github.com/containers/youki/pull/127
- Fix spec path in delete by @duduainankai in https://github.com/containers/youki/pull/130
- Fix same tmp dir in freezer v2 tests by @duduainankai in https://github.com/containers/youki/pull/133
- Fix alignment of cgroups info by @Furisto in https://github.com/containers/youki/pull/157
- Fix how closure is transferred to the clone call. by @yihuaf in https://github.com/containers/youki/pull/173
- Fix clone(2) with double fork by @yihuaf in https://github.com/containers/youki/pull/217
- Fix integration_test script for go env by @chenyukang in https://github.com/containers/youki/pull/222
- Fix #209, pass root-readonly by @chenyukang in https://github.com/containers/youki/pull/224
- Fix user namespace for integration tests by @yihuaf in https://github.com/containers/youki/pull/233
- Fix tutorial in readme by @chenyukang in https://github.com/containers/youki/pull/229
- Fix graceful shutdown when intermediate or init process errors or panic by @yihuaf in https://github.com/containers/youki/pull/238
- [Trivial] Fix a typo where gid should be uid. by @yihuaf in https://github.com/containers/youki/pull/253
- fix unstable the channel tests. by @utam0k in https://github.com/containers/youki/pull/267
- fix a failure because it is running before checkout. by @utam0k in https://github.com/containers/youki/pull/270
- CI Code Coverage Fix by @YJDoc2 in https://github.com/containers/youki/pull/273
- fix cargo clippy warning in cgroups. by @utam0k in https://github.com/containers/youki/pull/281
- fix: Mismatch of PWD in tutorial by @kenoss in https://github.com/containers/youki/pull/283
- fix cargo clippy warning in cgroups by @utam0k in https://github.com/containers/youki/pull/291
- fix a failure when dirs is empty at changes job. by @utam0k in https://github.com/containers/youki/pull/294
- fix doc comment of with_preserved_fds by @shorii in https://github.com/containers/youki/pull/302
- Fix Changes Job in CI by @YJDoc2 in https://github.com/containers/youki/pull/306
- Fix error message(`LinuixIdMapping` to `uid_mappings`) by @shorii in https://github.com/containers/youki/pull/318
- avoid cloning LinuxResources because it is a large structure. by @utam0k in https://github.com/containers/youki/pull/320
- fix vagrant errors #321 by @zidoshare in https://github.com/containers/youki/pull/322
- fix build error in vagrant by @zidoshare in https://github.com/containers/youki/pull/323
- fix flaky unit tests by @utam0k in https://github.com/containers/youki/pull/326
- fix inaccessiblity of private field. by @utam0k in https://github.com/containers/youki/pull/338
- Fix multi mapping for rootless containers by @Furisto in https://github.com/containers/youki/pull/381
- Fix path issues by @Furisto in https://github.com/containers/youki/pull/386
- fix running unit tests multiple times will cause a rare failed by @tommady in https://github.com/containers/youki/pull/380
- [Trivial] minor fixes by @yihuaf in https://github.com/containers/youki/pull/406
- Fix test_make_parent_mount_private by @tsturzl in https://github.com/containers/youki/pull/472
- Fix log files and remove env_logger by @yihuaf in https://github.com/containers/youki/pull/511
- Integration test: cgroup v1 network tests, fix to memory tests by @tsturzl in https://github.com/containers/youki/pull/516
- fix(libcgroup): make cgroup manager be able to set blkio weight by @knight42 in https://github.com/containers/youki/pull/543

### 0.0.2

- Resolved `needs_to_handle` TODO's by @SarthakSingh31 in https://github.com/containers/youki/pull/568
- Pin nightly version in CI as temporary fix to coverage issue by @YJDoc2 in https://github.com/containers/youki/pull/619 Nightly was sometimes broken
- Interpret a cpu quota of zero as default value by @Furisto in https://github.com/containers/youki/pull/569
- Use correct hugetlb interface file name by @Furisto in https://github.com/containers/youki/pull/579
- Improve cgroup path handling for rootless containers by @Furisto in https://github.com/containers/youki/pull/597
- Ensure youki runs under podman by @Furisto in https://github.com/containers/youki/pull/613
- Ensure exec command can find config.json by @Furisto in https://github.com/containers/youki/pull/616
- Create device as 0666 and not 066 by @adrianreber in https://github.com/containers/youki/pull/627

### 0.0.3

- Bump anyhow from 1.0.55 to 1.0.56 and fix warnings by @Furisto in https://github.com/containers/youki/pull/767
- Resolve deprecation warnings from clap by @YJDoc2 in https://github.com/containers/youki/pull/798
- Use /dev/null inside of the container by @adrianreber in https://github.com/containers/youki/pull/630
- Fix some typos and align formatting by @Szymongib in https://github.com/containers/youki/pull/631
- Always call setsid by @Furisto in https://github.com/containers/youki/pull/632
- ready for integration test for the exec command. by @utam0k in https://github.com/containers/youki/pull/622
- Ensure namespaces are entered in correct order by @Furisto in https://github.com/containers/youki/pull/674
- Remove duplication from commands execution in Integration tests by @Szymongib in https://github.com/containers/youki/pull/673
- make sure test_make_parent_mount_private() passes even when root is not a slave. by @utam0k in https://github.com/containers/youki/pull/682
- make the rootless code testable by @utam0k in https://github.com/containers/youki/pull/634
- Add tests to libcgroups/src/v2/devices/emulator.rs by @cr0ax in https://github.com/containers/youki/pull/704
- remove cargo config by @Junnplus in https://github.com/containers/youki/pull/712
- Always use the same permissions for youki dir by @Szymongib in https://github.com/containers/youki/pull/705
- Remove caching of OCI tests in CI by @YJDoc2 in https://github.com/containers/youki/pull/727
- Fix Cargo.lock file that gets generated after build by @harche in https://github.com/containers/youki/pull/734
- Bring back architecture diagrams to README. by @utam0k in https://github.com/containers/youki/pull/739
- Handle relative paths by @Szymongib in https://github.com/containers/youki/pull/740
- Create the pid file with integration test by @utam0k in https://github.com/containers/youki/pull/762
- Fix a comment explaining that `seccom_rule_add` requires multiple args to be broken into multiple rules. by @yihuaf in https://github.com/containers/youki/pull/775
- introduce the timeout for github actions by @utam0k in https://github.com/containers/youki/pull/777
- fix log control env val not passing properly. by @utam0k in https://github.com/containers/youki/pull/778
- fix the release workflow. by @utam0k in https://github.com/containers/youki/pull/781
- make dependabot work again. by @utam0k in https://github.com/containers/youki/pull/782

### 0.0.4

- Remove duplicated assignment by @cyyzero in https://github.com/containers/youki/pull/993
- Fix some typos by @z1cheng in https://github.com/containers/youki/pull/1057
- Fix bug that attempts is always 0 in delete_with_retry by @cyyzero in https://github.com/containers/youki/pull/1128
- Fix how cgroup manager is created based on cgroups path by @YJDoc2 in https://github.com/containers/youki/pull/1288
- Thaw a paused container in cgroup v1 when it is forcely deleted. by @cyyzero in https://github.com/containers/youki/pull/1204
- Ignore error when killing, if error is 'process does not exist' by @YJDoc2 in https://github.com/containers/youki/pull/1339
- Fixed set capability fail. by @higuruchi in https://github.com/containers/youki/pull/1349
- Fix README issue links by @LeoColomb in https://github.com/containers/youki/pull/1183
- fix a typo by @DriedYellowPeach in https://github.com/containers/youki/pull/1257
- Small fix and refine documents by @udzura in https://github.com/containers/youki/pull/1351
- Add flat logos to docs folder by @scary4cat in https://github.com/containers/youki/pull/873
- Remove the build dependency from some tests. by @utam0k in https://github.com/containers/youki/pull/909
- Added podman local system tests by @stefins in https://github.com/containers/youki/pull/1009
- Automatically publish packages by @MostlyAmiable in https://github.com/containers/youki/pull/1000
- Changed bats installation script to apt package manager by @stefins in https://github.com/containers/youki/pull/1125
- Fix whitespaces: replace TABs to SPACEs by @orimanabu in https://github.com/containers/youki/pull/1167
- Add git commit sha placeholder if .git not found by @YJDoc2 in https://github.com/containers/youki/pull/1251
- Log result of the command before returning from main by @YJDoc2 in https://github.com/containers/youki/pull/1302
- Add TestContainerKill required error message in kill command by @YJDoc2 in https://github.com/containers/youki/pull/1319
- Improve the flow of the containerd test with youki by @utam0k in https://github.com/containers/youki/pull/1297
- Fix TestContainerNoBinaryExists test, by making create behaviour similar to runc by @YJDoc2 in https://github.com/containers/youki/pull/1347
- [actions] add workflow file for containerd integration testing by @guni1192 in https://github.com/containers/youki/pull/968
- Add hostname test by @chermehdi in https://github.com/containers/youki/pull/1376
- Fix release script and prepare for release by @YJDoc2 in https://github.com/containers/youki/pull/1397

### 0.0.5

- Fixed container init process not re-parent to youki main process by @yihuaf in https://github.com/containers/youki/pull/1637
- Fix clippy warning by @yihuaf in https://github.com/containers/youki/pull/1638
- fix the warns from cargo clippy by @utam0k in https://github.com/containers/youki/pull/1564
- fix container delete error by @lengrongfu in https://github.com/containers/youki/pull/1649
- Fix github actions by @utam0k in https://github.com/containers/youki/pull/1588
- fix: doc link by @lengrongfu in https://github.com/containers/youki/pull/1542
- fix: youki's image in doc by @shimatar0 in https://github.com/containers/youki/pull/1614
- Fix CI rules not filtering integration test files properly by @lengrongfu in https://github.com/containers/youki/pull/1643
- fix(libcontainer): Run test_is_executable with a more common file by @Overflow0xFFFF in https://github.com/containers/youki/pull/1676


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.0.5**, the newest release recorded here for this line.

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
