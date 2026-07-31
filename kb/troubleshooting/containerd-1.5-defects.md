---
id: TROUBLE-CONTAINERD_1_5_DEFECTS
type: troubleshooting
title: "containerd 1.5: defects fixed in the 1.5 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.5.0 <1.6.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - containerd 1.5 known issues
  - containerd 1.5 fixed in
  - is this containerd bug already fixed
tags:
  - troubleshooting
  - upgrade
  - containerd
sources:
  - type: docs
    path: containerd/containerd release notes for the 1.5 line — bug-fix entries
    url: https://github.com/containerd/containerd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# containerd 1.5: defects fixed in the 1.5 line

## Summary

**495 defects** the project fixed across **17 releases** of the 1.5 line, from 1.5.0 to
1.5.18. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.5.0

- [`c4d30c173`](https://github.com/containerd/containerd/commit/c4d30c173f9bb7150ed39c707366697cd014e807) Merge pull request [#5379](https://github.com/containerd/containerd/pull/5379) from ktock/fix-push-race
- [`ab1654d0e`](https://github.com/containerd/containerd/commit/ab1654d0e2765c7774d5721db94bf8c570b06e9a) Fix PushHandler cannot push image that contains duplicated blobs
- [`cc393ea87`](https://github.com/containerd/containerd/commit/cc393ea87a9b0ce815ef9c94cbfeefbf14c9442d) Merge pull request [#5279](https://github.com/containerd/containerd/pull/5279) from wzshiming/fix/backoff
- [`fca0da46b`](https://github.com/containerd/containerd/commit/fca0da46b029054cf68cff31139040c6470c8a46) Merge pull request [#5364](https://github.com/containerd/containerd/pull/5364) from wzshiming/fix/list-pids-lock
- [`fdb76f55d`](https://github.com/containerd/containerd/commit/fdb76f55d8eacf8852fc18bcd9f7e07bb7b5f924) Fix backword-compatibility issue of non-versioned config file
- [`2de38a926`](https://github.com/containerd/containerd/commit/2de38a92696555d9c18e154b0d0153faa7e0bbd6) fix(windows): create debug npipe failure
- [`5c6ea7fdc`](https://github.com/containerd/containerd/commit/5c6ea7fdc1247939edaddb1eba62a94527418687) Merge pull request [#5293](https://github.com/containerd/containerd/pull/5293) from wzshiming/fix/eveny-error-message
- [`2305f0504`](https://github.com/containerd/containerd/commit/2305f050452f411dc9fb2f582d1938423fe4edd3) Merge pull request [#5307](https://github.com/containerd/containerd/pull/5307) from maoyangLiu/fix-url
- [`abd4be07a`](https://github.com/containerd/containerd/commit/abd4be07acbb51c2b53e718a7b65f91873e634f4) fix the 404 url
- [`45df696bf`](https://github.com/containerd/containerd/commit/45df696bf3fe3eda15bbf0f2c00ddc2cfeddcdcc) Fix return event publishing error
- [`7648ad289`](https://github.com/containerd/containerd/commit/7648ad289b487bc3cf568d2a3bf3522648a1cb07) Merge pull request [#5300](https://github.com/containerd/containerd/pull/5300) from adisky/fix-toml
- [`3d20fa930`](https://github.com/containerd/containerd/commit/3d20fa93092b73d455217f8bf2a5f09cb134b3ec) fix TestSetOOMScoreBoundaries
- [`9e19a2984`](https://github.com/containerd/containerd/commit/9e19a2984778e02cd888e9e3056f5c0425e98849) Fix hosts test on Windows
- [`10a498c7c`](https://github.com/containerd/containerd/commit/10a498c7c8a3b9672aa733c2db83491191ad8b22) Update go-winio to fix compile error on armv7
- [`1a9c6f557`](https://github.com/containerd/containerd/commit/1a9c6f557bd163f959f99661bd95e193b4505291) Revendor zfs to to fix integer overflow
- [`181e2d421`](https://github.com/containerd/containerd/commit/181e2d4216a31a13ddd25d4f7489a56175fba053) Merge pull request [#5250](https://github.com/containerd/containerd/pull/5250) from dmcgowan/cri-fix-reference-ordering
- [`eb7c7c71e`](https://github.com/containerd/containerd/commit/eb7c7c71e21bdff485ba54666c12a72c0bd4792c) Fix oom tests on non Linux
- [`0886ceaea`](https://github.com/containerd/containerd/commit/0886ceaea2470edc7339dfc5ebe0e3257ae84d06) Fix reference ordering in CRI image store
- [`4e919ffab`](https://github.com/containerd/containerd/commit/4e919ffaba66e9134d8695d71bc46d1af9980371) Merge pull request [#5244](https://github.com/containerd/containerd/pull/5244) from pacoxu/fix/night-run
- [`01765d097`](https://github.com/containerd/containerd/commit/01765d097493c0893ee7d41cf11f9247843f9ab0) night ci fix: add packages for ubuntu 20.04
- [`56f17a085`](https://github.com/containerd/containerd/commit/56f17a08564aeb090e1cf731be186e9e86ae34b5) Merge pull request [#5148](https://github.com/containerd/containerd/pull/5148) from wzshiming/fix/defer-cleanup
- [`30e1e66e5`](https://github.com/containerd/containerd/commit/30e1e66e5cb11925d78bc7d6743b8789d8ac9baf) runtime/v2: Fix defer cleanup
- [`0d569f8f4`](https://github.com/containerd/containerd/commit/0d569f8f4a9b8a4a5702beb71ee707c3e9a727d0) Merge pull request [#5229](https://github.com/containerd/containerd/pull/5229) from wzshiming/fix/log-cp-file
- [`1410220d8`](https://github.com/containerd/containerd/commit/1410220d8fcd8b56180502cb7c5bf2dafc2ead4b) Fix error log when copy file
- [`fbf79545d`](https://github.com/containerd/containerd/commit/fbf79545dff6b07949bd567812154aba966ed548) Merge pull request [#5230](https://github.com/containerd/containerd/pull/5230) from wzshiming/fix/log-kill-shim
- [`fe787efa2`](https://github.com/containerd/containerd/commit/fe787efa2b708e67749b126715246b00da009468) Fix error log when kill shim
- [`969b3d638`](https://github.com/containerd/containerd/commit/969b3d638bbf5fe0296f7b80adda24838266e92e) Merge pull request [#5202](https://github.com/containerd/containerd/pull/5202) from wzshiming/fix/dgst-debug
- [`a0cc9b432`](https://github.com/containerd/containerd/commit/a0cc9b432d8e269f01d6c13ad1f6654bc6aee4ec) Merge pull request [#5195](https://github.com/containerd/containerd/pull/5195) from fuweid/fix-5173
- [`1a0973dde`](https://github.com/containerd/containerd/commit/1a0973dde31de3fa317a76ffb66c4e1d3a0bc92b) Merge pull request [#5206](https://github.com/containerd/containerd/pull/5206) from Iceber/fix-new-container
- [`b520428b5`](https://github.com/containerd/containerd/commit/b520428b5a4f6815bb66f6eb538e203ec2597935) Fix CRIU
- [`5e484c961`](https://github.com/containerd/containerd/commit/5e484c96139d2e4c93a277ff0c0caf815acb466f) runtime/v2/runc: fix the defer cleanup of the NewContainer
- [`fad66f94e`](https://github.com/containerd/containerd/commit/fad66f94ece37988604aff419a405f62656fef4e) Merge pull request [#5174](https://github.com/containerd/containerd/pull/5174) from fuweid/fix-5130
- [`5461fa3a7`](https://github.com/containerd/containerd/commit/5461fa3a754d47a32de293d7fdf553dfb05395a7) Merge pull request [#5196](https://github.com/containerd/containerd/pull/5196) from Iceber/fix-rootfs
- [`d895118c7`](https://github.com/containerd/containerd/commit/d895118c7c48b52a1d6cd0975fdef4ce4c854d43) runtime/v2/runc: fix leaking socket path
- [`4e8b2f309`](https://github.com/containerd/containerd/commit/4e8b2f309a3576f82e7cae1656a34b4a30721de9) rootfs: fix the error handling of the createInitLayer
- [`6b410ba41`](https://github.com/containerd/containerd/commit/6b410ba41ff28471134ca508665f89a10610eb7f) Merge pull request [#5197](https://github.com/containerd/containerd/pull/5197) from Iceber/fix-ctr-command
- [`06e6f45c3`](https://github.com/containerd/containerd/commit/06e6f45c3130463d9412d97eb0a639b346d0f86f) Merge pull request [#5198](https://github.com/containerd/containerd/pull/5198) from Iceber/fix-usage
- [`231bbdc37`](https://github.com/containerd/containerd/commit/231bbdc37950098926b5e41db8b134bd70f14a85) cmd/ctr: fix export command
- [`1fd99e24a`](https://github.com/containerd/containerd/commit/1fd99e24a2d8f3ceeb69c430775e2a23183e3f77) Fix docker style cert loading
- [`8cf669ce3`](https://github.com/containerd/containerd/commit/8cf669ce34d138038de78a67ed6408d1a097e5c9) Fix unsupported files exporting functions for apparmor and seccomp
- [`35eeb24a1`](https://github.com/containerd/containerd/commit/35eeb24a17cf205a8fd8706486b8db7322e06512) Fix exported comments enforcer in CI
- [`a5d17eb50`](https://github.com/containerd/containerd/commit/a5d17eb5071b3809a110ea43d7648eabaa05d603) Merge pull request [#5143](https://github.com/containerd/containerd/pull/5143) from kevpar/fix-lookpath
- [`c9afc4250`](https://github.com/containerd/containerd/commit/c9afc4250ab183f9e944297c15df705851b3ec42) Fix error checking when resolving shim binary path
- [`8e2072661`](https://github.com/containerd/containerd/commit/8e20726618b8d4e6446d969af7b390d9552c9e7e) Merge pull request [#5095](https://github.com/containerd/containerd/pull/5095) from dims/fix-pull-containerd-node-e2e-failure
- [`fa66f93c0`](https://github.com/containerd/containerd/commit/fa66f93c0c0c6400fbfc41592eeb89815a42fe88) Merge pull request [#5117](https://github.com/containerd/containerd/pull/5117) from Iceber/fix-container-status
- [`92ab1a63b`](https://github.com/containerd/containerd/commit/92ab1a63b044a1bfc0e08446e8c007bf7a42d466) cri: fix container status
- [`15a4df0ba`](https://github.com/containerd/containerd/commit/15a4df0ba9bc8a702e01398104f474b32eee3aa3) fix names and paths for containerd master
- [`10bbd1a46`](https://github.com/containerd/containerd/commit/10bbd1a462869c3ff9b6723fb3105b13fcd73a58) Merge pull request [#5051](https://github.com/containerd/containerd/pull/5051) from wzshiming/fix/missing-close
- [`46c974650`](https://github.com/containerd/containerd/commit/46c9746507b7fd279e4834df6ca40180da4e6c0c) Merge pull request [#5064](https://github.com/containerd/containerd/pull/5064) from Iceber/fix-redundant-slice
- [`c61f0cead`](https://github.com/containerd/containerd/commit/c61f0ceada66ea719e414f974b6469b0a91974c1) Fix broken docs links (#5085)
- [`f7f6aabff`](https://github.com/containerd/containerd/commit/f7f6aabfff3a682326fb9c07ab8a32a8bad6f86d) oci: fix superfluous slice operations
- [`224efa9da`](https://github.com/containerd/containerd/commit/224efa9daec5760b0944da8719056deb62c1bd28) Fixed wording in docs, and broken link
- [`af4c55fa4`](https://github.com/containerd/containerd/commit/af4c55fa4a2625937c200e6645285760a3e988b7) Merge pull request [#5078](https://github.com/containerd/containerd/pull/5078) from AkihiroSuda/fix-5077
- [`b4ef1e9dc`](https://github.com/containerd/containerd/commit/b4ef1e9dc7fe4e6681a113d2870a2f1236ba60f2) CI: fix "ls: cannot access '/etc/cni/net.d': Permission denied"
- [`9173d3e92`](https://github.com/containerd/containerd/commit/9173d3e929f844c0411d5d23a1e10cb004022475) Merge pull request [#5021](https://github.com/containerd/containerd/pull/5021) from wzshiming/fix/signal_repeatedly
- [`d30a6c005`](https://github.com/containerd/containerd/commit/d30a6c005fd3d196e8e2922a861a34b46523ee61) Merge pull request [#5045](https://github.com/containerd/containerd/pull/5045) from wzshiming/fix/file-not-closed
- [`5e4acc043`](https://github.com/containerd/containerd/commit/5e4acc04363a9097cc9a2f29d93fd062fca1652b) Fix file is not closed
- [`05ef2fe2f`](https://github.com/containerd/containerd/commit/05ef2fe2fbb8768fef65f5a7c435a83d04907d43) Fix missing close
- [`746cef0bc`](https://github.com/containerd/containerd/commit/746cef0bc2afe8b8c4592fec3df966138bdcedff) Merge pull request [#5044](https://github.com/containerd/containerd/pull/5044) from wzshiming/fix/empty-error-warpping
- [`59db8a10e`](https://github.com/containerd/containerd/commit/59db8a10e0c382ddba00090302b72d74a797f1e3) Fix empty error warpping
- [`80e1d98f6`](https://github.com/containerd/containerd/commit/80e1d98f6bfe6171f2289cb793edf141ca266e9e) fix: issue #5032
- [`dc6f5ef3b`](https://github.com/containerd/containerd/commit/dc6f5ef3b98c71ff8da3ed39193c5745eb9329e1) Fix repeated sending signal
- [`d08aa4b68`](https://github.com/containerd/containerd/commit/d08aa4b6811e517610d9db6d79ce81cf7deee080) oci: fix the file mode of the device
- [`e9e3b1d6f`](https://github.com/containerd/containerd/commit/e9e3b1d6fde0127c6f456ff17f09015f553cf9b2) Merge pull request [#5000](https://github.com/containerd/containerd/pull/5000) from kzys/fix-assert-check
- [`2ac33d79f`](https://github.com/containerd/containerd/commit/2ac33d79fee41270205f5f86c6757dde5ebb9600) test: fix assert.Check's argumets to show its parameters correctly
- [`ccde82da2`](https://github.com/containerd/containerd/commit/ccde82da2b46b0a4d4cf24576c2499288594df96) Merge pull request [#4987](https://github.com/containerd/containerd/pull/4987) from Random-Liu/fix-auth-config-conversion
- [`b5bf1fd5d`](https://github.com/containerd/containerd/commit/b5bf1fd5d87d8401b5da1317bffedad440a7de35) Fix deprecated registry auth conversion
- [`f07e1811e`](https://github.com/containerd/containerd/commit/f07e1811ef1ae2d6c0fda7dd47537746381ba46d) Merge pull request [#4988](https://github.com/containerd/containerd/pull/4988) from Iceber/fix-runc-v2-service
- [`b458583b7`](https://github.com/containerd/containerd/commit/b458583b76e84204dca17587625757247bb4053e) runtime: fix shutdown runc v2 service
- [`49c5c1487`](https://github.com/containerd/containerd/commit/49c5c1487951307761e84de52477d640c8b0c84c) Merge pull request [#4906](https://github.com/containerd/containerd/pull/4906) from payall4u/bugfix/fix-open-shim-fifo
- [`219fa3d0a`](https://github.com/containerd/containerd/commit/219fa3d0a5a1d3a86479f6d54aef2b94c1fdf9ea) cio.copyIO: fix pipes potentially not being closed (Windows)
- [`c35b4cfed`](https://github.com/containerd/containerd/commit/c35b4cfed520bf4827737f294f9292ffa73bdf8b) Merge pull request [#4955](https://github.com/containerd/containerd/pull/4955) from adisky/fix-doc
- [`d09bf1886`](https://github.com/containerd/containerd/commit/d09bf1886288d0a0cac3eae795c014178e39d723) Clean Up Doc and fix some broken links
- [`38604a76c`](https://github.com/containerd/containerd/commit/38604a76ca9b1a7c3e00eeeb92d2d3975c76e5d1) Merge pull request [#4933](https://github.com/containerd/containerd/pull/4933) from TBBle/fix-resolver-header-map-panic
- [`6bf565045`](https://github.com/containerd/containerd/commit/6bf5650450fa09fe065a6f9456cc12a4c28eccb2) Merge pull request [#4923](https://github.com/containerd/containerd/pull/4923) from fuweid/fix-wrong-context
- [`3e7bb721d`](https://github.com/containerd/containerd/commit/3e7bb721d412b6d93c0ab5dfd965bc6ff271a762) Fix typo in comment
- [`d64917403`](https://github.com/containerd/containerd/commit/d64917403767d81d7acd413ad26ee0620099db86) standard makefile,fix not work no macos
- [`178e9a101`](https://github.com/containerd/containerd/commit/178e9a10121b344aece9fe918f6fc4dc4dbde9a3) Merge pull request [#4866](https://github.com/containerd/containerd/pull/4866) from zhsj/doc-fix
- [`7fa02f3af`](https://github.com/containerd/containerd/commit/7fa02f3afb3d4014d108701c45630600e159a94f) Merge pull request [#4854](https://github.com/containerd/containerd/pull/4854) from tonistiigi/fix-push-auth
- [`da6860986`](https://github.com/containerd/containerd/commit/da686098668ec60eaca77dd82076044b5aad6698) Fix devmapper test
- [`071a18550`](https://github.com/containerd/containerd/commit/071a185506bd348e0f43e8f2b7936cf73bdebdeb) cri/config: fix range iterator issue in ValidatePluginConfig
- [`7126310a0`](https://github.com/containerd/containerd/commit/7126310a09500e1278f62fd1c12b31177a6434ff) Merge pull request [#4784](https://github.com/containerd/containerd/pull/4784) from fuweid/fix-4769
- [`819ac05f3`](https://github.com/containerd/containerd/commit/819ac05f34d7852955d911c281a1075660b941e7) Fix hcsshim commit detection
- [`553a36915`](https://github.com/containerd/containerd/commit/553a36915878d6bf9d215ed88be6d7453be2783b) Fix reference to vendor.conf in scripts
- [`b69f36aa1`](https://github.com/containerd/containerd/commit/b69f36aa13743d98dfe207e683dbbcafc0b530e4) Fix some typos and grammars
- [`b2420ebcd`](https://github.com/containerd/containerd/commit/b2420ebcd1c403d29cd700fdcc032cce07006260) Fix Windows service panic file to not be read-only
- [`ebc0ddb28`](https://github.com/containerd/containerd/commit/ebc0ddb28cd4ccc81ebf9cc14a6758e4d4aea2ae) Merge pull request [#4761](https://github.com/containerd/containerd/pull/4761) from zhsj/fix-cri-proto
- [`625da6b3e`](https://github.com/containerd/containerd/commit/625da6b3e6525d11cfa0234eb4cca8a3e103830f) Merge pull request [#4719](https://github.com/containerd/containerd/pull/4719) from estesp/fix-shm-relabel-test
- [`fe767f95c`](https://github.com/containerd/containerd/commit/fe767f95c7fb0f6b8e8e8edaa149648dd7b84752) Fix package name in cri runtimeoptions protobuf
- [`618c8bd77`](https://github.com/containerd/containerd/commit/618c8bd77260061b33474abe7fcc5d17d1a114e4) Merge pull request [#4745](https://github.com/containerd/containerd/pull/4745) from estesp/fix-actions-cve
- [`159fb2e7e`](https://github.com/containerd/containerd/commit/159fb2e7e248a1865e26d9db42f72e5dbe003cd9) Update other actions for env/path CVE fix
- [`bd7c6ca6f`](https://github.com/containerd/containerd/commit/bd7c6ca6fa95295c20d531001fe4758bd4560d3a) Fix integer overflow on windows
- [`6fb56aa58`](https://github.com/containerd/containerd/commit/6fb56aa58bb97d67ca823baa41a8aa03a2ae195f) Update btrfs vendor for chkptr fix for Go >= 1.14
- [`78ac7bac8`](https://github.com/containerd/containerd/commit/78ac7bac84bf4122675826ec799314a4018e955e) Merge pull request [#4725](https://github.com/containerd/containerd/pull/4725) from kzys/fix-links-in-docs
- [`03cc4cedc`](https://github.com/containerd/containerd/commit/03cc4cedc556f5da4236fdf117e66d7d1937c171) docs: fix broken links
- [`97cee75da`](https://github.com/containerd/containerd/commit/97cee75da80ffe8f8859dda0fe93b1b3e5630910) ctr: fix the incorrect image unmount error hint
- [`019148ef4`](https://github.com/containerd/containerd/commit/019148ef4c1bdc287191574dc607ff6e58d66a4f) bug fix:#3448
- [`b086062cf`](https://github.com/containerd/containerd/commit/b086062cfd913acf6905b169e2bba4387edcf617) httpReadSeeker: fix typo in error-message
- [`839b13699`](https://github.com/containerd/containerd/commit/839b13699209acc9b10c6fc8d4d793338ac799da) Merge pull request [#4656](https://github.com/containerd/containerd/pull/4656) from zhuangqh/fix-unknown-state
- [`30c9addd6`](https://github.com/containerd/containerd/commit/30c9addd6ca0052ed38d541ff88812c6152013a6) fix: always set unknown to false when handling exit event
- [`4da306e1e`](https://github.com/containerd/containerd/commit/4da306e1e98afd964ea39cb2ed8c6d0ee4d5cadd) Fix panic in shim not logged
- [`e4e05c6c0`](https://github.com/containerd/containerd/commit/e4e05c6c01ee697432cd5e157d06959955fe73cb) Merge pull request [#4625](https://github.com/containerd/containerd/pull/4625) from dcantah/fix-removesandbox-comment
- [`d74225b58`](https://github.com/containerd/containerd/commit/d74225b5882f1c06e2a9ed102187a4ed4931f6c5) Fix comment in RemovePodSandbox
- [`116902cd2`](https://github.com/containerd/containerd/commit/116902cd2189df59732a1788456f78effc381460) fix no-pivot not working in io.containerd.runtime.v1.linux
- [`f1a3235e8`](https://github.com/containerd/containerd/commit/f1a3235e8434e51f646a96c6c8ff344ffd23c4af) Fix typo in examples of registry config
- [`c59d1cd5b`](https://github.com/containerd/containerd/commit/c59d1cd5b069ed6a978675e6d835f57464c364a8) Fix linter issues
- [`de546a154`](https://github.com/containerd/containerd/commit/de546a154f84c3efbb1ad11c74dd53e14184719c) Merge pull request [#4605](https://github.com/containerd/containerd/pull/4605) from mxpv/nri-fix
- [`a0b3b4e4d`](https://github.com/containerd/containerd/commit/a0b3b4e4da2e7802927f67efc77feb5433882b0e) Merge pull request [#1593](https://github.com/containerd/containerd/pull/1593) from moolen/fix/add-nri-labels
- [`bc08a19f3`](https://github.com/containerd/containerd/commit/bc08a19f3a44bda9fd141e6ee4b8c6b369e17e6b) Merge pull request [#1595](https://github.com/containerd/containerd/pull/1595) from dmcgowan/fix-unix-lint
- [`07c98d0bf`](https://github.com/containerd/containerd/commit/07c98d0bf1c27a6e57c2311a81f5e9e0d0db6f48) Fix lint in Unix environments
- [`d85278670`](https://github.com/containerd/containerd/commit/d8527867057daa93c17423ec7cd3438696b1c899) Merge pull request [#4599](https://github.com/containerd/containerd/pull/4599) from estesp/fix-script-var
- [`c178043f6`](https://github.com/containerd/containerd/commit/c178043f6b68cf024554aba7af4373e5cb1dac63) Merge pull request [#1584](https://github.com/containerd/containerd/pull/1584) from containerd/revert-1530-fix-doc-for-runtime-options
- [`0762fdd9e`](https://github.com/containerd/containerd/commit/0762fdd9e282c64a74fdd2d19489199cc62c9094) Revert "Fix doc for runtime specific options"
- [`5d7aa0cb6`](https://github.com/containerd/containerd/commit/5d7aa0cb6543db4750e62d90c98ab182e0e882ef) Merge pull request [#4549](https://github.com/containerd/containerd/pull/4549) from ukontainer/fix-missing-sha256
- [`f4741fb8c`](https://github.com/containerd/containerd/commit/f4741fb8c5c210565308c59836ca6e808cfbc9f3) fix `make test` failure of missing sha256 package
- [`ab5d93187`](https://github.com/containerd/containerd/commit/ab5d93187c224d66ce3d5486aff75dd7084a1274) cr: fix checkpoint from image getting skipped
- [`469b63735`](https://github.com/containerd/containerd/commit/469b637358b6202dedebdeebed32b4487ab9b1db) Fix ctr command typo
- [`c8523cc5b`](https://github.com/containerd/containerd/commit/c8523cc5bbce500eca3ec25369d8dcee1116f5d5) Merge pull request [#4470](https://github.com/containerd/containerd/pull/4470) from AkihiroSuda/fix-static-plugin
- [`412378ff0`](https://github.com/containerd/containerd/commit/412378ff021bd92f6f80db4d55a746878827afd5) Merge pull request [#4437](https://github.com/containerd/containerd/pull/4437) from kzys/fix-rollback
- [`a1f6c9dd8`](https://github.com/containerd/containerd/commit/a1f6c9dd881ec2205cac54a7296557e39cba826a) snapshots/devmapper: fix rollback
- [`43cbdf89e`](https://github.com/containerd/containerd/commit/43cbdf89e9142b9b8cb54fb0932e4c7a45f1daeb) BUILDING.md: fix description about static builds
- [`4c8164bcc`](https://github.com/containerd/containerd/commit/4c8164bccf35b134ad9864409882105ade5b3c85) Specify version = 2 & fix wrong key in registry.md (GCR example)
- [`a01750d89`](https://github.com/containerd/containerd/commit/a01750d89af991c37906165f8d6f68ceb5903730) Merge pull request [#1530](https://github.com/containerd/containerd/pull/1530) from hckuo/fix-doc-for-runtime-options
- [`904ab30f9`](https://github.com/containerd/containerd/commit/904ab30f9dc3bc33974daca112b7024609417436) Fix doc for runtime specifc options
- [`1bc5ba3f4`](https://github.com/containerd/containerd/commit/1bc5ba3f484ecae7feb3156ad0e3760b728de66e) Merge pull request [#1519](https://github.com/containerd/containerd/pull/1519) from AkihiroSuda/config-fix-toml-tag
- [`b69d7bdc5`](https://github.com/containerd/containerd/commit/b69d7bdc5fa9f61532819029c864cd3724a79db6) config: fix TOML tag for TolerateMissingHugePagesCgroupController
- [`8e0b789c9`](https://github.com/containerd/containerd/commit/8e0b789c9ade07497283546c0bde0fb5f99310cb) Merge pull request [#1520](https://github.com/containerd/containerd/pull/1520) from AkihiroSuda/fix-ci-apt-get-update
- [`682d15839`](https://github.com/containerd/containerd/commit/682d158399ed7c58c1bc8dd4f5282c4446c0aba3) Merge pull request [#1517](https://github.com/containerd/containerd/pull/1517) from mikebrow/fix-e2e-bucket
- [`f5c7ac927`](https://github.com/containerd/containerd/commit/f5c7ac92724405806eb4e330ecab8f4350601089) fix for image pull linter change
- [`098e04001`](https://github.com/containerd/containerd/commit/098e040014aa8e413c7419f7e6db1db51e7133ff) Fix typo
- [`e56347aab`](https://github.com/containerd/containerd/commit/e56347aabc6b5b26aaf6033826e791d1f3b43ab4) move up to latest critools pick up nginx fix
- [`17c61e36c`](https://github.com/containerd/containerd/commit/17c61e36cb5ed6ee59d27074e6be7e08663646fa) Fix cgroups path for base OCI spec
- [`e10e07b50`](https://github.com/containerd/containerd/commit/e10e07b50e6de4a553648206d4ba7d2e97795fdf) Merge pull request [#1489](https://github.com/containerd/containerd/pull/1489) from mikebrow/ltag-scan-symlink-fixed
- [`e2cedb946`](https://github.com/containerd/containerd/commit/e2cedb9469c03fb78837e3783775633b426dc01a) Increase port-forward timeout to 1s to fix e2e test
- [`cdac4dece`](https://github.com/containerd/containerd/commit/cdac4dece47e822afa83c78c890942d5cdb7715e) vendor: update go-events to fix alignment for 32bit systems
- [`414701057`](https://github.com/containerd/containerd/commit/41470105749546b2f9d2c67dff7f4c519fd37d79) Merge pull request [#1457](https://github.com/containerd/containerd/pull/1457) from hickeyma/fix-docs
- [`98f8ec499`](https://github.com/containerd/containerd/commit/98f8ec4995d688db3d62d265f298d3183e3d49f9) fix incomplete host device for PrivilegedWithoutHostDevices
- [`befc70b44`](https://github.com/containerd/containerd/commit/befc70b444e24eaa76b3ef18633e9fba64d5e795) Merge pull request [#1456](https://github.com/containerd/containerd/pull/1456) from mikebrow/fix-deprecated-greeting
- [`2b162b6c1`](https://github.com/containerd/containerd/commit/2b162b6c11ca02c6f4fdb4dd075a0b4cbb07cf4e) update selinux dependency to fix test failures
- [`3d250b828`](https://github.com/containerd/containerd/commit/3d250b8289d3dbb6c4551c78e8da9a4ede1f0474) Merge pull request [#1439](https://github.com/containerd/containerd/pull/1439) from mikebrow/fix-selinux-unit-test
- [`aa9b1885b`](https://github.com/containerd/containerd/commit/aa9b1885b58cc22081d48e6cd2e4cbceca132c77) fixes bad unit tests when selinux is enabled
- [`27d4fd597`](https://github.com/containerd/containerd/commit/27d4fd5979ef38c893147774e9801bb31d66d123) Merge pull request [#1425](https://github.com/containerd/containerd/pull/1425) from dims/fix-x/sys-dependency-version
- [`cb0140063`](https://github.com/containerd/containerd/commit/cb0140063e26eb56e937c2d4fae9d18216b8a80d) Fix goroutine leak when exec/attach
- [`c44ad801f`](https://github.com/containerd/containerd/commit/c44ad801f9e8fa4f2ba566dbdcda8a3a1c568475) Fixed merge conflicts
- [`a8cc66b37`](https://github.com/containerd/containerd/commit/a8cc66b37adc95aa9ef58cc859456399cfed87af) Fix store error serialization to gRPC status codes
- [`83a9d2460`](https://github.com/containerd/containerd/commit/83a9d2460c5fdd4843141386e3b3b462a137f51c) Merge pull request [#1363](https://github.com/containerd/containerd/pull/1363) from Random-Liu/fix-validate-config
- [`0c2d3b718`](https://github.com/containerd/containerd/commit/0c2d3b718d473157c0e97ebc4e8b217332c1358a) Fix privileged devices
- [`40e147cb7`](https://github.com/containerd/containerd/commit/40e147cb737335c43e3494c954952141627e9657) Merge pull request [#1347](https://github.com/containerd/containerd/pull/1347) from Random-Liu/fix-typo
- [`4f350ad47`](https://github.com/containerd/containerd/commit/4f350ad474c8f21bcc0ad704d4ba7ff9052476f8) Fix typo
- [`9f79be1b8`](https://github.com/containerd/containerd/commit/9f79be1b887af3df40f1e807ad2a1aedf0b931ad) Merge pull request [#1331](https://github.com/containerd/containerd/pull/1331) from erikwilson/fix-http-localhost
- [`fe757946c`](https://github.com/containerd/containerd/commit/fe757946cabdc36ac62bbfac7c888d37d57ab935) Merge pull request [#1319](https://github.com/containerd/containerd/pull/1319) from Random-Liu/fix-containerd-build
- [`8bfff7dbd`](https://github.com/containerd/containerd/commit/8bfff7dbd2c3e594bfb13b82f48ccc7c1971e5a4) Fix containerd build, use `libbtrfs-dev` when available
- [`2a9a982ae`](https://github.com/containerd/containerd/commit/2a9a982ae36cb0d4186b1e19259c990c62e29f6c) Fix integration test for golang 1.13
- [`10f88f99c`](https://github.com/containerd/containerd/commit/10f88f99cceabad292d1e5bd4a15cd2e6ca29b55) Fix appveyor test
- [`a1e4f99a3`](https://github.com/containerd/containerd/commit/a1e4f99a321435cb55cdbedd066d0e2419a6ee9c) Merge pull request [#1296](https://github.com/containerd/containerd/pull/1296) from Random-Liu/fix-ssh-disconnect
- [`0a6d9f188`](https://github.com/containerd/containerd/commit/0a6d9f188b06901b1e6778efa087a5f1a07d4875) Merge pull request [#1291](https://github.com/containerd/containerd/pull/1291) from Random-Liu/fix-indent-cni
- [`b4c46db79`](https://github.com/containerd/containerd/commit/b4c46db790f828e931da22b0d831dd83de92d3bc) Fix indent in cni.template
- [`161abf8f5`](https://github.com/containerd/containerd/commit/161abf8f5b5700dd838f23bbfd6520e893a70126) Fix golangci-lint findings
- [`7b606375a`](https://github.com/containerd/containerd/commit/7b606375ae4997112246c4cf237c0056c5b41aa3) Merge pull request [#1259](https://github.com/containerd/containerd/pull/1259) from Random-Liu/fix-potential-panic-for-unknown-state
- [`c6203ec13`](https://github.com/containerd/containerd/commit/c6203ec13bfd2cbe3cbed43f1622d27737d583cd) Fix panic for task in unknown state
- [`b5ec5ee4f`](https://github.com/containerd/containerd/commit/b5ec5ee4f63e2fee693eacc716d754385bbfe485) Merge pull request [#1255](https://github.com/containerd/containerd/pull/1255) from Random-Liu/fix-doc
- [`0997453f3`](https://github.com/containerd/containerd/commit/0997453f33fb1c46f8322820adc5c892b7490f52) Update cri-tools to fix all image reference test failure
- [`f41675d23`](https://github.com/containerd/containerd/commit/f41675d234bb8212457ea04eae5d47dc3606bf6b) fix: support empty auth config for anonymous registry
- [`eed395668`](https://github.com/containerd/containerd/commit/eed3956689afc616d8b9e1e74d1259e0bfc1ca12) Merge pull request [#1240](https://github.com/containerd/containerd/pull/1240) from Random-Liu/fix-apparmor-privileged
- [`10acd8e76`](https://github.com/containerd/containerd/commit/10acd8e7699d2014057e57bed9a7648c8097eb0e) Fix apparmor for privileged
- [`a4b145adb`](https://github.com/containerd/containerd/commit/a4b145adbbf45c2b61d4753620d322ccd39752c4) Merge pull request [#1234](https://github.com/containerd/containerd/pull/1234) from Random-Liu/update-containerd-to-fix-race
- [`7f330dc4a`](https://github.com/containerd/containerd/commit/7f330dc4aa4bd6b2b051f45209c480d0899a5e42) Update containerd to fix panic caused by race condition
- [`fe5eb76cb`](https://github.com/containerd/containerd/commit/fe5eb76cb488e186584bbe923d61099d2c4b0f28) Merge pull request [#1209](https://github.com/containerd/containerd/pull/1209) from Random-Liu/fix-proc-mount-support
- [`467f9e0e8`](https://github.com/containerd/containerd/commit/467f9e0e8a10097b793726bf89aeaa661a2e4007) Fix proc mount support
- [`5fdb4b8ee`](https://github.com/containerd/containerd/commit/5fdb4b8eefae630401832c2fa30ef326de7ddfb9) Merge pull request [#1204](https://github.com/containerd/containerd/pull/1204) from Random-Liu/fix-ctr-readiness-check
- [`e83fe5607`](https://github.com/containerd/containerd/commit/e83fe56075ed1a0727a88fc33c24710b07dd14cf) Fix ctr readiness check in test
- [`64bf4bebf`](https://github.com/containerd/containerd/commit/64bf4bebf31cc155bcce456095ac92671583a2e8) Merge pull request [#1188](https://github.com/containerd/containerd/pull/1188) from alculquicondor/fix/doc
- [`eaf792ed7`](https://github.com/containerd/containerd/commit/eaf792ed7bcbd406cbfee45e119c52f4b10290d8) Merge pull request [#1180](https://github.com/containerd/containerd/pull/1180) from Random-Liu/fix-version
- [`6afd137c0`](https://github.com/containerd/containerd/commit/6afd137c026ee2133dddb22bc9a8d405852df674) Fix runc and critools version in release
- [`806c2641a`](https://github.com/containerd/containerd/commit/806c2641a1945db654964f901165ed6e7719cf51) Merge pull request [#1178](https://github.com/containerd/containerd/pull/1178) from mikebrow/fix-slack-link
- [`55e5ce0e9`](https://github.com/containerd/containerd/commit/55e5ce0e951ee4675af88fe0c0f3cdccd5253fd1) Fix http client when TLS is enabled
- [`1275d6ded`](https://github.com/containerd/containerd/commit/1275d6ded393fd0582842c5996199451d2642303) Merge pull request [#1162](https://github.com/containerd/containerd/pull/1162) from Random-Liu/fix-image-pull
- [`1c826eb68`](https://github.com/containerd/containerd/commit/1c826eb6892d3bcc2ed04360f8cffd7dd6548b4f) Merge pull request [#1165](https://github.com/containerd/containerd/pull/1165) from ZYecho/fix-link
- [`397adbab8`](https://github.com/containerd/containerd/commit/397adbab859bcc2750734d845f64f36962e57353) fix: fix CRI dead link
- [`8ba5c02f8`](https://github.com/containerd/containerd/commit/8ba5c02f8f249c1f6edb5e34ff99bd43cf49a92b) Fix typo in WithoutRunMount
- [`47fc64568`](https://github.com/containerd/containerd/commit/47fc6456827e9424530fa39d58d8d3debcc84b6a) Integration test task.Delete fix
- [`fa759f6a1`](https://github.com/containerd/containerd/commit/fa759f6a1b93d4d6a3a09c7e6235e2b90996f8d1) Merge pull request [#1130](https://github.com/containerd/containerd/pull/1130) from Random-Liu/fix-status-hang
- [`63ad4c730`](https://github.com/containerd/containerd/commit/63ad4c7305576d96477ef779b0d8a5cfb87554d3) Merge pull request [#1114](https://github.com/containerd/containerd/pull/1114) from Random-Liu/fix-extra-handler
- [`b23b406fe`](https://github.com/containerd/containerd/commit/b23b406fedd2009f813c36206865ae2a8c51d5bb) Merge pull request [#1102](https://github.com/containerd/containerd/pull/1102) from Random-Liu/uts-namespace-and-fix-array
- [`3691cb655`](https://github.com/containerd/containerd/commit/3691cb6550c6eee1fb9957681b00e986b7a5d288) Fix /etc/hostname backward compatibility issue for in-place upgrade
- [`8d7526119`](https://github.com/containerd/containerd/commit/8d75261190509c46a4ff86a8cc91401e71143487) Merge pull request [#1065](https://github.com/containerd/containerd/pull/1065) from alculquicondor/fix/architecture
- [`c88e18b90`](https://github.com/containerd/containerd/commit/c88e18b907f10ce10aa395631d80fd7ec41d36f3) Fix architecture doc
- [`b2cd84004`](https://github.com/containerd/containerd/commit/b2cd840042d843e110625b5fd38db68b549377be) Merge pull request [#1045](https://github.com/containerd/containerd/pull/1045) from Random-Liu/fix-env-performance-issue
- [`97c7a1b17`](https://github.com/containerd/containerd/commit/97c7a1b17b8198f242db429072ec1306cbca209a) Merge pull request [#1027](https://github.com/containerd/containerd/pull/1027) from Random-Liu/fix-log-ending-newline
- [`556b21945`](https://github.com/containerd/containerd/commit/556b2194501d51e18ae6dd870a8579a56509b81f) Fix lint error
- [`50ac40097`](https://github.com/containerd/containerd/commit/50ac40097ee458f07aaeab97dadbf80b4fcddbc7) Fix the log ending newline handling
- [`ae1b7ac4f`](https://github.com/containerd/containerd/commit/ae1b7ac4fd8e4b5707b90b14bbf28b1159ff07c0) Fix some typos in comment
- [`3bfef0158`](https://github.com/containerd/containerd/commit/3bfef0158951049d96716814f99d4c79b02053c7) Fix the issue that pod or container config file without metadata will crash containerd
- [`55fb3b9fc`](https://github.com/containerd/containerd/commit/55fb3b9fce4cf3ff1bf0011d273eed9c0d7e8b1f) Fix return error message
- [`a9f3c86cc`](https://github.com/containerd/containerd/commit/a9f3c86cc12f7dd484b726919729accf9b5d1171) Merge pull request [#1004](https://github.com/containerd/containerd/pull/1004) from Random-Liu/fix-build
- [`5d5fc154a`](https://github.com/containerd/containerd/commit/5d5fc154ad6f36aa39cafd389653a84ba19d31d4) Revert "Temporary fix for golang regression #29241."
- [`afb12d728`](https://github.com/containerd/containerd/commit/afb12d728ce51d2b29ebdbf659e53fcc275045ff) Merge pull request [#997](https://github.com/containerd/containerd/pull/997) from Random-Liu/fix-for-golang-issue
- [`d7f6721de`](https://github.com/containerd/containerd/commit/d7f6721de591f9a46ebfdc8ed8de83a71d80743c) Temporary fix for golang regression #29241
- [`d53bcba99`](https://github.com/containerd/containerd/commit/d53bcba99149b25a5b46365e06852cbc97e5556c) Fix some typo errors
- [`37085692e`](https://github.com/containerd/containerd/commit/37085692e28a7584967374f085e2b94c16b54869) fix spelling error: contaner -> container
- [`f58105a71`](https://github.com/containerd/containerd/commit/f58105a71c92cd68e68e731dd9ebf9b7e85b91ce) Merge pull request [#983](https://github.com/containerd/containerd/pull/983) from Random-Liu/fix-shared-pid-ns-kill
- [`de967051d`](https://github.com/containerd/containerd/commit/de967051d488d415f7c2b66b4fd89cf2467536a9) Fix kill when shared pid namespace
- [`64b067d93`](https://github.com/containerd/containerd/commit/64b067d93fab68368be7dd58f1e13a1d1215c6ad) fix integration test
- [`728f636e3`](https://github.com/containerd/containerd/commit/728f636e32c97ea9c67dc9a654eaf19d2de0b801) Merge pull request [#949](https://github.com/containerd/containerd/pull/949) from Random-Liu/fix-ip-leakage
- [`8b0d53c09`](https://github.com/containerd/containerd/commit/8b0d53c09c41d9fbc3b3896548ecf011518e3c42) Merge pull request [#941](https://github.com/containerd/containerd/pull/941) from amshinde/fix-go-compile-error
- [`54b1c00b3`](https://github.com/containerd/containerd/commit/54b1c00b3b307b0fadd10c02d9467a6545c2c4d5) test: Fix compile error with go1.10.2
- [`801882b04`](https://github.com/containerd/containerd/commit/801882b046562ed1cf0299c8e4130e3f0865dcc6) Merge pull request [#935](https://github.com/containerd/containerd/pull/935) from mikebrow/makefile-fix-for-syntax
- [`6de38f1f3`](https://github.com/containerd/containerd/commit/6de38f1f3ab99b96b9bbf1723084a658dc676002) Merge pull request [#927](https://github.com/containerd/containerd/pull/927) from Random-Liu/fix-readiness-check
- [`68152dab8`](https://github.com/containerd/containerd/commit/68152dab84f403f9789e3e80c4aed9c186ee63e6) Fix readiness check in test utils
- [`d963c9c58`](https://github.com/containerd/containerd/commit/d963c9c58eb4cde524278919310fb066cfd2931c) Merge pull request [#920](https://github.com/containerd/containerd/pull/920) from Random-Liu/fix-indent
- [`e402ae2f0`](https://github.com/containerd/containerd/commit/e402ae2f027e28a86acfc33a9bd151902f5d5dbf) Merge pull request [#914](https://github.com/containerd/containerd/pull/914) from Random-Liu/fix-addition-gids
- [`ca3b806b5`](https://github.com/containerd/containerd/commit/ca3b806b5cb960e3d2de034434fe65ac7bc43793) Fix addition group ids
- [`ed68cfd54`](https://github.com/containerd/containerd/commit/ed68cfd543808f8f46142ab2f2ec866c7b505041) Merge pull request [#901](https://github.com/containerd/containerd/pull/901) from Random-Liu/fix-hostname-env
- [`f08a90ff6`](https://github.com/containerd/containerd/commit/f08a90ff64477116953de523188611c814462174) Fix hostname env
- [`db8500d10`](https://github.com/containerd/containerd/commit/db8500d10c38b3c6ef9464d7550e17abd9e32f5a) Merge pull request [#892](https://github.com/containerd/containerd/pull/892) from Random-Liu/fix-volume-mount-order
- [`bca304ff3`](https://github.com/containerd/containerd/commit/bca304ff3e1a52a58bf5c0564affbca35ff278bc) Fix an issue that container/sandbox can't be stopped
- [`c68b60514`](https://github.com/containerd/containerd/commit/c68b60514edb386fb9ad0bbd37bf56c6a90ea03c) Merge pull request [#831](https://github.com/containerd/containerd/pull/831) from Random-Liu/fix-link
- [`fd71c9f06`](https://github.com/containerd/containerd/commit/fd71c9f065cc72b6dfa6ee054621a1b888fc2e39) Fix another link
- [`47b8d30bb`](https://github.com/containerd/containerd/commit/47b8d30bb34547f7c597ed52ed118ed0371a0a2b) Merge pull request [#828](https://github.com/containerd/containerd/pull/828) from yujuhong/fix-gce-link
- [`e23c0e708`](https://github.com/containerd/containerd/commit/e23c0e708a3d60e72753949fd8a4a3b7adad0c5e) Fix link to GCE getting started guide
- [`860971025`](https://github.com/containerd/containerd/commit/860971025f1ad628f773b405446776f0e074cf68) vendoring latest go-cni with fixes
- [`441a57aa5`](https://github.com/containerd/containerd/commit/441a57aa56f26edbed328a20bc4eee61e66a8e34) Merge pull request [#821](https://github.com/containerd/containerd/pull/821) from Random-Liu/fix-snapshotter-panic
- [`b60e456bd`](https://github.com/containerd/containerd/commit/b60e456bd9913261956b664c9a34463884edce58) Fix snapshotter nil panic
- [`ad2937013`](https://github.com/containerd/containerd/commit/ad29370136777b4a471afbde280637ad121cab74) Merge pull request [#816](https://github.com/containerd/containerd/pull/816) from Random-Liu/fix-double-dev-shm-mount
- [`53f1ab414`](https://github.com/containerd/containerd/commit/53f1ab41458de4fa91f40f4cbe034aa3442ca1b8) Fix double /dev/shm mount
- [`b7aac6396`](https://github.com/containerd/containerd/commit/b7aac6396d76282304abe1c25b0e521004ed7fc2) Merge pull request [#811](https://github.com/containerd/containerd/pull/811) from Random-Liu/fix-volume-ownership
- [`c55776377`](https://github.com/containerd/containerd/commit/c55776377fd288bbca3e716056071f67909399c2) Fix empty volume ownership
- [`8bcb9a953`](https://github.com/containerd/containerd/commit/8bcb9a95394e8d7845da1d6a994d3ac2a86d22f0) Merge pull request [#801](https://github.com/containerd/containerd/pull/801) from Random-Liu/fix-ctr-timeout
- [`0faff1c22`](https://github.com/containerd/containerd/commit/0faff1c22fbc36cf3c12cfc9347b210e06845e24) Fix ctr cri timeout
- [`b68fb075d`](https://github.com/containerd/containerd/commit/b68fb075d49aa1c2885f45f2467142666c244f4a) Merge pull request [#793](https://github.com/containerd/containerd/pull/793) from Random-Liu/port-containerd-fix-#2364
- [`0fae42b9b`](https://github.com/containerd/containerd/commit/0fae42b9b8571df61acd474b4367a6f8f1db83d0) Port docker resolver fix #2364
- [`fb6bc66f0`](https://github.com/containerd/containerd/commit/fb6bc66f0aa04161b9c95727865c31ae01dad081) Bump continuity to fix copy files > 2^32 bytes
- [`a4ff7e994`](https://github.com/containerd/containerd/commit/a4ff7e9946eed21a650d68d790d6bdbfd7721aab) Merge pull request [#781](https://github.com/containerd/containerd/pull/781) from Random-Liu/fix-container-runtime-monitor
- [`ebed87fa9`](https://github.com/containerd/containerd/commit/ebed87fa951ad2b59dba8ed35b3cad570c1f3628) Fix kube-container-runtime-monitor
- [`927d37401`](https://github.com/containerd/containerd/commit/927d37401dc4b8a9f2dfc73eb6c085ae3c0e7ac2) Merge pull request [#779](https://github.com/containerd/containerd/pull/779) from Random-Liu/logo-fix
- [`6c7ec48da`](https://github.com/containerd/containerd/commit/6c7ec48daf08d0e496111cf7903a8b7c784a4fbe) Another logo fix
- [`66388aefd`](https://github.com/containerd/containerd/commit/66388aefd5f63bcd000e8e19eee32dd1495ca7a1) Merge pull request [#766](https://github.com/containerd/containerd/pull/766) from Random-Liu/fix-workingset-memory
- [`5d29598a6`](https://github.com/containerd/containerd/commit/5d29598a6d5db2405befb15c83c7f95cd42ae5fe) Fix workingset memory calculation
- [`7a6369deb`](https://github.com/containerd/containerd/commit/7a6369deb195336463ca60f82cdfbe2d49bc7edf) Merge pull request [#763](https://github.com/containerd/containerd/pull/763) from Random-Liu/fix-ro-sysfs
- [`2f370f6f5`](https://github.com/containerd/containerd/commit/2f370f6f5d246fcf5be242dfb8a288110b0d5117) Update cri-tools to fix `crictl logs` output
- [`8fec0469d`](https://github.com/containerd/containerd/commit/8fec0469d9cd0e3ae1692ece8840e6abea1b3fe0) Merge pull request [#751](https://github.com/containerd/containerd/pull/751) from Random-Liu/fix-official-release
- [`e0d707825`](https://github.com/containerd/containerd/commit/e0d70782516ccb24703a83fccfaa1848d3923f58) Fix tarball ownership and containerd binary path for containerd
- [`59d7112bf`](https://github.com/containerd/containerd/commit/59d7112bf9d175331197c709eb92e9189e3e1e6b) Merge pull request [#747](https://github.com/containerd/containerd/pull/747) from Random-Liu/fix-fluentd-support
- [`b3d15cf19`](https://github.com/containerd/containerd/commit/b3d15cf192b221b6568bda3e0a8d7fbe513c13e6) Add KUBE_CONTAINER_RUNTIME_NAME to fix fluentd support
- [`daa9f6008`](https://github.com/containerd/containerd/commit/daa9f6008ca89019543c53159eb768ccbadc98a7) Merge pull request [#743](https://github.com/containerd/containerd/pull/743) from Random-Liu/fix-sandbox-stop-race
- [`856534c84`](https://github.com/containerd/containerd/commit/856534c84603f8e2f8df090b84a025b0c47c9cc1) Fix sandbox stop race condition
- [`290eec8e3`](https://github.com/containerd/containerd/commit/290eec8e348f5fae6ee765062006e757be16825f) Merge pull request [#739](https://github.com/containerd/containerd/pull/739) from Random-Liu/fix-hostnet-port-forward
- [`5cb4744f2`](https://github.com/containerd/containerd/commit/5cb4744f27c6f6a1af0f138aafb9267e2375948d) Fix portforward for host network
- [`77a33b10a`](https://github.com/containerd/containerd/commit/77a33b10a995c1dcc2e5911320189ef97d55efe9) Merge pull request [#729](https://github.com/containerd/containerd/pull/729) from Random-Liu/fix-portforward
- [`b09489de9`](https://github.com/containerd/containerd/commit/b09489de96fd1870c70190dd2a18334038621aae) Merge pull request [#727](https://github.com/containerd/containerd/pull/727) from Random-Liu/fix-symlink-layer
- [`304045491`](https://github.com/containerd/containerd/commit/304045491c76f9c9aa2f073e861066d76bbfc099) Merge pull request [#725](https://github.com/containerd/containerd/pull/725) from Random-Liu/fix-resolver-race
- [`a68530c1e`](https://github.com/containerd/containerd/commit/a68530c1e895a553f4a03a70807688baaede0e63) Port containerd fix #2276
- [`f99f0be5a`](https://github.com/containerd/containerd/commit/f99f0be5ae51911dfdcef6b3e7be83c83ac02768) Merge pull request [#707](https://github.com/containerd/containerd/pull/707) from Random-Liu/fix-log-output
- [`be43ad09d`](https://github.com/containerd/containerd/commit/be43ad09da8c695fc5925e74e722f0103769bf2d) Fix a log output
- [`896e34700`](https://github.com/containerd/containerd/commit/896e347000d8ca6c2f4374b056422b2943f1be75) Merge pull request [#701](https://github.com/containerd/containerd/pull/701) from Random-Liu/fix-event-monitor-panic
- [`277edb2d3`](https://github.com/containerd/containerd/commit/277edb2d3be5625bc8de7145d8c4e0bf71c6c9d3) Fix event monitor panic
- [`7f959b6dd`](https://github.com/containerd/containerd/commit/7f959b6dd5c0cf43c6ff86524ad7b476ac81d03b) Merge pull request [#684](https://github.com/containerd/containerd/pull/684) from Random-Liu/fix-kube-up-and-docs
- [`904938fa9`](https://github.com/containerd/containerd/commit/904938fa9da5769a9a760f4c477dadab81a41747) Fix for kube-up.sh and update several documments
- [`9afdd1956`](https://github.com/containerd/containerd/commit/9afdd1956ba6c694dcf4564c1f7fec690b51d07a) Merge pull request [#680](https://github.com/containerd/containerd/pull/680) from Random-Liu/fix-containerd-test
- [`916e99d0a`](https://github.com/containerd/containerd/commit/916e99d0adfc5a6f59ec3a312e2e40986ee8a32c) Merge pull request [#675](https://github.com/containerd/containerd/pull/675) from Random-Liu/fix-containerd-repo-test
- [`524177e3e`](https://github.com/containerd/containerd/commit/524177e3efa9fdfc64136e04dfd5ef37a65c25ad) Fix containerd repo test
- [`1f28f8d2f`](https://github.com/containerd/containerd/commit/1f28f8d2fe420eeaedaca9cb2941dba35c8a9c2b) Merge pull request [#650](https://github.com/containerd/containerd/pull/650) from Random-Liu/fix-resolver
- [`5b3895932`](https://github.com/containerd/containerd/commit/5b3895932ff1d6ceadcb1ad083a4751c861ecbcf) Merge pull request [#648](https://github.com/containerd/containerd/pull/648) from Random-Liu/fix-context
- [`f01c6d73a`](https://github.com/containerd/containerd/commit/f01c6d73a6f09c14b6d3668704576702feb58c09) Fix cleanup context
- [`ffda916fd`](https://github.com/containerd/containerd/commit/ffda916fd04dbbaf28de35060929586b89ef2a3b) Merge pull request [#641](https://github.com/containerd/containerd/pull/641) from Random-Liu/fix-ansible-doc
- [`ceb540d82`](https://github.com/containerd/containerd/commit/ceb540d8231f102cc14ef311f98188b5cfebf123) Fix potential panic
- [`64b098a29`](https://github.com/containerd/containerd/commit/64b098a293831f742aeb3dd3e48a5405990c14c5) Merge pull request [#636](https://github.com/containerd/containerd/pull/636) from Random-Liu/fix-default-config
- [`f8fa536ff`](https://github.com/containerd/containerd/commit/f8fa536ff7478b4cdf85bf37d5f605dbe5b916a0) Merge pull request [#635](https://github.com/containerd/containerd/pull/635) from mikebrow/travis-golang-fix
- [`8364abc0f`](https://github.com/containerd/containerd/commit/8364abc0f314f645e63901bbb5b81cb23ed4d099) fix travis golang issue
- [`e43def70c`](https://github.com/containerd/containerd/commit/e43def70c1b1c049d512f8f7a0691f7feb62cf92) Fix travis test
- [`c9081b2ec`](https://github.com/containerd/containerd/commit/c9081b2ec0eefc799f0f1caabbea29d516c72c44) Merge pull request [#617](https://github.com/containerd/containerd/pull/617) from Random-Liu/fix-potential-panic
- [`f5390d01d`](https://github.com/containerd/containerd/commit/f5390d01d63892be5aead028ee13e8de18eca755) Fix a potential panic
- [`460eed77e`](https://github.com/containerd/containerd/commit/460eed77efa9805c6339ec11b02ca0708aff0950) Merge pull request [#611](https://github.com/containerd/containerd/pull/611) from Random-Liu/fix-shutdown
- [`4dec15641`](https://github.com/containerd/containerd/commit/4dec1564186f663ef399528b4732c50be15d770f) Merge pull request [#604](https://github.com/containerd/containerd/pull/604) from Random-Liu/fix-kube-up-env
- [`f4625ef76`](https://github.com/containerd/containerd/commit/f4625ef76c5294fae613b9ea9ad80a36a451295c) Merge pull request [#593](https://github.com/containerd/containerd/pull/593) from Random-Liu/fix-ocicni-commit
- [`2b8800df2`](https://github.com/containerd/containerd/commit/2b8800df2bc324a25c3b60292203e480dea1d50e) Merge pull request [#592](https://github.com/containerd/containerd/pull/592) from Random-Liu/fix-registry-mirror
- [`92995e29e`](https://github.com/containerd/containerd/commit/92995e29e5fb70d5d9ead5d8c4e28f5cf2125d8b) Fix registry mirror
- [`2d61bdbb0`](https://github.com/containerd/containerd/commit/2d61bdbb0a68927534641e6b2f96c8c471534e4f) Merge pull request [#588](https://github.com/containerd/containerd/pull/588) from Random-Liu/fix-registry-mirror
- [`a28672b08`](https://github.com/containerd/containerd/commit/a28672b08820a344e445d104bfb602139f99b342) Update containerd to fix mount.Lookup
- [`8d2d125d8`](https://github.com/containerd/containerd/commit/8d2d125d82dbb2c76e60370373e1f7fd4b852034) Merge pull request [#577](https://github.com/containerd/containerd/pull/577) from Random-Liu/fix-privileged-check
- [`4dfd8250f`](https://github.com/containerd/containerd/commit/4dfd8250fd973a034e58aa7503fc40460bf8dfdd) Fix a privileged check
- [`e7f2a74a8`](https://github.com/containerd/containerd/commit/e7f2a74a8452f234fb42fb474edd85f01eead6fa) Add runtime cgroup and fix a cli panic
- [`11042a414`](https://github.com/containerd/containerd/commit/11042a4141146e67eb44e23ca46c8cfaedcc4408) Merge pull request [#570](https://github.com/containerd/containerd/pull/570) from miaoyq/fixes-569
- [`07c8f07ba`](https://github.com/containerd/containerd/commit/07c8f07ba337fb5e13a5a2f07f584c4563665608) fix kubernetes-incubator links
- [`8e836140b`](https://github.com/containerd/containerd/commit/8e836140bda6534ef14a47b6d036a5598ed47e78) Merge pull request [#537](https://github.com/containerd/containerd/pull/537) from Random-Liu/fix-install-deps
- [`896cbd70f`](https://github.com/containerd/containerd/commit/896cbd70f7eff97d4e3ad6f72b3e9e1df5674e1f) Merge pull request [#526](https://github.com/containerd/containerd/pull/526) from yujuhong/fix-link
- [`07a068549`](https://github.com/containerd/containerd/commit/07a068549942025ea4987b203eb0dbec2c1df2f6) Fix typos and broken links in docs
- [`ca2c92e51`](https://github.com/containerd/containerd/commit/ca2c92e51231949bdfb1208d66224f2aaef38dc1) Merge pull request [#521](https://github.com/containerd/containerd/pull/521) from Random-Liu/fix-install-deps
- [`b3a4141ce`](https://github.com/containerd/containerd/commit/b3a4141ce58acb86ea6b5959559098cd42eb45ff) Merge pull request [#519](https://github.com/containerd/containerd/pull/519) from Random-Liu/fix-vendor
- [`d361ee542`](https://github.com/containerd/containerd/commit/d361ee542273669107263a69797f4b732130a015) Fix install-deps
- [`5b82e3a93`](https://github.com/containerd/containerd/commit/5b82e3a934d1206e63f866a640fe598ca7cbeb2d) Merge pull request [#518](https://github.com/containerd/containerd/pull/518) from Random-Liu/fix-privileged-caps
- [`36f05dd55`](https://github.com/containerd/containerd/commit/36f05dd5528193511d4b55d7e3c0eae7b95216d3) Merge pull request [#514](https://github.com/containerd/containerd/pull/514) from Random-Liu/fix-docs
- [`5c37f6dc6`](https://github.com/containerd/containerd/commit/5c37f6dc63dd247100e0db5be4bb4ea2945b7fa5) Fix kube-up document
- [`5003c6184`](https://github.com/containerd/containerd/commit/5003c618494df742c66374bc86848f493b7bd984) Merge pull request [#480](https://github.com/containerd/containerd/pull/480) from miaoyq/fix-466
- [`379a243e8`](https://github.com/containerd/containerd/commit/379a243e80b6eef092303fa2ce010d4f9895dc69) Merge pull request [#469](https://github.com/containerd/containerd/pull/469) from Random-Liu/fix-typos
- [`9a9550d7d`](https://github.com/containerd/containerd/commit/9a9550d7db6411e1b39fe4a624f783690c4727d5) Fix typos
- [`e0e5d9e13`](https://github.com/containerd/containerd/commit/e0e5d9e1390f2aa5a7bc79ebe1963aa6c5f1ddf4) Update containerd to try fix rootfs issue
- [`4c7974fe9`](https://github.com/containerd/containerd/commit/4c7974fe97f643dfad2de41fd3bb94f77b6f27a9) fixes for boilerplate
- [`3a0d40cc2`](https://github.com/containerd/containerd/commit/3a0d40cc2c1e3538bdec4198717d0bf6911b54fd) Merge pull request [#456](https://github.com/containerd/containerd/pull/456) from Random-Liu/fix-shim-cgroup-change
- [`b47770eae`](https://github.com/containerd/containerd/commit/b47770eaee36b144a1561934aca85179ade4dac8) Update containerd to fix fd leakage
- [`5ed43ea1a`](https://github.com/containerd/containerd/commit/5ed43ea1a357a6a1bc12bc4ca9bc5a00186bdca1) Update containerd to fix long exec issue
- [`4b4714eac`](https://github.com/containerd/containerd/commit/4b4714eaca91fddf005f8253be5e2fbeedc0aeb1) Merge pull request [#432](https://github.com/containerd/containerd/pull/432) from mikebrow/vet-fixes
- [`34340f502`](https://github.com/containerd/containerd/commit/34340f502df519b72dea3ad8ff9158faebd26a84) Merge pull request [#428](https://github.com/containerd/containerd/pull/428) from antony360/fix-readme-bug
- [`6d4e41e4e`](https://github.com/containerd/containerd/commit/6d4e41e4e414e16a527ea710e67328d99da97a45) Merge pull request [#414](https://github.com/containerd/containerd/pull/414) from Random-Liu/fix-data-race
- [`03aca5e82`](https://github.com/containerd/containerd/commit/03aca5e82bd6eef9de9453b11d74c86ce14bd524) Fix data race
- [`a61d86cf5`](https://github.com/containerd/containerd/commit/a61d86cf508c95ea3b24a4bde968d98524ff3c13) Merge pull request [#412](https://github.com/containerd/containerd/pull/412) from Random-Liu/fix-streaming-deadlock
- [`01493463d`](https://github.com/containerd/containerd/commit/01493463dbde602f180aedae1634fa781a0f7552) Fix streaming deadlock
- [`e1015b8d9`](https://github.com/containerd/containerd/commit/e1015b8d91d652202c5b59c297cf23fa8e2ef0f8) Merge pull request [#410](https://github.com/containerd/containerd/pull/410) from Random-Liu/refactor-and-fix-streaming
- [`3557cffbb`](https://github.com/containerd/containerd/commit/3557cffbbbd8edf88f0875adee952d2ffd9dcb61) Fix container exec
- [`b4c8efd89`](https://github.com/containerd/containerd/commit/b4c8efd898b0cc5aeaab4cefc3dec4d208d2e6f0) Merge pull request [#409](https://github.com/containerd/containerd/pull/409) from miaoyq/fix-408
- [`b6de04772`](https://github.com/containerd/containerd/commit/b6de04772db67b260d69834b012f1e1b013f634d) Merge pull request [#406](https://github.com/containerd/containerd/pull/406) from Random-Liu/fix-attach-stdin
- [`6ee3db482`](https://github.com/containerd/containerd/commit/6ee3db4825b670a2133a547224f002bfb50ad2cb) Merge pull request [#402](https://github.com/containerd/containerd/pull/402) from Random-Liu/fix-attach-tty
- [`68e74dc16`](https://github.com/containerd/containerd/commit/68e74dc16ab9f7ba0b7421128e9d3d71c18e4d32) Merge pull request [#394](https://github.com/containerd/containerd/pull/394) from Random-Liu/fix-container-streaming
- [`eec818e6a`](https://github.com/containerd/containerd/commit/eec818e6ab33a50db823c81f27072de33d4bbba0) Various fixes for container streaming
- [`e363c218d`](https://github.com/containerd/containerd/commit/e363c218d6eeaf430aef3e1a5498b65bc7b30d45) Merge pull request [#395](https://github.com/containerd/containerd/pull/395) from Random-Liu/fix-image-in-container-status
- [`e19e043a4`](https://github.com/containerd/containerd/commit/e19e043a4c562dbe08508edb0ace6eee54f37282) Merge pull request [#386](https://github.com/containerd/containerd/pull/386) from Random-Liu/fix-spammy-cni-log
- [`73c2cb563`](https://github.com/containerd/containerd/commit/73c2cb5632e5e9c93c2de10c544eff6b401739c7) Fix spammy CNI log
- [`3312c2f56`](https://github.com/containerd/containerd/commit/3312c2f56032412ca7c76d7bf826bfabf151db1f) Merge pull request [#387](https://github.com/containerd/containerd/pull/387) from Random-Liu/fix-node-e2e-test
- [`69c16929e`](https://github.com/containerd/containerd/commit/69c16929e3195d3124562cd5b97a56178af05109) Fix our node e2e test
- [`8679d1073`](https://github.com/containerd/containerd/commit/8679d1073305ef2da04a535b45052bf58372d396) Merge pull request [#380](https://github.com/containerd/containerd/pull/380) from Random-Liu/fix-deadlock
- [`c44f79814`](https://github.com/containerd/containerd/commit/c44f7981451941f829f5f53ee47665879f916a6f) Merge pull request [#371](https://github.com/containerd/containerd/pull/371) from Random-Liu/fix-removing
- [`4eaaee380`](https://github.com/containerd/containerd/commit/4eaaee380fbb76ee1a1b973a82b3955610b29472) Fix removing state recover
- [`64c719622`](https://github.com/containerd/containerd/commit/64c719622a51ef9c8850ea3e38d9e25f4529684c) Merge pull request [#365](https://github.com/containerd/containerd/pull/365) from Random-Liu/random-fix
- [`32806fa37`](https://github.com/containerd/containerd/commit/32806fa375755b140ab5f5d8fdf25994e44dcca8) Fix a log line and also set containerd log level to debug in node e2e
- [`486d7628c`](https://github.com/containerd/containerd/commit/486d7628c09e39116f39b9a6a66e9c6727648c51) Merge pull request [#363](https://github.com/containerd/containerd/pull/363) from Random-Liu/fix-node-e2e
- [`49c3876b8`](https://github.com/containerd/containerd/commit/49c3876b8b5e6321bf3a2a9cc08aca8e52875bc2) Merge pull request [#349](https://github.com/containerd/containerd/pull/349) from Random-Liu/fix-node-e2e
- [`313db2103`](https://github.com/containerd/containerd/commit/313db2103340c671d8096b0fc9f42932d2e5aead) Fix node e2e test
- [`d50c61094`](https://github.com/containerd/containerd/commit/d50c6109473df3e7467ca192dc060d14d0b5bf02) Merge pull request [#335](https://github.com/containerd/containerd/pull/335) from Random-Liu/fix-fs-uuid
- [`3a5ec1cf6`](https://github.com/containerd/containerd/commit/3a5ec1cf6e2a3f5d306b20816f21b46f88a6258b) Merge pull request [#328](https://github.com/containerd/containerd/pull/328) from Random-Liu/fix-container-stats-panic
- [`94b68ae66`](https://github.com/containerd/containerd/commit/94b68ae662ebba1cd268b2e8974c6b98cdfeeec1) Fix container stats panic
- [`d25c632bf`](https://github.com/containerd/containerd/commit/d25c632bfe284f3bc88cac939208a248342bbeb3) Merge pull request [#327](https://github.com/containerd/containerd/pull/327) from Random-Liu/fix-image-volume
- [`23b8330b4`](https://github.com/containerd/containerd/commit/23b8330b443c12aba60e3998de3b24dcfc728ce0) Merge pull request [#322](https://github.com/containerd/containerd/pull/322) from miaoyq/fix-314
- [`05f35f087`](https://github.com/containerd/containerd/commit/05f35f087b04d92a680abc706c444de87b02a5a3) Fix README.md typo
- [`aec175c9a`](https://github.com/containerd/containerd/commit/aec175c9a116ab65ef8a7f1eccdec5bc58670187) Merge pull request [#319](https://github.com/containerd/containerd/pull/319) from Random-Liu/fix-update-container-resources
- [`dfe615acc`](https://github.com/containerd/containerd/commit/dfe615acc050700de1c2db1d6493161207be434b) Merge pull request [#318](https://github.com/containerd/containerd/pull/318) from nikhita/fix-design-proposal-link
- [`bf2f942a1`](https://github.com/containerd/containerd/commit/bf2f942a117c83f45504e9fcd09d8ef591bd1fcd) Fix link to design proposal
- [`a81a47bf9`](https://github.com/containerd/containerd/commit/a81a47bf9bffefe10e075c128010ef30d7ac62dc) Fix update container resources
- [`1784b073b`](https://github.com/containerd/containerd/commit/1784b073bc916b309fd4525e107516947f875588) Merge pull request [#301](https://github.com/containerd/containerd/pull/301) from Random-Liu/fix-container-stats
- [`de6287d62`](https://github.com/containerd/containerd/commit/de6287d626f88506c30b6e75528af0db4fbdf52b) Fix container stats
- [`97b6e82d9`](https://github.com/containerd/containerd/commit/97b6e82d98ae7dfd9f7b49da4ee9134cd53dd9c0) Fix and cleanup container metrics
- [`b23165cb2`](https://github.com/containerd/containerd/commit/b23165cb2934686d0c21230f3bf3a9d3640d9438) Merge pull request [#282](https://github.com/containerd/containerd/pull/282) from Random-Liu/fix-ansible-playbook
- [`1fd8c2ffc`](https://github.com/containerd/containerd/commit/1fd8c2ffc3249dc3d6dcf15e3bd00e619f7f43ce) Merge pull request [#270](https://github.com/containerd/containerd/pull/270) from Random-Liu/fix-checkpoint-recovery
- [`ce9d27bd9`](https://github.com/containerd/containerd/commit/ce9d27bd94d3006459f62245f3b50b666a75db27) Fix checkpoint recovery
- [`90d6e44c2`](https://github.com/containerd/containerd/commit/90d6e44c22017744583c24cf1f9b235b3e2e490b) Merge pull request [#267](https://github.com/containerd/containerd/pull/267) from Random-Liu/fix-apparmor
- [`dd3421c3c`](https://github.com/containerd/containerd/commit/dd3421c3c7392978ee06ad1047b8371626b30d1b) Fix apparmor empty case
- [`3647ff597`](https://github.com/containerd/containerd/commit/3647ff597679c8277a470b1fb6c8e5f188d967aa) Merge pull request [#263](https://github.com/containerd/containerd/pull/263) from Random-Liu/fix-log
- [`45f98a0b3`](https://github.com/containerd/containerd/commit/45f98a0b3928b5eee1528546602b295b54c63418) Fix one line of log, we are writing not reading
- [`91ca17827`](https://github.com/containerd/containerd/commit/91ca178275a42aa0b968b185863f23ef72953d23) Update containerd to include the gcr private registry fix
- [`742995338`](https://github.com/containerd/containerd/commit/7429953386071a68023df6c6153a62e95003c71d) Fix install.deps
- [`159fa903c`](https://github.com/containerd/containerd/commit/159fa903cff0c67a2620b98b59f1f5346aa8a227) Merge pull request [#232](https://github.com/containerd/containerd/pull/232) from Random-Liu/fix-rootfs
- [`3e4b4234c`](https://github.com/containerd/containerd/commit/3e4b4234c697981af9641d6be447f9aff7af8645) Merge pull request [#218](https://github.com/containerd/containerd/pull/218) from miaoyq/fixes-185
- [`99a87f1a2`](https://github.com/containerd/containerd/commit/99a87f1a29861fca9602b9d6f40742eb1e192c5b) Add toml config file for cri-containerd fix #182
- [`59e75d8c5`](https://github.com/containerd/containerd/commit/59e75d8c5e691529f395105927d961cb9d7e9989) Merge pull request [#208](https://github.com/containerd/containerd/pull/208) from miaoyq/fixes-180
- [`5da08bd89`](https://github.com/containerd/containerd/commit/5da08bd892cb1cb43f531ddf8031e6db1dec3d74) Fix build for multiple GOPATHs
- [`9d479844c`](https://github.com/containerd/containerd/commit/9d479844c6eb87f422b1e9130b6b5810224b563e) vendor k8s and containerd for apparmor fix
- [`4f449cec5`](https://github.com/containerd/containerd/commit/4f449cec5f396b162b57588dad6cc00858c61045) Merge pull request [#202](https://github.com/containerd/containerd/pull/202) from Random-Liu/fix-image-repo-digest
- [`cfb5513a5`](https://github.com/containerd/containerd/commit/cfb5513a54cab38e7c166c897a7b7b97b2ed7243) Fix repo digest for schema 1 image
- [`80b57f54a`](https://github.com/containerd/containerd/commit/80b57f54a69e0f20f3b1d1bf289371f0dc23d6e3) Merge pull request [#192](https://github.com/containerd/containerd/pull/192) from Random-Liu/fix-sandbox-container-snapshotter
- [`c4d95aa2c`](https://github.com/containerd/containerd/commit/c4d95aa2c47c3903b93ea396a59ccb594650f252) Fix sandbox container snapshotter
- [`2aea0388b`](https://github.com/containerd/containerd/commit/2aea0388be7b3337f1242e9e60d0c473a62f2460) Merge pull request [#187](https://github.com/containerd/containerd/pull/187) from Random-Liu/fix-bind-mount
- [`c2fb61b5f`](https://github.com/containerd/containerd/commit/c2fb61b5fe961b21930436d1d56e841a31eb1bda) Merge pull request [#178](https://github.com/containerd/containerd/pull/178) from Random-Liu/fix-leak-files
- [`b73161627`](https://github.com/containerd/containerd/commit/b73161627db122cfaa0693363cf55bd735f84f04) Fix fifo files leakage
- [`113964e49`](https://github.com/containerd/containerd/commit/113964e499914f9bfacc16eb0b017449d5d7df2d) Merge pull request [#174](https://github.com/containerd/containerd/pull/174) from Random-Liu/fix-network-teardown
- [`8fd54d2f2`](https://github.com/containerd/containerd/commit/8fd54d2f2d0bbd829089bbbd0c603c2128d6d78f) Merge pull request [#172](https://github.com/containerd/containerd/pull/172) from Random-Liu/fix-run-as-user
- [`e1f74f00a`](https://github.com/containerd/containerd/commit/e1f74f00a5fbb4830476651168eb56f7f01933f1) Various security related fixes
- [`b671465d7`](https://github.com/containerd/containerd/commit/b671465d7fae11c270e03aa7f2f63e3220bb1cd1) Merge pull request [#165](https://github.com/containerd/containerd/pull/165) from Random-Liu/fix-node-e2e
- [`d2757cb8f`](https://github.com/containerd/containerd/commit/d2757cb8f94bff588b0cdd9f9c6b0b5ec26c6204) Checkpoint and restart recovery fix part of #120
- [`810ffbb9b`](https://github.com/containerd/containerd/commit/810ffbb9b69755b35c8c5685cffe47ea55843d1e) Merge pull request [#152](https://github.com/containerd/containerd/pull/152) from Random-Liu/fix-node-e2e
- [`77095f569`](https://github.com/containerd/containerd/commit/77095f569aa0f4e4958b6ad7fcfdd7239cd0b90c) Fix node e2e test
- [`5ce5868bf`](https://github.com/containerd/containerd/commit/5ce5868bf1897c4ac27eecba1c8806a333de3887) Fix Typo in Events Code of Conduct
- [`8f6558aee`](https://github.com/containerd/containerd/commit/8f6558aee696218378ffb60f99c6e242f81c3de1) Update docker and cri-o to include the sirupsen fix
- [`69251dd7e`](https://github.com/containerd/containerd/commit/69251dd7ecc231c7cae91891241b9ec8cce76260) Merge pull request [#116](https://github.com/containerd/containerd/pull/116) from Random-Liu/fix-devices
- [`502072e63`](https://github.com/containerd/containerd/commit/502072e63ede5455f574d40089d5b9389f413e19) Merge pull request [#107](https://github.com/containerd/containerd/pull/107) from Random-Liu/fix-deadlink
- [`4f98eac93`](https://github.com/containerd/containerd/commit/4f98eac93c86eff77bdb94789783055811b38c26) Fix deadlink of travis.yaml
- [`333ea0484`](https://github.com/containerd/containerd/commit/333ea048468a755121a37ce75fe0b5ca0d0936e1) Merge pull request [#95](https://github.com/containerd/containerd/pull/95) from Random-Liu/fix-verify
- [`4b53d843b`](https://github.com/containerd/containerd/commit/4b53d843bca5755b592776353c538d39ed9e259c) Merge pull request [#80](https://github.com/containerd/containerd/pull/80) from Random-Liu/fix-image-pull
- [`d4f7380f5`](https://github.com/containerd/containerd/commit/d4f7380f5903773559515f9fa501de2389875147) Merge pull request [#73](https://github.com/containerd/containerd/pull/73) from Random-Liu/fix-delete-race
- [`0e2db7e99`](https://github.com/containerd/containerd/commit/0e2db7e99a0491ec3cbb6069cca45c3cbde1c710) Merge pull request [#76](https://github.com/containerd/containerd/pull/76) from Random-Liu/fix-fake-execution-client-race
- [`2ae22b33b`](https://github.com/containerd/containerd/commit/2ae22b33b7de6d327369aa35da66f6d4acd9c194) Fix a race that fake execution client sends event to closed channel
- [`bd09d3177`](https://github.com/containerd/containerd/commit/bd09d31777b2b5cd29a8a7321201eddce821dbab) Fix Delete race
- [`b83270d08`](https://github.com/containerd/containerd/commit/b83270d08d45f7fd6fe0513e75642b3549d0222a) Merge pull request [#74](https://github.com/containerd/containerd/pull/74) from Random-Liu/fix-event-handler
- [`9b1708b40`](https://github.com/containerd/containerd/commit/9b1708b408871497d832a4427cd42b5d00bd3109) Merge pull request [#71](https://github.com/containerd/containerd/pull/71) from Random-Liu/fix-capabilities
- [`f247a0819`](https://github.com/containerd/containerd/commit/f247a0819dde881f37b6413603cc9b9139afcede) Fix capabilities support
- [`507eff04b`](https://github.com/containerd/containerd/commit/507eff04b34589eddf5b3cdc7a0998446984857a) Merge pull request [#33](https://github.com/containerd/containerd/pull/33) from Random-Liu/fix-godep
- [`8112c03f1`](https://github.com/containerd/containerd/commit/8112c03f15a964e482757585dee1f3e29d2b0257) Fix godeps
- [`fc884cf`](https://github.com/containerd/aufs/commit/fc884cfda0b1815c0d97d070945e700cb16d3574) Set up golangci-lint config and fix 2 files
- [`6f1a47b`](https://github.com/containerd/aufs/commit/6f1a47bea6be2a623f91cb587a58b6069c3bb8c5) Fix test build
- [`48eb88e`](https://github.com/containerd/btrfs/commit/48eb88e4fc0a1806012557496e50669afe671e30) Merge pull request [#27](https://github.com/containerd/btrfs/pull/27) from fuweid/fix-checkptr-issue
- [`d44cb8e`](https://github.com/containerd/btrfs/commit/d44cb8e80d3e3b8d924fa9db42cc666848679f58) fix: checkptr issue
- [`fefdccb`](https://github.com/containerd/cgroups/commit/fefdccba0483a08c01bcc89ed300871bcddb3654) v2: ebpf: replace deprecated prog.Attach/prog.Detach and fix closer
- [`8a68de5`](https://github.com/containerd/cgroups/commit/8a68de567b68b30602948417a7a8e99ccf00ee9b) Merge pull request [#187](https://github.com/containerd/cgroups/pull/187) from zhsj/fix-hugetlb
- [`0865f29`](https://github.com/containerd/cgroups/commit/0865f2932e6d1ce7ec420e1d3ffc42aa3eaaf563) Fix cgctl in gitignore
- [`2f1e3d2`](https://github.com/containerd/console/commit/2f1e3d2b6afd18e8b2077816c711205a0b4d8769) Merge pull request [#52](https://github.com/containerd/console/pull/52) from zhsj/fix-import
- [`65c9061`](https://github.com/containerd/console/commit/65c90614c5551d6955684f1fd7b68f9de51143b2) Merge pull request [#51](https://github.com/containerd/console/pull/51) from kolyshkin/fix-bi
- [`a261251`](https://github.com/containerd/console/commit/a2612510eb095c6db04e056a0fc6f892a35f518a) Fix ptsname() for big-endian architectures (again)
- [`ad71182`](https://github.com/containerd/console/commit/ad71182acd91820be6e7c730b34666db207b0e7f) Merge pull request [#47](https://github.com/containerd/console/pull/47) from estesp/fix-gh-env
- [`f847fbb`](https://github.com/containerd/console/commit/f847fbb1d1e05742f02e675000a69bb44c8857f0) Merge pull request [#41](https://github.com/containerd/console/pull/41) from estesp/fix-my-bad-actions
- [`cf8d0db`](https://github.com/containerd/console/commit/cf8d0db7c3dc638d8cf28585916ad335ea22e91a) Fix actions to follow the model from other repos
- [`c13fe94`](https://github.com/containerd/continuity/commit/c13fe94960c7da5d72b70962697fe395513d50aa) freebsd: fix compilation error
- [`1d9893e`](https://github.com/containerd/continuity/commit/1d9893e5674b5260c3fc11316d0d5fc0d12ea9e2) Merge pull request [#169](https://github.com/containerd/continuity/pull/169) from dmcgowan/fix-usage-block-size
- [`b97555e`](https://github.com/containerd/continuity/commit/b97555e75c86a5f693aa104085036ad4eb1467de) Fix incorrect usage calculation
- [`91328d7`](https://github.com/containerd/continuity/commit/91328d7c60e71160252e8271376d9efadd16f0ad) Merge pull request [#166](https://github.com/containerd/continuity/pull/166) from zhsj/fix-riscv64
- [`62ef0ff`](https://github.com/containerd/continuity/commit/62ef0fffa6a1bed97d4b034c146bc323b2447b72) Merge pull request [#165](https://github.com/containerd/continuity/pull/165) from zhsj/fix-arm64
- [`25269ef`](https://github.com/containerd/continuity/commit/25269efb6192a3f31d9ef6a57d8631cd48b5f3b9) Fix building on arm64
- [`310e183`](https://github.com/containerd/continuity/commit/310e183616c481b7237980a7787a26435d311c0d) gha: fix invalid workflow definition
- [`04c754f`](https://github.com/containerd/continuity/commit/04c754faca46997ba6d0733f611c42f1816d1199) Merge pull request [#163](https://github.com/containerd/continuity/pull/163) from dmcgowan/fix-sparse-file-usage
- [`bc5e3ed`](https://github.com/containerd/continuity/commit/bc5e3edd2b742c38c762d928f267ad82922a1b63) Fix usage calculation to account for sparse files
- [`5be08d2`](https://github.com/containerd/fifo/commit/5be08d276e59f56db16f4be5e0ace94bac2d9dfc) fix: goimports and unconvert
- [`30d0272`](https://github.com/containerd/go-cni/commit/30d0272257471dfb7ecc325e2a8e825bdcc7a33e) Temporarily disable EXC0002 until GoDoc is fixed in this repo
- [`7af6620`](https://github.com/containerd/go-cni/commit/7af6620bc1b8a169d374649cfa3f73b203e261d4) TestLibCNITypeCurrent: fix ineffassign
- [`7c5957f`](https://github.com/containerd/go-runc/commit/7c5957f67ef4ea97967237cbaca559ae04c88321) Merge pull request [#66](https://github.com/containerd/go-runc/pull/66) from thehajime/fix-win-build
- [`d6ba496`](https://github.com/containerd/go-runc/commit/d6ba49689be98a4278ce479200f72e1f25404dc4) Fix a regression of windows build issue of undefined symbol
- [`ad1414d`](https://github.com/containerd/go-runc/commit/ad1414ddd16e9cc77e5a9e76e14110fdd61bd4e6) Merge pull request [#64](https://github.com/containerd/go-runc/pull/64) from thehajime/fix-darwin-fchown
- [`c2dc10d`](https://github.com/containerd/imgcrypt/commit/c2dc10d877129d1a9b681df0621e041f7a3a75eb) Fix readme typo
- [`21e7083`](https://github.com/containerd/imgcrypt/commit/21e708327b038be3510b71a4c7a487451238005d) Fix readme typo
- [`6888caa`](https://github.com/containerd/imgcrypt/commit/6888caac6a46dfd5b800d96d2c050c6990050d0f) Merge pull request [#15](https://github.com/containerd/imgcrypt/pull/15) from Gsealy/fix-typos
- [`90611e1`](https://github.com/containerd/imgcrypt/commit/90611e10802cbdd1a47203166a9389837c7d1d06) fix typos. just use one dash for `out` flag
- [`db74117`](https://github.com/containerd/imgcrypt/commit/db74117e201416f46fb0611d2bd2840f097d1f1a) fix config.toml demo bugs
- [`3fae7eb`](https://github.com/containerd/nri/commit/3fae7eb35cad7481d2f3acdb61fc7eb9be2e1c2a) README: fix JSON syntax-error, and reformat JSON examples
- [`f91f2f9`](https://github.com/containerd/nri/commit/f91f2f9c1d7710c8fc810d3192d67462ccc31d1d) types/v1: fix goimports
- [`7b505d7`](https://github.com/containerd/nri/commit/7b505d726cca0c7b896cc536279836acf33b55aa) client.go: fix golint
- [`a1440a4`](https://github.com/containerd/nri/commit/a1440a44778fe4509578f18456f1bdc9e2c1d64d) Fix licensing (add license headers)
- [`c5cd955`](https://github.com/containerd/nri/commit/c5cd955110e1b289dbe9f47029011763391c924b) fix missing import for fmt in skel
- [`fd7a26c`](https://github.com/containerd/nri/commit/fd7a26c798d396d11f29238451f33b7f244e4cce) Fix "argument list too long" error
- [`df11695`](https://github.com/containerd/ttrpc/commit/df116954de0e86a90f7fc549f0391a7eecd2ba77) fix bug, failed to assert net error due to error wrap
- [`5e43fb8`](https://github.com/containerd/typeurl/commit/5e43fb8b75ed2f2305fc04e6918c8d10636771bc) Merge pull request [#25](https://github.com/containerd/typeurl/pull/25) from wzshiming/fix/lock_for_getTypeByUrl
- [`ca4a32a`](https://github.com/containerd/typeurl/commit/ca4a32a3354c36fa749252a76f84e723353f2ea3) Fix lock for getTypeByUrl
- [`4140c90`](https://github.com/containerd/zfs/commit/4140c9077d87eb8bea25bd935f56bc732b18c25c) Merge pull request [#43](https://github.com/containerd/zfs/pull/43) from samuelkarp/fix-config

### 1.5.1

- **Fix registry mirror authorization logic in CRI plugin** [#5446](https://github.com/containerd/containerd/pull/5446)
- **Fix regression in cri-cni-release to include cri tools** [#5462](https://github.com/containerd/containerd/pull/5462)
- [`5e742ea04`](https://github.com/containerd/containerd/commit/5e742ea04b8266db15e97ea4e7c2d35330b6416a) Fix different registry hosts referencing the same auth config

### 1.5.3

- **Fix invalid validation error checking** [#5565](https://github.com/containerd/containerd/pull/5565)
- **Fix error on image pull resume** [#5560](https://github.com/containerd/containerd/pull/5560)
- **Fix User Agent sent to registry authentication server** [#5533](https://github.com/containerd/containerd/pull/5533)
- **Fix symlink resolution for disk mounts on Windows** [#5411](https://github.com/containerd/containerd/pull/5411)
- [`0515f9d2d`](https://github.com/containerd/containerd/commit/0515f9d2d8b03d22654d6aef751b3f6d98873dab) Fix missing Body.Close() calls on push to docker remote
- [`3735a7dfe`](https://github.com/containerd/containerd/commit/3735a7dfe06f6598607d9f1dc42aadf479c46400) Fix incorrect UA used for registry authentication
- [`31ecdf77d`](https://github.com/containerd/containerd/commit/31ecdf77d9255402e73e7a7085cab14711c771f6) Fix cleanup context of teardownPodNetwork
- [`d31f5e6b6`](https://github.com/containerd/containerd/commit/d31f5e6b6b82e5c190aa487fb6eae263b45aabf8) fix invalid validation error checking

### 1.5.5

- [`7b17268fd`](https://github.com/containerd/containerd/commit/7b17268fd1803a4a1790967a32518ed6686864a3) remotes/docker/pusher.go: Fix missing Close()
- [`2f11d5855`](https://github.com/containerd/containerd/commit/2f11d58550fe0ce577746f86a1d7cef57dc40f38) remotes/docker/fetcher.go: Fix missing Close()

### 1.5.6

- **Update hcsshim to v0.8.21 to fix layer issue on Windows Server 2019** [#5942](https://github.com/containerd/containerd/pull/5942)
- **Add support for 'clone3' syscall to fix issue with certain images when seccomp is enabled** [#5982](https://github.com/containerd/containerd/pull/5982)
- **Fix panic in metadata content writer on copy error** [#6043](https://github.com/containerd/containerd/pull/6043)
- [`063195739`](https://github.com/containerd/containerd/commit/063195739c21d530ff6ea65f0105ce6ada089fd8) Merge pull request [#6045](https://github.com/containerd/containerd/pull/6045) from dmcgowan/1.5-fix-metadata-content-panic
- [`a4b51d119`](https://github.com/containerd/containerd/commit/a4b51d1197ee9a5547491a2ce0f15b23daaf1113) Fix panic in metadata content writer on copy error
- [`79e05529e`](https://github.com/containerd/containerd/commit/79e05529eaddf2950dea3a13915a94baa408afbf) Merge pull request [#5999](https://github.com/containerd/containerd/pull/5999) from dmcgowan/1.5-fix-unexpected-eof-handling
- [`210d3bc15`](https://github.com/containerd/containerd/commit/210d3bc15272b1ef33359065f533ecaf187ee32b) Fix content copy to not ignore unexpected EOF
- [`0ca2e2751`](https://github.com/containerd/containerd/commit/0ca2e2751f0f35688345e2e9aca18ee0f044dfaf) Fix dir support for devices V3 (#4847)
- [`fe195c343`](https://github.com/containerd/containerd/commit/fe195c3432493277fff4e050e7622660ecc26415) mergo: Upgrade to 0.3.12 to fix panic

### 1.5.7

- **Fix insufficiently restricted permissions on container root and plugin directories** [GHSA-c2h3-6mxw-7mvq](https://github.com/containerd/containerd/security/advisories/GHSA-c2h3-6mxw-7mvq)

### 1.5.8

- [release/1.5] Fix containerd fails to pull OCI image with non-`http(s)://` urls ([#6238](https://github.com/containerd/containerd/pull/6238)) [`01428ec40`](https://github.com/containerd/containerd/commit/01428ec4095d23727d227e5602690a2ad356d02f) Fix containerd fails to pull OCI image with non-`http(s)://` urls
- [release/1.5] Use deactivatelayer to recover layers that we cannot rename ([#6133](https://github.com/containerd/containerd/pull/6133)) [`16762f3e5`](https://github.com/containerd/containerd/commit/16762f3e5c26688dd7482b9b880f1b46e4185661) Fix spelling mistake in Windows snapshotter [`6094bc770`](https://github.com/containerd/containerd/commit/6094bc77050820c5433c2281d9f3e2a0883eb580) Use DeactivateLayer to recover layers that we cannot rename
- [release/1.5] Fix pull fails on unexpected EOF ([#6117](https://github.com/containerd/containerd/pull/6117)) [`aa7c9d9da`](https://github.com/containerd/containerd/commit/aa7c9d9daf5876311c4a77bb445c51225ba19956) Fix pull fails on unexpected EOF

### 1.5.9

- **Fix unprivileged pod using 'hostPath' bypassing SELinux labels** ([GHSA-mvff-h3cj-wj9c](https://github.com/containerd/containerd/security/advisories/GHSA-mvff-h3cj-wj9c))
- **Fix setting the "container_kvm_t" SELinux label**
- [release/1.5] seutil: Fix setting the "container_kvm_t" label ([#6381](https://github.com/containerd/containerd/pull/6381)) [`da5749b67`](https://github.com/containerd/containerd/commit/da5749b670823abd3fa03298c2e89cd22c8bfb6d) seutil: Fix setting the "container_kvm_t" label

### 1.5.10

- [release/1.5 backport] GHA fixes, update GolangCI-Lint v1.42.0, and go-mdman v2.0.1 ([#6511](https://github.com/containerd/containerd/pull/6511)) script: update golangci-lint from v1.38.0 and v1.36.0 to v1.42.0 Fix Linux CI Linter using go 1.15.14 Update cpuguy83/go-md2man binary to v2.0.1

### 1.5.11

- **Fix the inheritable capability defaults** ([GHSA-c9cp-9c75-9v8c](https://github.com/containerd/containerd/security/advisories/GHSA-c9cp-9c75-9v8c))
- [release/1.5] fix critools installation ([#6718](https://github.com/containerd/containerd/pull/6718)) Update get to install for cri tools
- Github Security Advisory [GHSA-c9cp-9c75-9v8c](https://github.com/containerd/containerd/security/advisories/GHSA-c9cp-9c75-9v8c) Fix the Inheritable capability defaults

### 1.5.12

- **Fix inotify fd leak when cgroup is deleted**
- **Fix deadlock from abandoned transactions in native snapshotter**
- [release/1.5] fix #6054 MaxConcurrentDownloads is not effect when Unpack is true ([#6774](https://github.com/containerd/containerd/pull/6774)) [`4dbd0c851`](https://github.com/containerd/containerd/commit/4dbd0c851b9b0cb0d8b02c44d72c311a25a2512a) fix #6054 MaxConcurrentDownloads is not effect when Unpack is true
- [release/1.5 backport] native: fix deadlock from leaving transactions open ([#6726](https://github.com/containerd/containerd/pull/6726)) [`603ef55e0`](https://github.com/containerd/containerd/commit/603ef55e0e696b382ad08d83168d608f54f1b6e2) native: fix deadlock from leaving transactions open
- v2: Fix inotify fd leak when cgroup is deleted ([#212](https://github.com/containerd/cgroups/pull/212)) [`a7d6888`](https://github.com/containerd/cgroups/commit/a7d6888aa30218c8aff15d979eb3f6aec0b7979c) v2: add test case for Manager.EventChan() behavior [`cf1f978`](https://github.com/containerd/cgroups/commit/cf1f978b93bf784118d3ab7dec6a47b8204918c2) v2: flip error handling for readKVStat("memory.events") to reduce indentation [`6a46df2`](https://github.com/containerd/cgroups/commit/6a46df25065d551a8d998495c34263354c84f2c1) v2: manager: factor out memory.events parsing [`35b5b55`](https://github.com/containerd/cgroups/commit/35b5b55c686080de64facf127d6d6a5ca9a0fe6b) v2: Fix inotify leak when cgroup is deleted
- fix Implicit memory aliasing in for loop ([#214](https://github.com/containerd/cgroups/pull/214)) [`182c3af`](https://github.com/containerd/cgroups/commit/182c3afa53b8cccce0611cca9dee46410c4f82f7) fix Implicit memory aliasing in for loop
- Fix potential dirfd leak. ([#210](https://github.com/containerd/cgroups/pull/210)) [`17fece8`](https://github.com/containerd/cgroups/commit/17fece81870ef8aa1a31f05210b8f425e37038a0) Fix potential dirfd leak

### 1.5.13

- **Fix ExecSync handler to cap console output size** ([GHSA-5ffw-gxpp-mxpf](https://github.com/containerd/containerd/security/advisories/GHSA-5ffw-gxpp-mxpf))

### 1.5.14

- **Fix WWW-Authenticate parsing to allow empty quoted string**
- **Fix createTarFile: make xattr EPERM non-fatal**
- **Fix dockerPusher to handle abort correctly**
- **Fix CRI: PodSandboxStatus should tolerate missing task**
- **Fix io.containerd.runc.v1: Stats() shouldn't assume s.container is non-nil**
- [release/1.5] cherry-pick: remotes: fix dockerPusher to handle abort correctly ([#7467](https://github.com/containerd/containerd/pull/7467)) [`2fe813d36`](https://github.com/containerd/containerd/commit/2fe813d368ffc5e1224e0748b30d6d240b858250) remotes: fix dockerPusher to handle abort correctly
- [release 1.5 backport] Fix cleanup in critest ([#7275](https://github.com/containerd/containerd/pull/7275)) [`c2ace6ebc`](https://github.com/containerd/containerd/commit/c2ace6ebc8bf3cda5faee1c4861670257f238bed) Fix cleanup in critest
- [release/1.5] Fix WWW-Authenticate parsing ([#7132](https://github.com/containerd/containerd/pull/7132)) [`8ae864ae9`](https://github.com/containerd/containerd/commit/8ae864ae9871d8f7d16c5f21cd9d54e5fcaabd97) [release/1.5] Fix WWW-Authenticate parsing
- [release/1.5] ctr: fix label args used in NewContainer ([#7071](https://github.com/containerd/containerd/pull/7071)) [`febb0e82d`](https://github.com/containerd/containerd/commit/febb0e82d6c6a8974fc2b3bdfa80a92895106fa6) ctr: fix label args used in NewContainer

### 1.5.15

- **Fix CNI leaks by changing pod network setup order in CRI plugin**
- **Fix lease labels unexpectedly overwriting expiration**
- [release/1.5] cherry-pick: Fix order of operations when setting lease labels ([#7746](https://github.com/containerd/containerd/pull/7746)) Fix order of operations when setting lease labels
- [release/1.5] retry request on writer reset ([#7479](https://github.com/containerd/containerd/pull/7479)) fix pusher concurrent close channel retry request on writer reset
- [release/1.5] feat: support import image for specific platform ([#7595](https://github.com/containerd/containerd/pull/7595)) fix: wrong flag type feat: support import image for specific platform
- Various small fix-ups ([#202](https://github.com/containerd/continuity/pull/202)) README: update badges and links golangci-lint: replace "golint" with "revive" sysx: remove unused sysx/generate.sh script fs: fix minor linting and gofmt issue
- Fix wrapping errors ([#196](https://github.com/containerd/continuity/pull/196)) fs: fix wrapping nil err fmt.Errorf: use %w, not %v to wrap errors
- fix fmt.Errorf("%w", err) on err == nil ([#187](https://github.com/containerd/continuity/pull/187)) fix fmt.Errorf("%w", err) on err == nil
- Fix darwin issues ([#186](https://github.com/containerd/continuity/pull/186)) update AUTHORS darwin: use utimensat syscall instead of utimes fix darwin usage of du command

### 1.5.16

- **Fix goroutine leak during Exec in CRI plugin** ([GHSA-2qjp-425j-52j9](https://github.com/containerd/containerd/security/advisories/GHSA-2qjp-425j-52j9))
- Github Security Advisory [GHSA-2qjp-425j-52j9](https://github.com/containerd/containerd/security/advisories/GHSA-2qjp-425j-52j9) Prepare release notes for v1.5.16 CRI stream server: Fix goroutine leak in Exec

### 1.5.17

- **Fix no CNI info for pod sandbox on restart**
- [release/1.5] CRI: Fix no CNI info for pod sandbox on restart ([#7849](https://github.com/containerd/containerd/pull/7849)) [`23c2a863e`](https://github.com/containerd/containerd/commit/23c2a863e338c6e1ddb2bb56d1b2e35f118f5284) CRI: Fix no CNI info for pod sandbox on restart

### 1.5.18

- **Fix supplementary groups not being set up properly** ([GHSA-hmfx-3pcx-653p](https://github.com/containerd/containerd/security/advisories/GHSA-hmfx-3pcx-653p))
- **Fix OCI image importer memory exhaustion** ([GHSA-259w-8hf6-59c2](https://github.com/containerd/containerd/security/advisories/GHSA-259w-8hf6-59c2))
- Github Security Advisory [GHSA-hmfx-3pcx-653p](https://github.com/containerd/containerd/security/advisories/GHSA-hmfx-3pcx-653p) [`a62c38bf2`](https://github.com/containerd/containerd/commit/a62c38bf2173faa813018939710fc8491e4f7dba) oci: fix additional GIDs [`3b89da580`](https://github.com/containerd/containerd/commit/3b89da580b76471d6c03cb1fc6c14db6aa23d3db) oci: fix loop iterator aliasing [`b07ec6b25`](https://github.com/containerd/containerd/commit/b07ec6b251bd51f06bc72ef408f31e3f6e6e87f9) oci: skip checking gid for WithAppendAdditionalGroups [`356672cb5`](https://github.com/containerd/containerd/commit/356672cb56fd5a0eed11e5089ac824c7ab09ffac) refactor: reduce duplicate code [`6a7b7617c`](https://github.com/containerd/containerd/commit/6a7b7617cfbd90009a2e05e0e5eff4ef92028d7b) add WithAdditionalGIDs test [`832bcf300`](https://github.com/containerd/containerd/commit/832bcf300b1ec29c9b08326aab2d4eafee58dd85) add WithAppendAdditionalGroups helper
- [release/1.5] Fix retry logic within devmapper device deactivation ([#8089](https://github.com/containerd/containerd/pull/8089)) [`0d16d045d`](https://github.com/containerd/containerd/commit/0d16d045dfd0d800a00dc362736b815f6cc96de8) Fix retry logic within devmapper device deactivation


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.5.18**, the newest release recorded here for this line.

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
