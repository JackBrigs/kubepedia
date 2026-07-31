---
id: TROUBLE-YOUKI_0_3_DEFECTS
type: troubleshooting
title: "youki 0.3: defects fixed in the 0.3 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.3.0 <0.4.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - youki 0.3 known issues
  - youki 0.3 fixed in
  - is this youki bug already fixed
tags:
  - troubleshooting
  - upgrade
  - youki
sources:
  - type: docs
    path: youki-dev/youki release notes for the 0.3 line — bug-fix entries
    url: https://github.com/youki-dev/youki/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# youki 0.3: defects fixed in the 0.3 line

## Summary

**65 defects** the project fixed across **4 releases** of the 0.3 line, from 0.3.0 to
0.3.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.3.0

- Use raw syscalls to avoid sporadic hangs by @jprendes in https://github.com/containers/youki/pull/2425
- Fix device duplication in rootfs preparation by @YJDoc2 in https://github.com/containers/youki/pull/2438
- Change rootless required function and privilege decision by @YJDoc2 in https://github.com/containers/youki/pull/2279
- Skip the tests related to criu when criu is not found by @utam0k in https://github.com/containers/youki/pull/2365
- Refactor doc test and justfile by @yihuaf in https://github.com/containers/youki/pull/2330
- Add initial tests for rootless podman by @YJDoc2 in https://github.com/containers/youki/pull/2406
- update nix to 0.27.1 by @anti-entropy123 in https://github.com/containers/youki/pull/2369
- Refactor test dir structure by @YJDoc2 in https://github.com/containers/youki/pull/2421
- Use static build of wasmedge by @jprendes in https://github.com/containers/youki/pull/2420
- v0.3.0 by @utam0k in https://github.com/containers/youki/pull/2437

### 0.3.1

- fix(libcgroups): report CPU throttling stats in 'libcgroups::v2' by @xiaoyang-sde in https://github.com/containers/youki/pull/2524
- fix(main): support arm64 release youki by @cuisongliu in https://github.com/containers/youki/pull/2498
- Specify the protobuf crate because of the rust-criu crate by @utam0k in https://github.com/containers/youki/pull/2497
- docs(main): auto release node using just by @cuisongliu in https://github.com/containers/youki/pull/2573
- Fix emulated cgroups v1 subsystem when running docker-in-docker by @jprendes in https://github.com/containers/youki/pull/2532
- fix docs by @lengrongfu in https://github.com/containers/youki/pull/2550
- Grouping patch updates in dependabot. by @utam0k in https://github.com/containers/youki/pull/2496
- Fix the config of the dependenda bot by @utam0k in https://github.com/containers/youki/pull/2502
- feature(main): add release strip by @cuisongliu in https://github.com/containers/youki/pull/2503
- test(integration_test): port 'runtime-tools/validation/linux_sysctl' by @xiaoyang-sde in https://github.com/containers/youki/pull/2527
- docs(libcgroup): add docs for several items in 'libcgroup::v2' by @xiaoyang-sde in https://github.com/containers/youki/pull/2525
- test(integration_test): port 'runtime-tools/validation/linux_seccomp' by @xiaoyang-sde in https://github.com/containers/youki/pull/2531
- fix(libcgroups): clean up 'libcgroups::v1::manager' by @xiaoyang-sde in https://github.com/containers/youki/pull/2530
- small typo in trace message by @Pvlerick in https://github.com/containers/youki/pull/2535
- Set up userns in a straightforward way by @utam0k in https://github.com/containers/youki/pull/2548
- Rust 1.74.1 by @utam0k in https://github.com/containers/youki/pull/2557
- Simplify release workflow by @jprendes in https://github.com/containers/youki/pull/2541
- config: Automated Tagpr Update for 0.3.1 by @github-actions in https://github.com/containers/youki/pull/2571
- Release for v0.3.1 by @github-actions in https://github.com/containers/youki/pull/2570
- Ignore CHANGELOG.md in typos by @utam0k in https://github.com/containers/youki/pull/2572

