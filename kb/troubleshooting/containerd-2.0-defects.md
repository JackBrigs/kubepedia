---
id: TROUBLE-CONTAINERD_2_0_DEFECTS
type: troubleshooting
title: "containerd 2.0: defects fixed in the 2.0 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.0.0 <2.1.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - containerd 2.0 known issues
  - containerd 2.0 fixed in
  - is this containerd bug already fixed
tags:
  - troubleshooting
  - upgrade
  - containerd
sources:
  - type: docs
    path: containerd/containerd release notes for the 2.0 line — bug-fix entries
    url: https://github.com/containerd/containerd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# containerd 2.0: defects fixed in the 2.0 line

## Summary

**68 defects** the project fixed across **11 releases** of the 2.0 line, from 2.0.0 to
2.0.11. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.0.0

- Fix deadlock during NRI plugin registration ([containerd/nri#79](https://github.com/containerd/nri/pull/79))
- Fix deadlock when writing to pipe blocks ([containerd/ttrpc#168](https://github.com/containerd/ttrpc/pull/168))
- Switch runc shim to task service v3 and fix restore

### 2.0.1

- Fix apply IoOwner options when not in user namespace
- Fix apply IoOwner options when not in user namespace ([#11151](https://github.com/containerd/containerd/pull/11151)) [`018d83650`](https://github.com/containerd/containerd/commit/018d83650fd4b23d61cd7af381ea5123935005c6) internal/cri: should not apply IoOwner options
- Fix cri grpc plugin config migration ([#11140](https://github.com/containerd/containerd/pull/11140)) [`a2302ea89`](https://github.com/containerd/containerd/commit/a2302ea89f90cb8ef2cafea3ca4ed20933d5d8b5) Add integration test for custom configuration [`be5eda069`](https://github.com/containerd/containerd/commit/be5eda069f1055d934b40815d0ee30eeeda3771e) complete cri grpc config migration
- Fix panic due to nil dereference cgroups v2 ([#11098](https://github.com/containerd/containerd/pull/11098)) [`3ba2df924`](https://github.com/containerd/containerd/commit/3ba2df924a3f23419b7e8fe2626fa55cd934eb16) fix panic due to nil dereference cgroups v2
- fix: set the credentials even if not provided ([#11031](https://github.com/containerd/containerd/pull/11031)) [`986088866`](https://github.com/containerd/containerd/commit/9860888666f7e96a37d0a412ee80be065ea74903) fix: set the credentials even if not provided
- fsverity_test.go: fix nil pointer derefence, fix test fail, fix minor/major device numbers resolving ([#10978](https://github.com/containerd/containerd/pull/10978)) [`30b929ece`](https://github.com/containerd/containerd/commit/30b929ece7e79e030a710de13a58d73b79853e7c) fsverity_test.go: fix major/minor device number resolving [`10996a334`](https://github.com/containerd/containerd/commit/10996a334b2d507e919244fd60be09f62384e3c0) fsverity_test.go: fix nil pointer dereference, fix test fail
- fsverity_linux.go: Fix fsverity.IsEnabled() for big endian systems ([#11005](https://github.com/containerd/containerd/pull/11005)) [`a7f2b562f`](https://github.com/containerd/containerd/commit/a7f2b562f3b6f87733ae4e3e4fd04afad3b24816) fsverity_linux.go: Fix fsverity.IsEnabled() for big endian systems
- Avoid arch info in the sed/replace when building cri-cni-containerd.tar.gz ([#10968](https://github.com/containerd/containerd/pull/10968)) [`e99c2b55c`](https://github.com/containerd/containerd/commit/e99c2b55c3fcbb2e04e0bc2fed37b0c2d7fe9245) Avoid arch info in the sed/replace when building cri-cni-containerd.tar.gz
- Bump github actions dependencies to match containerd CI repo and fix lint ([containerd/go-cni#122](https://github.com/containerd/go-cni/pull/122)) [`386f475`](https://github.com/containerd/go-cni/commit/386f4757e63914b2589b8abe6098bfa23f83fa8b) Fix ci.yml indent [`a9b0675`](https://github.com/containerd/go-cni/commit/a9b0675fc9b8b5ce52d84f91a4fc049501853862) Another doc commit to trigger lint? [`14af454`](https://github.com/containerd/go-cni/commit/14af4542b76fa694f2e1853b35554f23c6829f5d) Bump github actions dependency versions [`9e0d096`](https://github.com/containerd/go-cni/commit/9e0d096d58145757809ddce8b8650efc07e19916) Trivial doc commit to trigger lint

### 2.0.2

- Fix runtime platform loading in cri image plugin init
- Fix runtime platform loading in cri image plugin init ([#11248](https://github.com/containerd/containerd/pull/11248)) [`a2d9d4fd5`](https://github.com/containerd/containerd/commit/a2d9d4fd556970c39d1fe80d94a77a1aa025c032) Fix runtime platform loading in cri image plugin init
- make sure console master tty is closed on task exit ([#11246](https://github.com/containerd/containerd/pull/11246)) [`184ffad01`](https://github.com/containerd/containerd/commit/184ffad01ff70e513f969a392de03b6d18b5e31e) Add integ test to check tty leak [`17181ed33`](https://github.com/containerd/containerd/commit/17181ed33e018a629deeb08889bef4cc3412c64e) fix master tty leak due to leaking init container object
- ctr: `ctr images import --all-platforms`: fix unpack ([#11236](https://github.com/containerd/containerd/pull/11236)) [`c4270430d`](https://github.com/containerd/containerd/commit/c4270430db0f7e27a4c03b60822c7e14d210ae46) ctr: `ctr images import --all-platforms`: fix unpack
- Fix concurrent map panic on metadata ([containerd/otelttrpc#2](https://github.com/containerd/otelttrpc/pull/2)) [`2ba3be1`](https://github.com/containerd/otelttrpc/commit/2ba3be1e39398b8d2544f5ea962edc1e2f906d32) Fix concurrent map panic on inject metadata [`f50a922`](https://github.com/containerd/otelttrpc/commit/f50a9220fc748442b274390c45773191367262ec) UT for concurrent inject/extract metadata
- server: fix a Serve() vs. (immediate) Shutdown() race ([containerd/ttrpc#175](https://github.com/containerd/ttrpc/pull/175)) [`c4d96d5`](https://github.com/containerd/ttrpc/commit/c4d96d55ad9c4f4cf6036c70a5b18ba80655d648) server: fix Serve() vs. immediate Shutdown() race. [`ed6c3ba`](https://github.com/containerd/ttrpc/commit/ed6c3ba082bdbc82284c198d93ca5f07ad9900dd) server_test: add Serve()/Shutdown() race test

### 2.0.3

- Fix privileged container sysfs can't be rw because pod is ro by default
- Fix recursive RLock() mutex acquisition ([containerd/go-cni#126](https://github.com/containerd/go-cni/pull/126))
- Fix initial sync race when registering NRI plugins
- Fix privileged container sysfs can't be rw because pod is ro by default ([#11456](https://github.com/containerd/containerd/pull/11456)) [`c7f64196f`](https://github.com/containerd/containerd/commit/c7f64196fcbc792fd9383eb9aa8d43be0f9fa748) Fix privileged container sysfs can't be rw because pod is ro by default
- Upgrade x/net to 0.33.0 to fix vulnerability GHSA-w32m-9786-jp63 ([#11387](https://github.com/containerd/containerd/pull/11387)) [`fcf64305c`](https://github.com/containerd/containerd/commit/fcf64305cef019c8bf135d7373e2b658e02019b3) Update vendor files to fix build failure [`d3437eb29`](https://github.com/containerd/containerd/commit/d3437eb2918f6e266e97c5ee08737926519dc40d) Upgrade x/net to 0.33.0
- Update go-cni version to fix Race Condition issue ([#11269](https://github.com/containerd/containerd/pull/11269)) [`06891f899`](https://github.com/containerd/containerd/commit/06891f899d25de9dd1cb5e5443ec099e17a57e00) fix go-cni race condition
- Fix initial sync race when registering NRI plugins ([#11329](https://github.com/containerd/containerd/pull/11329)) [`79cdbf61b`](https://github.com/containerd/containerd/commit/79cdbf61b6f7e4be2feb1bb2d631bdb1b9c5cd7f) cri,nri: block NRI plugin sync. during event processing

### 2.0.4

- Fix integer overflow in User ID handling ([GHSA-265r-hfxg-fhmg](https://github.com/containerd/containerd/security/advisories/GHSA-265r-hfxg-fhmg))
- Fix incorrect runtime name being passed to NRI
- Fix incorrect runtime name being passed to NRI ([#11529](https://github.com/containerd/containerd/pull/11529)) [`4f037050c`](https://github.com/containerd/containerd/commit/4f037050ce83224d79e8b65e270222abb9ce6ab0) add name in package version

### 2.0.5

- Prevent panic on zero length push ([#11698](https://github.com/containerd/containerd/pull/11698)) [`8a638b71a`](https://github.com/containerd/containerd/commit/8a638b71aef45e16b7dcf86bd5267229d715a2e9) Prevent panic in Docker pusher
- Fix CI lint error (cherry-picked #11555) ([#11567](https://github.com/containerd/containerd/pull/11567)) [`16f20abdf`](https://github.com/containerd/containerd/commit/16f20abdffa6041382660f1374f25eb9fdfd2fc7) Fix CI lint error

### 2.0.6

- Fix containerd panic when sandbox extension is missing
- Fix the panic caused by the failure of RunPodSandbox
- Fix issue where Prometheus metric names changed for CRI
- Fix issue preventing some v2 shims from shutting down properly
- Fix lazy gRPC connection mode waiting for connect on client creation
- Fix cross-repo mount fallback after authorization failure
- Fix container io to close after runtime create failure
- Fix lazy gRPC connection mode waiting for connect on client creation ([#12080](https://github.com/containerd/containerd/pull/12080)) [`bed6d1401`](https://github.com/containerd/containerd/commit/bed6d1401087abe707a05da15eaae9626d43fc2a) client/New: Don't unlazy the gRPC connection implicitly
- Fix containerd panic when sandbox extension is missing ([#12077](https://github.com/containerd/containerd/pull/12077)) [`8094fa21a`](https://github.com/containerd/containerd/commit/8094fa21a62d67ee70369e1bb3e2973134de18a2) cri:fix containerd panic when can't find sandbox extension
- Fix container io to close after runtime create failure ([#12051](https://github.com/containerd/containerd/pull/12051)) [`552f717be`](https://github.com/containerd/containerd/commit/552f717be4dc2ec67c99afa0a2d305bf8a2b55f8) bugfix:close container io when runtime create failed
- Fix the panic caused by the failure of RunPodSandbox ([#12047](https://github.com/containerd/containerd/pull/12047)) [`c4394d05a`](https://github.com/containerd/containerd/commit/c4394d05a152b3382b9ecd0bc21c6be915b41216) Fix the panic caused by the failure of RunPodSandbox
- Fix incompatibility with some pre-v3 shims ([#11973](https://github.com/containerd/containerd/pull/11973)) [`7fc3151fc`](https://github.com/containerd/containerd/commit/7fc3151fca7e0f7548aa7cf2aa76010e8f70b6a8) *: properly shutdown non-groupable shims to prevent resource leaks [`4396336a1`](https://github.com/containerd/containerd/commit/4396336a11c306064ef2bc3358a157fda538400e) core/runtime: should invoke shim binary [`10bcc6929`](https://github.com/containerd/containerd/commit/10bcc6929552f75f8bcbc90447b977ec10edc671) Revert "not set sandbox id when use podsandbox type" [`f38eb62b6`](https://github.com/containerd/containerd/commit/f38eb62b63b5b5a209399a0d9301e4960ef17a12) integration: add testcase to recover ungroupable shim [`2358561d5`](https://github.com/containerd/containerd/commit/2358561d5258624c56f21969fcbfe8c57f189fe3) Update release upgrade tests to test 1.7 and 2.0 [`8931b1464`](https://github.com/containerd/containerd/commit/8931b14647cf4c0ca750fd12ebb44d074ea04f73) Fix upgrade test runtime config
- Fix cross-repo mount fallback after authorization failure ([#11832](https://github.com/containerd/containerd/pull/11832)) [`cbfa66223`](https://github.com/containerd/containerd/commit/cbfa662234d8ebe78e35a8b6da46dfe5a50ff5c7) fix(docker pusher): if authorizing a cross-repo mount fails, fall back
- Revert "disable portmap test in ubuntu-22 to make CI happy" ([#11784](https://github.com/containerd/containerd/pull/11784)) [`7cf3c604e`](https://github.com/containerd/containerd/commit/7cf3c604eb0bf0b8776f60b7e841476be727c32b) fix unbound SKIP_TEST variable error [`827be7c9d`](https://github.com/containerd/containerd/commit/827be7c9dd805fad6f3e94ca0070045935c38051) Revert "disable portmap test in ubuntu-22 to make CI happy"
- Update containerd config dump to reflect plugin config migrations ([#11772](https://github.com/containerd/containerd/pull/11772)) [`626a57dd7`](https://github.com/containerd/containerd/commit/626a57dd72c64ea22fc67f55b0cc8d42e94ba055) fix: update containerd config dump to reflect plugin config migrations
- Fix issue where Prometheus metric names changed for CRI ([#11750](https://github.com/containerd/containerd/pull/11750)) [`d2a30ea0c`](https://github.com/containerd/containerd/commit/d2a30ea0caab6bda8dc1dca5823d9d462c3d1b96) Revert criserver metrics subsystem back to cri
- Fix issue preventing some v2 shims from shutting down properly ([#11741](https://github.com/containerd/containerd/pull/11741)) [`e9804ee0e`](https://github.com/containerd/containerd/commit/e9804ee0e9d85788648b589c17e67a024a93151e) not set sandbox id when use podsandbox type
- [CI] Fix vagrant ([#11740](https://github.com/containerd/containerd/pull/11740)) [`9ddeff7f7`](https://github.com/containerd/containerd/commit/9ddeff7f7df90a7b1a732e2b48a5fcdef199def1) Fix vagrant setup

### 2.0.7

- **Fix userns with container image VOLUME mounts that need copy**
- **Fix lost container logs from quickly closing io**
- **Fix pidfd leak in UnshareAfterEnterUserns**
- Prepare release notes for v2.0.7 ([#12482](https://github.com/containerd/containerd/pull/12482)) [`4931e24f1`](https://github.com/containerd/containerd/commit/4931e24f169091cb4e425b7bfdd4fb0d3c20543b) Prepare release notes for v2.0.7 [`205bc4f2d`](https://github.com/containerd/containerd/commit/205bc4f2dbce3df32d2d5140a3d039332b02dbe6) Update mailmap [`5f708b76a`](https://github.com/containerd/containerd/commit/5f708b76a41a1cf56e167971e271c7581cb2f8cb) Merge commit from fork [`8cd112d82`](https://github.com/containerd/containerd/commit/8cd112d8295bafcf4a992816ff9e07f5a78ff71b) Fix directory permissions [`05290b5bc`](https://github.com/containerd/containerd/commit/05290b5bc8fd938c8f77856927a280a1d5eec7b6) Merge commit from fork [`4d1edf4ad`](https://github.com/containerd/containerd/commit/4d1edf4addf8c31b096680f04fee499cabc75439) fix goroutine leak of container Attach
- Fix lost container logs from quickly closing io ([#12376](https://github.com/containerd/containerd/pull/12376)) [`f953ee8a3`](https://github.com/containerd/containerd/commit/f953ee8a3c1feeaa60a3c9d386afa424040d56de) bugfix:fix container logs lost because io close too quickly
- Fix userns with container image VOLUME mounts that need copy ([#12241](https://github.com/containerd/containerd/pull/12241)) [`3212afc2f`](https://github.com/containerd/containerd/commit/3212afc2f2d464157bcb24663360ee7dfa7207e6) integration: Add test for directives with userns [`b855c6e10`](https://github.com/containerd/containerd/commit/b855c6e10372eb43d51186ab156cdce3d9eefb04) cri: Fix userns with Dockerfile VOLUME mounts that need copy
- Fix overlayfs issues related to user namespace ([#12223](https://github.com/containerd/containerd/pull/12223)) [`05c0c99f4`](https://github.com/containerd/containerd/commit/05c0c99f432b341152b54ce49d9b43c5cf3d131f) core/mount: Retry unmounting idmapped directories [`afdede4ce`](https://github.com/containerd/containerd/commit/afdede4ced8c848191062b31dfcff1352161a844) core/mount: Test cleanup of DoPrepareIDMappedOverlay() [`47205f814`](https://github.com/containerd/containerd/commit/47205f814d552a4eea9935375dd2f0874e107e5b) core/mount: Properly cleanup on doPrepareIDMappedOverlay errors [`6f4abd970`](https://github.com/containerd/containerd/commit/6f4abd970aeea241f07edc1e0fd74f69a9a05979) core/mount: Don't call nil function on errors [`a2f0d65d7`](https://github.com/containerd/containerd/commit/a2f0d65d78871832da6d2aa452aeeb180cd6d8f5) core/mount: Only idmap once per overlayfs, not per layer [`1c32accd7`](https://github.com/containerd/containerd/commit/1c32accd71d34e3cb5798214adf26911609d11f1) Make ovl idmap mounts read-only
- Create bootstrap.json with 0644 permission ([#12184](https://github.com/containerd/containerd/pull/12184)) [`009622e04`](https://github.com/containerd/containerd/commit/009622e0424fa4234d67272339fb7e282c302190) fix: create bootstrap.json with 0644 permission
- Fix pidfd leak in UnshareAfterEnterUserns ([#12178](https://github.com/containerd/containerd/pull/12178)) [`5bec0a332`](https://github.com/containerd/containerd/commit/5bec0a33297ad485f96116efb333ea750a27c926) sys: fix pidfd leak in UnshareAfterEnterUserns
- Fix windows test failures ([#12120](https://github.com/containerd/containerd/pull/12120)) [`2a2488131`](https://github.com/containerd/containerd/commit/2a2488131e3602bbbecf4afa11d0f3e4135f01a4) Fix intermittent test failures on Windows CIs [`018470948`](https://github.com/containerd/containerd/commit/018470948db89512760e9c25d4c5da9c7bef5321) Remove WS2025 from CIs due to regression

### 2.0.8

- Fix CNI issue where DEL is never executed after a restart
- fix: sanitize error before gRPC return to prevent credential leak in pod events ([#13181](https://github.com/containerd/containerd/pull/13181)) [`868869eb9`](https://github.com/containerd/containerd/commit/868869eb9eff7a639bee9ba6324bd654a0449232) fix: sanitize error before gRPC return to prevent credential leak in pod events [`40632e4f2`](https://github.com/containerd/containerd/commit/40632e4f2aa7b8996afe29071db2d7ca072df0a6) fix: redact all query parameters in CRI error logs
- Fix CNI issue where CNI DEL is never executed ([#13179](https://github.com/containerd/containerd/pull/13179)) [`e92d7b131`](https://github.com/containerd/containerd/commit/e92d7b131182de4738ef7d6973e20048f9a9f658) make linter happy in release [`12fc0e6ca`](https://github.com/containerd/containerd/commit/12fc0e6ca205bae9c97ef4e6ad534549818a8456) add integration test for cni result nil [`8d912c6a2`](https://github.com/containerd/containerd/commit/8d912c6a2be3546e5de0b221d9beb76e62c148ed) address comment [`742f8b8f6`](https://github.com/containerd/containerd/commit/742f8b8f60a2d5e806ea858265d491d9b4930eab) fix issue where cni del is never executed
- Cherry-picks to fix CI ([#13175](https://github.com/containerd/containerd/pull/13175)) [`f24653597`](https://github.com/containerd/containerd/commit/f246535975c99ad48b3c7f5faa3eed9cfc2aa728) Ignore NOCHANGE error [`9c656fab4`](https://github.com/containerd/containerd/commit/9c656fab42dc6a14a929f09bc4e6e24f8fe1a7b1) ci: update CIFuzz actions to support Ubuntu 24.04 [`c71c4a091`](https://github.com/containerd/containerd/commit/c71c4a091aebff6af86c107e26235ead10cf9b4b) integration: Fix TestImageLoad() failure on CI [`bfee29999`](https://github.com/containerd/containerd/commit/bfee299990b409f709d03d026b74393cf6396cc9) ci: modprobe xt_comment on almalinux

### 2.0.9

- Fix handling of out-of-range USER values in OCI spec to avoid unexpected username/group lookups
- Fix bugs in sandbox service affecting sandbox creation configuration and event publishing
- backport: sandbox: forward Create fields, fix event topics ([#13271](https://github.com/containerd/containerd/pull/13271)) [`3d34dc820`](https://github.com/containerd/containerd/commit/3d34dc82065b8cab9d20188583ce6979cdf6d30b) sandbox: forward Create fields, fix event topics
- Fix TOCTOU race bug in tar extraction ([#13237](https://github.com/containerd/containerd/pull/13237)) [`cf73e6873`](https://github.com/containerd/containerd/commit/cf73e68731f80077fad3124bee8c0cfe6aa063f8) Fix TOCTOU race bug in tar extraction
- cri:fix lost container exit events if they arrive before info is cached ([#11633](https://github.com/containerd/containerd/pull/11633)) [`2320b319e`](https://github.com/containerd/containerd/commit/2320b319e096c5926f956d4abfe52177c5e05727) cri:fix lost container exit events if they arrive before info is cached

### 2.0.11

- fix: avoid content storage pollution by limiting the fallback on ref resolution ([#13622](https://github.com/containerd/containerd/pull/13622)) [`179b642d6`](https://github.com/containerd/containerd/commit/179b642d662ddbaeebe57214164a399ceaed5fbd) fix:avoid content storage pollution by limiting the fallback on ref resolution


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.0.11**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `containerd/containerd`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/containerd.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
