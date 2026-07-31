---
id: TROUBLE-CONTAINERD_1_3_DEFECTS
type: troubleshooting
title: "containerd 1.3: defects fixed in the 1.3 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.3.0 <1.4.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - containerd 1.3 known issues
  - containerd 1.3 fixed in
  - is this containerd bug already fixed
tags:
  - troubleshooting
  - upgrade
  - containerd
sources:
  - type: docs
    path: containerd/containerd release notes for the 1.3 line — bug-fix entries
    url: https://github.com/containerd/containerd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# containerd 1.3: defects fixed in the 1.3 line

## Summary

**305 defects** the project fixed across **10 releases** of the 1.3 line, from 1.3.0 to
1.3.10. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.3.0

- Updated cni plugins to v0.7.6 to fix a race condition in the `bridge` plugin. (https://github.com/containerd/containerd/issues/3507)
- **Fix garbage collection scheduling on reference removal.** Ensures removal of leases or containers triggers the next scheduled garbage collection
- [`a668365eca`](https://github.com/containerd/containerd/commit/a668365eca1ddcdc3046e04d8a6421f956ddefc7) Merge pull request [#3696](https://github.com/containerd/containerd/pull/3696) from dmcgowan/fix-all-media-types
- [`394db03f15`](https://github.com/containerd/containerd/commit/394db03f1531bfaa7018ecc470f29930aa30590f) Fix all media types in Accept header to match RFC
- [`62c2eea78d`](https://github.com/containerd/containerd/commit/62c2eea78d28e023d7497d5b80eca6924f4f8799) fix-up typo
- [`da66333271`](https://github.com/containerd/containerd/commit/da66333271f372204aed6b83c2ecf37fa7d9ae2c) Merge pull request [#3677](https://github.com/containerd/containerd/pull/3677) from dmcgowan/gc-fix-notes
- [`85eac2550f`](https://github.com/containerd/containerd/commit/85eac2550ff6a34a16f51ace05b103869565ada8) Add release note for gc fix
- [`9c10bf89ba`](https://github.com/containerd/containerd/commit/9c10bf89ba9a70aa554310e2b219d1bdb94c4c46) Merge pull request [#3668](https://github.com/containerd/containerd/pull/3668) from dmcgowan/fix-metadata-dirty
- [`fd6299be98`](https://github.com/containerd/containerd/commit/fd6299be9843ef684f66d1bcd3d5511ac1c8f847) Fix density spec generation
- [`86442dfbb9`](https://github.com/containerd/containerd/commit/86442dfbb9c76d20031718d471c0d5b33c938ef3) Merge pull request [#3653](https://github.com/containerd/containerd/pull/3653) from lalyos/fix-connect-timeout
- [`93391048bd`](https://github.com/containerd/containerd/commit/93391048bd2cc8dc4921071407bb88e7a8fdf30b) Merge pull request [#3650](https://github.com/containerd/containerd/pull/3650) from dmcgowan/fix-vendor-issue
- [`5bb0281d16`](https://github.com/containerd/containerd/commit/5bb0281d1615cf84ad3ce7289590a360fd7020a3) Fix missing vendor packages
- [`9dccbaa6ec`](https://github.com/containerd/containerd/commit/9dccbaa6ec3b2ba46daf90ff0ee09695f61a8adf) Merge pull request [#3636](https://github.com/containerd/containerd/pull/3636) from dmcgowan/fix-cri-darwin-release
- [`3db5a5ad2e`](https://github.com/containerd/containerd/commit/3db5a5ad2ed9a91c1d3ed615bc81cb513523b6d2) Fix darwin build for cri release
- [`1b4cec9796`](https://github.com/containerd/containerd/commit/1b4cec9796e669e46d6e633e3e361fd00d448a74) Update cri test to fix image reference test and fix gcs deploy
- [`ce8d63255c`](https://github.com/containerd/containerd/commit/ce8d63255c7f43c90f9a856870583cb0ada76ff2) Merge pull request [#3634](https://github.com/containerd/containerd/pull/3634) from Random-Liu/fix-cri-release
- [`e3abd03ae1`](https://github.com/containerd/containerd/commit/e3abd03ae190bf11c11a035aafb139196c6f7794) Fix CRI release build
- [`1eaf601453`](https://github.com/containerd/containerd/commit/1eaf6014532e9afc6d87a8cb42c78a560301784a) Merge pull request [#3616](https://github.com/containerd/containerd/pull/3616) from Random-Liu/fix-unpack-on-windows
- [`3050b36640`](https://github.com/containerd/containerd/commit/3050b3664006ac2aa335f256f359b49dd80b464b) Merge pull request [#3615](https://github.com/containerd/containerd/pull/3615) from dmcgowan/fix-proxy-plugin-config
- [`a4482d9a6f`](https://github.com/containerd/containerd/commit/a4482d9a6f230091274d45afa0ea34d5cfe6c4d9) Fix proxy plugin config validation
- [`cd79e0edfe`](https://github.com/containerd/containerd/commit/cd79e0edfe815875f33609e839caff2a4b914b55) travis: fix Xenial tests not being run on master
- [`f7bd7e309c`](https://github.com/containerd/containerd/commit/f7bd7e309cd91e0fa08f1a0168dff55f17d2eeb2) Merge pull request [#3611](https://github.com/containerd/containerd/pull/3611) from Random-Liu/fix-panic-for-unknown-task
- [`24f7585ed8`](https://github.com/containerd/containerd/commit/24f7585ed83b788cc89a153b9e4b42c9174170ed) Merge pull request [#3610](https://github.com/containerd/containerd/pull/3610) from Random-Liu/fix-containerd-panic
- [`c410f0eaef`](https://github.com/containerd/containerd/commit/c410f0eaef7eae2d73d51387bdf30834e9b72ec9) Fix potential panic for task in unknown state
- [`dd24d76a13`](https://github.com/containerd/containerd/commit/dd24d76a1383333b316e340acfa8b62bd2621e63) Fix potential containerd panic during graceful shutdown
- [`f4927a2985`](https://github.com/containerd/containerd/commit/f4927a2985da06e3050008b6bb9f4837020f3e71) fix mis-spelling in nvidia.go
- [`d177ffd309`](https://github.com/containerd/containerd/commit/d177ffd309ba9a424db6d155c85992f1105638a5) Merge pull request [#3590](https://github.com/containerd/containerd/pull/3590) from tanjunchen/fix-grammar-mistake
- [`92a5b08a68`](https://github.com/containerd/containerd/commit/92a5b08a68b9986e73976147ef26d01bd14fb97d) fix-grammar-mistake
- [`cbfff2fb78`](https://github.com/containerd/containerd/commit/cbfff2fb789ae8b6f2233a13fe123a1a2cd53e21) Merge pull request [#3585](https://github.com/containerd/containerd/pull/3585) from tanjunchen/fix-up-spelling-mistake
- [`8266a3c5e7`](https://github.com/containerd/containerd/commit/8266a3c5e7d7150fa323975e72f8adff0b52c11e) fix-up spelling mistake
- [`aae2d0d754`](https://github.com/containerd/containerd/commit/aae2d0d754a75ad523cb27e8f386b2cd2cc7b1ed) delete unnecessary checks and fix a test
- [`bca0857530`](https://github.com/containerd/containerd/commit/bca0857530d1ead52d03595b1558bfe98112d187) Fix toml plugin decoding
- [`89eae6429f`](https://github.com/containerd/containerd/commit/89eae6429f5e4a2e2e6cdf65f82357fb27779e61) Cleanup: fix some typos in code comment
- [`bd46ea5191`](https://github.com/containerd/containerd/commit/bd46ea519173cc28445da9b2a031b6139e18eb05) Merge pull request [#3570](https://github.com/containerd/containerd/pull/3570) from dmcgowan/fix-apply-trailing-data
- [`bb4c92c773`](https://github.com/containerd/containerd/commit/bb4c92c773e195b86af92d5db26db6ca67164d7c) Fix shim hung
- [`3ef26cd87c`](https://github.com/containerd/containerd/commit/3ef26cd87c73ec62c9dda1c17800416fc2323e8d) bump x/sys to fix riscv64 epoll
- [`dce8541387`](https://github.com/containerd/containerd/commit/dce8541387a5e8e6fefe3f921c40b4ee1a9ac50e) Merge pull request [#3493](https://github.com/containerd/containerd/pull/3493) from dmcgowan/fix-travis-matrix
- [`2398421d50`](https://github.com/containerd/containerd/commit/2398421d50978b653398f3ead57ec243fb0ff665) Fix travis matrix
- [`ca2463a719`](https://github.com/containerd/containerd/commit/ca2463a7196a992935e5365eacbff1e9e5a0d44f) Merge pull request [#3485](https://github.com/containerd/containerd/pull/3485) from Random-Liu/fix-containerd-on-windows
- [`bb99688914`](https://github.com/containerd/containerd/commit/bb9968891449193c8a074b1a97fe0e850092612d) Fix containerd on windows
- [`d3e539af79`](https://github.com/containerd/containerd/commit/d3e539af799057ccd832c44e5bf333c1a506c558) Merge pull request [#3480](https://github.com/containerd/containerd/pull/3480) from dmcgowan/fix-export-named-manifest-opt
- [`69d65c9764`](https://github.com/containerd/containerd/commit/69d65c9764e196ea3d5e186fb93bcad72f497cec) Merge pull request [#3476](https://github.com/containerd/containerd/pull/3476) from dmcgowan/fix-push-exist-check
- [`3e52e29025`](https://github.com/containerd/containerd/commit/3e52e290259c463152e0c8dac0de2f76f491d270) Fix bug in export named manifest option
- [`612628c2f9`](https://github.com/containerd/containerd/commit/612628c2f9b8e04828f306d5bbf156570e2e79eb) fix wrong spells in compression.go
- [`e3cc9c20cb`](https://github.com/containerd/containerd/commit/e3cc9c20cb63e0dc35f35c273556216f57d699c9) bug fix:#3448
- [`c27e48d666`](https://github.com/containerd/containerd/commit/c27e48d666764937bcea75adf3581c7fada471ed) fix mis-spelling in client.go
- [`29930e9185`](https://github.com/containerd/containerd/commit/29930e918597c91a353669dd606c4b079b2a09e1) Merge pull request [#3455](https://github.com/containerd/containerd/pull/3455) from dmcgowan/fix-default-import-compression
- [`c00517a94c`](https://github.com/containerd/containerd/commit/c00517a94c80c0e5540097d4068c850f46888038) Made fixes and optimizations to encryption GC
- [`5631fe3b32`](https://github.com/containerd/containerd/commit/5631fe3b32e004b7c43fc267e1a08165e1289e8c) Merge pull request [#3431](https://github.com/containerd/containerd/pull/3431) from dmcgowan/fix-nil-body
- [`518be1cb07`](https://github.com/containerd/containerd/commit/518be1cb070551e5cd8e69f9cea33f7abd5cfdca) Fix bug in setting request body
- [`063a4ff278`](https://github.com/containerd/containerd/commit/063a4ff27844fb1e751499cd8f6df5ad249d4e0d) Merge pull request [#3419](https://github.com/containerd/containerd/pull/3419) from AkihiroSuda/fix-task-start
- [`ce0d2489ac`](https://github.com/containerd/containerd/commit/ce0d2489acdcd93ef6d213d855fec1f2e2cb22b8) Fix regiression from #3403 with snapshot cmd
- [`ef7f46eb7b`](https://github.com/containerd/containerd/commit/ef7f46eb7bff5fad55b108027332a2938f77066a) Fix linter errors
- [`abc152d14c`](https://github.com/containerd/containerd/commit/abc152d14c950a64deb833b597082b68eaf5ea06) fix name in containers file
- [`70b00a0fa9`](https://github.com/containerd/containerd/commit/70b00a0fa9b1e754758153d9d649c4fb56fcd02c) fix variable name
- [`4988424fc0`](https://github.com/containerd/containerd/commit/4988424fc0c459f5a07ce1cd1d5f39fa6ebf39f1) * fix: view snapshot is deleted before diff
- [`550a6f1d73`](https://github.com/containerd/containerd/commit/550a6f1d733ad4960ecbe8247c6cb2a545d7dd66) Fix integration tests
- [`7d21172453`](https://github.com/containerd/containerd/commit/7d21172453876b17915c141d3522f06dc7a90db8) Fix metadata content store to call writer digest after commit
- [`174c4907d0`](https://github.com/containerd/containerd/commit/174c4907d0cb23cbb5d80c95e6dcfb42d0f31164) Fix shim's file IO logging
- [`12a14c4424`](https://github.com/containerd/containerd/commit/12a14c4424208a90d2344b0b893c57452a9eb9ad) fix: polish log to make more clear
- [`fbf96d302a`](https://github.com/containerd/containerd/commit/fbf96d302aff95f8c52ab0161e7ff8ae7d33b9b9) Fix path in LogFile creator
- [`5e0d793801`](https://github.com/containerd/containerd/commit/5e0d793801aefe1be5740a26771c9d30dac46f90) Fix bugs in BinaryIO creator
- [`434f69e790`](https://github.com/containerd/containerd/commit/434f69e7906454e0177ff06d711614c34af9bf4e) Merge pull request [#3353](https://github.com/containerd/containerd/pull/3353) from mikebrow/fix-slack-invite
- [`41e1bb8328`](https://github.com/containerd/containerd/commit/41e1bb83289568c12866ae22803fbfb8b7eaf536) Fix snapshotter getter in client code
- [`667195fdd9`](https://github.com/containerd/containerd/commit/667195fdd96be38a88a2a426d6da11591c2d4c54) Merge pull request [#3339](https://github.com/containerd/containerd/pull/3339) from YLonely/typo-fix
- [`d15a06b190`](https://github.com/containerd/containerd/commit/d15a06b1909acd6d6d0996858d7e91b410a0baa8) docs: Fix typo to some markdown files in /docs
- [`31afff2944`](https://github.com/containerd/containerd/commit/31afff294400b5a69bdb3ec387ecdf5bad57a038) Fix backwards compat with v2 containerd configs
- [`53896d7820`](https://github.com/containerd/containerd/commit/53896d7820a3a6e6dac5767c42fd2cd33e7b0d2c) Merge pull request [#3335](https://github.com/containerd/containerd/pull/3335) from dmcgowan/fix-user-agent
- [`9e0cd529d3`](https://github.com/containerd/containerd/commit/9e0cd529d35a9951f292ed35940f1cd6eff99a39) fix shim std logs not close after shim exit
- [`48a1fca855`](https://github.com/containerd/containerd/commit/48a1fca855215c98fbb622cdb1cab4b40077fd77) Merge pull request [#3314](https://github.com/containerd/containerd/pull/3314) from KentaTada/fix-clone-seccomp-cgroupns
- [`5b9a43d2e7`](https://github.com/containerd/containerd/commit/5b9a43d2e7aff575a398477a9b13b29a313f15a6) Fix seccomp contributed profile for clone syscall
- [`a274dbe822`](https://github.com/containerd/containerd/commit/a274dbe82258d40e8fd09dc2c8f4331717e1045d) Fix run with specified platform
- [`b7f093eaa2`](https://github.com/containerd/containerd/commit/b7f093eaa2785af9ca41ea27d0fd2a15a34603a2) Merge pull request [#3296](https://github.com/containerd/containerd/pull/3296) from dmcgowan/fix-export-labels
- [`2088fc999c`](https://github.com/containerd/containerd/commit/2088fc999c20cb9759b0b537276e608f918e7c16) Merge pull request [#3294](https://github.com/containerd/containerd/pull/3294) from dmcgowan/fix-metadata-panic
- [`62609d66d0`](https://github.com/containerd/containerd/commit/62609d66d06a963036bc368a72f0524559d55dc2) Fix typo in description comment
- [`cf6e008542`](https://github.com/containerd/containerd/commit/cf6e0085423af8938a16c850ff5607dad4ca7c73) Fix fd leak of shim log
- [`d68b593de4`](https://github.com/containerd/containerd/commit/d68b593de4ab10bb8b4fd64560e10d43c7156db2) Merge pull request [#3263](https://github.com/containerd/containerd/pull/3263) from Random-Liu/fix-task-deletion
- [`660554d671`](https://github.com/containerd/containerd/commit/660554d671f41e0a96851b8012dd626e34f53f38) Fix error handling for task deletion
- [`836cf53e40`](https://github.com/containerd/containerd/commit/836cf53e403e539ff4fa146b3f32b82810d0c0a5) Merge pull request [#3244](https://github.com/containerd/containerd/pull/3244) from Random-Liu/fix-container-cleanup
- [`2f22d8e677`](https://github.com/containerd/containerd/commit/2f22d8e67735eff5e4499c66f8a503b0c87841dc) Fix broken link to containerd logo
- [`eded188f4f`](https://github.com/containerd/containerd/commit/eded188f4fbb24f7a0c3f58e61a28ddfd277c6a5) Fix misspells
- [`5b9bd993a8`](https://github.com/containerd/containerd/commit/5b9bd993a87008e06a34258f0672a78564adab13) differ: fix deadlock on commit error
- [`a4942ca4fe`](https://github.com/containerd/containerd/commit/a4942ca4fe45b75ad4873f33d2cec44ce2d6a3e3) Fix error on pull hang in CI
- [`4c16017e2f`](https://github.com/containerd/containerd/commit/4c16017e2f372598d5169965d1c8758cc1bfcce5) Merge pull request [#3209](https://github.com/containerd/containerd/pull/3209) from Random-Liu/fix-v1-shim-cleanup
- [`8722ec03c3`](https://github.com/containerd/containerd/commit/8722ec03c3a11874d47fbd7468d4473507d0d95f) Merge pull request [#3213](https://github.com/containerd/containerd/pull/3213) from jcordasc/small-fixes
- [`acca107732`](https://github.com/containerd/containerd/commit/acca10773205905a96ada4f6590a65265c535daa) Merge pull request [#3204](https://github.com/containerd/containerd/pull/3204) from crosbymichael/fix-forward
- [`4ba756edda`](https://github.com/containerd/containerd/commit/4ba756edda18c0afac99a32ba89bc6070c27a0f1) Fix API forward events for shims
- [`c22effb168`](https://github.com/containerd/containerd/commit/c22effb1686972d1a12f9aa32f1ad06d1aa253f0) fix parseInfoFile does not handle spaces in filenames
- [`872296642a`](https://github.com/containerd/containerd/commit/872296642ac395acbc4344f529fcf4c6fddb5de2) fix shouldKillAllOnExit check for v2
- [`fa5f744a79`](https://github.com/containerd/containerd/commit/fa5f744a790356472d4649b9ad1d955e36d0c7c0) fix shouldKillAllOnExit check
- [`f2a20ead83`](https://github.com/containerd/containerd/commit/f2a20ead833f8caf3ffc12be058d6ce668b4ebed) Merge pull request [#3137](https://github.com/containerd/containerd/pull/3137) from Random-Liu/fix-race-and-panic
- [`808b223536`](https://github.com/containerd/containerd/commit/808b223536e6553ddee2944d7ec6bc6d86e0da88) Fix race and panic
- [`9ab4c8cbcc`](https://github.com/containerd/containerd/commit/9ab4c8cbcc3846bf89eeff2f7d9f7bdd85994878) Merge pull request [#3108](https://github.com/containerd/containerd/pull/3108) from alculquicondor/fix/import
- [`14a050688d`](https://github.com/containerd/containerd/commit/14a050688d4be028a56a9a52f1358091d52acad2) ctr: fix image cmd ArgsUsage
- [`160737d2c8`](https://github.com/containerd/containerd/commit/160737d2c803cec1a19f45e0a552ef1670e486ee) Fix no pivot and keyring opts
- [`30b6f460b9`](https://github.com/containerd/containerd/commit/30b6f460b96137947b3de5ec92134d56cb763708) Merge pull request [#3063](https://github.com/containerd/containerd/pull/3063) from zhsj/fix-mipsx
- [`277147135d`](https://github.com/containerd/containerd/commit/277147135d64661914040085d6630e39a1f507d3) Fix issue with NewFIFOSetInDir with Terminal true
- [`828f6eb842`](https://github.com/containerd/containerd/commit/828f6eb842451a3bb9577b731e2e09bbd59d0e42) Fix a bug in shim log on Windows that can cause 100% CPU utilization
- [`37cdedc61c`](https://github.com/containerd/containerd/commit/37cdedc61c902047e9f97759196d30e0b5a9ba01) devmapper: add linux tags, fix build
- [`0c6d194cce`](https://github.com/containerd/containerd/commit/0c6d194ccef882e9424c2078949eb2f4bb8076f1) devmapper: add README and minor fixes
- [`58dc0677b4`](https://github.com/containerd/containerd/commit/58dc0677b43011d0a6b44f232e0c7e3e0e876412) Merge pull request [#3030](https://github.com/containerd/containerd/pull/3030) from veerun14/venuvvul/add-comments-fix-typos
- [`bfb266ab5d`](https://github.com/containerd/containerd/commit/bfb266ab5d24fa05809aa800b5fc785cb55992b3) Fix some misspells in helpers_test.go
- [`225d9b120c`](https://github.com/containerd/containerd/commit/225d9b120c139688a43a25ba34500c0e6a4dd4c9) Fix LCOW layer ordering
- [`5ba368748b`](https://github.com/containerd/containerd/commit/5ba368748b0275d8f45f909413d94738992f0050) Merge pull request [#2976](https://github.com/containerd/containerd/pull/2976) from Random-Liu/fix-potential-panic
- [`7bd8dcd0d3`](https://github.com/containerd/containerd/commit/7bd8dcd0d30fa565b1b2f31f1ebd53b9a1aa029d) Fix potential containerd panic
- [`f014adfa17`](https://github.com/containerd/containerd/commit/f014adfa1740bd7b4f12bf5bb70c2b261b7f1883) readme: fix example for checkpoint
- [`6b25c1e45c`](https://github.com/containerd/containerd/commit/6b25c1e45c2b8246dba17de3b1d574f6720ce79f) Merge pull request [#2970](https://github.com/containerd/containerd/pull/2970) from Random-Liu/fix-exec-race-condition
- [`dfcc5942f1`](https://github.com/containerd/containerd/commit/dfcc5942f152471dd9373afc0750e3f04e0fb111) Fix deadlock in Windows runhcs shim exec
- [`6ed293ba94`](https://github.com/containerd/containerd/commit/6ed293ba94a0751b3d5c0b332978b5ccb8222768) Fix bug in shim path lookup
- [`3762378760`](https://github.com/containerd/containerd/commit/37623787603e0ab61efda2a5964d92c68b67e79d) Merge pull request [#2944](https://github.com/containerd/containerd/pull/2944) from Random-Liu/fix-stdin-close
- [`132ee9b826`](https://github.com/containerd/containerd/commit/132ee9b826df4ae99e3f98d2e028128a1b79afda) fix: linter issue
- [`c5a8c9fc12`](https://github.com/containerd/containerd/commit/c5a8c9fc12555b0229c1fd8f1c75d8b838656d69) Fix issue in runhcs shim CloseIO
- [`31616e7945`](https://github.com/containerd/containerd/commit/31616e7945ab37f659c97edba4e0238053cfb3c4) Fix runhcs shim bug in Create with "len(Rootfs) == 0"
- [`bcd4cc51c8`](https://github.com/containerd/containerd/commit/bcd4cc51c853081b8e4b1cf5c548b9e6a515ce14) Fixes a bug in runhcs shim Exec.Pid
- [`adfaa697a8`](https://github.com/containerd/containerd/commit/adfaa697a8b778eb319a49c02406c84bc0f1bdf9) Merge pull request [#2887](https://github.com/containerd/containerd/pull/2887) from andrey-ko/args-fix
- [`dee0945e18`](https://github.com/containerd/containerd/commit/dee0945e184a067b2adc2562e3d2734e696f5018) Fix spurious ttrpc client shutdown error log on success
- [`17b77aeb0e`](https://github.com/containerd/containerd/commit/17b77aeb0efdd9d0aef96d9f270e1ece4126841e) Fix annotation typo errors
- [`7faaa64cf9`](https://github.com/containerd/containerd/commit/7faaa64cf987db33eaa663e29068bf84d07c69f5) fix: miss remove temp file in createSnapshot
- [`da9471fb11`](https://github.com/containerd/containerd/commit/da9471fb1114cee9e977485e0d39a51237d84d7a) fix oci.WithImageConfigArgs for windows
- [`897afeaf35`](https://github.com/containerd/containerd/commit/897afeaf35b6d18a91cdf87b563e8ba78ae11869) Revert "Fix CI due to Golang 1.10.6 / 1.11.3 regressions (workaround)"
- [`b62f3b6fe9`](https://github.com/containerd/containerd/commit/b62f3b6fe914786446546f96a14f6df03fc61de7) Merge pull request [#2883](https://github.com/containerd/containerd/pull/2883) from ZYecho/fix-args
- [`081921628e`](https://github.com/containerd/containerd/commit/081921628e11e759e1a2a9ba84cbc737b8d6da79) Merge pull request [#2875](https://github.com/containerd/containerd/pull/2875) from ZYecho/fix-defer
- [`40267382c5`](https://github.com/containerd/containerd/commit/40267382c54e5d704f23d4040f1678c2ab5e654b) fix ctr image export not found error
- [`8be05eb237`](https://github.com/containerd/containerd/commit/8be05eb237a026d797deba448eef3cf54b8fce7e) Fix freebsd build
- [`7b1e6f323a`](https://github.com/containerd/containerd/commit/7b1e6f323ae6dd5316c30d71d3d7cc5361bea27e) fix: use func args instead of build new one
- [`9baecf66b8`](https://github.com/containerd/containerd/commit/9baecf66b815b8c9e6a3250bc3f06b6705780bb8) fix: fix defer in loop
- [`903abf33cf`](https://github.com/containerd/containerd/commit/903abf33cf1c1f2e53873cc08a69d35f87a14352) Fix annotation typo error
- [`52de371700`](https://github.com/containerd/containerd/commit/52de3717005eb20141c305bd93ff0d6ee5dfecb6) Fix CI due to Golang 1.10.6 / 1.11.3 regressions (workaround)
- [`155d7acb01`](https://github.com/containerd/containerd/commit/155d7acb014671bc675367ec99cad8144548802c) Merge pull request [#2874](https://github.com/containerd/containerd/pull/2874) from ZYecho/fix-deadcode
- [`6f944e4190`](https://github.com/containerd/containerd/commit/6f944e41909625e90540585c0032a33c9b5be801) fix: SCHILY.xattrs should be SCHILY.xattr
- [`6ccb0d0629`](https://github.com/containerd/containerd/commit/6ccb0d0629d91d5ca174d41b97fa6e056d652f9a) fix: remove dead code
- [`a0fe7f0f78`](https://github.com/containerd/containerd/commit/a0fe7f0f783495857a3d8ca9d593c6821ff38c1f) Merge pull request [#2829](https://github.com/containerd/containerd/pull/2829) from ZYecho/fix-error
- [`996c60616a`](https://github.com/containerd/containerd/commit/996c60616a9e6252ac4ffbd5a69172537425de88) fix: fix error info start capitalized
- [`461222dba8`](https://github.com/containerd/containerd/commit/461222dba8c2f3410fc702237a8bc7defc091a77) fix: should get runtime name from container info
- [`f801661dcf`](https://github.com/containerd/containerd/commit/f801661dcf1838e1ee2da4a82347a6708bb9fa66) Merge pull request [#2809](https://github.com/containerd/containerd/pull/2809) from HusterWan/zr/octet-stream-fix
- [`e76a8879eb`](https://github.com/containerd/containerd/commit/e76a8879eb10594113d70556c80dd2e456202e22) fix pipe in broken may cause shim lock forever for runtime v1
- [`b3438f7a6f`](https://github.com/containerd/containerd/commit/b3438f7a6f63849d2179a2a76b804aea460affd9) fix pipe in broken may cause shim lock forever for runtime v2
- [`bd2a21985c`](https://github.com/containerd/containerd/commit/bd2a21985cc473c2b36cff5de05e482872bdc79e) fix container cmd args may parsed as ctr args
- [`831a41b958`](https://github.com/containerd/containerd/commit/831a41b9585fc021c1036da17afa1513e7b4f908) Fix process locking and state management
- [`c4feaa75cf`](https://github.com/containerd/containerd/commit/c4feaa75cf37cf0af272e443c2d5c6dd632dcc5c) fix: fix failed to get container-shim relation with io.containerd.runc.v1
- [`7d70d2b78d`](https://github.com/containerd/containerd/commit/7d70d2b78dd3917f5da4fd233483fd903dfb2919) Fix Makefile to run protobuild on paths with spaces
- [`f1a3a6fba6`](https://github.com/containerd/containerd/commit/f1a3a6fba616861b9f0d472b816ff70cf744307a) Merge pull request [#2760](https://github.com/containerd/containerd/pull/2760) from estesp/fix-appveyor-mingw-vers
- [`2bb7da8431`](https://github.com/containerd/containerd/commit/2bb7da8431adf035a137baaed9ac7897f1d85cf6) Fix mingw version back to working version with Golang
- [`9035063a5b`](https://github.com/containerd/containerd/commit/9035063a5b3a3d93d45eff6473a8c60365e00918) Merge pull request [#2753](https://github.com/containerd/containerd/pull/2753) from Charliekenney23/fix-typo-resolveroptions-docs
- [`7c85d873a0`](https://github.com/containerd/containerd/commit/7c85d873a006bafe6d5ec9dd94751018a5c76a70) fix typo in ResolverOptions.Credentials documentation
- [`13a3ac4`](https://github.com/containerd/cgroups/commit/13a3ac4f154c85e85ffc2eb9709387e5040548f7) fixed an issue with invalid soft memory limits
- [`db27230`](https://github.com/containerd/cgroups/commit/db272301ab8449d05f062e6db6f13d8a6aaff466) Merge pull request [#88](https://github.com/containerd/cgroups/pull/88) from woshijpf/fix-cgroup-left-problem
- [`0ecd2b6`](https://github.com/containerd/cgroups/commit/0ecd2b66d378b21c371721046c14d9f23bc07877) cgroups: fix MoveTo function fail problem
- [`42091f5`](https://github.com/containerd/cgroups/commit/42091f5cd88c6ce37c803d5f7a807197a3659aaa) Merge pull request [#85](https://github.com/containerd/cgroups/pull/85) from odinuge/cgroups-hugetlb-fix
- [`51dcf5f`](https://github.com/containerd/cgroups/commit/51dcf5fa00efa7947e3f454333e254ee97139226) Fix cgroup hugetlb size prefix for kB
- [`6b552a8`](https://github.com/containerd/cgroups/commit/6b552a86e60e31903d3f8f3f494eda71f562cc54) Fix net_prio typo
- [`4479d11`](https://github.com/containerd/cgroups/commit/4479d118c89b5500a08cce7a78bbe822229c1e65) Merge pull request [#62](https://github.com/containerd/cgroups/pull/62) from estesp/fix-gofmt
- [`9a09e58`](https://github.com/containerd/cgroups/commit/9a09e5899acc95fabcc620d6489fec674e6dddfa) Fix gofmt of systemd.go
- [`0f3de2f`](https://github.com/containerd/cgroups/commit/0f3de2f77d3b76b3871242fbab2a6116179229af) Fix empty device type
- [`f2a389a`](https://github.com/containerd/continuity/commit/f2a389ac0a02ce21c09edd7344677a601970f41c) Merge pull request [#142](https://github.com/containerd/continuity/pull/142) from dmcgowan/fix-fstests
- [`9ca0eb9`](https://github.com/containerd/continuity/commit/9ca0eb98eb6fc5ecc23953cb3242946a1219bd19) Fix fstest missing file updates
- [`aaeac12`](https://github.com/containerd/continuity/commit/aaeac12a7ffcd198ae25440a9dff125c2e2703a7) Merge pull request [#140](https://github.com/containerd/continuity/pull/140) from dmcgowan/fix-directory-comparison
- [`5a839c7`](https://github.com/containerd/continuity/commit/5a839c78cafc28b9d72643b577a36df2e66f8b5a) Fix directory comparison in changes
- [`bea7585`](https://github.com/containerd/continuity/commit/bea7585dbfac2847dbf49a6b8e7738a36c09bc75) Merge pull request [#122](https://github.com/containerd/continuity/pull/122) from poizan42/fix-mips
- [`9621bb9`](https://github.com/containerd/continuity/commit/9621bb9b56b02056aab3d7cb07434e77febeed20) Fix copy_file_range usage for files > 2GB on 32-bit archs
- [`53ca3b35`](https://github.com/containerd/cri/commit/53ca3b35e09e287b0aa9954a87c4708ebfd27bef) Backport fix for default path env for CRI created OCI config
- [`2a3928b2`](https://github.com/containerd/cri/commit/2a3928b2d389486c21a0dfcbbcaad4b4e6715653) Fix panic for task in unknown state
- [`4eff3e25`](https://github.com/containerd/cri/commit/4eff3e25a7e6b57decc375e950465ec7457d195c) fix: support empty auth config for anonymous registry
- [`eed39566`](https://github.com/containerd/cri/commit/eed3956689afc616d8b9e1e74d1259e0bfc1ca12) Merge pull request [#1240](https://github.com/containerd/cri/pull/1240) from Random-Liu/fix-apparmor-privileged
- [`10acd8e7`](https://github.com/containerd/cri/commit/10acd8e7699d2014057e57bed9a7648c8097eb0e) Fix apparmor for privileged
- [`a4b145ad`](https://github.com/containerd/cri/commit/a4b145adbbf45c2b61d4753620d322ccd39752c4) Merge pull request [#1234](https://github.com/containerd/cri/pull/1234) from Random-Liu/update-containerd-to-fix-race
- [`7f330dc4`](https://github.com/containerd/cri/commit/7f330dc4aa4bd6b2b051f45209c480d0899a5e42) Update containerd to fix panic caused by race condition
- [`fe5eb76c`](https://github.com/containerd/cri/commit/fe5eb76cb488e186584bbe923d61099d2c4b0f28) Merge pull request [#1209](https://github.com/containerd/cri/pull/1209) from Random-Liu/fix-proc-mount-support
- [`467f9e0e`](https://github.com/containerd/cri/commit/467f9e0e8a10097b793726bf89aeaa661a2e4007) Fix proc mount support
- [`5fdb4b8e`](https://github.com/containerd/cri/commit/5fdb4b8eefae630401832c2fa30ef326de7ddfb9) Merge pull request [#1204](https://github.com/containerd/cri/pull/1204) from Random-Liu/fix-ctr-readiness-check
- [`e83fe560`](https://github.com/containerd/cri/commit/e83fe56075ed1a0727a88fc33c24710b07dd14cf) Fix ctr readiness check in test
- [`64bf4beb`](https://github.com/containerd/cri/commit/64bf4bebf31cc155bcce456095ac92671583a2e8) Merge pull request [#1188](https://github.com/containerd/cri/pull/1188) from alculquicondor/fix/doc
- [`eaf792ed`](https://github.com/containerd/cri/commit/eaf792ed7bcbd406cbfee45e119c52f4b10290d8) Merge pull request [#1180](https://github.com/containerd/cri/pull/1180) from Random-Liu/fix-version
- [`6afd137c`](https://github.com/containerd/cri/commit/6afd137c026ee2133dddb22bc9a8d405852df674) Fix runc and critools version in release
- [`806c2641`](https://github.com/containerd/cri/commit/806c2641a1945db654964f901165ed6e7719cf51) Merge pull request [#1178](https://github.com/containerd/cri/pull/1178) from mikebrow/fix-slack-link
- [`55e5ce0e`](https://github.com/containerd/cri/commit/55e5ce0e951ee4675af88fe0c0f3cdccd5253fd1) Fix http client when TLS is enabled
- [`1275d6de`](https://github.com/containerd/cri/commit/1275d6ded393fd0582842c5996199451d2642303) Merge pull request [#1162](https://github.com/containerd/cri/pull/1162) from Random-Liu/fix-image-pull
- [`1c826eb6`](https://github.com/containerd/cri/commit/1c826eb6892d3bcc2ed04360f8cffd7dd6548b4f) Merge pull request [#1165](https://github.com/containerd/cri/pull/1165) from ZYecho/fix-link
- [`397adbab`](https://github.com/containerd/cri/commit/397adbab859bcc2750734d845f64f36962e57353) fix: fix CRI dead link
- [`8ba5c02f`](https://github.com/containerd/cri/commit/8ba5c02f8f249c1f6edb5e34ff99bd43cf49a92b) Fix typo in WithoutRunMount
- [`47fc6456`](https://github.com/containerd/cri/commit/47fc6456827e9424530fa39d58d8d3debcc84b6a) Integration test task.Delete fix
- [`fa759f6a`](https://github.com/containerd/cri/commit/fa759f6a1b93d4d6a3a09c7e6235e2b90996f8d1) Merge pull request [#1130](https://github.com/containerd/cri/pull/1130) from Random-Liu/fix-status-hang
- [`63ad4c73`](https://github.com/containerd/cri/commit/63ad4c7305576d96477ef779b0d8a5cfb87554d3) Merge pull request [#1114](https://github.com/containerd/cri/pull/1114) from Random-Liu/fix-extra-handler
- [`b23b406f`](https://github.com/containerd/cri/commit/b23b406fedd2009f813c36206865ae2a8c51d5bb) Merge pull request [#1102](https://github.com/containerd/cri/pull/1102) from Random-Liu/uts-namespace-and-fix-array
- [`3691cb65`](https://github.com/containerd/cri/commit/3691cb6550c6eee1fb9957681b00e986b7a5d288) Fix /etc/hostname backward compatibility issue for in-place upgrade
- [`8d752611`](https://github.com/containerd/cri/commit/8d75261190509c46a4ff86a8cc91401e71143487) Merge pull request [#1065](https://github.com/containerd/cri/pull/1065) from alculquicondor/fix/architecture
- [`c88e18b9`](https://github.com/containerd/cri/commit/c88e18b907f10ce10aa395631d80fd7ec41d36f3) Fix architecture doc
- [`b2cd8400`](https://github.com/containerd/cri/commit/b2cd840042d843e110625b5fd38db68b549377be) Merge pull request [#1045](https://github.com/containerd/cri/pull/1045) from Random-Liu/fix-env-performance-issue
- [`97c7a1b1`](https://github.com/containerd/cri/commit/97c7a1b17b8198f242db429072ec1306cbca209a) Merge pull request [#1027](https://github.com/containerd/cri/pull/1027) from Random-Liu/fix-log-ending-newline
- [`556b2194`](https://github.com/containerd/cri/commit/556b2194501d51e18ae6dd870a8579a56509b81f) Fix lint error
- [`50ac4009`](https://github.com/containerd/cri/commit/50ac40097ee458f07aaeab97dadbf80b4fcddbc7) Fix the log ending newline handling
- [`ae1b7ac4`](https://github.com/containerd/cri/commit/ae1b7ac4fd8e4b5707b90b14bbf28b1159ff07c0) Fix some typos in comment
- [`3bfef015`](https://github.com/containerd/cri/commit/3bfef0158951049d96716814f99d4c79b02053c7) Fix the issue that pod or container config file without metadata will crash containerd
- [`55fb3b9f`](https://github.com/containerd/cri/commit/55fb3b9fce4cf3ff1bf0011d273eed9c0d7e8b1f) Fix return error message
- [`a9f3c86c`](https://github.com/containerd/cri/commit/a9f3c86cc12f7dd484b726919729accf9b5d1171) Merge pull request [#1004](https://github.com/containerd/cri/pull/1004) from Random-Liu/fix-build
- [`5d5fc154`](https://github.com/containerd/cri/commit/5d5fc154ad6f36aa39cafd389653a84ba19d31d4) Revert "Temporary fix for golang regression #29241."
- [`afb12d72`](https://github.com/containerd/cri/commit/afb12d728ce51d2b29ebdbf659e53fcc275045ff) Merge pull request [#997](https://github.com/containerd/cri/pull/997) from Random-Liu/fix-for-golang-issue
- [`d7f6721d`](https://github.com/containerd/cri/commit/d7f6721de591f9a46ebfdc8ed8de83a71d80743c) Temporary fix for golang regression #29241
- [`d53bcba9`](https://github.com/containerd/cri/commit/d53bcba99149b25a5b46365e06852cbc97e5556c) Fix some typo errors
- [`37085692`](https://github.com/containerd/cri/commit/37085692e28a7584967374f085e2b94c16b54869) fix spelling error: contaner -> container
- [`f58105a7`](https://github.com/containerd/cri/commit/f58105a71c92cd68e68e731dd9ebf9b7e85b91ce) Merge pull request [#983](https://github.com/containerd/cri/pull/983) from Random-Liu/fix-shared-pid-ns-kill
- [`de967051`](https://github.com/containerd/cri/commit/de967051d488d415f7c2b66b4fd89cf2467536a9) Fix kill when shared pid namespace
- [`64b067d9`](https://github.com/containerd/cri/commit/64b067d93fab68368be7dd58f1e13a1d1215c6ad) fix integration test
- [`728f636e`](https://github.com/containerd/cri/commit/728f636e32c97ea9c67dc9a654eaf19d2de0b801) Merge pull request [#949](https://github.com/containerd/cri/pull/949) from Random-Liu/fix-ip-leakage
- [`8b0d53c0`](https://github.com/containerd/cri/commit/8b0d53c09c41d9fbc3b3896548ecf011518e3c42) Merge pull request [#941](https://github.com/containerd/cri/pull/941) from amshinde/fix-go-compile-error
- [`54b1c00b`](https://github.com/containerd/cri/commit/54b1c00b3b307b0fadd10c02d9467a6545c2c4d5) test: Fix compile error with go1.10.2
- [`801882b0`](https://github.com/containerd/cri/commit/801882b046562ed1cf0299c8e4130e3f0865dcc6) Merge pull request [#935](https://github.com/containerd/cri/pull/935) from mikebrow/makefile-fix-for-syntax
- [`6de38f1f`](https://github.com/containerd/cri/commit/6de38f1f3ab99b96b9bbf1723084a658dc676002) Merge pull request [#927](https://github.com/containerd/cri/pull/927) from Random-Liu/fix-readiness-check
- [`68152dab`](https://github.com/containerd/cri/commit/68152dab84f403f9789e3e80c4aed9c186ee63e6) Fix readiness check in test utils
- [`d963c9c5`](https://github.com/containerd/cri/commit/d963c9c58eb4cde524278919310fb066cfd2931c) Merge pull request [#920](https://github.com/containerd/cri/pull/920) from Random-Liu/fix-indent
- [`17c7e3a`](https://github.com/containerd/fifo/commit/17c7e3ac42ee4479da01e97d3e17cd6c51042447) Fix indent in errors.go
- [`8f8e80a`](https://github.com/containerd/go-cni/commit/8f8e80adbf4c65df18feb20d326c8d67fca0ff77) Fix some typos in comment (#34)
- [`9007c24`](https://github.com/containerd/go-runc/commit/9007c2405372fe28918845901a3276c0915689a1) Merge pull request [#52](https://github.com/containerd/go-runc/pull/52) from Ace-Tang/fix-error-return
- [`4e99c72`](https://github.com/containerd/go-runc/commit/4e99c72acdb052ba374135c009bbc8ac9dd68249) Fix Method of judging command execution failure
- [`271238a`](https://github.com/containerd/ttrpc/commit/271238abf2f97c4f48f466e71641382b7b5257d1) Fix method full name generation
- [`3afb82b`](https://github.com/containerd/ttrpc/commit/3afb82bd2726e56810fb416d4869420ad6d0b2b1) Fix error handling with server shutdown
- [`ce5c1c4`](https://github.com/containerd/ttrpc/commit/ce5c1c4546907f3b1146f3bb28c1fea8f0094528) Fix returns error message
- [`2ceb2db`](https://github.com/containerd/zfs/commit/2ceb2dbb8154202ed1b8fd32e4ea25b491d7b251) Merge pull request [#24](https://github.com/containerd/zfs/pull/24) from AkihiroSuda/fix-remove-committed
- [`6fde16e`](https://github.com/containerd/zfs/commit/6fde16e2c480f7dc6f61a905744dbd3980bfc340) fix removing Committed

### 1.3.1

- Fix deadlock on image pull and unpack after a registry error [containerd/containerd#3816](https://github.com/containerd/containerd/issues/3816)
- Add local-fs.target to service file to fix corrupt image after unexpected host reboot. Reported in [containerd/containerd#3671](https://github.com/containerd/containerd/issues/3671), and fixed by [containerd/containerd#3745](https://github.com/containerd/containerd/pull/3745)
- Fix large output of processes with TTY getting occasionally truncated. Reported in [containerd/containerd#3738](https://github.com/containerd/containerd/issues/3738) and fixed by [containerd/containerd#3754](https://github.com/containerd/containerd/pull/3754)
- Fix direct unpack when running in user namespace. Reported in [containerd/containerd#3762](https://github.com/containerd/containerd/issues/3762), and fixed by [containerd/containerd#3779](https://github.com/containerd/containerd/pull/3779)
- CRI fixes: Fix shim delete error code to avoid unnecessary retries in the CRI plugin. Discovered in [containerd/cri#1309](https://github.com/containerd/cri/issues/1309), and fixed by [containerd/containerd#3733](https://github.com/containerd/containerd/pull/3733) and [containerd/containerd#3740](https://github.com/containerd/containerd/pull/3740)
- [`ffb05aeb1f`](https://github.com/containerd/containerd/commit/ffb05aeb1f61910dd20a0f0fa9a70c059e0a7051) build: Fix manpage generation
- [`b3e9ded8ce`](https://github.com/containerd/containerd/commit/b3e9ded8ce8211ae39e80320fce1eb64ed706aa0) Fix delete error code on the containerd daemon side
- [`6746ae3e0a`](https://github.com/containerd/containerd/commit/6746ae3e0a4c4fbd33c230542b0e7dfb1108b99c) Fix shim delete error code

### 1.3.2

- Fix containerd pid race condition [containerd/containerd#3857](https://github.com/containerd/containerd/pull/3857)
- [`306d6d4b55`](https://github.com/containerd/containerd/commit/306d6d4b5514399930aa7851dafc7877488b8732) Fix container pid
- [`04fbb97ad0`](https://github.com/containerd/containerd/commit/04fbb97ad016e6f0cc2e09c447aeafb75ff53ea5) Fix cleanup error on content client test
- [`c0dee957`](https://github.com/containerd/cri/commit/c0dee957b994e69146db3b49f78d4ccd8f0cafd2) Fix containerd build, use `libbtrfs-dev` when available

### 1.3.3

- Fix eventfd leak [containerd/containerd#3961](https://github.com/containerd/containerd/pull/3961)
- Fix API filters to properly handle and return parse errors [containerd/containerd#3950](https://github.com/containerd/containerd/pull/3950)
- Update Golang runtime to 1.12.15, which includes a fix to the runtime (Go 1.12.14, Go 1.12.15) and and the `net/http` package (Go 1.12.15)
- [`92dc96af08`](https://github.com/containerd/containerd/commit/92dc96af086472b443be9b89beb9d4d1c1bd1e30) Merge pull request [#3961](https://github.com/containerd/containerd/pull/3961) from sethp-nr/fix/eventfd-leak-1.3-backport
- [`03ee836eea`](https://github.com/containerd/containerd/commit/03ee836eea38c46d798af63d5b10ab3256c9a056) fix: repair bad merge
- [`c458f2fb41`](https://github.com/containerd/containerd/commit/c458f2fb41ecf5d122ec06674aaafa5c6d92e9c1) fix: eventfd leak for v2 runtime with v1 cgroups
- [`258e10ddd6`](https://github.com/containerd/containerd/commit/258e10ddd6c112c646cd49e5084e292d1702ecdd) fix: eventfd leak
- [`eb5e164812`](https://github.com/containerd/containerd/commit/eb5e1648125d9387df7f6e0b72193d7389e169a3) Merge pull request [#3953](https://github.com/containerd/containerd/pull/3953) from dmcgowan/backport-1.3-filters-fix
- [`7d0e217f53`](https://github.com/containerd/containerd/commit/7d0e217f534165d3902d03763ec25f99b8824dff) Fix filter errors
- [`e49256efa5`](https://github.com/containerd/containerd/commit/e49256efa51d1b737acac051f680c255eb0dec13) Fix flaky btrfs test
- [`bc43dc071b`](https://github.com/containerd/containerd/commit/bc43dc071b124840780e9a2b4f1466ca130c13e6) Merge pull request [#3907](https://github.com/containerd/containerd/pull/3907) from estesp/cp-platform-close-fix
- [`945cb97b`](https://github.com/containerd/cri/commit/945cb97bd82126dd5f9a71b1a7cc205d37bdf267) Merge pull request [#1360](https://github.com/containerd/cri/pull/1360) from AkihiroSuda/fix-runcv2-nopivot
- [`63817131`](https://github.com/containerd/cri/commit/6381713164fb69d05626df2776cee3351f4d87b4) [release/1.3] fix NoPivot for RuntimeRuncV2

### 1.3.4

- Correct logic of FIFO cleanup [containerd/containerd#4150](https://github.com/containerd/containerd/pull/4150)
- Man page fixes [containerd/containerd#4144](https://github.com/containerd/containerd/pull/4144)
- [`60bc128245`](https://github.com/containerd/containerd/commit/60bc1282458f5f77d9a541969642f972d28d63df) Merge pull request [#4190](https://github.com/containerd/containerd/pull/4190) from mxpv/ci-fix
- [`7a57e50778`](https://github.com/containerd/containerd/commit/7a57e5077855a0b5fe784b211dfaafb11746900d) Fix protobuild
- [`7d41344804`](https://github.com/containerd/containerd/commit/7d413448043b62bf274067a21676f6100c5e3f49) vendor: update go-events to fix alignment for 32bit systems
- [`4584e7188d`](https://github.com/containerd/containerd/commit/4584e7188db161bccf0c8502f6b34023c3895453) Update containerd/console vendor for fix
- [`57f41a2aad`](https://github.com/containerd/containerd/commit/57f41a2aada3d29f4483384bde704b52dd01350a) man: move ctr.1, containerd-config to section 8, and fix generation
- [`c090014b44`](https://github.com/containerd/containerd/commit/c090014b4436cfd783a0d18d7e7592c341db09ca) fix killall when use pidnamespace
- [`9a428a3c9e`](https://github.com/containerd/containerd/commit/9a428a3c9e89f840579f495cd349025d0146935a) Fix incorrect comment from copy/paste of starting script
- [`9f1c62d`](https://github.com/containerd/cgroups/commit/9f1c62dddf4bc7cc72822ebe353bae7006141b1b) Merge pull request [#156](https://github.com/containerd/cgroups/pull/156) from mxpv/bug-fix
- [`f864905c`](https://github.com/containerd/cri/commit/f864905c93b97db15503c217dc9a43eb65670b53) Merge pull request [#1420](https://github.com/containerd/cri/pull/1420) from chavafg/topic/fix-tests-go1.13
- [`98a694ed`](https://github.com/containerd/cri/commit/98a694ed44e035e17a8cc7cf7aa6296ecf977414) Fix integration test for golang 1.13

### 1.3.5

- Fix image usage calculation error [containerd/containerd#4276](https://github.com/containerd/containerd/pull/4276)
- [`1e902b2d7e`](https://github.com/containerd/containerd/commit/1e902b2d7e2cdb21e88b11cdf16e267b500d15a8) Merge pull request [#4276](https://github.com/containerd/containerd/pull/4276) from estesp/cp-usage-fix
- [`868a235972`](https://github.com/containerd/containerd/commit/868a23597276d97de13795703b673f2b0738fa65) Fix image usage calculation error

### 1.3.6

- [`fbdd528199`](https://github.com/containerd/containerd/commit/fbdd5281996af1aa4cfd4742ac277dbca5440192) Prepare v1.3.6 fix release

### 1.3.7

- [`a60b483c`](https://github.com/containerd/containerd/commit/a60b483cbd8b94eee625cdfe0dcaf8d3b23e97ff) Prepare v1.3.7 fix release
- [`6bc17344`](https://github.com/containerd/containerd/commit/6bc173446e6b7bffb5bc6d9129c6c9d1f1894dfb) Update to later version of critools with timing fix
- [`431b5b5c`](https://github.com/containerd/containerd/commit/431b5b5c90d038efa8574a04af993c7cb72330ad) fixes for backports to 1.3 from 1.4
- [`9053787a`](https://github.com/containerd/containerd/commit/9053787a70d9aafce33ac6f4eddb6a6e2a4fd573) Minor actions fixes/updates

### 1.3.8

- Fix metrics monitoring of v2 runtime tasks [containerd/containerd#4486](https://github.com/containerd/containerd/pull/4486)
- Fix nil pointer error when restoring checkpoint [containerd/containerd#4754](https://github.com/containerd/containerd/pull/4754)
- Fix devmapper device deletion on rollback [containerd/containerd#4437](https://github.com/containerd/containerd/pull/4437)
- Fix integer overflow on Windows [containerd/containerd#4589](https://github.com/containerd/containerd/pull/4589)
- [`bcb8bd3e4`](https://github.com/containerd/containerd/commit/bcb8bd3e43b5549b37f8c2608c4814e6a35e5178) bug fix:#3448
- [`7f4ecee09`](https://github.com/containerd/containerd/commit/7f4ecee097e35e28559a1a55d2be2a95bf4eba60) Fix integer overflow on windows
- [`609788376`](https://github.com/containerd/containerd/commit/609788376d872c45f379a2e0269c9be64129e3a7) Merge pull request [#4747](https://github.com/containerd/containerd/pull/4747) from estesp/fix-gha-cve-1.3
- [`8fcab2e3f`](https://github.com/containerd/containerd/commit/8fcab2e3fe9333cefa184861828a687408388096) Fix release.yml script for GH Actions changes to env/path
- [`e97ecf499`](https://github.com/containerd/containerd/commit/e97ecf499dbf9c7359eef49f33d4081d14e1dc80) Merge pull request [#4744](https://github.com/containerd/containerd/pull/4744) from estesp/fix-ci-1.3
- [`651188ccf`](https://github.com/containerd/containerd/commit/651188ccf9d9efc927a5aae716384b2f8761d7b5) Fix GH Actions CI deprecations
- [`6eef06eab`](https://github.com/containerd/containerd/commit/6eef06eab48549d9f0b309c18a76c39fd2ce3fa1) Fix DCO commit limit
- [`da709fe9b`](https://github.com/containerd/containerd/commit/da709fe9bbc1afc7140d9e1e6ddc4390d8b224cb) Fix indent in cni.template
- [`d5a7d0d40`](https://github.com/containerd/containerd/commit/d5a7d0d40bceb1738c089035847f41d9aaf85d26) Fix kube-container-runtime-monitor
- [`78bc3160c`](https://github.com/containerd/containerd/commit/78bc3160cc4483de176101995e41e589ac8c04f4) Add KUBE_CONTAINER_RUNTIME_NAME to fix fluentd support
- [`eca3ca166`](https://github.com/containerd/containerd/commit/eca3ca1668c47b254275318a4afd50ad30d81aed) Fix for kube-up.sh and update several documments
- [`5ad7db207`](https://github.com/containerd/containerd/commit/5ad7db2070818ef3b335c400201e36022198379b) Add runtime cgroup and fix a cli panic
- [`fd6c9153a`](https://github.com/containerd/containerd/commit/fd6c9153aaf47fb1e0bac84e71a0878d86843bf1) snapshots/devmapper: fix rollback

### 1.3.10

- **Fix container create in CRI to prevent possible environment variable leak between containers** [#1629](https://github.com/containerd/cri/pull/1629)
- **Fix incorrect usage calculation** [#5126](https://github.com/containerd/containerd/pull/5126)
- [`8f71d98c6`](https://github.com/containerd/containerd/commit/8f71d98c6296e499827a0dc3fe390448f32f501d) Update continuity to fix usage calculation
- [`3405c1d61`](https://github.com/containerd/containerd/commit/3405c1d6179e81defa278b27f956ce323825512c) Merge pull request [#4992](https://github.com/containerd/containerd/pull/4992) from Iceber/fix-runc-v2-service-1.3
- [`fb872ce79`](https://github.com/containerd/containerd/commit/fb872ce79bc7340874735420e553e09db9435f1c) runtime: fix shutdown runc v2 service
- [`7a2410592`](https://github.com/containerd/containerd/commit/7a2410592ae71269064863e21dda0aa28d58de55) v2: Fix missing ns when openShimLog on windows
- [`1d9893e`](https://github.com/containerd/continuity/commit/1d9893e5674b5260c3fc11316d0d5fc0d12ea9e2) Merge pull request [#169](https://github.com/containerd/continuity/pull/169) from dmcgowan/fix-usage-block-size
- [`b97555e`](https://github.com/containerd/continuity/commit/b97555e75c86a5f693aa104085036ad4eb1467de) Fix incorrect usage calculation
- [`91328d7`](https://github.com/containerd/continuity/commit/91328d7c60e71160252e8271376d9efadd16f0ad) Merge pull request [#166](https://github.com/containerd/continuity/pull/166) from zhsj/fix-riscv64
- [`62ef0ff`](https://github.com/containerd/continuity/commit/62ef0fffa6a1bed97d4b034c146bc323b2447b72) Merge pull request [#165](https://github.com/containerd/continuity/pull/165) from zhsj/fix-arm64
- [`25269ef`](https://github.com/containerd/continuity/commit/25269efb6192a3f31d9ef6a57d8631cd48b5f3b9) Fix building on arm64
- [`310e183`](https://github.com/containerd/continuity/commit/310e183616c481b7237980a7787a26435d311c0d) gha: fix invalid workflow definition
- [`04c754f`](https://github.com/containerd/continuity/commit/04c754faca46997ba6d0733f611c42f1816d1199) Merge pull request [#163](https://github.com/containerd/continuity/pull/163) from dmcgowan/fix-sparse-file-usage
- [`bc5e3ed`](https://github.com/containerd/continuity/commit/bc5e3edd2b742c38c762d928f267ad82922a1b63) Fix usage calculation to account for sparse files
- [`9365a1b`](https://github.com/containerd/continuity/commit/9365a1b01a63247561eab02c7d5914a554736c69) Fix golangci-lint errors
- [`f265cff`](https://github.com/containerd/continuity/commit/f265cff0764e5f8155e80d532db78f617e08e021) fix gofmt issues
- [`cf53015`](https://github.com/containerd/continuity/commit/cf53015a8bae42a53c5725e0d9bef11fde50694e) Merge pull request [#153](https://github.com/containerd/continuity/pull/153) from tomfaulhaber/empty-file-fix
- [`11900e8`](https://github.com/containerd/continuity/commit/11900e88c487c2e28650d44cc88a95e86734f01c) Fix sameFile() to recognize empty files as the same
- [`9e256e6`](https://github.com/containerd/continuity/commit/9e256e61eee8fc393366eb5c00d8b5fed8bb94fe) sysx/xattr: fix getxattrAll
- [`0ec5967`](https://github.com/containerd/continuity/commit/0ec596719c75bfd42908850990acea594b7593ac) Merge pull request [#148](https://github.com/containerd/continuity/pull/148) from zhsj/fix-gccgo
- [`75bee3e`](https://github.com/containerd/continuity/commit/75bee3e2ccb6402e3a986ab8bd3b17003fc0fdec) Merge pull request [#143](https://github.com/containerd/continuity/pull/143) from tiborvass/fix-sockets
- [`c04aabc3`](https://github.com/containerd/cri/commit/c04aabc3ab78f44b767079281856ca3526063c0f) Fix golangci-lint installation
- [`52678022`](https://github.com/containerd/cri/commit/52678022c3f2c764270706fcfb81c3f02fcd9b49) Fix header for new seccomp files
- [`2cc11e5e`](https://github.com/containerd/cri/commit/2cc11e5ef099054b1df855e5958c743612415714) fix for image pull linter change


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.3.10**, the newest release recorded here for this line.

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
