---
id: TROUBLE-CONTAINERD_1_7_DEFECTS
type: troubleshooting
title: "containerd 1.7: defects fixed in the 1.7 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.7.0 <1.8.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - containerd 1.7 known issues
  - containerd 1.7 fixed in
  - is this containerd bug already fixed
tags:
  - troubleshooting
  - upgrade
  - containerd
sources:
  - type: docs
    path: containerd/containerd release notes for the 1.7 line — bug-fix entries
    url: https://github.com/containerd/containerd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# containerd 1.7: defects fixed in the 1.7 line

## Summary

**200 defects** the project fixed across **32 releases** of the 1.7 line, from 1.7.0 to
1.7.34. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.7.0

- **Fix CRI plugin to setup pod network after creating the sandbox container**
- Sandbox: Fix/enhance error messages for Create
- epoch: fix unit test when SOURCE_DATE_EPOCH is set
- Fix concurrent writes for UpdateContainerStats
- pkg/cri/config: fix Mirrors deprecation comment
- Fix retry logic within devmapper device deactivation
- fix(docs): minor fix on the windows installation steps
- fix incorrect namespace of event when create/update namespace
- cri: Fix TestUpdateOCILinuxResource for host w/o swap controller
- Fix Flaky Windows CRI Integration test on TestContainerConsumedStats
- Fix TestUpdateContainerResources_Memory* on cgroup v2 hosts
- Fix incorrect defer usage and refactor judgement
- fix `ctr tasks kill` does not remove cni network under windows
- Avoid using canceled context in unpacker cleanup
- Fix cpu architecture detection issue on linux/arm
- CRI: Fix no CNI info for pod sandbox on restart
- cri: fix `memory.memsw.limit_in_bytes: no such file or directory`
- fix: check for tmpfs when evaluating if userxattr is needed
- fix panic when containerd-stress density --count 0
- Fix order of operations when setting lease labels
- integration/client: fix go.mod grouping, containerd to v1.7.0-beta.0, cgroups back to v1.0.4
- Resolve warnings in Windows GitHub Actions periodic workflows
- Resolve Scorecards GitHub Actions workflow warnings
- Fix slice append error (`spec.Linux.Resources.HugepageLimits`)
- Fix "getCPUInfo for OS freebsd: not implemented" on FreeBSD/arm64
- Fix ctr crash when pulling with --http-dump and --http-trace simultaneously
- Fix LogURI generation-related tests on Windows
- fix the --no-pivot flag being ignored by `ctr tasks start`
- fix: support simultaneous create diff for same parent snapshot
- Fix out of date comments for CRI store packages
- fix can't edit object by using ctr content edit command
- ctr: Fix `ctr c create` fails to parse arguments
- Correct spelling mistake ("sanbdox" to "sandbox")
- vendor: github.com/urfave/cli v1.22.9 and fix "verify-vendor" script
- Fix tx closed error when upperdirlabel specified
- fix comments on metadata schema and update namespace doc
- (Vagrant CI) Enable git commands due to git CVE fix
- fix the restart desired to running when task not found
- tracing: fix panic on startup when configured
- metrics/cgroups: fix deadlock issue in Add during Collect
- fix: ctr images mount with snapshotter option can't get snapshotter
- native: fix deadlock from leaving transactions open
- [Windows] Fix deadline exceeded in daemon restart
- cri: fix integration test on cgroupsv2 system
- ParseCgroupFile: fix wrong comment about unified hierarchy ; add ParseCgroupFileUnified to get the unified path
- fixes: fix resource adjustment to properly ignore unset/unadjusted fields
- adaptation: fix a panic for unsolicited updates
- server: Fix connection issues when receiving ECONNRESET

### 1.7.1

