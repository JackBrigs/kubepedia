---
id: TROUBLE-CONTAINERD_1_2_DEFECTS
type: troubleshooting
title: "containerd 1.2: defects fixed in the 1.2 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.2.0 <1.3.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - containerd 1.2 known issues
  - containerd 1.2 fixed in
  - is this containerd bug already fixed
tags:
  - troubleshooting
  - upgrade
  - containerd
sources:
  - type: docs
    path: containerd/containerd release notes for the 1.2 line — bug-fix entries
    url: https://github.com/containerd/containerd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# containerd 1.2: defects fixed in the 1.2 line

## Summary

**237 defects** the project fixed across **15 releases** of the 1.2 line, from 1.2.0 to
1.2.14. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.2.0

- Fixed an issue that a container can't be stopped when container processes are accidentally moved out of the container cgroups
- [`c3cac72b92`](https://github.com/containerd/containerd/commit/c3cac72b92a5017423ce2358b8bfc3a56bb45fbb) ctr: fix potential panic in metric
- [`acc3b839d3`](https://github.com/containerd/containerd/commit/acc3b839d3dfd81e3fe1b152c3794f09bb76e88a) Merge pull request [#2714](https://github.com/containerd/containerd/pull/2714) from dmcgowan/fix-content-deadlock-after-error
- [`0f756495a9`](https://github.com/containerd/containerd/commit/0f756495a9c7ab71edfbe198f1181779f96557b6) Fix writer deadlock in local store
- [`e86a0689fb`](https://github.com/containerd/containerd/commit/e86a0689fbfa6f83e9ec96c02fef3f373c582d11) Fix stress test for image config opt requirements
- [`440c7ed249`](https://github.com/containerd/containerd/commit/440c7ed249d255d7426e9ac8b017463ec346d3ca) Fix commit already exists not leasing
- [`beb1f432be`](https://github.com/containerd/containerd/commit/beb1f432be15ac27d162a8b8835e272646e62f4b) Review fixes
- [`df60d3272a`](https://github.com/containerd/containerd/commit/df60d3272ad214d6bae5cb27812b6a091065ec80) Merge pull request [#2687](https://github.com/containerd/containerd/pull/2687) from dmcgowan/fix-pigz-panic
- [`772644e978`](https://github.com/containerd/containerd/commit/772644e978a5f7a95cca419e3894d39b5a468b2c) Fixes containerd-shim-runhcs State on exec id
- [`83437ef646`](https://github.com/containerd/containerd/commit/83437ef646eb61fbe3788d0e66004b904c0272fd) Fixes containerd-shim-runhcs Delete on exec id
- [`db358a9fd2`](https://github.com/containerd/containerd/commit/db358a9fd2fed9bd4456ec67ea724fc06b617e5e) Fix panic when bufio Reader called in 2 goroutines
- [`e373126bfb`](https://github.com/containerd/containerd/commit/e373126bfb31a7338b1f91fae27bdba3f50a558a) Fix race in lcow snapshot scratch.vhdx creation
- [`a121b2fb56`](https://github.com/containerd/containerd/commit/a121b2fb5642357f75e1defd813fe291debcc843) typo: fix misspells in comments of containers/contaienrs.go
- [`6496078ef8`](https://github.com/containerd/containerd/commit/6496078ef821bfe2949b04336b7a81e215b356cb) Merge pull request [#2669](https://github.com/containerd/containerd/pull/2669) from estesp/fix-withuser-comment
- [`557e8e0b0d`](https://github.com/containerd/containerd/commit/557e8e0b0d038ad7a3c0eb976226f5ef314eb535) fix delete running bundle dir when run t start cmd again
- [`547bb94e4b`](https://github.com/containerd/containerd/commit/547bb94e4bc500bd70754b58363b6117873fef72) Fix ctr run for Windows containers
- [`03b1dae195`](https://github.com/containerd/containerd/commit/03b1dae195ccadd9dd59ccc3091f3a1f714a6148) typo fix
- [`af23a4c1f2`](https://github.com/containerd/containerd/commit/af23a4c1f213b7a6356c3098b1bcadd42db3f923) fix: typo omitted -> ommitted
- [`bd902372de`](https://github.com/containerd/containerd/commit/bd902372dee89ce6f26c5551812550458701826d) typo fix oci/typo_spec_opts_test
- [`05984a966d`](https://github.com/containerd/containerd/commit/05984a966d3a20db9018be859a120b4edbe2d96a) Merge pull request [#2642](https://github.com/containerd/containerd/pull/2642) from dmcgowan/fix-commit-already-exists
- [`0120dec799`](https://github.com/containerd/containerd/commit/0120dec7992aced23067583dcfb1dc5b33ea45f5) fix typo
- [`079292e3fc`](https://github.com/containerd/containerd/commit/079292e3fc20b7319b6e7c35dcda6864bb128f1c) fix: modify lock location of exec delete
- [`c48cafea40`](https://github.com/containerd/containerd/commit/c48cafea4048908a77bf389ed1cf770ee1fdd299) Merge pull request [#2619](https://github.com/containerd/containerd/pull/2619) from nashasha1/fix/typo-in-runtime
- [`e6d787172c`](https://github.com/containerd/containerd/commit/e6d787172c01e47d720170d0f46571821dc686e6) Fix some typo in runtime and snapshots
- [`6ca8355a4e`](https://github.com/containerd/containerd/commit/6ca8355a4e8ae1857c0577fcd648976916c7ce33) Merge pull request [#2615](https://github.com/containerd/containerd/pull/2615) from tossmilestone/fix-forward-typo
- [`55952ad087`](https://github.com/containerd/containerd/commit/55952ad087be028c5aa98d47a4aa851e7ef32dba) Merge pull request [#2612](https://github.com/containerd/containerd/pull/2612) from nashasha1/fix/contrib-typo
- [`dcb4d72f98`](https://github.com/containerd/containerd/commit/dcb4d72f98a05d2b526e3fae95f2a2f31f968607) Merge pull request [#2614](https://github.com/containerd/containerd/pull/2614) from mirake/fix-typos-outputing
- [`7f03ad6579`](https://github.com/containerd/containerd/commit/7f03ad6579521b2ccec6e5d6cf9798e7ded7e3b1) Fix typos
- [`9f817000cc`](https://github.com/containerd/containerd/commit/9f817000cc3074c640c2c34c2fb978889a00cd32) Fix 'forward' typos
- [`67849c4714`](https://github.com/containerd/containerd/commit/67849c471438ed4bdd73144bceff708ce0849538) fix typo
- [`1f5ab28216`](https://github.com/containerd/containerd/commit/1f5ab282169035ee5e6271bb0dcfc3af7ae52393) Typo fix: outputing -> outputting
- [`96986c04db`](https://github.com/containerd/containerd/commit/96986c04db9b1e61339a3d1e6e2af010b4ced58c) Merge pull request [#2609](https://github.com/containerd/containerd/pull/2609) from Callisto13/pr-fix-typos
- [`32e6aa742b`](https://github.com/containerd/containerd/commit/32e6aa742ba732a89610ff1021b4fceda1aa493a) Fix teeny tiny typos
- [`d5aebde04c`](https://github.com/containerd/containerd/commit/d5aebde04c5cee94d4e80ad3bd7bbf42b426783f) Merge pull request [#2580](https://github.com/containerd/containerd/pull/2580) from HusterWan/zr/fix-read-empty-timestamp
- [`a09bad557f`](https://github.com/containerd/containerd/commit/a09bad557f9ff363722631b642c26ef092dc4b48) Merge pull request [#2598](https://github.com/containerd/containerd/pull/2598) from Random-Liu/fix-state-error-handling
- [`7a4e0806c2`](https://github.com/containerd/containerd/commit/7a4e0806c2d10d5f0014ff756b50a5e3a45931b0) Fix `runc state` error handling
- [`e88ec1f1a6`](https://github.com/containerd/containerd/commit/e88ec1f1a6d249f999da66a8d0c51052477685e6) Fix incorrect ID usage in Windows runtime v2
- [`1d9b96988f`](https://github.com/containerd/containerd/commit/1d9b96988fd4cdfcf229e5be511de292247b2d3c) fix when --config provided, don't need Image/RootFS
- [`9ff702b9a1`](https://github.com/containerd/containerd/commit/9ff702b9a146c02b90df58e558cafde0d398debe) Fix a typo in runc-v1 shim
- [`123de20b59`](https://github.com/containerd/containerd/commit/123de20b5975a9a59bb3a52504fa7202c017a099) Merge pull request [#2517](https://github.com/containerd/containerd/pull/2517) from estesp/fix-travis-script
- [`9622369f0e`](https://github.com/containerd/containerd/commit/9622369f0eaee16a9ac752c216b88eb8863dc31a) Fix loss of CRI test failure status in CI
- [`e8f7c2af26`](https://github.com/containerd/containerd/commit/e8f7c2af26a4337a4a1f27f8eb21be70307b0d79) Merge pull request [#2507](https://github.com/containerd/containerd/pull/2507) from flx42/fix-readme-runtime-v2
- [`26e2dd6754`](https://github.com/containerd/containerd/commit/26e2dd6754b8098911d80ed0369bd1c54b93fbd4) Merge pull request [#2425](https://github.com/containerd/containerd/pull/2425) from avagin/docker-fixes
- [`da73b98b63`](https://github.com/containerd/containerd/commit/da73b98b638c8dfbbabaaedf395976cf655b2bde) Set default log formatting to use RFC3339Nano with fixed width
- [`65ef8310d9`](https://github.com/containerd/containerd/commit/65ef8310d982768d2bde8a2115fc1fad5bc0ca4c) Fix compilation failures on Go 1.11
- [`92d147ebde`](https://github.com/containerd/containerd/commit/92d147ebde3f8372dbce80b29c38a344e4232b8e) Merge pull request [#2485](https://github.com/containerd/containerd/pull/2485) from AkihiroSuda/fix-native-root-permission
- [`17ab11a236`](https://github.com/containerd/containerd/commit/17ab11a23619b25407ca088a179ba0780bbeb6c2) Fixes for runtimev2 and checkpoint restore
- [`6de11ab973`](https://github.com/containerd/containerd/commit/6de11ab973faa67f0f8fe2e67a055f50b4f2ac4b) Merge pull request [#2470](https://github.com/containerd/containerd/pull/2470) from dmcgowan/fix-checkprotos
- [`d3cd5f1d01`](https://github.com/containerd/containerd/commit/d3cd5f1d015da1f8a9107f0b58b9c614c4b153cf) Fix options ordering in proto api txt files
- [`77a26427c3`](https://github.com/containerd/containerd/commit/77a26427c34cd52bd9e46d840b6b4f090abd4fa4) update containerd/console to fix race: lock Cond before Signal
- [`5a4f007e48`](https://github.com/containerd/containerd/commit/5a4f007e488bb934c1174808513d4a930b81baaa) Fix the formatting directives error during compilation
- [`37ab93e2c8`](https://github.com/containerd/containerd/commit/37ab93e2c89fd8bc1e08c914246926fabf902893) Fix arm platform matching
- [`ef449aa38e`](https://github.com/containerd/containerd/commit/ef449aa38edc8f21a3819663b07519681ad0409a) Docs: Fix incomplete instructions for building using docker
- [`63522d9eaa`](https://github.com/containerd/containerd/commit/63522d9eaa5a0443d225642c4b6f4f5fdedf932b) Merge pull request [#2390](https://github.com/containerd/containerd/pull/2390) from AkihiroSuda/fix-schema1
- [`703c25e452`](https://github.com/containerd/containerd/commit/703c25e4522fa0c5dab85e29a93556b03df74848) fix schema1 fetchBlob()
- [`84bebdd91d`](https://github.com/containerd/containerd/commit/84bebdd91d347c99069d1705b7d4e6d6f746160c) Merge pull request [#2379](https://github.com/containerd/containerd/pull/2379) from dmcgowan/fix-direct-io-terminal-setting
- [`6b9be1bfc3`](https://github.com/containerd/containerd/commit/6b9be1bfc37d18a5f028a6ca8275a272c6696138) Fix creation of DirectIO overwriting fifo config
- [`7f800e0a7b`](https://github.com/containerd/containerd/commit/7f800e0a7bb1e2547baca4d5bbf317ceeb341c14) Merge pull request [#2364](https://github.com/containerd/containerd/pull/2364) from dmcgowan/fix-http-seeker-unsupported-range
- [`59740d8985`](https://github.com/containerd/containerd/commit/59740d8985f4ac892200eb4b66bd514a8d0530af) Fix invalid length bug with some registries
- [`7e5a91fa51`](https://github.com/containerd/containerd/commit/7e5a91fa51ed80a039968000a2b8a817a558b9b1) Bump continuity to fix copy files > 2^32 bytes
- [`e63768ea09`](https://github.com/containerd/containerd/commit/e63768ea09fe230216f57675ed06a8f1ef3f62b7) Merge pull request [#2331](https://github.com/containerd/containerd/pull/2331) from dmcgowan/fix-image-remove-race
- [`fcc66f5685`](https://github.com/containerd/containerd/commit/fcc66f568594a3dead231d5c9d1df2ace0ff9168) Merge pull request [#2337](https://github.com/containerd/containerd/pull/2337) from AkihiroSuda/fix-vendorconf-runcmd-mismatch
- [`b1e202c327`](https://github.com/containerd/containerd/commit/b1e202c32724e82779544365528a1a082b335553) fix RUNC.md vs vendor.conf mismatch
- [`d791232cd3`](https://github.com/containerd/containerd/commit/d791232cd332f0182bb1651f2eeb9f05880b8eb7) Fix typo, should be register instead of regster
- [`a15e7a0be0`](https://github.com/containerd/containerd/commit/a15e7a0be093db114409d377dcee75c4ddce5e34) Merge pull request [#2332](https://github.com/containerd/containerd/pull/2332) from dmcgowan/fix-missing-return-in-client-pull
- [`f701b3b960`](https://github.com/containerd/containerd/commit/f701b3b96086622f792b7a6d8b00d39b19d18ba6) Fix race in ctr pull
- [`5539584`](https://github.com/containerd/cgroups/commit/5539584069073a678346861117642026f267fba3) Fix incorrect use of OCI runtime specs-go cgroup dev types
- [`8894ab3`](https://github.com/containerd/console/commit/8894ab362e7a6b6b88af5c790ac4ad4cb559e9c4) Revert "Fix reading from and writing to console on windows"
- [`5d1b48d`](https://github.com/containerd/console/commit/5d1b48d6114b8c9666f0c8b916f871af97b0a761) console_linux: Fix race: lock Cond before Signal
- [`a7ba593`](https://github.com/containerd/console/commit/a7ba5931bf5ac6dcc0be44ec74b62c2cee55fa3f) Fix reading from and writing to console on windows
- [`6fe6f36`](https://github.com/containerd/console/commit/6fe6f36970bfff15699191d9beb163cfafb36d69) Fix some typos in comments
- [`94af800`](https://github.com/containerd/continuity/commit/94af8008a7b687f8748385cf34f5a46c333ec511) Lchmod(): fix for Linux/Go 1.11
- [`a60600a`](https://github.com/containerd/continuity/commit/a60600ad77f38aaa70165825f61e2ea72e51c9b1) Merge pull request [#117](https://github.com/containerd/continuity/pull/117) from dmcgowan/fix-create-file-reader-creation
- [`7d784df`](https://github.com/containerd/continuity/commit/7d784dfeb6c7548970a142b65a4f0ef700614a03) Fix bug in multiple calls to file applier
- [`afba265`](https://github.com/containerd/continuity/commit/afba265aa60a6dab3bf3a7809b2e6e9a95704b04) Fix copy_file_range usage for files > 2GB
- [`7a71e24`](https://github.com/containerd/continuity/commit/7a71e2431373f4e854947798e4f6659253ffbd8a) Fix vet failure
- [`e402ae2f`](https://github.com/containerd/cri/commit/e402ae2f027e28a86acfc33a9bd151902f5d5dbf) Merge pull request [#914](https://github.com/containerd/cri/pull/914) from Random-Liu/fix-addition-gids
- [`ca3b806b`](https://github.com/containerd/cri/commit/ca3b806b5cb960e3d2de034434fe65ac7bc43793) Fix addition group ids
- [`ed68cfd5`](https://github.com/containerd/cri/commit/ed68cfd543808f8f46142ab2f2ec866c7b505041) Merge pull request [#901](https://github.com/containerd/cri/pull/901) from Random-Liu/fix-hostname-env
- [`f08a90ff`](https://github.com/containerd/cri/commit/f08a90ff64477116953de523188611c814462174) Fix hostname env
- [`db8500d1`](https://github.com/containerd/cri/commit/db8500d10c38b3c6ef9464d7550e17abd9e32f5a) Merge pull request [#892](https://github.com/containerd/cri/pull/892) from Random-Liu/fix-volume-mount-order
- [`bca304ff`](https://github.com/containerd/cri/commit/bca304ff3e1a52a58bf5c0564affbca35ff278bc) Fix an issue that container/sandbox can't be stopped
- [`c68b6051`](https://github.com/containerd/cri/commit/c68b60514edb386fb9ad0bbd37bf56c6a90ea03c) Merge pull request [#831](https://github.com/containerd/cri/pull/831) from Random-Liu/fix-link
- [`fd71c9f0`](https://github.com/containerd/cri/commit/fd71c9f065cc72b6dfa6ee054621a1b888fc2e39) Fix another link
- [`47b8d30b`](https://github.com/containerd/cri/commit/47b8d30bb34547f7c597ed52ed118ed0371a0a2b) Merge pull request [#828](https://github.com/containerd/cri/pull/828) from yujuhong/fix-gce-link
- [`e23c0e70`](https://github.com/containerd/cri/commit/e23c0e708a3d60e72753949fd8a4a3b7adad0c5e) Fix link to GCE getting started guide
- [`86097102`](https://github.com/containerd/cri/commit/860971025f1ad628f773b405446776f0e074cf68) vendoring latest go-cni with fixes
- [`441a57aa`](https://github.com/containerd/cri/commit/441a57aa56f26edbed328a20bc4eee61e66a8e34) Merge pull request [#821](https://github.com/containerd/cri/pull/821) from Random-Liu/fix-snapshotter-panic
- [`b60e456b`](https://github.com/containerd/cri/commit/b60e456bd9913261956b664c9a34463884edce58) Fix snapshotter nil panic
- [`ad293701`](https://github.com/containerd/cri/commit/ad29370136777b4a471afbde280637ad121cab74) Merge pull request [#816](https://github.com/containerd/cri/pull/816) from Random-Liu/fix-double-dev-shm-mount
- [`53f1ab41`](https://github.com/containerd/cri/commit/53f1ab41458de4fa91f40f4cbe034aa3442ca1b8) Fix double /dev/shm mount
- [`b7aac639`](https://github.com/containerd/cri/commit/b7aac6396d76282304abe1c25b0e521004ed7fc2) Merge pull request [#811](https://github.com/containerd/cri/pull/811) from Random-Liu/fix-volume-ownership
- [`c5577637`](https://github.com/containerd/cri/commit/c55776377fd288bbca3e716056071f67909399c2) Fix empty volume ownership
- [`8bcb9a95`](https://github.com/containerd/cri/commit/8bcb9a95394e8d7845da1d6a994d3ac2a86d22f0) Merge pull request [#801](https://github.com/containerd/cri/pull/801) from Random-Liu/fix-ctr-timeout
- [`0faff1c2`](https://github.com/containerd/cri/commit/0faff1c22fbc36cf3c12cfc9347b210e06845e24) Fix ctr cri timeout
- [`b68fb075`](https://github.com/containerd/cri/commit/b68fb075d49aa1c2885f45f2467142666c244f4a) Merge pull request [#793](https://github.com/containerd/cri/pull/793) from Random-Liu/port-containerd-fix-#2364
- [`0fae42b9`](https://github.com/containerd/cri/commit/0fae42b9b8571df61acd474b4367a6f8f1db83d0) Port docker resolver fix #2364
- [`fb6bc66f`](https://github.com/containerd/cri/commit/fb6bc66f0aa04161b9c95727865c31ae01dad081) Bump continuity to fix copy files > 2^32 bytes
- [`a4ff7e99`](https://github.com/containerd/cri/commit/a4ff7e9946eed21a650d68d790d6bdbfd7721aab) Merge pull request [#781](https://github.com/containerd/cri/pull/781) from Random-Liu/fix-container-runtime-monitor
- [`ebed87fa`](https://github.com/containerd/cri/commit/ebed87fa951ad2b59dba8ed35b3cad570c1f3628) Fix kube-container-runtime-monitor
- [`927d3740`](https://github.com/containerd/cri/commit/927d37401dc4b8a9f2dfc73eb6c085ae3c0e7ac2) Merge pull request [#779](https://github.com/containerd/cri/pull/779) from Random-Liu/logo-fix
- [`6c7ec48d`](https://github.com/containerd/cri/commit/6c7ec48daf08d0e496111cf7903a8b7c784a4fbe) Another logo fix
- [`66388aef`](https://github.com/containerd/cri/commit/66388aefd5f63bcd000e8e19eee32dd1495ca7a1) Merge pull request [#766](https://github.com/containerd/cri/pull/766) from Random-Liu/fix-workingset-memory
- [`5d29598a`](https://github.com/containerd/cri/commit/5d29598a6d5db2405befb15c83c7f95cd42ae5fe) Fix workingset memory calculation
- [`7a6369de`](https://github.com/containerd/cri/commit/7a6369deb195336463ca60f82cdfbe2d49bc7edf) Merge pull request [#763](https://github.com/containerd/cri/pull/763) from Random-Liu/fix-ro-sysfs
- [`2f370f6f`](https://github.com/containerd/cri/commit/2f370f6f5d246fcf5be242dfb8a288110b0d5117) Update cri-tools to fix `crictl logs` output
- [`8fec0469`](https://github.com/containerd/cri/commit/8fec0469d9cd0e3ae1692ece8840e6abea1b3fe0) Merge pull request [#751](https://github.com/containerd/cri/pull/751) from Random-Liu/fix-official-release
- [`e0d70782`](https://github.com/containerd/cri/commit/e0d70782516ccb24703a83fccfaa1848d3923f58) Fix tarball ownership and containerd binary path for containerd
- [`5a6d9f3`](https://github.com/containerd/go-runc/commit/5a6d9f37cfa36b15efba46dc7ea349fa9b7143c3) Fix windows build for io options
- [`2e95e46`](https://github.com/containerd/typeurl/commit/2e95e4697860e423bec6d760ab66571178b38be6) Fix marshal tests with local type

### 1.2.1

- Fix race in process state when pausing containers
- Fix a bug that containers sharing pod pid namespace can't be stopped
- [`cd83a4e0ba`](https://github.com/containerd/containerd/commit/cd83a4e0bae33514f9155703a72e8d0bf39cae6d) fix pipe in broken may cause shim lock forever for runtime v1
- [`275f99feb9`](https://github.com/containerd/containerd/commit/275f99feb99668064e0bd23418731eca95465dd0) fix pipe in broken may cause shim lock forever for runtime v2
- [`4c72befe09`](https://github.com/containerd/containerd/commit/4c72befe097fb5d9e99ede3536c884608d0af474) Fix process locking and state management
- [`c4a256d342`](https://github.com/containerd/containerd/commit/c4a256d3420bcb545e145d5a36eb8c840b3488f1) Merge pull request [#2790](https://github.com/containerd/containerd/pull/2790) from estesp/cherrypick-v1v2-runtime-fix
- [`d58c1893`](https://github.com/containerd/cri/commit/d58c18939638c1db8a0c21961cbfeeeb4cf56a42) Fix kill when shared pid namespace

### 1.2.2

- Fix rare deadlock on FIFO creation with timeout
- Fix a bug that a container can't be stopped or inspected when its corresponding image is deleted
- Fix a bug that the cri plugin handles containerd events outside of `k8s.io` namespace
- [`e71a191f6d`](https://github.com/containerd/containerd/commit/e71a191f6dfc71a8bc5f88ec3b0e63ee84cf167b) Revert "Fix CI due to Golang 1.10.6 / 1.11.3 regressions (workaround)"
- [`27c6449c2c`](https://github.com/containerd/containerd/commit/27c6449c2c50f7e66076a4186e81aa3167e0dd5a) Fix CI due to Golang 1.10.6 / 1.11.3 regressions (workaround)
- [`6ca182a8`](https://github.com/containerd/cri/commit/6ca182a85842fe6ed2fe71f5a536ee0cb63fe220) Revert "Temporary fix for golang regression #29241."
- [`298c7fd9`](https://github.com/containerd/cri/commit/298c7fd93eaabf1d0f75fef65a0e800596fae937) Temporary fix for golang regression #29241

### 1.2.3

- fix in Tar xattrs to restore compatibility with older container images [#2953](https://github.com/containerd/containerd/pull/2953)
- background `O_NONBLOCK` in OpenFifo to fix uncancelled context timeout issue
- runtime: exec race condition fixed [#2970](https://github.com/containerd/containerd/pull/2970)
- cri: fixed issues with extra newline character in log without an extra newline [#2984](https://github.com/containerd/containerd/pull/2984)
- cri: fixed an issue with pods being ignored after load failures [#2984](https://github.com/containerd/containerd/pull/2984)
- [`7daf0804`](https://github.com/containerd/containerd/commit/7daf0804fce3b82ff19aa5cb0483edca403660a2) Fix potential containerd panic
- [`2244a20c`](https://github.com/containerd/containerd/commit/2244a20c446c7b06967268e1edf7a4246cabd41a) fix: SCHILY.xattrs should be SCHILY.xattr
- [`bf3c932a`](https://github.com/containerd/containerd/commit/bf3c932a5b5ef42c55644eb59eac3113d6a5bcee) [release 1.2] fix: linter issue
- [`10073e49`](https://github.com/containerd/cri/commit/10073e49b0a7415da3853776e3ea1348f581fb24) Fix lint error
- [`283aac3d`](https://github.com/containerd/cri/commit/283aac3d3c2cebd21dc0b419e97d5892e5477d16) Fix the log ending newline handling

### 1.2.4

- cri: Fix env performance issue [#1045](https://github.com/containerd/cri/pull/1045)
- [`7908802cb5`](https://github.com/containerd/containerd/commit/7908802cb558fa6d3cbc4351f623357db120b3bb) Fix Makefile to run protobuild on paths with spaces

### 1.2.5

- Fix an issue that non-existent parent directory in image layers is created with permission
- Fix an issue that snapshots of the base image can be deleted by mistake, when images
- cri: Fix a bug that pod can't get started when the same volume is defined
- cri: Fix a bug that causes container start failure after in-place upgrade containerd
- cgroups updated to dbea6f2bd41658b84b00417ceefa416b97 to fix issues for systemd 420 and
- [`6b552a8`](https://github.com/containerd/cgroups/commit/6b552a86e60e31903d3f8f3f494eda71f562cc54) Fix net_prio typo
- [`4479d11`](https://github.com/containerd/cgroups/commit/4479d118c89b5500a08cce7a78bbe822229c1e65) Merge pull request [#62](https://github.com/containerd/cgroups/pull/62) from estesp/fix-gofmt
- [`9a09e58`](https://github.com/containerd/cgroups/commit/9a09e5899acc95fabcc620d6489fec674e6dddfa) Fix gofmt of systemd.go
- [`0f3de2f`](https://github.com/containerd/cgroups/commit/0f3de2f77d3b76b3871242fbab2a6116179229af) Fix empty device type
- [`616d154e`](https://github.com/containerd/cri/commit/616d154eb0b6a4a290eb2b593e3a35e135373c9c) Fix /etc/hostname backward compatibility issue for in-place upgrade

### 1.2.6

- Fix a bug that custom containerd cgroup path does not work in containerd 1.2.5. [#3143](https://github.com/containerd/containerd/pull/3143)
- Fix a bug in the containerd client that `WithAllCapabilities` applies incomplete capability list. [#3147](https://github.com/containerd/containerd/pull/3147)
- Fix a bug that container output can be incomplete when stdout and stderr are pointed to the same file. [#3118](https://github.com/containerd/containerd/issues/3118)
- Fix a bug that containerd can't properly handle space in mount point path. [3161](https://github.com/containerd/containerd/pull/3161)
- cri: fix a bug that containers being gracefully stopped are SIGKILLed when kubelet is restarted. [cri#1098](https://github.com/containerd/cri/issues/1098)
- cri: Fix a bug that pod UTS namespace is used for host network. [cri#1111](https://github.com/containerd/cri/pull/1111)
- Update runc to v1.0.0-rc7-6-g029124da [#3183](https://github.com/containerd/containerd/pull/3183) to fix potential container start failure on non-SELinux system. [runc#2030](https://github.com/opencontainers/runc/issues/2030)
- [`50cb294d08`](https://github.com/containerd/containerd/commit/50cb294d08b8558ddce98bcdde4a4587022a8fba) fix parseInfoFile does not handle spaces in filenames
- [`de1b991122`](https://github.com/containerd/containerd/commit/de1b99112208b56d4ba86448eb4d1bd2fa36315b) Fix race and panic

### 1.2.7

- Fix a bug that containerd shim leaks goroutine and file descriptor after containerd restarts. [ttrpc#37](https://github.com/containerd/ttrpc/pull/37)
- Fix a bug that a container can't be deleted if first deletion attempt is canceled or timeout. [#3264](https://github.com/containerd/containerd/pull/3264)
- Fix a bug that containerd leaks file descriptor when using v2 containerd shims, e.g. `containerd-shim-runc-v1`. [#3273](https://github.com/containerd/containerd/pull/3273)
- Fix a bug that a container with lingering processes can't terminate when it shares pid namespace with another container. [moby/moby#38978](https://github.com/moby/moby/issues/38978)
- Fix a bug that containerd can't read shim logs after restart. [#3282](https://github.com/containerd/containerd/pull/3282)
- Fix a bug that `shim_debug` option is not honored for existing containerd shims after containerd restarts. [#3283](https://github.com/containerd/containerd/pull/3283)
- cri: Fix a bug that a container can't be stopped when the exit event is not successfully published by the containerd shim. [#3125](https://github.com/containerd/containerd/issues/3125), [#3177](https://github.com/containerd/containerd/issues/3177)
- cri: Fix a bug that exec process is not cleaned up if grpc context is canceled or timeout. [cri#1159](https://github.com/containerd/cri/pull/1159)
- Fix a selinux keyring labeling issue by updating runc to v1.0.0-rc.8 and selinux library to v1.2.2. [opencontainers/selinux#50](https://github.com/opencontainers/selinux/pull/50)
- [`1bda2ed`](https://github.com/containerd/containerd/commit/1bda2ed0d5be5bf332d51a19094f3b323c6a28bc) Merge pull request [#3338](https://github.com/containerd/containerd/pull/3338) from dmcgowan/backport-user-agent-fix
- [`e4e631a`](https://github.com/containerd/containerd/commit/e4e631ad5e92886d2adb74d1d59443d2460f0abe) differ: fix deadlock on commit error
- [`1014235`](https://github.com/containerd/containerd/commit/1014235c6d80933528edc7266e498d0098ae8b61) fix shouldKillAllOnExit check
- [`5cd83f3`](https://github.com/containerd/containerd/commit/5cd83f397f162bd672c4865b3cc126541ff877b2) Fix fd leak of shim log
- [`3d276b4`](https://github.com/containerd/containerd/commit/3d276b4b0234adee69cd4295472b122c6cfeaa02) Fix error handling for task deletion
- [`3923c02`](https://github.com/containerd/containerd/commit/3923c02491f88c4d277a709c3703c9bdcbb9a3fe) Merge pull request [#3254](https://github.com/containerd/containerd/pull/3254) from jcordasc/cherrypick-annotation-fix-1.2
- [`b9da989`](https://github.com/containerd/containerd/commit/b9da989b47dd014d5de5c61e889330c0a0b677ed) Merge pull request [#3213](https://github.com/containerd/containerd/pull/3213) from jcordasc/small-fixes
- [`56a6552`](https://github.com/containerd/containerd/commit/56a655285c61fc48dd1385c3f8d297e57aa27719) Merge pull request [#3229](https://github.com/containerd/containerd/pull/3229) from estesp/fix-appveyor
- [`0b2d89c`](https://github.com/containerd/containerd/commit/0b2d89cc821c0ae10715e518a9fe3e7aba42befa) Fix error on pull hang in CI
- [`ce5c1c4`](https://github.com/containerd/ttrpc/commit/ce5c1c4546907f3b1146f3bb28c1fea8f0094528) Fix returns error message

### 1.2.8

- Skip rootfs unmount when no mounts are provided. Fixed by [PR #3148](https://github.com/containerd/containerd/pull/3148) {cherry-picked as [PR #3402](https://github.com/containerd/containerd/pull/3402)}
- Close inherited socket file descriptor. Fixed in [PR #3359](https://github.com/containerd/containerd/pull/3359) {cherry-picked as [PR #3364](https://github.com/containerd/containerd/pull/3364)}
- Call CloseIO when stdin closes in ctr. Fixed by [PR #3462](https://github.com/containerd/containerd/pull/3462) {cherry-picked as [PR 3490](https://github.com/containerd/containerd/pull/3490)}
- Several multi-arch image fixes, including: ARM platform matching, selecting the proper manifest, and limited to best matched manifest to solve discrepancies with multi-arch image operations. Backported [PR #3270](https://github.com/containerd/containerd/pull/3270) as [PR #3404](https://github.com/containerd/containerd/pull/3404), [PR #3484](https://github.com/containerd/containerd/pull/3484) as [PR #3512](https://github.com/containerd/containerd/pull/3512), and added [PR #3421](https://github.com/containerd/containerd/pull/3421)
- Override image's environment config with process config; including backport of fixes and tests for merging/replacing env variables; fix in [PR #3542](https://github.com/containerd/containerd/pull/3542), backported via [PR #3546](https://github.com/containerd/containerd/pull/3546) which included a backport of [PR #2887](https://github.com/containerd/containerd/pull/2887). Additional fix to logic for override re: image `$PATH` cherry-picked in [PR #3565](https://github.com/containerd/containerd/pull/3565)
- Shim hang fix in master via [PR #3540](https://github.com/containerd/containerd/pull/3540) backported to `release/1.2` via [PR #3561](https://github.com/containerd/containerd/pull/3561)
- CRI: Fix a bug that if an image is deleted immediately after being pulled, the image may still exist after the deletion finishes successfully. (https://github.com/containerd/cri/issues/1161)
- CRI: Fix a bug that `runc` and `crictl` binaries shipped in https://storage.googleapis.com/cri-containerd-release are versioned with the containerd version. (https://github.com/containerd/cri/pull/1193)
- CRI: Fix a bug that the images become unusable if 2 images have the same image ID and RepoTag, but different RepoDigests. (https://github.com/containerd/containerd/issues/3401)
- CRI: Fix [ProcMount](https://stupefied-goodall-e282f7.netlify.com/contributors/design-proposals/auth/proc-mount-type/) support (https://github.com/containerd/cri/pull/1216). ***NOTE: To use containerd 1.2.8+ with Kubernetes 1.11 or below, you MUST set `disable_proc_mount=true` in the cri plugin config.*** (https://github.com/containerd/cri/issues/1208)
- CRI: Fix a bug that containerd tries to connect image registry with `https` even if the `http` endpoint is configured. (https://github.com/containerd/cri/issues/1201)
- [`9b5b55b142`](https://github.com/containerd/containerd/commit/9b5b55b142c0412c232fb3819946a8c393ed68a0) Fix shim hung
- [`4579a892be`](https://github.com/containerd/containerd/commit/4579a892beae99b2fbcdef67fcbe0d066be0a925) Merge pull request [#3428](https://github.com/containerd/containerd/pull/3428) from AkihiroSuda/fix-task-start-1.2
- [`d928a4dd`](https://github.com/containerd/cri/commit/d928a4dd337fd2a992dbe72380eff2063c3ec62f) Merge pull request [#1230](https://github.com/containerd/cri/pull/1230) from Random-Liu/fix-https-release-1.2
- [`ecd021d4`](https://github.com/containerd/cri/commit/ecd021d4fc99ce6b82efe08ed74081a461018d42) Fix unnecessary https trial in release/1.2
- [`21343bf7`](https://github.com/containerd/cri/commit/21343bf742b566ffd80de97a3048e9e680504d70) Fix proc mount support
- [`0c86149e`](https://github.com/containerd/cri/commit/0c86149e2fd52ab44566c2b84b860bcda0b154f4) Fix runc and critools version in release

### 1.2.9

- CRI fixes: Fix a bug that the default apparmor profile is mistakenly applied to privileged containers with runtime/default specified. [containerd/cri#1239](https://github.com/containerd/cri/issues/1239) Fix a bug that image can't be pulled if an empty AuthConfig is specified. [containerd/cri#1249](https://github.com/containerd/cri/issues/1249)
- Bug fix: Compute manifest data when not provided (Docker-Content-Digest header missing). [PR #3591](https://github.com/containerd/containerd/pull/3591) {cherry-picked from master [PR #3245](https://github.com/containerd/containerd/pull/3245) with backports of [#2871](https://github.com/containerd/containerd/pull/2871) and [#3335](https://github.com/containerd/containerd/pull/3335) required}
- Bug fix: Use default UNIX env when image has no environment. [PR #3601](https://github.com/containerd/containerd/pull/3601) {cherry-picked from master branch [PR #3599](https://github.com/containerd/containerd/pull/3599)}
- Bug fix: archive: truncate modification time. [PR #3602](https://github.com/containerd/containerd/pull/3602) {cherry-picked from master branch [PR #3589](https://github.com/containerd/containerd/pull/3589)}
- Bug fix: zfs: Datasets don't seem to be cleaned up properly on image removal. Reported in [containerd/zfs#22](https://github.com/containerd/zfs/issues/22) and fixed by [PR containerd/zfs#24](https://github.com/containerd/zfs/pull/24) and re-vendored into containerd `release/1.2` via [PR #3596](https://github.com/containerd/containerd/pull/3596)
- [`ce727bab`](https://github.com/containerd/cri/commit/ce727bab729ad258c4e2b4346e363de20d7196e9) fix: support empty auth config for anonymous registry
- [`f5a171f4`](https://github.com/containerd/cri/commit/f5a171f400d0e8ece77e1e6972b7aba0f131564f) Fix apparmor for privileged
- [`271238a`](https://github.com/containerd/ttrpc/commit/271238abf2f97c4f48f466e71641382b7b5257d1) Fix method full name generation
- [`3afb82b`](https://github.com/containerd/ttrpc/commit/3afb82bd2726e56810fb416d4869420ad6d0b2b1) Fix error handling with server shutdown
- [`2ceb2db`](https://github.com/containerd/zfs/commit/2ceb2dbb8154202ed1b8fd32e4ea25b491d7b251) Merge pull request [#24](https://github.com/containerd/zfs/pull/24) from AkihiroSuda/fix-remove-committed
- [`6fde16e`](https://github.com/containerd/zfs/commit/6fde16e2c480f7dc6f61a905744dbd3980bfc340) fix removing Committed

### 1.2.10

- CRI fixes: Fix a bug that the default UNIX path is not in the default OCI config via the CRI plugin. Reported in [containerd/cri#1279](https://github.com/containerd/cri/issues/1279) and fixed by [containerd/cri#1283](https://github.com/containerd/cri/pull/1283)
- [`6d433c50`](https://github.com/containerd/cri/commit/6d433c506a3808fbd0a37079924b62b2cd256fa5) Backport fix for default UNIX environment in OCI container config
- [`9007c24`](https://github.com/containerd/go-runc/commit/9007c2405372fe28918845901a3276c0915689a1) Merge pull request [#52](https://github.com/containerd/go-runc/pull/52) from Ace-Tang/fix-error-return
- [`4e99c72`](https://github.com/containerd/go-runc/commit/4e99c72acdb052ba374135c009bbc8ac9dd68249) Fix Method of judging command execution failure

### 1.2.11

- Add local-fs.target to service file to fix corrupt image after unexpected host reboot. Reported in [containerd/containerd#3671](https://github.com/containerd/containerd/issues/3671), and fixed by [containerd/containerd#3746](https://github.com/containerd/containerd/pull/3746)
- CRI fixes: Fix shim delete error code to avoid unnecessary retries in the CRI plugin. Discovered in [containerd/cri#1309](https://github.com/containerd/cri/issues/1309), and fixed by [containerd/containerd#3732](https://github.com/containerd/containerd/pull/3732) and [containerd/containerd#3739](https://github.com/containerd/containerd/pull/3739)
- [`847f74c284`](https://github.com/containerd/containerd/commit/847f74c284008247ae0d028c20910a0abcd90593) Fix delete error code on the containerd daemon side
- [`611766aff3`](https://github.com/containerd/containerd/commit/611766aff3da9b79ae3d18c2a8633bb1e374e76f) Fix shim delete error code

### 1.2.12

- Update Golang runtime to 1.12.15, which includes a fix to the runtime (Go 1.12.14, Go 1.12.15) and and the `net/http` package (Go 1.12.15)
- A fix to prevent `SIGSEGV` when starting containerd-shim [containerd/containerd#3960](https://github.com/containerd/containerd/pull/3960)
- Fixes to `exec` [containerd/containerd#3755](https://github.com/containerd/containerd/pull/3755) Prevent `docker exec` hanging if an earlier `docker exec` left a zombie process Prevent High system load/CPU utilization with liveness and readiness probes Prevent Docker healthcheck causing high CPU utilization
- Fix API filters to properly handle and return parse errors [containerd/containerd#3950](https://github.com/containerd/containerd/pull/3950)
- [`5db3987ebf`](https://github.com/containerd/containerd/commit/5db3987ebff7b5baa9338d55e78461690432cbb7) Fix dependency in BUILDING.md
- [`de8ed89b12`](https://github.com/containerd/containerd/commit/de8ed89b12a31eefbbe447ffa5543b1045390f4c) Fix cleanup error on content client test
- [`c229ad5c`](https://github.com/containerd/cri/commit/c229ad5c2fd96d456bf7afdfb2f1b767ca9b86b4) Fix containerd build, use `libbtrfs-dev` when available

### 1.2.13

- Fix container pid race condition [containerd#4025](https://github.com/containerd/containerd/pull/4025)
- Update Golang runtime to 1.12.17, which includes a fix to the runtime [containerd#4031](https://github.com/containerd/containerd/pull/4031)
- [`b970987628`](https://github.com/containerd/containerd/commit/b97098762834040359099e72be359e288d250a42) Fix container pid
- [`01edb7cddb`](https://github.com/containerd/containerd/commit/01edb7cddb34221a3121b709ae6c7c9db45fdea3) Merge pull request [#4015](https://github.com/containerd/containerd/pull/4015) from hakman/fix-libseccomp-ver
- [`a7c9b7605c`](https://github.com/containerd/containerd/commit/a7c9b7605cc62772851802ac0c653fc4e2f556c8) Fix incorrect comment from copy/paste of starting script
- [`13a3ac4`](https://github.com/containerd/cgroups/commit/13a3ac4f154c85e85ffc2eb9709387e5040548f7) fixed an issue with invalid soft memory limits
- [`db27230`](https://github.com/containerd/cgroups/commit/db272301ab8449d05f062e6db6f13d8a6aaff466) Merge pull request [#88](https://github.com/containerd/cgroups/pull/88) from woshijpf/fix-cgroup-left-problem
- [`0ecd2b6`](https://github.com/containerd/cgroups/commit/0ecd2b66d378b21c371721046c14d9f23bc07877) cgroups: fix MoveTo function fail problem
- [`42091f5`](https://github.com/containerd/cgroups/commit/42091f5cd88c6ce37c803d5f7a807197a3659aaa) Merge pull request [#85](https://github.com/containerd/cgroups/pull/85) from odinuge/cgroups-hugetlb-fix
- [`51dcf5f`](https://github.com/containerd/cgroups/commit/51dcf5fa00efa7947e3f454333e254ee97139226) Fix cgroup hugetlb size prefix for kB

### 1.2.14

- Fix regression pushing manifests as octet stream [#4268](https://github.com/containerd/containerd/pull/4268)
- [`abbb17959`](https://github.com/containerd/containerd/commit/abbb17959f55bbb9b7eb37f965d7dad2f4ea8744) Add comment clarifying fix for security issue
- [`3b72766af`](https://github.com/containerd/containerd/commit/3b72766af2f4404b9a09e3bd9608692949ad4e25) Merge pull request [#4268](https://github.com/containerd/containerd/pull/4268) from dmcgowan/1.2-fix-bad-backport-push-octet-stream
- [`f8ae16778`](https://github.com/containerd/containerd/commit/f8ae167780e2f00df6d1f58f0833e11ff487c57c) Fix incorrect backport of setting octet-stream
- [`d4242f0d3`](https://github.com/containerd/containerd/commit/d4242f0d3c09b47c5a483807291ec3a2564bbc19) Merge pull request [#4270](https://github.com/containerd/containerd/pull/4270) from estesp/travis-ci-fixes
- [`17a506c94`](https://github.com/containerd/containerd/commit/17a506c94f453ca678fc4bb844fa918a9a29481a) golangci-lint update and fix
- [`053f4d6fd`](https://github.com/containerd/containerd/commit/053f4d6fd856727e48fd9a537753e3146bcdfcb5) Update containerd/console vendor for fix
- [`a18c08347`](https://github.com/containerd/containerd/commit/a18c083471e070e601289852c807cdb35e7a80ef) fix additional linting failures
- [`961c23a57`](https://github.com/containerd/containerd/commit/961c23a5700b194455a64172217e4d837afdd6d7) fix killall when use pidnamespace
- [`a386eb648`](https://github.com/containerd/containerd/commit/a386eb648eb099d087ea50ea999713a0e8f61575) Fix linter errors


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.2.14**, the newest release recorded here for this line.

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