### 0.3.2

- fix: just instead make by @bestgopher in https://github.com/containers/youki/pull/2585
- New Releases needs approval from the maintainer by @utam0k in https://github.com/containers/youki/pull/2583
- Updaet to Containerd 1.7.11 by @utam0k in https://github.com/containers/youki/pull/2558
- chore(deps) bump tabwriter, windows-core, tempfile, memchr, clang-sys by @YJDoc2 in https://github.com/containers/youki/pull/2608
- Name the test tools `contest` by @utam0k in https://github.com/containers/youki/pull/2486
- Fix the missed naming changes in integration test validation CI by @YJDoc2 in https://github.com/containers/youki/pull/2629
- Roll up various minor and major version dep upgrade by @YJDoc2 in https://github.com/containers/youki/pull/2638
- Add docker-in-docker e2e test by @jprendes in https://github.com/containers/youki/pull/2645
- Add domainname test by @higuruchi in https://github.com/containers/youki/pull/1544
- Re enable skipped e2e tests by @YJDoc2 in https://github.com/containers/youki/pull/2647

### 0.3.3

- Fix cgroups determination in exec implementation by @YJDoc2 in https://github.com/containers/youki/pull/2720
- Remove unnecessary chdir by @utam0k in https://github.com/containers/youki/pull/2780
- Rollup dep updates by @YJDoc2 in https://github.com/containers/youki/pull/2667
- Fill in TODO by @utam0k in https://github.com/containers/youki/pull/2677
- Fix the links of contest by @utam0k in https://github.com/containers/youki/pull/2680
- Set '--test-threads' option to 1 in unit tests by @YJDoc2 in https://github.com/containers/youki/pull/2685
- add io priority e2e test by @lengrongfu in https://github.com/containers/youki/pull/2646
- (fix) podman e2e : Update workflow for new required deps, add vagrantfile by @YJDoc2 in https://github.com/containers/youki/pull/2687
- Add missed test-threads=1 to coverage CI by @YJDoc2 in https://github.com/containers/youki/pull/2699
- Fix integration test validation CI, make io_priority test conditional by @YJDoc2 in https://github.com/containers/youki/pull/2707
- memo: Remove GitPod and add link to GitHub codespaces by @homersimpsons in https://github.com/containers/youki/pull/2717
- Limt dependabot updates to only direct dependencies by @utam0k in https://github.com/containers/youki/pull/2725
- fix observability default log level comment by @zahash in https://github.com/containers/youki/pull/2737
- Update deps via cargo update by @YJDoc2 in https://github.com/containers/youki/pull/2747
- Rust 1.77.1 by @utam0k in https://github.com/containers/youki/pull/2746
- Make our codespaces more useful by @utam0k in https://github.com/containers/youki/pull/2753
- Fix README.md by @utam0k in https://github.com/containers/youki/pull/2759
- update wasmtime dep to 19.0.1, replace wasmtime-wasi with wasi-common by @YJDoc2 in https://github.com/containers/youki/pull/2752
- Reset console sockets to original in setup_console test by @YJDoc2 in https://github.com/containers/youki/pull/2764
- Update rust version to 1.77.2 by @YJDoc2 in https://github.com/containers/youki/pull/2779
- Add linux_devices test by @omprakaash in https://github.com/containers/youki/pull/2708
- deps: Disable unused/unnecessary regex features in libcontainer by @jirutka in https://github.com/containers/youki/pull/2781
- Add `rustfmt.toml` to standardize formatting by @jprendes in https://github.com/containers/youki/pull/2787
- Update the release workflow by @utam0k in https://github.com/containers/youki/pull/2789
- Release v0.3.3 by @utam0k in https://github.com/containers/youki/pull/2794


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.3.3**, the newest release recorded here for this line.

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