- **Fix premature close of CRI service when there are no CNI configuration monitors**
- **Fix skip docker manifest option on image exporter**
- **Fix transfer service configuration options**
- **Fix server-side goroutine leak on receive message error** ([ttrpc#141](https://github.com/containerd/ttrpc/pull/141))
- **Fix panic caused by race to close send channel** ([ttrpc#140](https://github.com/containerd/ttrpc/pull/140))
- **Fix unmarshal to return non-nil object when nil value** ([ttrpc#140](https://github.com/containerd/typeurl/pull/41))
- [release/1.7] runtime/shim: fix the nil checkpoint options ([#8475](https://github.com/containerd/containerd/pull/8475)) [`3ef5b689a`](https://github.com/containerd/containerd/commit/3ef5b689a7b7f6bb670ad59345c290114e5e29ef) runtime/shim: fix the nil checkpoint options
- [release/1.7] Transfer service backports ([#8491](https://github.com/containerd/containerd/pull/8491)) [`35e86f96c`](https://github.com/containerd/containerd/commit/35e86f96c24da795b3977f181b16a493a7400fdb) [transfer] avoid setting limiters when max is 0 [`f7233811f`](https://github.com/containerd/containerd/commit/f7233811f6fb2d521e65ecf5b156f82a1aba2f91) Update transfer configuration [`4510eac00`](https://github.com/containerd/containerd/commit/4510eac009eb066501761a1dae05d4e126ef88e0) Fix image pulling with Transfer service
- [release/1.7] cri: Fix umarshal metrics ([#8472](https://github.com/containerd/containerd/pull/8472)) [`95ef67e19`](https://github.com/containerd/containerd/commit/95ef67e19552aaec3618cdfa06d6d3ffb57d085b) Fix umarshal metrics for CRI server
- [release/1.7] fix the task setting the runtime path ([#8453](https://github.com/containerd/containerd/pull/8453)) [`c0e128624`](https://github.com/containerd/containerd/commit/c0e128624a8d6a02bb7d2ab3d29369f54791b68e) skip TestContainerStartWithAbsRuntimePath if the runtime is v1 [`aa3c63c15`](https://github.com/containerd/containerd/commit/aa3c63c15f379eec906cb89f7e1204a42a5d1317) integration: add container start test using abs runtime path [`d2d9eedb1`](https://github.com/containerd/containerd/commit/d2d9eedb1d1b2d047fbdd847ce7c67724f27bde4) WithRuntimePath uses the TaskInfo.RuntimePath field
- [release/1.7] Fix argsEscaped tests ([#8405](https://github.com/containerd/containerd/pull/8405)) [`a6d336c1f`](https://github.com/containerd/containerd/commit/a6d336c1f6674c2b342d65ca78fba7fac955eaf1) Fix argsEscaped tests
- [release/1.7] ctr/tasks: fix unmarshal the task metrics for cgroups v1 ([#8335](https://github.com/containerd/containerd/pull/8335)) [`1a64f1b43`](https://github.com/containerd/containerd/commit/1a64f1b4341ebda4b8f8cf67cac543394a10a4c3) ctr/tasks: fix unmarshal the task metrics for cgroups v1
- [release/1.7] Backport Sandbox/CRI fixes ([#8282](https://github.com/containerd/containerd/pull/8282)) [`1c1b6bcb2`](https://github.com/containerd/containerd/commit/1c1b6bcb2b4a47053855bd7adaed5d9bfdf2a5f5) CRI: Don't always close netConfMonitor channel [`cf2e454bf`](https://github.com/containerd/containerd/commit/cf2e454bf052bee63c0582552566c96357bd2250) Sandbox: Correct/add some fields to Status() [`ce68e8e0d`](https://github.com/containerd/containerd/commit/ce68e8e0db47174580fc74ecdeb66c26695ecd0b) Sandbox: Cleanup shim on Start failure

### 1.7.2

- [1.7 backport] Fix panic when remote differ returns empty result ([#8631](https://github.com/containerd/containerd/pull/8631)) [`e134b6393`](https://github.com/containerd/containerd/commit/e134b639396ab07513fecfa221fc4ad8634b2154) Fix panic when remote differ returns empty result
- [release/1.7 backport] Mount snapshots on Windows ([#8616](https://github.com/containerd/containerd/pull/8616)) [`313c226b8`](https://github.com/containerd/containerd/commit/313c226b8b9c30995b90d9a6535b2972707afbd4) Update continuity to a tagged version [`8dd16285a`](https://github.com/containerd/containerd/commit/8dd16285a0558c56255f7d88a509d0e8d930efe3) UnmountAll is a no-op for missing mount points [`acff3eefa`](https://github.com/containerd/containerd/commit/acff3eefa69b6d0238062396fb91df5cfb699603) Improve error messages and remove check [`b4dd3bf4e`](https://github.com/containerd/containerd/commit/b4dd3bf4e291b6be928de1be272740c6a9f2dd3e) Make ReadOnly() available on all platforms [`08d8baf3f`](https://github.com/containerd/containerd/commit/08d8baf3f4d82d5917e8acc94e50d25b4d7d6500) Increase integration test tmieout to 20m [`1f0dbd011`](https://github.com/containerd/containerd/commit/1f0dbd011ae5b635039646f29bba2e0b288d95ca) Remove bind code path in mount() [`8f37b1c63`](https://github.com/containerd/containerd/commit/8f37b1c63712aefeef8e3c357e85ebde8f670ba8) Remove "bind" code path from diff [`9139208b3`](https://github.com/containerd/containerd/commit/9139208b319828e0cafe8110743fa455dc3b75f1) Properly mount base layers [`e61e7b312`](https://github.com/containerd/containerd/commit/e61e7b31263ca717d2ff00b37abdc83ff0f5346f) Skip parent layer options on bind mounts [`e4307926f`](https://github.com/containerd/containerd/commit/e4307926f327e35cc5fcd012ac4854cf85cbee07) Add ReadOnly() function [`0277b9b01`](https://github.com/containerd/containerd/commit/0277b9b01a4992ba315f379ca599bf080dd6495b) Remove escalated privileges [`d5c18dfb7`](https://github.com/containerd/containerd/commit/d5c18dfb7ed449e0232ccafcc6f4cb9a2473221d) Use DefaultSnapshotter [`853179366`](https://github.com/containerd/containerd/commit/853179366b2aa7bebd17903faa0ada9dcf9297cc) use t.Fatal if we cannot enable process privileges [`5b3ee413f`](https://github.com/containerd/containerd/commit/5b3ee413f49fac47017cfacf09176e9701052096) Update continuity [`375172604`](https://github.com/containerd/containerd/commit/375172604df61e312810efbb7fc0080df5a0ab2c) Fix go.mod, simplify boolean logic, add logging [`600abd137`](https://github.com/containerd/containerd/commit/600abd13791fcc6b3dd23c7f78f8c8c796340e33) Ignore ERROR_NOT_FOUND error when removing mount [`df7295dcd`](https://github.com/containerd/containerd/commit/df7295dcdf00839423109ac65b1dc9429f632e00) Update continuity, go-winio and hcsshim [`0db78c482`](https://github.com/containerd/containerd/commit/0db78c48269f54b9335183b2b0d7b6138253e9e5) Remove unused function [`219058766`](https://github.com/containerd/containerd/commit/2190587661ded992f2b0a55a08e3201b93e0b5a2) Grant needed privileges for snapshotter tests [`96fbe5bc8`](https://github.com/containerd/containerd/commit/96fbe5bc882658780ca36499a0e0a79d095b83e8) Fix layer comparison and enable read-only checks [`279e0d3c9`](https://github.com/containerd/containerd/commit/279e0d3c9ab199458387b670c19301a94dac8032) Use bind filer for mounts [`93e94da40`](https://github.com/containerd/containerd/commit/93e94da4084f3fbe2d89f3145a8e56c8c24dc458) Enable TestSnapshotterClient on Windows [`3a3da693a`](https://github.com/containerd/containerd/commit/3a3da693aee68afdc84ca42c0191cee88ee9c21f) Run Windows snapshotter through the test suite [`e7b62322f`](https://github.com/containerd/containerd/commit/e7b62322f9218387e6f715442b2235c9feec2e01) Fix misspelling of 'Native' as 'Naive' [`e1f999a18`](https://github.com/containerd/containerd/commit/e1f999a1827242a31fa85cbb4a44ee31eeebfb30) Add paired 'mount' log for 'unmount' [`5788d6e52`](https://github.com/containerd/containerd/commit/5788d6e520cef08aaf2d15ceaf5c4c6b1ce735e6) Don't use all-upper-case filenames in snapshot tests [`3cdcb2f10`](https://github.com/containerd/containerd/commit/3cdcb2f1088eab8d18075b0549ae59688bf15792) Skip tests that do not apply to WCOW on Windows [`b0968b8bb`](https://github.com/containerd/containerd/commit/b0968b8bb920c99d341cb212bde9a4d15c050dfc) Ensure mounts are unmounted before leaving the test [`b57424851`](https://github.com/containerd/containerd/commit/b57424851cc56745d677ee41e0d5a02dde29bc41) Unify testutil.Unmount on Windows and Unix [`b9a8aad45`](https://github.com/containerd/containerd/commit/b9a8aad45149c40c8b5c327657a5320de29231c5) Implement Windows mounting for bind and windows-layer mounts [`1a64ee183`](https://github.com/containerd/containerd/commit/1a64ee1835544d37903f667415c821526200ed8b) Implement WCOW parentless active snapshots and view snapshots
- [release/1.7] fix: cio.Cancel() should close the pipes ([#8624](https://github.com/containerd/containerd/pull/8624)) [`99582fb1a`](https://github.com/containerd/containerd/commit/99582fb1a32e9d051585219d11146afb07805abf) fix: cio.Cancel() should close the pipes
- [release/1.7 backport] remotes/docker: ResolverOptions: fix deprecation comments ([#8621](https://github.com/containerd/containerd/pull/8621)) [`eeda70fb0`](https://github.com/containerd/containerd/commit/eeda70fb04814f240c7e5d0f59a6369b1fdae69e) remotes/docker: ResolverOptions: fix deprecation comments
- [release/1.7] Publish sandbox events ([#8613](https://github.com/containerd/containerd/pull/8613)) [`e21c8beee`](https://github.com/containerd/containerd/commit/e21c8beee6c07fd289af2cf0011e0aa8156882e4) Post cherry-pick fixes [`246240f71`](https://github.com/containerd/containerd/commit/246240f71ce2adcfc5b161343f21a72fa32c1273) Move PLEG event back to CRI [`16f3726dd`](https://github.com/containerd/containerd/commit/16f3726dd61ba8fa71d04957681b53a14cc5b055) Generate sandbox exit events from CRI [`0c8cfb1a7`](https://github.com/containerd/containerd/commit/0c8cfb1a7c0f852842016ad0805bf8a121ede970) Move pod sandbox recovery to podsandbox/ package [`91d9f5c64`](https://github.com/containerd/containerd/commit/91d9f5c643c4bc6d44964c161a56eb04201fc885) Publish sandbox events [`4b77683b4`](https://github.com/containerd/containerd/commit/4b77683b46182fcdf756509767660389d2eb7169) Add sandbox events protos
- [release/1.7 backport] snapshots/testsuite: Rename: fix fuse-overlayfs incompatibility ([#8510](https://github.com/containerd/containerd/pull/8510)) [`9e60300ea`](https://github.com/containerd/containerd/commit/9e60300ea0b1635d8d7798fc99c824cab82926f3) snapshots/testsuite: Rename: fix fuse-overlayfs incompatibility
- Enable tests for all platforms ([#220](https://github.com/containerd/continuity/pull/220)) [`b449cd0`](https://github.com/containerd/continuity/commit/b449cd0f764c0dc97ed496c2d3b5f8d673c6b7a6) Fix tests on Windows [`eb05879`](https://github.com/containerd/continuity/commit/eb058795cb5ebba43e2a0a33f540bbc2c37945c4) Fix Darwin tests [`9cd17be`](https://github.com/containerd/continuity/commit/9cd17bee62e96e79fd579ef64d86b86ec6ac6cc8) Enable tests for all platforms

### 1.7.3

- **CRI: Fix additionalGids: it should fallback to imageConfig.User when securityContext.RunAsUser,RunAsUsername are empty**
- **Resolve docker.NewResolver race condition**
- **Fix net.ipv4.ping_group_range with userns**
- [release/1.7 backport] [CRI] fix additionalGids: it should fallback to imageConfig.User when securityContext.RunAsUser,RunAsUsername are empty ([#8824](https://github.com/containerd/containerd/pull/8824)) [`083f57160`](https://github.com/containerd/containerd/commit/083f571609a83be94785b77a822aa7c332eeabfd) capture desc variable in range variable just in case that it run in parallel mode [`a9440ce6b`](https://github.com/containerd/containerd/commit/a9440ce6b5a150be998c70549984b508231a6dbe) Use t.TempDir instead of os.MkdirTemp [`eea3440d8`](https://github.com/containerd/containerd/commit/eea3440d899f6ce74fca5257dcc53e6cecc4fce4) use strings.Cut instead of strings.Split for parsing imageConfig.User [`eace67180`](https://github.com/containerd/containerd/commit/eace671808e39d351c54e917fed86a58b92fe43b) fix userstr for dditionalGids on Linux
- [release/1.7] Fix net.ipv4.ping_group_range with userns ([#8786](https://github.com/containerd/containerd/pull/8786)) [`241514815`](https://github.com/containerd/containerd/commit/241514815d278865199a701f23b83a20efe169be) pkg/cri/server: Test net.ipv4.ping_group_range works with userns [`801e8c806`](https://github.com/containerd/containerd/commit/801e8c8069c4613de305c756c0f497f271ef3648) pkg/cri/server: Fix net.ipv4.ping_group_range with userns
- [release/1.7] Fix issue for HPC pod metrics ([#8634](https://github.com/containerd/containerd/pull/8634)) [`89415fe36`](https://github.com/containerd/containerd/commit/89415fe36162576fb88b0fd7c117238834f2c967) Fix issue for HPC pod metrics
- follow-up-#52: fix the order of cause in fmt.Errorf ([#53](https://github.com/containerd/zfs/pull/53)) [`b3f193d`](https://github.com/containerd/zfs/commit/b3f193d7f00753424184bfd0c584e5c56e7de659) follow-up-#52: fix the order of cause in fmt.Errorf
- README.md: fix CI badge ([#46](https://github.com/containerd/zfs/pull/46)) [`0977d81`](https://github.com/containerd/zfs/commit/0977d815b7d76b21cb861b04c0f0414d26af3046) README.md: fix CI badge

### 1.7.4

- **Fix leaked shim caused by high IO pressure**
- [release/1.7] Port fix for Linux Integration test failure ([#8950](https://github.com/containerd/containerd/pull/8950)) [`c0b1c8f74`](https://github.com/containerd/containerd/commit/c0b1c8f74aa5616c5e27845d18d4dca5ab30f9fd) fix ci Linux Integration test fail
- [release/1.7] fix: allow attaching to any combination of stdin/stdout/stderr ([#8910](https://github.com/containerd/containerd/pull/8910)) [`34a5d0330`](https://github.com/containerd/containerd/commit/34a5d033007eaae0530a89470407fbe920eec033) fix: allow attaching to any combination of stdin/stdout/stderr
- [release/1.7] cherry-pick: Fix ro mount option being passed ([#8887](https://github.com/containerd/containerd/pull/8887)) [`2eaeb3205`](https://github.com/containerd/containerd/commit/2eaeb3205a1bd61b385a259d43f29ccc09993e18) Fix ro mount option being passed

### 1.7.6

- **Fix log package for clients overwriting the global logger**
- [release/1.7] Invoke Stable ABI compatibility function in windows platform matcher ([#9069](https://github.com/containerd/containerd/pull/9069)) [`c7a35ccdc`](https://github.com/containerd/containerd/commit/c7a35ccdcc674e42c2364f062890b1e40507f543) Fix transfer service dependencies: [`38d4e506d`](https://github.com/containerd/containerd/commit/38d4e506dd261b48bffbdd04e775d2b687290e2f) Invoke Stable ABI compatibility function in windows platform matcher

### 1.7.7

- **remotes/docker: Fix MountedFrom prefixed with target repository**
- [release 1.7] remotes/docker: Fix MountedFrom prefixed with target repository ([#9193](https://github.com/containerd/containerd/pull/9193)) [`7df492a95`](https://github.com/containerd/containerd/commit/7df492a95c7283a3f402b5a0e96030e42724d9d0) remotes/docker: Fix MountedFrom prefixed with target repository
- stub: pass context to plugins, pass updated resources to UpdateContainers. ([#40](https://github.com/containerd/nri/pull/40)) [`01d5f14`](https://github.com/containerd/nri/commit/01d5f14d96708830f232b2744742fc14763816b1) Add a note about NRI API stability and release notes. [`ea9976d`](https://github.com/containerd/nri/commit/ea9976d8dae3a6e630da76a26dbef44b5c8a3de3) adaptation: add UpdateContainer tests. [`d042d24`](https://github.com/containerd/nri/commit/d042d24bc4a96fa5fcf1aa0d2195ff75833d7d4e) stub: fix plugin UpdateContainerInterface. [`f5d0f51`](https://github.com/containerd/nri/commit/f5d0f513608b2afc3fcc5e6bdf76b10b3004c14c) plugins: update plugins for stub changes. [`b4bd301`](https://github.com/containerd/nri/commit/b4bd301a1ead4d277af088e321c05e76102c8769) adaptation: update tests with stub changes. [`9d86150`](https://github.com/containerd/nri/commit/9d86150fce4318491481e354d0f34c6b76e8806e) stub: pass context to plugin event handlers
- Fix ParseEventMask to produce proper masks for 'pod' and 'container' shorthand event notations. ([#39](https://github.com/containerd/nri/pull/39)) [`da291a6`](https://github.com/containerd/nri/commit/da291a66180b6989a6dcc6bcffcc3257c185f8f8) Fix ParseEventMask to produce proper masks
- fix the `NRI_PLUGIN_NAME` env value when launching a pre-installed plugin ([#42](https://github.com/containerd/nri/pull/42)) [`4a4cea6`](https://github.com/containerd/nri/commit/4a4cea6142a5a34301b796a36355e3b38bb98522) fix the NRI_PLUGIN_NAME env value when launching a pre-installed plugin [`a67478e`](https://github.com/containerd/nri/commit/a67478ed7c0b38454f3ef4e86f36d870c365c0d5) stub: update setIdentify to ensureIdentify

### 1.7.8

- **Fix handling for missing basic auth credentials**
- **Fix potential deadlock in create handler for containerd-shim-runc-v2**
- [release/1.7] Fix ambiguous tls fallback ([#9299](https://github.com/containerd/containerd/pull/9299)) [`68abc543b`](https://github.com/containerd/containerd/commit/68abc543b1eb4a8196842de6c83115ba4e5698b0) Check scheme and host of request on push redirect [`35c7634e3`](https://github.com/containerd/containerd/commit/35c7634e33651053a934bbcb831c90ddc65ede2e) Avoid TLS fallback when protocol is not ambiguous

### 1.7.9

- [release/1.7] fix: shimv1 leak issue ([#9344](https://github.com/containerd/containerd/pull/9344)) [`449912857`](https://github.com/containerd/containerd/commit/449912857d8191c986537af00325d9999922fce3) fix: shimv1 leak issue

### 1.7.10

- **cri: fix using the pinned label to pin image**
- **fix: ImagePull should close http connection if there is no available data to read.**
- [release/1.7] fix: ImagePull should close http connection if there is no available data to read. ([#9409](https://github.com/containerd/containerd/pull/9409)) [`206806128`](https://github.com/containerd/containerd/commit/206806128917276994f0949dc599e4c8b8ad8f14) remotes/docker: close connection if no more data [`328493962`](https://github.com/containerd/containerd/commit/32849396263f9c68f7c4f43a2abc1319488546de) integration: reproduce #9347 [`d1aab27cb`](https://github.com/containerd/containerd/commit/d1aab27cbd8ae75d90ad962a256d6af092dcf451) fix: deflake TestCRIImagePullTimeout/HoldingContentOpenWriter
- [release/1.7] cri: fix using the pinned label to pin image ([#9381](https://github.com/containerd/containerd/pull/9381)) [`a2b16d7f9`](https://github.com/containerd/containerd/commit/a2b16d7f9cd44f81ebdcffe92dee107b2ebdca8a) cri: fix update of pinned label for images [`8dc861844`](https://github.com/containerd/containerd/commit/8dc8618442ad99a254de79200c89eb12284dac6e) cri: fix using the pinned label to pin image

### 1.7.11

- **Fix Windows snapshotter blocking snapshot GC on remove failure**
- [release/1.7] Fix otel version incompatibility ([#9483](https://github.com/containerd/containerd/pull/9483)) [`f8f659e66`](https://github.com/containerd/containerd/commit/f8f659e66c6ec56fef092dced085d129c0e67176) Add HTTP client update function to tracing library [`807ddd658`](https://github.com/containerd/containerd/commit/807ddd658b4cd6c0325204e7a19a4561a10906d2) fix(tracing): use latest version of semconv
- [release/1.7] cri: add deprecation warnings for deprecated CRI configs ([#9469](https://github.com/containerd/containerd/pull/9469)) [`9d1bad62e`](https://github.com/containerd/containerd/commit/9d1bad62e16f31e0b06c75e1007a623879529a6d) deprecation: fix missing spaces in warnings [`51a604c07`](https://github.com/containerd/containerd/commit/51a604c0733437f4b7a20aa5ec1e6d4b4f0ab96e) cri: add deprecation warning for runtime_root [`8040e74bf`](https://github.com/containerd/containerd/commit/8040e74bf8e6c25c02bb461b82f482cff24ce611) cri: add deprecation warning for rutnime_engine [`99adc40eb`](https://github.com/containerd/containerd/commit/99adc40eb28db7cb93c378ff8bceb8e77559ae09) cri: add deprecation warning for default_runtime [`afef7ec64`](https://github.com/containerd/containerd/commit/afef7ec646910ce1db3e824bfe17848428f3b47b) cri: add warning for untrusted_workload_runtime [`6220dc190`](https://github.com/containerd/containerd/commit/6220dc1909883119a960bc96c496ae2361b94749) cri: add warning for old form of systemd_cgroup
- [release/1.7] Windows default path overwrite fix ([#9440](https://github.com/containerd/containerd/pull/9440)) [`31fe03764`](https://github.com/containerd/containerd/commit/31fe03764c436677a1db9be24c25f7c11780eceb) Fix windows default path overwrite issue

### 1.7.12

- [release 1.7] backport: fix on dialer function for windows ([#9501](https://github.com/containerd/containerd/pull/9501)) [`68d237392`](https://github.com/containerd/containerd/commit/68d2373926bc0a9dcc2fb6cdf49dd2188a327b9f) fix(pkg/dialer): minor fix on dialer function for windows

### 1.7.14

- update to go 1.21.6, test 1.22.0 ([#9860](https://github.com/containerd/containerd/pull/9860)) [`3b3e537ea`](https://github.com/containerd/containerd/commit/3b3e537eab7f81e32f34c95833caa2af9bc8753f) Uninstall mingw before attempting upgrade [`9e24388b2`](https://github.com/containerd/containerd/commit/9e24388b209e519d7cc3805b3266b9a4a82e59cc) CI: Explicitly upgrade MinGW on Windows 2019 GitHub runners. [`5b23a4127`](https://github.com/containerd/containerd/commit/5b23a412759f27465906f86196c686cd0925be15) seccomp, apparmor: add go:noinline [`753422ac1`](https://github.com/containerd/containerd/commit/753422ac11e3485b14a62bfdfcc75a0001f3dd70) Drop go 1.20 and build against 1.22 [`a2d64218c`](https://github.com/containerd/containerd/commit/a2d64218c5a5abc676556925d63b222dbd606469) Fix windows integration tests [`6379dd6f4`](https://github.com/containerd/containerd/commit/6379dd6f428fc3f55cb4625d7741b84751d42278) Update workflow files to install Go via composite action [`a5c0d061c`](https://github.com/containerd/containerd/commit/a5c0d061cd3a4154f31fd5a5c8a4f77da5da1dcd) Extract a composite action to install Go
- Fix various timing issues with docker pusher ([#9921](https://github.com/containerd/containerd/pull/9921)) [`52a1402df`](https://github.com/containerd/containerd/commit/52a1402df64ca286b5084b1b150c4219343ad6d7) copy: prevent potential deadlock if close before fully written [`872746386`](https://github.com/containerd/containerd/commit/872746386237b1076f8449a7f7d3d5a07ed30a42) copy: setError should imply Close [`a8004007a`](https://github.com/containerd/containerd/commit/a8004007a2ababa6ac7dbf508edf1c49faf06110) copy: remove max number of ErrResets [`0465472ed`](https://github.com/containerd/containerd/commit/0465472ed3807b6dcf785d160783019e3fed5cf6) pushWriter: refactor reset pipe logic into separate function [`2577207cc`](https://github.com/containerd/containerd/commit/2577207cc0611f36e582111f88f16fd5ae777068) copy: improve error detection from closed pipes [`d081da86b`](https://github.com/containerd/containerd/commit/d081da86bfc3b1b65efacdefba0e48aadaac4d91) copy: check if writer was closed before setting a pipe [`2a25c085b`](https://github.com/containerd/containerd/commit/2a25c085b21e074667bf6ded0dbb6ebf892a889c) copy: remove wrapping io.NopCloser from push writer pipe
- github: windows should use fix critool version ([#9874](https://github.com/containerd/containerd/pull/9874)) [`d9c099a9a`](https://github.com/containerd/containerd/commit/d9c099a9ac39956aee0a720be8b3b6af8861351b) .github: windows should use fix critool version
- bug fix: make sure cri image is pinned when it is pulled outside cri ([#9784](https://github.com/containerd/containerd/pull/9784)) [`26c057423`](https://github.com/containerd/containerd/commit/26c057423c614deb0c510ceea84ed22bbe4f7f1d) bug fix: make sure cri image is pinned when it is pulled outside cri
- scripts: fix protobuf URL on arm64 ([containerd/nri#52](https://github.com/containerd/nri/pull/52)) [`9b43daa`](https://github.com/containerd/nri/commit/9b43daaeceae6750053c5693a15edc59819886b9) scripts: fix protobuf URL on arm64
- Fix grammar in comment for UserOnCloseWait. ([containerd/ttrpc#153](https://github.com/containerd/ttrpc/pull/153)) [`8ca4110`](https://github.com/containerd/ttrpc/commit/8ca4110ebc91819c5b0e2f17c9ded818b2462c50) Fix comment for UserOnCloseWait

### 1.7.15

- Fix runc shim to only defer init process exits
- Fix runc shim to only defer init process exits ([#10037](https://github.com/containerd/containerd/pull/10037)) [`21df46766`](https://github.com/containerd/containerd/commit/21df4676621559e46b46810de3c900d105f10210) runc-shim: only defer init process exits
- Fix compile from version control system (source) use case ([#10012](https://github.com/containerd/containerd/pull/10012)) [`2a054213e`](https://github.com/containerd/containerd/commit/2a054213e7d167d697a27bbe8409872c67e8df46) Fix compile from version control system (source) use case

### 1.7.16

- Prevent GC from schedule itself with 0 period
- Fix issue with using invalid token to retry fetching layer
- Fix deadlock during NRI plugin registration ([containerd/nri#79](https://github.com/containerd/nri/pull/79))
- Update Go to 1.21.9 and 1.22.2 with net/http security fix
- Fix CRI snapshotter root path when not under containerd root
- Fix network creation failure from CreatedAt time as 269 years ago
- Fix default working directory Windows HostProcess containers
- Fix ListPodSandboxStats to skip sandboxes with missing tasks
- Fix config import relative path glob ([#9834](https://github.com/containerd/containerd/pull/9834)) [`62e9535f2`](https://github.com/containerd/containerd/commit/62e9535f295f4026d69280107c08c6b6a4eb5417) Fix config import relative path glob
- Fix CRI snapshotter root path when not under containerd root ([#10096](https://github.com/containerd/containerd/pull/10096)) [`a8ebceb97`](https://github.com/containerd/containerd/commit/a8ebceb972efdc5ead7535640f531972a95280cb) CRI: "Fix" imageFSPath behavior [`bd423bf84`](https://github.com/containerd/containerd/commit/bd423bf84d2ddef9680f54670a1e6ec2d7a18329) Snapshotters: Export the root path [`8fb6bfa71`](https://github.com/containerd/containerd/commit/8fb6bfa71753481f065e53245707d74473498d78) Add exports to proxy plugin config [`8916e2cf9`](https://github.com/containerd/containerd/commit/8916e2cf9dfa7e1dfe609334540a14a15156bfe6) Add platform config to proxy plugins
- Fix network creation failure from CreatedAt time as 269 years ago ([#10122](https://github.com/containerd/containerd/pull/10122)) [`293f5151d`](https://github.com/containerd/containerd/commit/293f5151d44c8a700a7244fed09c37524a89a82a) pod: CreatedAt time will be 269 years ago while creating cri network failed
- Update Go to 1.21.9 and 1.22.2 with net/http security fix ([#10115](https://github.com/containerd/containerd/pull/10115)) [`637d259dd`](https://github.com/containerd/containerd/commit/637d259dd6646d16c71e295e056dec291b506892) update to go1.21.9, go1.22.2
- Prevent GC from schedule itself with 0 period. ([#10102](https://github.com/containerd/containerd/pull/10102)) [`5c15bf406`](https://github.com/containerd/containerd/commit/5c15bf406da3a40d19ba89c7cd90080047d3793e) Prevent GC from schedule itself with 0 period
- Fix issue with using invalid token to retry fetching layer ([#10065](https://github.com/containerd/containerd/pull/10065)) [`f61de0864`](https://github.com/containerd/containerd/commit/f61de08644b73e7836ac46234b3f6283fc9715dd) fix bug that using invalid token to retry fetching layer
- Fix default working directory Windows HostProcess containers ([#10071](https://github.com/containerd/containerd/pull/10071)) [`989f1ec54`](https://github.com/containerd/containerd/commit/989f1ec54f6764020447b03020b97592312c5f85) fix default working directory `hostProcess`
- Fix unexpected order of mounts since go 1.19 ([#10063](https://github.com/containerd/containerd/pull/10063)) [`9f774e438`](https://github.com/containerd/containerd/commit/9f774e438b9d96a901adb11e580fa03c6264f667) fix(cri): fix unexpected order of mounts since go 1.19
- Fix HTTPFallback fails when pushing manifest ([#10044](https://github.com/containerd/containerd/pull/10044)) [`18f4ad5ee`](https://github.com/containerd/containerd/commit/18f4ad5ee0cb65fa99df752e2ce7d4728b19f9f0) remote: Fix HTTPFallback fails when pushing manifest
- Fix ListPodSandboxStats to skip sandboxes with missing tasks ([#10042](https://github.com/containerd/containerd/pull/10042)) [`90c309fe2`](https://github.com/containerd/containerd/commit/90c309fe2f6fac7cc620467edf2eeb8b19211067) Add IsNotFound case to ListPodSandboxStats

### 1.7.17

- Fix deadlock when writing to pipe blocks ([containerd/ttrpc#168](https://github.com/containerd/ttrpc/pull/168))
- Update tooling to Go 1.21.10, 1.22.3 for net/http bug fixes ([#10207](https://github.com/containerd/containerd/pull/10207)) [`c53b635f9`](https://github.com/containerd/containerd/commit/c53b635f927a905ff431a51d12f42f4f5c36d959) Update toolchain to Go 1.21.10 and 1.22.3
- Fix some issues in the test script ([containerd/imgcrypt#115](https://github.com/containerd/imgcrypt/pull/115)) [`aa517cc`](https://github.com/containerd/imgcrypt/commit/aa517cc77654cf517cc7bba5529b07da92f033dc) test: Fix order of parameters and remove unnecessary key parameter [`ec72311`](https://github.com/containerd/imgcrypt/commit/ec7231185e276feb10f5b4b974ade62a81d5e9ad) test: Add comments to test case [`2959ec0`](https://github.com/containerd/imgcrypt/commit/2959ec0ec47786956223715812f40eb9e7301786) test: To be able to run testLocalKeys alone add missing env variable
- README: Fix a typo ([containerd/imgcrypt#105](https://github.com/containerd/imgcrypt/pull/105)) [`12e84f5`](https://github.com/containerd/imgcrypt/commit/12e84f51fb70e1fb2bcc624206f707b48671b352) README: Fix a typo
- Fix proto3 generation error ([containerd/ttrpc#158](https://github.com/containerd/ttrpc/pull/158)) [`73b6a91`](https://github.com/containerd/ttrpc/commit/73b6a9156d6dc4644c94f5a683219ba8aac9fb18) Add optional feature in protobuf compiler

### 1.7.18

- Fix usage of "unknown" platform ([#10261](https://github.com/containerd/containerd/pull/10261)) [`f4d11912a`](https://github.com/containerd/containerd/commit/f4d11912a77c1e15db200aed7481d45bd12b5eb1) core/image: fix usage of "unknown" platform

### 1.7.19

- Fix panic in NRI from nil CRI reference ([#10406](https://github.com/containerd/containerd/pull/10406)) [`7f5d3c5f4`](https://github.com/containerd/containerd/commit/7f5d3c5f4d5325265f3dfe76f9cc4c17859a6e8a) cri: ensure NRI API never has nil CRI
- Updating hcsshim vendoring to 0.11.7 to include an important backported fix ([#10396](https://github.com/containerd/containerd/pull/10396)) [`415dd74a8`](https://github.com/containerd/containerd/commit/415dd74a81ad3a5ed5cc416ad16cfe3cbb09aec3) updating hcsshim to 0.11.7
- Fix support for OTLP config ([#10360](https://github.com/containerd/containerd/pull/10360)) [`1ce1c8f3e`](https://github.com/containerd/containerd/commit/1ce1c8f3e6d36202dab28fe910bf9282fafc2aab) 1.7: Add back support for OTLP config from toml
- Fix Windows HPC working directory ([#10306](https://github.com/containerd/containerd/pull/10306)) [`33b62936e`](https://github.com/containerd/containerd/commit/33b62936ea56c85183331ad2b1d9cb3c76dce8da) [release/1.7]: HPC working directory fix in pkg/cri/server code
- Fix windows matching when os version is empty ([containerd/platforms#11](https://github.com/containerd/platforms/pull/11)) [`983ba15`](https://github.com/containerd/platforms/commit/983ba156b67be3c9597b773bd1f509f0ba693c3d) Update windows matcher to not compare empty os version [`17c859f`](https://github.com/containerd/platforms/commit/17c859f02e8008cc3a4fba44314aa35c947e3f7f) Add tests for osversion matching with no version
- fix grammar and highlights in README ([containerd/platforms#3](https://github.com/containerd/platforms/pull/3)) [`cb03428`](https://github.com/containerd/platforms/commit/cb034281bd28d792528b116680b2bbabac7bef75) fix grammar and highlights in README
- Fix link in README ([containerd/platforms#1](https://github.com/containerd/platforms/pull/1)) [`5b937b0`](https://github.com/containerd/platforms/commit/5b937b0167e6bbe5c715dc03e0d37a00f6e833f2) Fix link in README
- Fix CI build status badge in readme ([containerd/ttrpc#162](https://github.com/containerd/ttrpc/pull/162)) [`e0f3ead`](https://github.com/containerd/ttrpc/commit/e0f3eadca58efdd8f24904d02ba8e1d8a561ec37) Fix CI build status badge in readme

### 1.7.20

- Fix for `[cri] ttrpc: closed` during ListPodSandboxStats
- Fix for `[cri] ttrpc: closed` during ListPodSandboxStats ([#10423](https://github.com/containerd/containerd/pull/10423)) [`610498df7`](https://github.com/containerd/containerd/commit/610498df750c3b30b137ddb4ab236e5b0a84ceda) Fix for `[cri] ttrpc: closed` during ListPodSandboxStats

### 1.7.21

- Fix failed force deletion for tasks with PID 0
- Fix packaged runc reporting incorrect version
- Fix TestNewBinaryIOCleanup on Go 1.23 and Linux 5.4 ([#10590](https://github.com/containerd/containerd/pull/10590)) [`09ca004de`](https://github.com/containerd/containerd/commit/09ca004dee1fe7752a652f474661e23d7e3489d4) Fix TestNewBinaryIOCleanup on Go 1.23 and Linux 5.4
- Fix TestNewBinaryIOCleanup failing with gotip ([#10554](https://github.com/containerd/containerd/pull/10554)) [`3ff82ba0f`](https://github.com/containerd/containerd/commit/3ff82ba0f007e0fb856f7b2b174f5bc1ab1237cd) Fix TestNewBinaryIOCleanup failing with gotip
- Fix packaged runc reporting incorrect version ([#10559](https://github.com/containerd/containerd/pull/10559)) [`d51143f6f`](https://github.com/containerd/containerd/commit/d51143f6fad370fce2c2f5b0507365fb0a229372) script/setup/install-runc: fix runc using incorrect version
- Fix failed force deletion for tasks with PID 0 ([#10523](https://github.com/containerd/containerd/pull/10523)) [`0db46f664`](https://github.com/containerd/containerd/commit/0db46f664ab1394add6c813b764121a5f12d6ef3) client: fix tasks with PID 0 cannot be forced to delete

### 1.7.22

- Fix bug where init exits were being dropped ([#10675](https://github.com/containerd/containerd/pull/10675)) [`f338717ed`](https://github.com/containerd/containerd/commit/f338717ed4fdc06d289b8d6e2862eeb3035b32da) runc-shim: handle pending execs as running [`686c69490`](https://github.com/containerd/containerd/commit/686c69490d0bb9ed6513b3ed2f2502ec65b11d75) runc-shim: refuse to start execs after init exits [`760935e52`](https://github.com/containerd/containerd/commit/760935e5211df1b6681fcf14d62804710fe512cd) runc-shim: remove misleading comment

### 1.7.23

- Fix the race condition during GC of snapshots when client retries
- TestNewBinaryIOCleanup: fix a comment, minor rewrite ([#10776](https://github.com/containerd/containerd/pull/10776)) [`7fd794a7c`](https://github.com/containerd/containerd/commit/7fd794a7cd9ce246d1792842f2c6c0c16d9bdd76) TestNewBinaryIOCleanup: fix a comment, minor rewrite
- Fix the race condition during GC of snapshots when client retries ([#10763](https://github.com/containerd/containerd/pull/10763)) [`cb5e6a01a`](https://github.com/containerd/containerd/commit/cb5e6a01a30dd6a34d4f7c25d8d429a5173bc541) Fix the race condition during GC of snapshots when client retries
- Fix Cancelled interface typo ([containerd/errdefs#6](https://github.com/containerd/errdefs/pull/6)) [`9564d8f`](https://github.com/containerd/errdefs/commit/9564d8ff88294257499cd16f16b8814ef78021b6) Fix Cancelled interface typo

### 1.7.24

- Fix "invalid metric type" error message for cgroup v1
- Fix retry logic and concurrency issue with http fallback
- Fix retry logic and concurrency issue with http fallback ([#11032](https://github.com/containerd/containerd/pull/11032)) [`10af0d60f`](https://github.com/containerd/containerd/commit/10af0d60fbaa20cc07c0d54c60ef22e349efce42) Adds a mutex to protect fallback host [`e426ec51b`](https://github.com/containerd/containerd/commit/e426ec51ba9f27a64ba21a2c9a0902cfc8493832) Use unix and windows specific connection error checks [`49c9f303b`](https://github.com/containerd/containerd/commit/49c9f303b1d35101bb798cb37c57b06cd1eacf5e) Allow fallback across default ports
- Avoid arch info in the sed/replace when building cri-cni-containerd.tar.gz ([#10976](https://github.com/containerd/containerd/pull/10976)) [`b7bb8d515`](https://github.com/containerd/containerd/commit/b7bb8d5158a497cff0f4735160f528e94b2b8e8b) Avoid arch info in the sed/replace when building cri-cni-containerd.tar.gz
- Fix "invalid metric type" error message for cgroup v1 ([#10814](https://github.com/containerd/containerd/pull/10814)) [`d6f577843`](https://github.com/containerd/containerd/commit/d6f5778439dd9b2bdd7ab3199e6eaaddb3ba39b8) metrics: Use UnmarshalTo instead of UnmarshalAny

### 1.7.25

- Fix `ip_pref` configuration option ([#11223](https://github.com/containerd/containerd/pull/11223)) [`0cfc1edf3`](https://github.com/containerd/containerd/commit/0cfc1edf34648807bd02caf1835fe2c6fddf46fa) Fix "even if IPv4 comes first" test to have IPv4 first [`53d1fd0d9`](https://github.com/containerd/containerd/commit/53d1fd0d96c2c1f3c4997c2fb376203f6491c7d9) Don't use `To16() != nil` to detect IPv6 addresses
- Fix panic due to nil dereference cgroups v2 ([#11099](https://github.com/containerd/containerd/pull/11099)) [`a40aa60a5`](https://github.com/containerd/containerd/commit/a40aa60a5452f92338e252f047871fee2ddd8727) fix panic due to nil dereference cgroups v2
- kind.String(): fix missing case statements for iota consts in switch ([containerd/continuity#256](https://github.com/containerd/continuity/pull/256)) [`7d074e7`](https://github.com/containerd/continuity/commit/7d074e72420162b4e873d4699f2518c02fcb983f) kind.String(): fix missing case statements for iota consts in switch
- go-fix: remove pre-go1.17 build-tags ([containerd/continuity#252](https://github.com/containerd/continuity/pull/252)) [`433b975`](https://github.com/containerd/continuity/commit/433b9755fb2e7489793942d7e7d795c91ded249a) go-fix: remove pre-go1.17 build-tags
- Fix TestDiffDirChangeWithOverlayfs (also updates the CI to use Ubuntu 24.04) ([containerd/continuity#249](https://github.com/containerd/continuity/pull/249)) [`97eff17`](https://github.com/containerd/continuity/commit/97eff17e2d69acf3724a694badf7eedb1c59684f) Fix TestDiffDirChangeWithOverlayfs [`d934057`](https://github.com/containerd/continuity/commit/d93405730daf33f10e26855303a94e126378c90f) CI: use ubuntu-24.04

### 1.7.26

- Fix race between serve and immediate shutdown on the server ([containerd/ttrpc#175](https://github.com/containerd/ttrpc/pull/175))
- Fix fatal concurrency error in port forwarding
- Fix initial sync race when registering NRI plugins
- Fix plugin sync to use multiple messages if ttrpc max message limit is hit ([containerd/nri#111](https://github.com/containerd/nri/pull/111))
- Fix mount removal in adjustments ([containerd/nri#107](https://github.com/containerd/nri/pull/107))
- Upgrade x/net to 0.33.0 to fix vulnerability GHSA-w32m-9786-jp63 ([#11434](https://github.com/containerd/containerd/pull/11434)) [`3486bc8dd`](https://github.com/containerd/containerd/commit/3486bc8dd19acbde278ed6c4c4fa42c7299e1278) Upgrade x/net to 0.33.0
- Fix initial sync race when registering NRI plugins ([#11326](https://github.com/containerd/containerd/pull/11326)) [`11af05177`](https://github.com/containerd/containerd/commit/11af05177545dbb97d87aa861b15d70ab911307c) cri,nri: block NRI plugin sync. during event processing. [`d4036cd3d`](https://github.com/containerd/containerd/commit/d4036cd3d1eb174ea379c8e1d139c25cfe9f18d8) go.{mod,sum}: bump NRI to v0.8.0, re-vendor
- Fix console TTY leak in runc shim ([#11250](https://github.com/containerd/containerd/pull/11250)) [`c3e24e024`](https://github.com/containerd/containerd/commit/c3e24e0248f0ca83d0bfbb0262862c2a06a632e2) Add integ test to check tty leak [`4e45a463d`](https://github.com/containerd/containerd/commit/4e45a463d90fd44f6b92978721779d7b09045cee) fix master tty leak due to leaking init container object
- Fix fatal concurrency error in port forwarding ([#11306](https://github.com/containerd/containerd/pull/11306)) [`0fe9f0b52`](https://github.com/containerd/containerd/commit/0fe9f0b52f7b700689df46d13de36e67b62486e1) fix fatal error: concurrent map iteration and map write
- codespell: add codespell config, workflow, fix spelling errors. ([containerd/nri#105](https://github.com/containerd/nri/pull/105)) [`df84c47`](https://github.com/containerd/nri/commit/df84c475025e3fc536701aa99f6ca6d14dbea648) .github: add codespell workflow. [`a03dc93`](https://github.com/containerd/nri/commit/a03dc9359c2d526924e56a9d167445a69588d3ae) pkg,plugins,.codespellrc: add codespellrc, fix spelling
- Add API support for NRI-native CDI injection ([containerd/nri#98](https://github.com/containerd/nri/pull/98)) [`8783973`](https://github.com/containerd/nri/commit/87839736588c90995cd7d8a19beb47076efd3319) device-injector: clarify precedence of annotations. [`4eb7075`](https://github.com/containerd/nri/commit/4eb70757f7095a9928d6a34a9e8f28eaac066a42) pkg/adaptation: fix grammatical mistakes in comments. [`4bd8da8`](https://github.com/containerd/nri/commit/4bd8da8cf7128f9ac88ebed28f2e3afd73d0fab1) device-injector: add support for CDI injection. [`44773bd`](https://github.com/containerd/nri/commit/44773bdd8b2fc5ed0e193975f54cfdf7153f708c) runtime-tools/generate: add support CDI injection. [`65282fe`](https://github.com/containerd/nri/commit/65282fe079414600930b9fa084a46fb0bd0e0c8b) adaptation: add CDI device injection unit test. [`01f3b7a`](https://github.com/containerd/nri/commit/01f3b7a6681de5961920091f88e71335778ecc21) adaptation: add support for native CDI injection. [`f1aa58f`](https://github.com/containerd/nri/commit/f1aa58f8157aacbdda3826316c77e4e96914235a) api: add support for native CDI device injection
- types: Fix a typo ([containerd/nri#101](https://github.com/containerd/nri/pull/101)) [`8434439`](https://github.com/containerd/nri/commit/8434439b76e0b4c8dad1c5e2b1fadc4bbfea4b1a) types: Fix a typo
- plugins/device-injector: fix a small typo in README.md. ([containerd/nri#97](https://github.com/containerd/nri/pull/97)) [`f96a550`](https://github.com/containerd/nri/commit/f96a550770396c0e83763d2ff1a48c74facbbff7) device-injector: small grammar fix in README.md
- server_test: fix error message in TestOversizeCall. ([containerd/ttrpc#170](https://github.com/containerd/ttrpc/pull/170)) [`84e1784`](https://github.com/containerd/ttrpc/commit/84e1784f340651f94891fbd091cbb3d5bfdf9e62) server_test: fix error message in TestOversizeCall

### 1.7.27

- Fix integer overflow in User ID handling ([GHSA-265r-hfxg-fhmg](https://github.com/containerd/containerd/security/advisories/GHSA-265r-hfxg-fhmg))
- Remove hashicorp/go-multierror dependency and fix CI ([#11499](https://github.com/containerd/containerd/pull/11499)) [`49537b3a7`](https://github.com/containerd/containerd/commit/49537b3a75bdcd982e7e26855779b346bb363a54) e2e: use the shim bundled with containerd artifact [`fe490b76f`](https://github.com/containerd/containerd/commit/fe490b76fd78cc1461f20aab89951be5f88fc454) Bump up github.com/intel/goresctrl to 0.5.0 [`13fc9d313`](https://github.com/containerd/containerd/commit/13fc9d3132fc4c77f6533551049d2d865d4e4b45) update containerd/project-checks to 1.2.1 [`585699c94`](https://github.com/containerd/containerd/commit/585699c94f68649a89b0af46d675d6e998d67ccd) Remove unnecessary joinError unwrap [`4b9df59be`](https://github.com/containerd/containerd/commit/4b9df59be202a011c4f65604bbeab75eeb85ab46) Remove hashicorp/go-multierror

### 1.7.28

- Backport windows test fixes ([#12121](https://github.com/containerd/containerd/pull/12121)) [`3c06bcc4d`](https://github.com/containerd/containerd/commit/3c06bcc4d2f5b55c501f9c5333596c5a6d0a980a) Fix intermittent test failures on Windows CIs [`c6c0c6854`](https://github.com/containerd/containerd/commit/c6c0c6854ff663deb46363a8884a9015598c9f9b) Remove WS2025 from CIs due to regression
- update runners to ubuntu 24.04 ([#11802](https://github.com/containerd/containerd/pull/11802)) [`c362e18cc`](https://github.com/containerd/containerd/commit/c362e18ccd613b5baf04fff87832b871edfdecd5) CI: install OVMF for Vagrant [`1d99bec21`](https://github.com/containerd/containerd/commit/1d99bec213063acdad8d7ad96ea4cbb78ab6b560) CI: fix "Unable to find a source package for vagrant" error [`dafa3c48d`](https://github.com/containerd/containerd/commit/dafa3c48dffaff915bea2293eecd949fbdd94228) add debian sources for ubuntu-24 [`b03301d85`](https://github.com/containerd/containerd/commit/b03301d851a5492808f36e5233a808a39575a1a0) partial: enable ubuntu 24 runners [`13fbc5f97`](https://github.com/containerd/containerd/commit/13fbc5f970d1dee5425443a9b346d56ccc98db45) update release runners to ubuntu 24.04
- [CI] Fix vagrant ([#11739](https://github.com/containerd/containerd/pull/11739)) [`effc49e8b`](https://github.com/containerd/containerd/commit/effc49e8b096bebfd73effb9257ad4fd80aa4e84) Fix vagrant setup
- Fix CI ([#11722](https://github.com/containerd/containerd/pull/11722)) [`d3e7dd716`](https://github.com/containerd/containerd/commit/d3e7dd716a7988bf49f92972998a5260fd538505) Skip criu on Arms [`7cf9ebe94`](https://github.com/containerd/containerd/commit/7cf9ebe94676a443f5df2802f2c784a93dba6b9a) Disable port mapping tests in CRI-in-UserNS [`42657a4ed`](https://github.com/containerd/containerd/commit/42657a4ed1bcc2a5162264cb820d97bdd0a56a6b) disable portmap test in ubuntu-22 to make CI happy [`b300fd37b`](https://github.com/containerd/containerd/commit/b300fd37b840dcad8c0635e1f8ce848413441445) add option to skip tests in critest [`6f4ffad27`](https://github.com/containerd/containerd/commit/6f4ffad27695c7e297c0052091b0d5e7fad7e48a) Address cgroup mountpoint does not exist [`cef298331`](https://github.com/containerd/containerd/commit/cef2983317494d0a7b67e89ef81e083f75102066) Update Ubuntu to 24 [`2dd9be16e`](https://github.com/containerd/containerd/commit/2dd9be16e71e97b922ae42b05a7ae837c28563ca) ci: update GitHub Actions release runner to ubuntu-24.04

### 1.7.29

- **Fix lost container logs from quickly closing io**
- Update GHA images and bump Go 1.24.9; 1.25.3 ([#12471](https://github.com/containerd/containerd/pull/12471)) [`667409fb6`](https://github.com/containerd/containerd/commit/667409fb63098cb80280940ab06038114e7712da) ci: bump Go 1.24.9, 1.25.3 [`294f8c027`](https://github.com/containerd/containerd/commit/294f8c027b607c4450b3e52f44280581a737a73f) Update GHA runners to use latest images for basic binaries build [`cf66b4141`](https://github.com/containerd/containerd/commit/cf66b4141defb757dee0fc5653bfd0a7ba1e8fed) Update GHA runners to use latest image for most jobs [`fa3e6fa18`](https://github.com/containerd/containerd/commit/fa3e6fa18aa8dc7e699428958e1fb1d38e832e15) pkg/epoch: extract parsing SOURCE_DATE_EPOCH to a function [`ac334bffc`](https://github.com/containerd/containerd/commit/ac334bffc4e759f188afb58efd74a603ade0855a) pkg/epoch: fix tests on macOS [`d04b8721f`](https://github.com/containerd/containerd/commit/d04b8721fc5bff2677beadb4f3d15d7c0ec989ca) pkg/epoch: replace some fmt.Sprintfs with strconv
- Fix lost container logs from quickly closing io ([#12375](https://github.com/containerd/containerd/pull/12375)) [`d30024db2`](https://github.com/containerd/containerd/commit/d30024db25590e6ec74b639746a5dc792f5c1403) bugfix:fix container logs lost because io close too quickly

### 1.7.30

- **Fix NRI dropping requested CDI devices silently**
- Fix NRI dropping requested CDI devices silently ([#12650](https://github.com/containerd/containerd/pull/12650)) [`0bc74f47e`](https://github.com/containerd/containerd/commit/0bc74f47e708bd843e676c5a8617f0498ea6459a) cri,nri: don't drop requested CDI devices silently
- Redact all query parameters in CRI error logs ([#12551](https://github.com/containerd/containerd/pull/12551)) [`65271ea89`](https://github.com/containerd/containerd/commit/65271ea895cd62016f2baf0e758b1cd7388344e7) fix: redact all query parameters in CRI error logs

### 1.7.31

- Fix CNI issue where DEL is never executed after a restart
- Fix vagrant on CI ([#13064](https://github.com/containerd/containerd/pull/13064)) [`9b4cfa271`](https://github.com/containerd/containerd/commit/9b4cfa27113b4117e4d47dfca0fe84075ea2ff45) Ignore NOCHANGE error
- Fix TOCTOU race bug in tar extraction ([#12970](https://github.com/containerd/containerd/pull/12970)) [`61c2733fd`](https://github.com/containerd/containerd/commit/61c2733fde2971d2d5fb3b9d5363d626700350fd) Fix TOCTOU race bug in tar extraction
- Fix CNI issue where CNI DEL is never executed ([#12931](https://github.com/containerd/containerd/pull/12931)) [`f854c1890`](https://github.com/containerd/containerd/commit/f854c1890468b12e4517c155eee5840f46b22e59) fix issue where cni del is never executed
- backport: integration: Fix TestImageLoad() failure on CI ([#12908](https://github.com/containerd/containerd/pull/12908)) [`177ac10fe`](https://github.com/containerd/containerd/commit/177ac10fee6803c41cb39e67f17357ad843a8fe1) integration: Fix TestImageLoad() failure on CI
- fix: sanitize error before gRPC return to prevent credential leak in pod events ([#12805](https://github.com/containerd/containerd/pull/12805)) [`b1fa03843`](https://github.com/containerd/containerd/commit/b1fa038433bba840e3be76c0fb125da4defc17e6) fix: sanitize error before gRPC return to prevent credential leak in pod events

### 1.7.32

- Fix handling of out-of-range USER values in OCI spec to avoid unexpected username/group lookups
- Fix issue with empty host tree in hosts.toml ([#10028](https://github.com/containerd/containerd/pull/10028)) [`24007441d`](https://github.com/containerd/containerd/commit/24007441d3bb191e0045b83fce5890a67aa98449) Fix error parsing hosts.toml without any `host` tree

### 1.7.34

- Fix lost container exit events when events arrive before container info is cached
- cri:fix lost container exit events if they arrive before info is cached ([#11634](https://github.com/containerd/containerd/pull/11634)) [`2fe076ea7`](https://github.com/containerd/containerd/commit/2fe076ea7ebaac58d3e731bcb6dcde84d3fe5719) cri:fix lost container exit events if they arrive before info is cached


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.7.34**, the newest release recorded here for this line.

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
