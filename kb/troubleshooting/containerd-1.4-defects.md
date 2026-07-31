---
id: TROUBLE-CONTAINERD_1_4_DEFECTS
type: troubleshooting
title: "containerd 1.4: defects fixed in the 1.4 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.4.0 <1.5.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - containerd 1.4 known issues
  - containerd 1.4 fixed in
  - is this containerd bug already fixed
tags:
  - troubleshooting
  - upgrade
  - containerd
sources:
  - type: docs
    path: containerd/containerd release notes for the 1.4 line — bug-fix entries
    url: https://github.com/containerd/containerd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# containerd 1.4: defects fixed in the 1.4 line

## Summary

**274 defects** the project fixed across **10 releases** of the 1.4 line, from 1.4.0 to
1.4.12. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.4.0

- **Create image record after blob download to fix concurrent download issue** [#3972](https://github.com/containerd/containerd/pull/3972)
- **Fix privileged supported** [cri#1356](https://github.com/containerd/cri/pull/1356)
- [`60fa35f1`](https://github.com/containerd/containerd/commit/60fa35f11eba7422119d76dc72e15f315786a37c) Fix DCO commit limit
- [`cb7ffd4b`](https://github.com/containerd/containerd/commit/cb7ffd4b0bf9d76217cd4075aac66521e0769130) Fix indent in cni.template
- [`f938a166`](https://github.com/containerd/containerd/commit/f938a166cd55784efe9cc8c25d92b19501990791) Fix kube-container-runtime-monitor
- [`1b995fca`](https://github.com/containerd/containerd/commit/1b995fcaf2ae73872f4c1a2df983f4854d4c9c9d) Add KUBE_CONTAINER_RUNTIME_NAME to fix fluentd support
- [`af8bd806`](https://github.com/containerd/containerd/commit/af8bd80689b4e3ece62c286c30b696d72a60e50c) Fix for kube-up.sh and update several documments
- [`be72f47e`](https://github.com/containerd/containerd/commit/be72f47ec93361e6975a342317193d8b75e9a3d4) Add runtime cgroup and fix a cli panic
- [`67f19bfd`](https://github.com/containerd/containerd/commit/67f19bfdd8b878d42e5e9ad39cc9816aaec50728) Merge pull request [#4388](https://github.com/containerd/containerd/pull/4388) from AkihiroSuda/fix-mount-wait-no-child-processes
- [`ca15cb0d`](https://github.com/containerd/containerd/commit/ca15cb0d81a0b89b656b96858648730b328830a1) Fix incorrect (cut-and-paste) method comment
- [`3560a453`](https://github.com/containerd/containerd/commit/3560a453e4435a8d0b9382c5e631c68644dd0671) Merge pull request [#4385](https://github.com/containerd/containerd/pull/4385) from AkihiroSuda/fix-cri-dead-link
- [`decbb049`](https://github.com/containerd/containerd/commit/decbb0499705e08d4e93534487314d4418c4b4c7) RELEASES.md: fix a dead link
- [`b47c7ec2`](https://github.com/containerd/containerd/commit/b47c7ec274ff34488409f767a3026a0e0c0750e3) Update to later version of critools with timing fix
- [`852587cd`](https://github.com/containerd/containerd/commit/852587cd18c43f0b8086649865a0c9cad5403e03) [events/exchange_test] Fix deadlock in TestExchangeFilters
- [`468d4e1c`](https://github.com/containerd/containerd/commit/468d4e1ccf4ccb1425cca6417a49837d15605c73) Merge pull request [#4356](https://github.com/containerd/containerd/pull/4356) from estesp/actions-fixes
- [`57a9f0b5`](https://github.com/containerd/containerd/commit/57a9f0b50d6a8dd6e01cd774d6e9fcdd786e5bb0) Minor actions fixes/updates
- [`148cc8f7`](https://github.com/containerd/containerd/commit/148cc8f713e383f6fc8f1e598ecdd4978cfbcb16) [events] Fix deadlock in TestExchangeBasic
- [`492c0141`](https://github.com/containerd/containerd/commit/492c014136a301eff66a970311cd480d1d31228b) Merge pull request [#4340](https://github.com/containerd/containerd/pull/4340) from AkihiroSuda/fix-4312
- [`b96f5f4b`](https://github.com/containerd/containerd/commit/b96f5f4b524f58755ea18540513f80c99cc07b76) Fix deprecation warnings in CRI tests due to missing unix:// scheme
- [`fb80a49e`](https://github.com/containerd/containerd/commit/fb80a49ec111d11d2cd50743c00ecd8ebbb27c3a) Merge pull request [#4327](https://github.com/containerd/containerd/pull/4327) from AkihiroSuda/fix-4326
- [`49b0743c`](https://github.com/containerd/containerd/commit/49b0743c1c07500a062a6996c8afba2dafc8c64e) Merge pull request [#4324](https://github.com/containerd/containerd/pull/4324) from AkihiroSuda/fix-get-runtimeversion
- [`ae2f3fdf`](https://github.com/containerd/containerd/commit/ae2f3fdfd1a435fe83fb083e4db9fa63a9e0a13e) Merge pull request [#4315](https://github.com/containerd/containerd/pull/4315) from fuweid/fix-4294
- [`d36810d6`](https://github.com/containerd/containerd/commit/d36810d66d87f08b09003b2e2455bcabe116ab08) overlay: use index=off to fix EBUSY on mount
- [`7213cd89`](https://github.com/containerd/containerd/commit/7213cd89d659876c31468dd1c9f5c98ec16ecdcb) Process I/O: Fix goroutine leak
- [`ae08491b`](https://github.com/containerd/containerd/commit/ae08491bff2fdef7a91ff9c2d9e532d2f63d4bbd) waitForPid: fix goroutine leak
- [`be23b965`](https://github.com/containerd/containerd/commit/be23b965e4e71092da4a05e67f12f5f0a5b8684d) Merge pull request [#4291](https://github.com/containerd/containerd/pull/4291) from estesp/fix-release-markdown-length
- [`32262834`](https://github.com/containerd/containerd/commit/3226283470dbdaf7d5518620a9c68b67ac0b11f8) Fix client tests to work on Windows
- [`1c58c5d4`](https://github.com/containerd/containerd/commit/1c58c5d440f424e2d192f35f02306c5dc1a1e8c9) Merge pull request [#4277](https://github.com/containerd/containerd/pull/4277) from lucaskanashiro/fix-build-on-riscv64
- [`7ef3c0f4`](https://github.com/containerd/containerd/commit/7ef3c0f47d322a12c543fbd96cdcb14b3c561644) Merge pull request [#4275](https://github.com/containerd/containerd/pull/4275) from estesp/fix-image-usage
- [`0c9b05fa`](https://github.com/containerd/containerd/commit/0c9b05fa60e9b3a8ab2b0eb0254833741a73db74) Fix image usage calculation error
- [`84619ee9`](https://github.com/containerd/containerd/commit/84619ee99812fa865e19da85ffebcfaf890bbcb2) Fix configurations with no server provided
- [`06b0cd45`](https://github.com/containerd/containerd/commit/06b0cd45ba7b40a80e239d66827f421c674f6e49) Fix nil pointer errors
- [`db74d311`](https://github.com/containerd/containerd/commit/db74d3115ee35362935d584f0b7dd51faacc628f) unpacker: Fix data race and possible data corruption
- [`23251825`](https://github.com/containerd/containerd/commit/2325182529cbc6ce824adcfe4396f5553ca521ad) docker: fix data race on err
- [`80859e8f`](https://github.com/containerd/containerd/commit/80859e8fd8fb9f5822ab93f07ece4fdc40928bfd) Merge pull request [#4235](https://github.com/containerd/containerd/pull/4235) from renzhengeek/renzhen/fix-iohang
- [`63b7587c`](https://github.com/containerd/containerd/commit/63b7587cd64ec03c5a46180a6d5e4a286d10a30c) snapshots/devmapper: fix race windown causing IO hangup
- [`e094d363`](https://github.com/containerd/containerd/commit/e094d363ac2328305805c8d72b64ae2542617dd3) Merge pull request [#4206](https://github.com/containerd/containerd/pull/4206) from estesp/fix-golang-lint
- [`32649fe3`](https://github.com/containerd/containerd/commit/32649fe3055e9a5966a6311d7ea233d47bc5f23c) Fix retrieval of golangci-lint specific version
- [`327c92f7`](https://github.com/containerd/containerd/commit/327c92f7d79a4ffb7972b3edd1b30bd372b41358) Merge pull request [#4189](https://github.com/containerd/containerd/pull/4189) from estesp/actions-fixes
- [`74ceb35f`](https://github.com/containerd/containerd/commit/74ceb35f508e67abb00366ceeb42156a721316c5) Small fixes to our Actions CI workflow
- [`ccaf35b0`](https://github.com/containerd/containerd/commit/ccaf35b01c8799267ee51c414bc48fd1cb49fb05) Merge pull request [#4188](https://github.com/containerd/containerd/pull/4188) from estesp/fix-proto-gen
- [`041545cd`](https://github.com/containerd/containerd/commit/041545cd6ad53bd8a5279c3ea0ede101865cdc83) Fix protobuild and CI check protos
- [`59578495`](https://github.com/containerd/containerd/commit/595784954416a482dd8bde138e82305270b825e7) Merge pull request [#4162](https://github.com/containerd/containerd/pull/4162) from mxpv/log-fix
- [`056d6022`](https://github.com/containerd/containerd/commit/056d60224046ef4ede772633ebdba6c61784be3b) vendor: update go-events to fix alignment for 32bit systems
- [`ad090e67`](https://github.com/containerd/containerd/commit/ad090e67e9d72fdce6259c51ff56d2df824b25cd) man: move ctr.1, containerd-config to section 8, and fix generation
- [`488d6194`](https://github.com/containerd/containerd/commit/488d6194f2080709d9667e00ff244fbdc7ff95b2) fix dial error when clean up a dead shim
- [`6e638ad2`](https://github.com/containerd/containerd/commit/6e638ad27a6b5708f8b0eb06b17d3d0352609a2f) Nit: fix use of bufio.Scanner.Err
- [`dc085abd`](https://github.com/containerd/containerd/commit/dc085abda5a4ca48cdec11dfd3011279477ff238) Merge pull request [#4097](https://github.com/containerd/containerd/pull/4097) from tklauser/fix-duplicate-imports
- [`cad67b73`](https://github.com/containerd/containerd/commit/cad67b73f2bebc59cc450e830605df38a1ebdef7) Update btrfs dependencies in docs for debian buster and ubuntu 19.10 * Fixes: #4090
- [`c7eec0c1`](https://github.com/containerd/containerd/commit/c7eec0c1786595b9aa4c31cf43c65acd2c204f8f) Fix file header in builtins_cri.go
- [`4105135e`](https://github.com/containerd/containerd/commit/4105135e368071ece17f46484e3b5d84921d8161) fix killall when use pidnamespace
- [`2c5279e8`](https://github.com/containerd/containerd/commit/2c5279e820f86714df591b7f8d4b71052cf8ad87) Merge pull request [#4049](https://github.com/containerd/containerd/pull/4049) from fuweid/me-fix-flaky-testcase
- [`7811aa75`](https://github.com/containerd/containerd/commit/7811aa755265ba3f017683afb1ee3b5a1e0f29b4) Merge pull request [#4022](https://github.com/containerd/containerd/pull/4022) from estesp/fix-script-comment
- [`75d0c5f2`](https://github.com/containerd/containerd/commit/75d0c5f2e74b44353da357c5603a52871bea3940) Fix incorrect comment from copy/paste of starting script
- [`0dd6d24d`](https://github.com/containerd/containerd/commit/0dd6d24d2ae34680d6fb59fcd58c617ad0d61b34) Fix reference to LICENSE in README.md
- [`5abacb62`](https://github.com/containerd/containerd/commit/5abacb62da89dd18219f8ce28a2d4c3d28d8304d) Merge pull request [#4017](https://github.com/containerd/containerd/pull/4017) from bloodorangeio/octet-stream-fix
- [`cbf3ee0e`](https://github.com/containerd/containerd/commit/cbf3ee0e22635920adc221b7bf570cd82ab7bab9) Merge pull request [#4010](https://github.com/containerd/containerd/pull/4010) from zhsj/fix-zsh-complete
- [`348e683c`](https://github.com/containerd/containerd/commit/348e683cebe4ddada6d9b11c2581bfeacba8d458) Fix zsh autocomplete script
- [`12cb1554`](https://github.com/containerd/containerd/commit/12cb1554be8e3ba3fa6a7d11db2e8606a3163c0c) Merge pull request [#3972](https://github.com/containerd/containerd/pull/3972) from fuweid/me-fix-3937
- [`431cfd86`](https://github.com/containerd/containerd/commit/431cfd86e7bc636cdd5254ea8a30bd4f547c7bfc) Merge pull request [#3991](https://github.com/containerd/containerd/pull/3991) from mihaicmn/fix-default-config
- [`5e6d56ee`](https://github.com/containerd/containerd/commit/5e6d56ee2deaeeebf15cb6a19d4898e365a3d926) Fix startup_delay within default configuration
- [`e42110f3`](https://github.com/containerd/containerd/commit/e42110f3263bdf826b113b00fe66ff3ed6109ef2) Fix broken link to release-tool
- [`1189cc40`](https://github.com/containerd/containerd/commit/1189cc40f2bea63d2d381a4c95617c869c5c99cc) snapshots: fix flaky TestMetastore
- [`c55bd87f`](https://github.com/containerd/containerd/commit/c55bd87f471a4de48ea349e66bfdf7c454327421) Merge pull request [#3956](https://github.com/containerd/containerd/pull/3956) from sethp-nr/fix/eventfd-leak
- [`66508589`](https://github.com/containerd/containerd/commit/66508589d33c3ae0ad3db5a581c75c8257bc4bfc) fix: eventfd leak for v2 runtime with v1 cgroups
- [`9456040a`](https://github.com/containerd/containerd/commit/9456040acb746dccf65e700563fb7371a03f79e6) fix: eventfd leak
- [`95fbf3dc`](https://github.com/containerd/containerd/commit/95fbf3dc28d8dcc2531904c3efa5b53caa8ee6a4) Fix unpacker to pass use apply options
- [`7804afb2`](https://github.com/containerd/containerd/commit/7804afb226b6b44d6baac469157cd50f7a6bd761) Merge pull request [#3950](https://github.com/containerd/containerd/pull/3950) from dmcgowan/fix-printf-scanner-error
- [`3af3a760`](https://github.com/containerd/containerd/commit/3af3a7602650a8de47b77457fa05835ebcbff3bf) Fix filter errors
- [`8b3ef5fb`](https://github.com/containerd/containerd/commit/8b3ef5fb205730fc45614586b2aa95dfa2444f6f) Merge pull request [#3944](https://github.com/containerd/containerd/pull/3944) from zhsj/fix-openlabci
- [`41088e40`](https://github.com/containerd/containerd/commit/41088e405fa46a8325eeea3217fd05b48779419e) Merge pull request [#3939](https://github.com/containerd/containerd/pull/3939) from zhsj/fix-arm
- [`82fdac1c`](https://github.com/containerd/containerd/commit/82fdac1cd602fa3f1800d9fa82a9d3b90a0cf024) Merge pull request [#3935](https://github.com/containerd/containerd/pull/3935) from zhsj/fix-gccgo
- [`465c11dc`](https://github.com/containerd/containerd/commit/465c11dc8736d3e2a9a3b76ece6abdeb63a2f676) Fix build with gccgo
- [`52e477f9`](https://github.com/containerd/containerd/commit/52e477f947434989e93d0a9c22a7389d08b9b056) Fix outdated comments
- [`1fb1d932`](https://github.com/containerd/containerd/commit/1fb1d93212af763bd481b476293040b1566ae00b) v2: Fix missing ns when openShimLog on windows
- [`87e2a959`](https://github.com/containerd/containerd/commit/87e2a95951c3e00e8d672922a8bc07337c7a331c) Fix a typo in task.go
- [`496836c0`](https://github.com/containerd/containerd/commit/496836c09266a0ab00205bec78589c0aa83ee125) Update containerd/console vendor for fix
- [`f602b7b8`](https://github.com/containerd/containerd/commit/f602b7b8834cbbd99ffd4416a09c09a8f841269e) Merge pull request [#3899](https://github.com/containerd/containerd/pull/3899) from AkihiroSuda/fix-sys-mkdiras
- [`929ab521`](https://github.com/containerd/containerd/commit/929ab521c67e59a34983d9bffc513e1b20c3d647) fix system usage naming
- [`659c971c`](https://github.com/containerd/containerd/commit/659c971cad1fa1c0e183e17e3349bb2270fa1a3a) task metrics fix
- [`23dbae3e`](https://github.com/containerd/containerd/commit/23dbae3e71550e43b21c963f859dc7ecee444f8f) Schema name fix
- [`17d61d6b`](https://github.com/containerd/containerd/commit/17d61d6b7e7ac55c9b8bd52d41606aeca8b6bd03) Units fix
- [`f287bc22`](https://github.com/containerd/containerd/commit/f287bc2292efadee8e4ed2092ae7c782e595cdbd) Schema names fix
- [`6bfb2482`](https://github.com/containerd/containerd/commit/6bfb24824b552cf09d8078750f565a0d72f8c711) Fix prometheus metrics units
- [`cd23ad24`](https://github.com/containerd/containerd/commit/cd23ad2447d7c6c694572d35a96752e3daaab89b) Bump go-runc for buffer race fix
- [`f92470b3`](https://github.com/containerd/containerd/commit/f92470b3ebf5fec28f9d3129b48387ef99384652) Fix dependency in BUILDING.md
- [`b0821c80`](https://github.com/containerd/containerd/commit/b0821c801dc2225bb7478f91e967888a353fb60a) Merge pull request [#3857](https://github.com/containerd/containerd/pull/3857) from Random-Liu/fix-container-pid
- [`a6b6097c`](https://github.com/containerd/containerd/commit/a6b6097c90c02ad2c8aac45e4f0332dc1a00a60c) Fix container pid
- [`3a31ce26`](https://github.com/containerd/containerd/commit/3a31ce267db4cb64e543bede342f59b2beedbeb8) Merge pull request [#3853](https://github.com/containerd/containerd/pull/3853) from dmcgowan/fix-content-test-cleanup-race
- [`8da43466`](https://github.com/containerd/containerd/commit/8da4346686f339241efed3e6bf752cc4f8670103) Fix cleanup error on content client test
- [`2e293874`](https://github.com/containerd/containerd/commit/2e293874f1bdb8400aea4b5b011a786227e2db77) Merge pull request [#3825](https://github.com/containerd/containerd/pull/3825) from Random-Liu/fix-unpacker
- [`f684e5a7`](https://github.com/containerd/containerd/commit/f684e5a775a60d428122dc4a4127ef1273cd192e) Merge pull request [#3815](https://github.com/containerd/containerd/pull/3815) from estesp/fix-Dockerfile
- [`5bf2c6fc`](https://github.com/containerd/containerd/commit/5bf2c6fc25ad321b89f6d6fbad850276871d05f2) Fix panic on reference.Spec.Hostname()
- [`a647407c`](https://github.com/containerd/containerd/commit/a647407ca038bc208280ab5d5832f08c2f149464) Fix dependency in BUILDING.md
- [`f05e19c5`](https://github.com/containerd/containerd/commit/f05e19c5c6fa330753b84fe200f887cb3d62df41) Merge pull request [#3777](https://github.com/containerd/containerd/pull/3777) from Random-Liu/fix-containerd-config
- [`aaccfcbe`](https://github.com/containerd/containerd/commit/aaccfcbe2b8792e5fa3711811f3025562485e8bb) Fix `containerd config dump`
- [`a6a0c8b6`](https://github.com/containerd/containerd/commit/a6a0c8b6e36415a151d93d096c1c0af9e0bd7977) Merge pull request [#3736](https://github.com/containerd/containerd/pull/3736) from Random-Liu/final-fix-delete-code
- [`ffcb1cc9`](https://github.com/containerd/containerd/commit/ffcb1cc9be3eda8478d75c46ca02928db43b2693) Fix delete error code on the containerd daemon side
- [`036db34f`](https://github.com/containerd/containerd/commit/036db34f37617d6a02f07b04fc2d35a91732c6e3) build: Fix manpage generation
- [`c0c6b511`](https://github.com/containerd/containerd/commit/c0c6b511792575fd07d1b1c63e9c2f36f8d1ffb0) Merge pull request [#3730](https://github.com/containerd/containerd/pull/3730) from Random-Liu/fix-error-code
- [`06be794c`](https://github.com/containerd/containerd/commit/06be794cb228a5df073545d366965000ca25f3a4) Fix shim delete error code
- [`635dbf25`](https://github.com/containerd/containerd/commit/635dbf251a8e325064bdc3695a373628b035ec38) Merge pull request [#3720](https://github.com/containerd/containerd/pull/3720) from dmcgowan/fix-flaky-btrfs
- [`77203259`](https://github.com/containerd/containerd/commit/772032598a4282a50ccee29e9cc23be88bd74b2f) Fix flaky btrfs test
- [`702852f`](https://github.com/containerd/aufs/commit/702852f40822cd17a1c92073ef46c42f4b0e8d7c) Merge pull request [#16](https://github.com/containerd/aufs/pull/16) from Zyqsempai/fix-walk-method-interface
- [`1539353`](https://github.com/containerd/btrfs/commit/153935315f4ab9be5bf03650a1341454b05efa5d) Merge pull request [#24](https://github.com/containerd/btrfs/pull/24) from zhsj/fix-mipsle
- [`6d8cb52`](https://github.com/containerd/btrfs/commit/6d8cb5218ef717b43b6b994456467c1decb805c8) fix slice size overflow on mipsle
- [`ff6e9c8`](https://github.com/containerd/cgroups/commit/ff6e9c8c63dde78d6b84182ae38dc9315fb202da) cpuset: typo fix for function name
- [`666f4a0`](https://github.com/containerd/cgroups/commit/666f4a009ffb2741d4d3884aead4dfc17497c2d6) Merge pull request [#158](https://github.com/containerd/cgroups/pull/158) from AkihiroSuda/fix-event-chan
- [`d77cdc4`](https://github.com/containerd/cgroups/commit/d77cdc42998ffb8adc38cb14962b1ef14ae733cf) Merge pull request [#159](https://github.com/containerd/cgroups/pull/159) from AkihiroSuda/fix-vagrant
- [`7a4b407`](https://github.com/containerd/cgroups/commit/7a4b4074b7d191f77c127d185d7d04488f961962) v2: fix EventChan
- [`45229ee`](https://github.com/containerd/cgroups/commit/45229ee60b6d744a01351e14d6948c44aca15672) fix Vagrant on Travis (switch to KVM)
- [`8a7151d`](https://github.com/containerd/cgroups/commit/8a7151d737af59df0be4c145c4884ae66fa13d2f) Fix bufio.Scanner.Err usage
- [`6c3dec4`](https://github.com/containerd/cgroups/commit/6c3dec43a1030a55584ab8b5b181411029d43ecc) Merge pull request [#147](https://github.com/containerd/cgroups/pull/147) from kzys/blkio-fix
- [`42ee50a`](https://github.com/containerd/cgroups/commit/42ee50a2c342eaf24c1f95b8a7376ef2da3fcf86) eof fix
- [`69a639c`](https://github.com/containerd/cgroups/commit/69a639c59786aec5f73d35cec6f1e7a0277ad851) Fixed io.weight conversation + systemd io.weight controll added
- [`7347743`](https://github.com/containerd/cgroups/commit/7347743e5d1e8500d9f27c8e748e689ed991d92b) Merge pull request [#141](https://github.com/containerd/cgroups/pull/141) from AkihiroSuda/fix-iostat
- [`3f83850`](https://github.com/containerd/cgroups/commit/3f83850c48d225466698517ad34f4848d2ddaeeb) Merge pull request [#140](https://github.com/containerd/cgroups/pull/140) from Zyqsempai/dbus-fix-version
- [`7305d12`](https://github.com/containerd/cgroups/commit/7305d123a75b0f622f2ee543761e2cadf3b1c86e) go mod fix
- [`140bd90`](https://github.com/containerd/cgroups/commit/140bd90a7ae79a5d347a4394675f0a1a5d09a0ab) Fix dbus version in utils
- [`7d585c4`](https://github.com/containerd/cgroups/commit/7d585c40f10b87650d114877dbcec2b72a852357) Resource rework + path fix
- [`7b4fbc7`](https://github.com/containerd/cgroups/commit/7b4fbc7a0b3877704bdc4b82bc4ded8bc42f18e7) Toggle controllers fix
- [`b0a15b1`](https://github.com/containerd/cgroups/commit/b0a15b1d1682d7555d4793bc2122c8f9b162fb4f) conflict fix
- [`07c51ec`](https://github.com/containerd/cgroups/commit/07c51ec75fa7fc5ce7813c735571947723a77fb7) dbus version fix
- [`94c46b4`](https://github.com/containerd/cgroups/commit/94c46b4c3e607eb8d8aebb46bcd1a0b704850d8a) proto fix
- [`ac62cf6`](https://github.com/containerd/cgroups/commit/ac62cf6dd3afcbac5a4dadbf8fefb5918878f070) fix out of range err for cpuset.cpus
- [`9b3ab60`](https://github.com/containerd/cgroups/commit/9b3ab60f90931a1f8447d077b911219e7b69bf80) Test fix
- [`e284b4a`](https://github.com/containerd/cgroups/commit/e284b4ab2fcfbee98c0d2c004534fc3587403a1d) comment fix
- [`5dba053`](https://github.com/containerd/cgroups/commit/5dba05335a7d92d7ec6abb0d6166e77131542571) GroupPath fix 2
- [`f40b256`](https://github.com/containerd/cgroups/commit/f40b25688bb5cce86d6bcc6cf7fb213109848af3) GroupPath fix
- [`28f74d7`](https://github.com/containerd/cgroups/commit/28f74d748f4cf34c33386d8b3d7b3c827e93d17e) Fixed memory convertion for `reservation` from high to low
- [`bd09c0d`](https://github.com/containerd/cgroups/commit/bd09c0d4a78929b7acaebc4bdc979a445138481e) Merge pull request [#124](https://github.com/containerd/cgroups/pull/124) from AkihiroSuda/fix-toggle
- [`e0c89c3`](https://github.com/containerd/cgroups/commit/e0c89c36d7a50f945a17f1865023a46cbe51fa3e) Merge pull request [#123](https://github.com/containerd/cgroups/pull/123) from AkihiroSuda/fix-stat-panic
- [`3a0e799`](https://github.com/containerd/cgroups/commit/3a0e799bed92fe66eb71391f1f8d337fb8bbe7ba) v2: fix rdma nil panic
- [`e56683d`](https://github.com/containerd/cgroups/commit/e56683d3d5a15abdea66d7511b5e16083da2f594) Merge pull request [#120](https://github.com/containerd/cgroups/pull/120) from AkihiroSuda/fix-v2-stats
- [`c4993ae`](https://github.com/containerd/cgroups/commit/c4993aebedaa31fe8435702ddae54ec0a5c0ac9f) v2: fix nil panic on statting disabled controllers
- [`1c26af6`](https://github.com/containerd/cgroups/commit/1c26af6c55f531b70d57f7058796c8e6d6aa6e09) v2: fix parsing pids stat
- [`dc02b2f`](https://github.com/containerd/cgroups/commit/dc02b2f5d16be7b3ac6e1bc770a28e430c2753ca) Header fix
- [`2036eb8`](https://github.com/containerd/cgroups/commit/2036eb8905da80070184eae3155f45bbac66f4e8) Test fix
- [`d0f61b7`](https://github.com/containerd/cgroups/commit/d0f61b75b2777e567a0504d584d733b8cc5760df) Set GO111MODULE=on to fix Go 1.11/1.12 builds
- [`b15f984`](https://github.com/containerd/cgroups/commit/b15f98493ecf98710faa65af8eb3e4eeef892859) v2: fix TestParseCgroupFromReader
- [`fa1a76b`](https://github.com/containerd/cgroups/commit/fa1a76b28faaff678184549171de676315645c09) Fixed test file permissions
- [`9365a1b`](https://github.com/containerd/continuity/commit/9365a1b01a63247561eab02c7d5914a554736c69) Fix golangci-lint errors
- [`f265cff`](https://github.com/containerd/continuity/commit/f265cff0764e5f8155e80d532db78f617e08e021) fix gofmt issues
- [`cf53015`](https://github.com/containerd/continuity/commit/cf53015a8bae42a53c5725e0d9bef11fde50694e) Merge pull request [#153](https://github.com/containerd/continuity/pull/153) from tomfaulhaber/empty-file-fix
- [`11900e8`](https://github.com/containerd/continuity/commit/11900e88c487c2e28650d44cc88a95e86734f01c) Fix sameFile() to recognize empty files as the same
- [`9e256e6`](https://github.com/containerd/continuity/commit/9e256e61eee8fc393366eb5c00d8b5fed8bb94fe) sysx/xattr: fix getxattrAll
- [`0ec5967`](https://github.com/containerd/continuity/commit/0ec596719c75bfd42908850990acea594b7593ac) Merge pull request [#148](https://github.com/containerd/continuity/pull/148) from zhsj/fix-gccgo
- [`75bee3e`](https://github.com/containerd/continuity/commit/75bee3e2ccb6402e3a986ab8bd3b17003fc0fdec) Merge pull request [#143](https://github.com/containerd/continuity/pull/143) from tiborvass/fix-sockets
- [`4c8164bc`](https://github.com/containerd/cri/commit/4c8164bccf35b134ad9864409882105ade5b3c85) Specify version = 2 & fix wrong key in registry.md (GCR example)
- [`a01750d8`](https://github.com/containerd/cri/commit/a01750d89af991c37906165f8d6f68ceb5903730) Merge pull request [#1530](https://github.com/containerd/cri/pull/1530) from hckuo/fix-doc-for-runtime-options
- [`904ab30f`](https://github.com/containerd/cri/commit/904ab30f9dc3bc33974daca112b7024609417436) Fix doc for runtime specifc options
- [`1bc5ba3f`](https://github.com/containerd/cri/commit/1bc5ba3f484ecae7feb3156ad0e3760b728de66e) Merge pull request [#1519](https://github.com/containerd/cri/pull/1519) from AkihiroSuda/config-fix-toml-tag
- [`b69d7bdc`](https://github.com/containerd/cri/commit/b69d7bdc5fa9f61532819029c864cd3724a79db6) config: fix TOML tag for TolerateMissingHugePagesCgroupController
- [`8e0b789c`](https://github.com/containerd/cri/commit/8e0b789c9ade07497283546c0bde0fb5f99310cb) Merge pull request [#1520](https://github.com/containerd/cri/pull/1520) from AkihiroSuda/fix-ci-apt-get-update
- [`682d1583`](https://github.com/containerd/cri/commit/682d158399ed7c58c1bc8dd4f5282c4446c0aba3) Merge pull request [#1517](https://github.com/containerd/cri/pull/1517) from mikebrow/fix-e2e-bucket
- [`f5c7ac92`](https://github.com/containerd/cri/commit/f5c7ac92724405806eb4e330ecab8f4350601089) fix for image pull linter change
- [`098e0400`](https://github.com/containerd/cri/commit/098e040014aa8e413c7419f7e6db1db51e7133ff) Fix typo
- [`e56347aa`](https://github.com/containerd/cri/commit/e56347aabc6b5b26aaf6033826e791d1f3b43ab4) move up to latest critools pick up nginx fix
- [`17c61e36`](https://github.com/containerd/cri/commit/17c61e36cb5ed6ee59d27074e6be7e08663646fa) Fix cgroups path for base OCI spec
- [`e10e07b5`](https://github.com/containerd/cri/commit/e10e07b50e6de4a553648206d4ba7d2e97795fdf) Merge pull request [#1489](https://github.com/containerd/cri/pull/1489) from mikebrow/ltag-scan-symlink-fixed
- [`e2cedb94`](https://github.com/containerd/cri/commit/e2cedb9469c03fb78837e3783775633b426dc01a) Increase port-forward timeout to 1s to fix e2e test
- [`cdac4dec`](https://github.com/containerd/cri/commit/cdac4dece47e822afa83c78c890942d5cdb7715e) vendor: update go-events to fix alignment for 32bit systems
- [`41470105`](https://github.com/containerd/cri/commit/41470105749546b2f9d2c67dff7f4c519fd37d79) Merge pull request [#1457](https://github.com/containerd/cri/pull/1457) from hickeyma/fix-docs
- [`98f8ec49`](https://github.com/containerd/cri/commit/98f8ec4995d688db3d62d265f298d3183e3d49f9) fix incomplete host device for PrivilegedWithoutHostDevices
- [`befc70b4`](https://github.com/containerd/cri/commit/befc70b444e24eaa76b3ef18633e9fba64d5e795) Merge pull request [#1456](https://github.com/containerd/cri/pull/1456) from mikebrow/fix-deprecated-greeting
- [`2b162b6c`](https://github.com/containerd/cri/commit/2b162b6c11ca02c6f4fdb4dd075a0b4cbb07cf4e) update selinux dependency to fix test failures
- [`3d250b82`](https://github.com/containerd/cri/commit/3d250b8289d3dbb6c4551c78e8da9a4ede1f0474) Merge pull request [#1439](https://github.com/containerd/cri/pull/1439) from mikebrow/fix-selinux-unit-test
- [`aa9b1885`](https://github.com/containerd/cri/commit/aa9b1885b58cc22081d48e6cd2e4cbceca132c77) fixes bad unit tests when selinux is enabled
- [`27d4fd59`](https://github.com/containerd/cri/commit/27d4fd5979ef38c893147774e9801bb31d66d123) Merge pull request [#1425](https://github.com/containerd/cri/pull/1425) from dims/fix-x/sys-dependency-version
- [`cb014006`](https://github.com/containerd/cri/commit/cb0140063e26eb56e937c2d4fae9d18216b8a80d) Fix goroutine leak when exec/attach
- [`c44ad801`](https://github.com/containerd/cri/commit/c44ad801f9e8fa4f2ba566dbdcda8a3a1c568475) Fixed merge conflicts
- [`a8cc66b3`](https://github.com/containerd/cri/commit/a8cc66b37adc95aa9ef58cc859456399cfed87af) Fix store error serialization to gRPC status codes
- [`83a9d246`](https://github.com/containerd/cri/commit/83a9d2460c5fdd4843141386e3b3b462a137f51c) Merge pull request [#1363](https://github.com/containerd/cri/pull/1363) from Random-Liu/fix-validate-config
- [`0c2d3b71`](https://github.com/containerd/cri/commit/0c2d3b718d473157c0e97ebc4e8b217332c1358a) Fix privileged devices
- [`40e147cb`](https://github.com/containerd/cri/commit/40e147cb737335c43e3494c954952141627e9657) Merge pull request [#1347](https://github.com/containerd/cri/pull/1347) from Random-Liu/fix-typo
- [`4f350ad4`](https://github.com/containerd/cri/commit/4f350ad474c8f21bcc0ad704d4ba7ff9052476f8) Fix typo
- [`9f79be1b`](https://github.com/containerd/cri/commit/9f79be1b887af3df40f1e807ad2a1aedf0b931ad) Merge pull request [#1331](https://github.com/containerd/cri/pull/1331) from erikwilson/fix-http-localhost
- [`fe757946`](https://github.com/containerd/cri/commit/fe757946cabdc36ac62bbfac7c888d37d57ab935) Merge pull request [#1319](https://github.com/containerd/cri/pull/1319) from Random-Liu/fix-containerd-build
- [`8bfff7db`](https://github.com/containerd/cri/commit/8bfff7dbd2c3e594bfb13b82f48ccc7c1971e5a4) Fix containerd build, use `libbtrfs-dev` when available
- [`2a9a982a`](https://github.com/containerd/cri/commit/2a9a982ae36cb0d4186b1e19259c990c62e29f6c) Fix integration test for golang 1.13
- [`10f88f99`](https://github.com/containerd/cri/commit/10f88f99cceabad292d1e5bd4a15cd2e6ca29b55) Fix appveyor test
- [`a1e4f99a`](https://github.com/containerd/cri/commit/a1e4f99a321435cb55cdbedd066d0e2419a6ee9c) Merge pull request [#1296](https://github.com/containerd/cri/pull/1296) from Random-Liu/fix-ssh-disconnect
- [`0a6d9f18`](https://github.com/containerd/cri/commit/0a6d9f188b06901b1e6778efa087a5f1a07d4875) Merge pull request [#1291](https://github.com/containerd/cri/pull/1291) from Random-Liu/fix-indent-cni
- [`b4c46db7`](https://github.com/containerd/cri/commit/b4c46db790f828e931da22b0d831dd83de92d3bc) Fix indent in cni.template
- [`161abf8f`](https://github.com/containerd/cri/commit/161abf8f5b5700dd838f23bbfd6520e893a70126) Fix golangci-lint findings
- [`7b606375`](https://github.com/containerd/cri/commit/7b606375ae4997112246c4cf237c0056c5b41aa3) Merge pull request [#1259](https://github.com/containerd/cri/pull/1259) from Random-Liu/fix-potential-panic-for-unknown-state
- [`c6203ec1`](https://github.com/containerd/cri/commit/c6203ec13bfd2cbe3cbed43f1622d27737d583cd) Fix panic for task in unknown state
- [`b5ec5ee4`](https://github.com/containerd/cri/commit/b5ec5ee4f63e2fee693eacc716d754385bbfe485) Merge pull request [#1255](https://github.com/containerd/cri/pull/1255) from Random-Liu/fix-doc
- [`0997453f`](https://github.com/containerd/cri/commit/0997453f33fb1c46f8322820adc5c892b7490f52) Update cri-tools to fix all image reference test failure
- [`f41675d2`](https://github.com/containerd/cri/commit/f41675d234bb8212457ea04eae5d47dc3606bf6b) fix: support empty auth config for anonymous registry
- [`9dbe056`](https://github.com/containerd/fifo/commit/9dbe056af80075321f69c046d721a8085aa810b6) Fix golangci-lint problems
- [`5ff6bce`](https://github.com/containerd/fifo/commit/5ff6bcedcec9724bced307648a6ea1fd93250288) fix gofmt
- [`7332d8a`](https://github.com/containerd/go-cni/commit/7332d8a46103cfa7d2f0d59e07bbed7f959143b8) Fix "modules disabled inside GOPATH/src by GO111MODULE=auto"
- [`469fa2c`](https://github.com/containerd/go-runc/commit/469fa2cf9fac19d820cfabe4073c55703d09c794) Fix data race in use of cmd output buffers
- [`a2952bc`](https://github.com/containerd/go-runc/commit/a2952bc25f5116103a8b78f3817f6df759aa7def) Merge pull request [#56](https://github.com/containerd/go-runc/pull/56) from tonistiigi/typo-fix
- [`925bf84`](https://github.com/containerd/go-runc/commit/925bf842108f87a6bf7a1f5a8f0f11be64206ec9) fix typo in successfully
- [`1fe292f`](https://github.com/containerd/imgcrypt/commit/1fe292fc35261ded6b7590a592021378f56e4bbc) Fixed linting
- [`9ece5ae`](https://github.com/containerd/ttrpc/commit/9ece5ae787377199802deacb7f174f4c9ee09f8c) server: fix the issue if connections leak
- [`2ef8878`](https://github.com/containerd/ttrpc/commit/2ef8878926f84f015a51f4a68218d101af747b73) ttrpc: fix the issue of marshaling on nil will crash the server
- [`a1e455d`](https://github.com/containerd/typeurl/commit/a1e455d55b64d818790940929bc5055f65f81096) fix 404 link
- [`9abf673`](https://github.com/containerd/zfs/commit/9abf673ca6ff9ab8d9bd776a4ceff8f6dc699c3d) Merge pull request [#25](https://github.com/containerd/zfs/pull/25) from Zyqsempai/fix-walk-method-interface
- [`456dcfd`](https://github.com/containerd/zfs/commit/456dcfd8803bbaabd31a91d346ce7e37af7a5053) Fix snapshot commit to pass opts to storage

### 1.4.1

- Fix error deleting v2 bundle directory when removing rootfs returns `ErrNotExist` [containerd/containerd#4472](https://github.com/containerd/containerd/pull/4472)
- Fix metrics monitoring of v2 runtime tasks [containerd/containerd#4486](https://github.com/containerd/containerd/pull/4486)
- Fix incorrect stat for Windows containers [containerd/containerd#4468](https://github.com/containerd/containerd/pull/4468)
- Fix devmapper device deletion on rollback [containerd/containerd#4437](https://github.com/containerd/containerd/pull/4437)
- [`086e859d`](https://github.com/containerd/containerd/commit/086e859d2172d524d9069e3a50871a62081eda09) BUILDING.md: fix description about static builds
- [`23e0ea27`](https://github.com/containerd/containerd/commit/23e0ea27b7398d499d7e7781395a2b59e4c9f931) snapshots/devmapper: fix rollback

### 1.4.2

- Fix bug limiting the number of layers by default [containerd/cri#1602](https://github.com/containerd/cri/pull/1602)
- Fix selinux shared memory issue by relabeling /dev/shm [containerd/cri#1605](https://github.com/containerd/cri/pull/1605)
- Fix unknown state preventing removal of containers [containerd/containerd#4656](https://github.com/containerd/containerd/pull/4656)
- Fix nil pointer error when restoring checkpoint [containerd/containerd#4754](https://github.com/containerd/containerd/pull/4754)
- Fix integer overflow on Windows [containerd/containerd#4589](https://github.com/containerd/containerd/pull/4589)
- Fix lcow snapshotter to read trailing tar data [containerd/containerd#4628](https://github.com/containerd/containerd/pull/4628)
- [`ca9950755`](https://github.com/containerd/containerd/commit/ca9950755257ad316709f4c819f239fa332fb6a6) Update cri version to pickup unknown state fix
- [`c0f1add3c`](https://github.com/containerd/containerd/commit/c0f1add3c95ce1c06c566488d85c20a77070ef12) Fix Windows service panic file to not be read-only
- [`9c24574c9`](https://github.com/containerd/containerd/commit/9c24574c99643f94a050395637b328ce2d48e2c9) Merge pull request [#4763](https://github.com/containerd/containerd/pull/4763) from estesp/cp-tests-fix-1.4
- [`fbe18caa1`](https://github.com/containerd/containerd/commit/fbe18caa19f7b414dca8433455b5d4b4662c7d4c) Update btrfs vendor for chkptr fix for Go >= 1.14
- [`56291a221`](https://github.com/containerd/containerd/commit/56291a2212c4723c73932a76a8cbc78ce0c14a61) bug fix:#3448
- [`16e51fc31`](https://github.com/containerd/containerd/commit/16e51fc3173a4eb066443571ee974f67ad24a4e5) Fix integer overflow on windows
- [`6ebd9a94a`](https://github.com/containerd/containerd/commit/6ebd9a94a47bf8a885b2a8441ccea4494dcd0d21) Update other actions for env/path CVE fix
- [`49889957e`](https://github.com/containerd/containerd/commit/49889957e6e1e1519332beef349a08b9bc55ba93) Merge pull request [#4743](https://github.com/containerd/containerd/pull/4743) from estesp/fix-ci
- [`0a3488c71`](https://github.com/containerd/containerd/commit/0a3488c712d699694f7b2c2458e7498f29d5e89a) Fix GH Actions CI deprecations
- [`48eb88e`](https://github.com/containerd/btrfs/commit/48eb88e4fc0a1806012557496e50669afe671e30) Merge pull request [#27](https://github.com/containerd/btrfs/pull/27) from fuweid/fix-checkptr-issue
- [`d44cb8e`](https://github.com/containerd/btrfs/commit/d44cb8e80d3e3b8d924fa9db42cc666848679f58) fix: checkptr issue
- [`adc0b6a5`](https://github.com/containerd/cri/commit/adc0b6a578ed6f646bb24c1c639d65b70e14cccc) Merge pull request [#1600](https://github.com/containerd/cri/pull/1600) from zhuangqh/fix-unknown-state
- [`7973126f`](https://github.com/containerd/cri/commit/7973126fbc933fd35284a799cc22bc97157bb825) fix: always set unknown to false when handling exit event

### 1.4.4

- **Fix container create in CRI to prevent possible environment variable leak between containers** [#1628](https://github.com/containerd/cri/pull/1628)
- **Fix incorrect usage calculation** [#5019](https://github.com/containerd/containerd/pull/5019)
- [`23495ab4a`](https://github.com/containerd/containerd/commit/23495ab4a1252e0ca2b2494c008807d9fe6238e7) Merge pull request [#5082](https://github.com/containerd/containerd/pull/5082) from AkihiroSuda/fix-5077-14
- [`e7851d743`](https://github.com/containerd/containerd/commit/e7851d743c71e9c13e30137219ef8323f3033ff6) CI: fix "ls: cannot access '/etc/cni/net.d': Permission denied"
- [`02df14f78`](https://github.com/containerd/containerd/commit/02df14f783472f05a5df949ceb4c596dd9c90ec2) Merge pull request [#4993](https://github.com/containerd/containerd/pull/4993) from Iceber/fix-runc-v2-service-1.4
- [`f087d7849`](https://github.com/containerd/containerd/commit/f087d7849111a35fe3a6ec32bcca3bdaf1298568) runtime: fix shutdown runc v2 service
- [`349f7a5ef`](https://github.com/containerd/containerd/commit/349f7a5ef916aff33d717685a49b796b114f02f3) Merge pull request [#4971](https://github.com/containerd/containerd/pull/4971) from payall4u/bugfix/fix-open-shim-fifo-rebase
- [`1d9893e`](https://github.com/containerd/continuity/commit/1d9893e5674b5260c3fc11316d0d5fc0d12ea9e2) Merge pull request [#169](https://github.com/containerd/continuity/pull/169) from dmcgowan/fix-usage-block-size
- [`b97555e`](https://github.com/containerd/continuity/commit/b97555e75c86a5f693aa104085036ad4eb1467de) Fix incorrect usage calculation
- [`91328d7`](https://github.com/containerd/continuity/commit/91328d7c60e71160252e8271376d9efadd16f0ad) Merge pull request [#166](https://github.com/containerd/continuity/pull/166) from zhsj/fix-riscv64
- [`62ef0ff`](https://github.com/containerd/continuity/commit/62ef0fffa6a1bed97d4b034c146bc323b2447b72) Merge pull request [#165](https://github.com/containerd/continuity/pull/165) from zhsj/fix-arm64
- [`25269ef`](https://github.com/containerd/continuity/commit/25269efb6192a3f31d9ef6a57d8631cd48b5f3b9) Fix building on arm64
- [`310e183`](https://github.com/containerd/continuity/commit/310e183616c481b7237980a7787a26435d311c0d) gha: fix invalid workflow definition
- [`04c754f`](https://github.com/containerd/continuity/commit/04c754faca46997ba6d0733f611c42f1816d1199) Merge pull request [#163](https://github.com/containerd/continuity/pull/163) from dmcgowan/fix-sparse-file-usage
- [`bc5e3ed`](https://github.com/containerd/continuity/commit/bc5e3edd2b742c38c762d928f267ad82922a1b63) Fix usage calculation to account for sparse files
- [`7efa54f0`](https://github.com/containerd/cri/commit/7efa54f003dac800f79599a5b460e29cca5fc5a6) Fix deprecated registry auth conversion
- [`5848b5ba`](https://github.com/containerd/cri/commit/5848b5babbe0728881abb78757b54a0c9ccdf642) cri/config: fix range iterator issue in ValidatePluginConfig

### 1.4.5

- **Fix leaking socket path in runc shim v2** [#5195](https://github.com/containerd/containerd/pull/5195)
- **Fix cleanup logic in new container in runc shim v2** [#5206](https://github.com/containerd/containerd/pull/5206)
- **Fix registry mirror authorization logic in CRI plugin** [#5446](https://github.com/containerd/containerd/pull/5446)
- [`8263eb3ea`](https://github.com/containerd/containerd/commit/8263eb3eaee447b16856eeb8839d5df4c9cca71a) Merge pull request [#5488](https://github.com/containerd/containerd/pull/5488) from dmcgowan/fix-1.4-seccomp-build
- [`691606d45`](https://github.com/containerd/containerd/commit/691606d4507d5e4a0121578252711da5b7a5a7cb) Fix seccomp build in release
- [`409c87ba5`](https://github.com/containerd/containerd/commit/409c87ba59dd96965239573aa9458a3585c05468) Merge pull request [#5319](https://github.com/containerd/containerd/pull/5319) from Iceber/fix-new-container-1.4
- [`c64cfa03b`](https://github.com/containerd/containerd/commit/c64cfa03b9defd0b11f3f40e5a1ba524cc52533e) runtime/v2/runc: fix the defer cleanup of the NewContainer
- [`425a6e4f8`](https://github.com/containerd/containerd/commit/425a6e4f89fd02e290cae86172ad83720cbfcc86) night ci fix: add packages for ubuntu 20.04
- [`218f47057`](https://github.com/containerd/containerd/commit/218f470576548b318cf8cc27b625e176577660a8) Merge pull request [#5363](https://github.com/containerd/containerd/pull/5363) from mikebrow/move-up-to-fixed-cri-tools
- [`8c5422eb6`](https://github.com/containerd/containerd/commit/8c5422eb69ac04f93576bbb85dcea56dabe9675d) Fix error log when copy file
- [`f9d6a7604`](https://github.com/containerd/containerd/commit/f9d6a7604a97a0a1c2ddf3ad85e35e7e95e0252f) runtime/v2/runc: fix leaking socket path
- [`24921417f`](https://github.com/containerd/containerd/commit/24921417f5cf60b07afbce708b4affc7ce6b5d22) Fix missing close
- [`0dea19170`](https://github.com/containerd/containerd/commit/0dea191709319db5a9949112448dfc325f7d8621) Merge pull request [#5201](https://github.com/containerd/containerd/pull/5201) from Iceber/fix-ctr-command-1.4
- [`4c875c81a`](https://github.com/containerd/containerd/commit/4c875c81a8ebebce8f150dca83bbd853254a8387) cmd/ctr: fix export command
- [`4c2f6a7ab`](https://github.com/containerd/containerd/commit/4c2f6a7ab4c5d0b5c85e6a4e42f7fb058df7f80d) Fix advisory link in release notes for containerd 1.4.4

### 1.4.7

- **Fix invalid validation error checking** [#5565](https://github.com/containerd/containerd/pull/5565)
- **Fix error on image pull resume** [#5560](https://github.com/containerd/containerd/pull/5560)
- **Fix symlink resolution for disk mounts on Windows** [#5411](https://github.com/containerd/containerd/pull/5411)
- [`591744a85`](https://github.com/containerd/containerd/commit/591744a859c11f906d3f179ce6a4cbc40be8efc1) [release/1.4] Fix missing Body.Close() calls on push to docker remote
- [`208a2f649`](https://github.com/containerd/containerd/commit/208a2f6493aa04847c8fd884d381b64bd7e4e7b6) fix invalid validation error checking
- [`f3ae4a5c`](https://github.com/containerd/cri/commit/f3ae4a5c110d1e5dddb217ac25a44c8574b8fdd0) Fix cleanup context of teardownPodNetwork

### 1.4.9

- **Fix user agent used for fetching registry authentication tokens** [#5761](https://github.com/containerd/containerd/pull/5761)
- [`14c3a8e21`](https://github.com/containerd/containerd/commit/14c3a8e21441070ec2c904b878f908f9a59ddb85) remotes/docker/pusher.go: Fix missing Close()
- [`06c90e7b5`](https://github.com/containerd/containerd/commit/06c90e7b597eb28b8834db92797fa38a601b2132) remotes/docker/fetcher.go: Fix missing Close()
- [`67a0576df`](https://github.com/containerd/containerd/commit/67a0576df96ad2da414d8d26720cb4edf9357600) [release/1.4] Fix incorrect UA used for registry authentication

### 1.4.10

- **Fix panic in metadata content writer on copy error** [#6043](https://github.com/containerd/containerd/pull/6043)
- [`9b712ec73`](https://github.com/containerd/containerd/commit/9b712ec731b5a457c6cff35676beeaf3b82f9998) Merge pull request [#6044](https://github.com/containerd/containerd/pull/6044) from dmcgowan/1.4-fix-metadata-content-panic
- [`6dddee4c8`](https://github.com/containerd/containerd/commit/6dddee4c8ffde7112a9ff1b6e2256b060733c12e) Fix panic in metadata content writer on copy error

### 1.4.11

- **Fix insufficiently restricted permissions on container root and plugin directories** [GHSA-c2h3-6mxw-7mvq](https://github.com/containerd/containerd/security/advisories/GHSA-c2h3-6mxw-7mvq)

### 1.4.12

- [release/1.4] Fix containerd fails to pull OCI image with non-`http(s)://` urls ([#6239](https://github.com/containerd/containerd/pull/6239)) [`e9f59a95e`](https://github.com/containerd/containerd/commit/e9f59a95ed5131d2a907fb26d4be2841e1787d28) Fix containerd fails to pull OCI image with non-`http(s)://` urls


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.4.12**, the newest release recorded here for this line.

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
