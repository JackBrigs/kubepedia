---
id: TROUBLE-HELM_3_1_DEFECTS
type: troubleshooting
title: "helm 3.1: defects fixed in the 3.1 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.1.0 <3.2.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 3.1 known issues
  - helm 3.1 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 3.1 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 3.1: defects fixed in the 3.1 line

## Summary

**113 defects** the project fixed across **3 releases** of the 3.1 line, from 3.1.0 to
3.1.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.1.0

- fix recursion count in templates 805a591b5057845be0e872a3f667e81d07203367 (Daniel Cheng)
- Fix shasums to be usable by shasum and sha256sum applications 9887a3e4ca4ef473a4ddd419573edbd5c82bb231 (Matt Farina)
- fix(comp): Fix broken completion for --output flag 374e9d8c7dc49cdd5623d15c794e46a80e3134b5 (Marc Khouzam)
- fix(version): fix typo in doc comment 8b6233fc3ef50903bd527605ffe9a2f617b3e616 (Matthew Fisher)
- fix(memory_test): rebase master 8e1fc4bc6fb871af3aa73fc79a2ca86901092610 (Matthew Fisher)
- fix(cmd): Specify namespace for template command be7de1c376347b3f97d24aab85270ced0c039a58 (Marc Khouzam)
- fix(tests): Add namespace support to memory driver e6d2d10bad8a872478783b0b1483cf467c05741b (Marc Khouzam)
- Fixes issue where non-CRDs are read in from the crd directory ed80cf4548712cb779bd1607f98dff21d905d346 (Matt Farina)
- Fix engine.newFiles doc comment 43e628599564bafd5b16514fae799eab9fbc5ffd (Jon Huhn)
- Fixes issue where <CHARTNAME> is left in starter values file 1bd819a7b28d48a931db3f89be35f346d3e61e37 (Matt Farina)
- fix(tests): Ignores tarball that will change on dep update 15e2659191cdba73afc8c5c08d2645f8b32d3433 (Taylor Thomas)
- fix(chart): lock digest differs when dependency build with Helm 2 and then Helm 3 (#7261) 5ec70ab27fbf54ab529984db154953cbf68da78f (Martin Hickey)
- fix(tests): Make tests pass on MacOS 1897d4d60a387f4b516c2382b5ae2f36abde844c (Marc Khouzam)
- fix(test) use newly created index instead of ignoring it 6cfcc96cea4344b9b1003eafbf4cbe670494d5b0 (Karuppiah Natarajan)
- Fix tests on arm64 and ppc64le (#7500) df20164cd27f12d8f4cadda608ca1caea5c25759 (Yaakov Selkowitz)
- fix(lookup_func): do not return error when object is not found 1b1d6bba9cec81a6bbc77dd948779a45bc8a63c8 (Matthew Fisher)
- Fix typo d70b50b3a11b62efe942d0429d1d7c54f8656a52 (Jon Huhn)
- fix(template): helm template "--show-only" flag producing duplicates when flag used more than once (#7204) e483dce2895dd23400816b7852405edbf726e396 (Lee Bontecou)
- Fix some spelling errors in comment (#7492) 1d79ed2c189da65315a597d51a92f0213f224126 (LongKB)
- fix(comp): Allow zsh completion to handle -n flag 4f4779ca3a456468851f446fd978c4c71563fa96 (Marc Khouzam)
- fix(package): remove --set, --values, etc. flags 50dcd39ba5a3c50bd046b5b539c2c7e6ac68aea1 (Matthew Fisher)
- fix(chartutil): remove empty lines and a space from rendered chart templates (#7455) 0beb9f70407bed715e67dc28eaf6e6eb3c3263e1 (Shota Nakamura)
- fix test-style 16a85f757066c44aff6dacd8c598ac7a9d699eaa (zwwhdls)
- fix(test): Remove invalid subcommand in test 559c4053620352f76953a8ef7adbeed50c5fef32 (Marc Khouzam)
- fix(kube) only add to scheme.Scheme once 8fe2097ffeb0d5a6d898b6850738c14fdca0991e (Jakub Bielecki)
- fix(comp): Update based on review comments 77b900106f923bf1d9b787f5e1d2c6c85be9722f (Marc Khouzam)
- fix: catch one additional discovery client warning (#7176) 6cc039ea79a435c9f335d677b78d9be574b8e770 (Matt Butcher)
- fix(helm): improve handling of corrupted storage 1f0582cadc1ba222c5d7a7f9977a091edd55f6af (Cristian Klein)
- Signed-off-by: Ahmad Kazemi <ahmad.kazemi@recordpoint.com> log.Printf replaced to fix the log issue. d4c37d33d1a186d8b271b4f4276da434da6a20e0 (Ahmad Kazemi)
- Fix: helm3 - kind sorter incorrectly compares unknown and namespace e2946c7e343f0b0404b5f4e9ecabdccd970a87c8 (Bradley Skuse)
- Fix typo in comment for func IsReachable 0cdbbf287f04e10f6b44faf1bf9185b48ca7f3fa (Guangwen Feng)
- fix(test): Make resetEnv() properly reset settings 16f62050044d8eaca1ee794ab1903a719895662f (Marc Khouzam)
- fix(helm): move ServiceAccount before Secret in InstallOrder. 08663e6bb3c5694726aac665d71be26494475781 (Daniel Strobusch)
- fix error output ab905010fd3ce671f9e0cd74f4d8ca3bc944c130 (bakito)
- fix(tests): use sigs.k8s.io/yaml ff0257de29e589f9550aa6c04bc3283d652dc976 (Matthew Fisher)
- Fix a typo "update" -> "updates" (#7346) de9118b87961c3ec15370d6b77293d6fe36fa88a (Hu Shuai)
- fix(cmd): Fixes logging on action conf init error (#6909) ad07bb690dbf34e7067171235861a3c0fb9897b6 (Jorge I. Gasca)
- Fix typo in --values cmd flag a58430a944454ff8e5a560a9d3d70f5e05385310 (Anton Kvashenkin)
- Fix a typo "the the" -> "the" 3eb8df0c5ee5b6e9753cf99440644423e392073e (Hu Shuai)
- fix(comp): tail cannot open +2 for reading 2eab781b35019ce452738012092f9df4ce9fdf00 (Frank Lin PIAT)
- fix(tests): Use relative path to acceptance tests b47a5b746d57e0ca93c9e31066a2c4ef6fa9cdc4 (Marc Khouzam)
- fix(helm): add .orig as typical backup file a2bbb67839722713d48b3c775d9402efba12c108 (Jan Heylen)
- feat(checksum): update to get/get-helm-3 to match shasum fix 5680f4d50644de2f4d3fd6c890b7153b533410ed (Thilak Somasundaram)
- Port PR #4161 Fix incorrect timestamp when helm package to Helmv3 8cb3c02c47a6133d87efbefe507878d900809f36 (Romain Grenet)
- Add back fix for CRD patch creation afa612df9d132180837e7c122088d44b1c72df1e (Adrian Gonzalez-Martin)
- fix(kube): Port use of watcher with retries to wait for resources (#7217) b6e2a14306964a6fe756abff85d3195542a2f1fd (Martin Hickey)
- fixed golint fa643cfa31af72f06b6d041c310a29bed18f0ac4 (raffaelespazzoli)
- additional fixes based on @thomastaylor312 comment a62ba049624d3212619005bc87fec410a248ca22 (raffaelespazzoli)
- fixed test issue 8e088fc4a2a616354872b21d9ceb84e9d55a40de (raffaelespazzoli)
- fixed circle ci issues 02ce01b2415fe270a760c984f2e0158b18476573 (raffaelespazzoli)
- fix(install) crd install with apiextensions.k8s.io/v1 1c6424cb189817c46dc7ea3e3812f7f75df52cff (Vibhav Bobade)
- fix(helm): Validate number of arguments in install client a3f00fde691585ffa2dc4934c6813d69ff0ec284 (Lennard Eijsackers)
- fix(cmd): Add message about deprecated chart (#6889) 0fd76b2a2bca5b3febf6488c860a7c6502c70086 (kvendingoldo)
- fix(*): Helm v3 handling of APIVersion v1 charts dependencies (#7009) 0cb0eaca948d55da1c824f201aa78f9313763f69 (Paul "TBBle" Hampson)
- fix(tests): Repair tests failures 735bc652a6618afb7502d8154086a1535c7629ea (Marc Khouzam)
- fix(helm): add --description flag to helm (#7074) 357d265de0e72f02c493701cdbee9ecc6eb0a016 (Juan Matías de la Cámara Beovide)
- fix: clarified behavior of 'list --deleted' (#6950) e47c67c427e9831d3df20befc7fa139404829ddc (Matt Butcher)
- fix this inconsistency in the docs (#7157) 36a8001e2adc0e5cf1bc3a06c75777a0b2ee15b6 (海的澜色)
- Fix godoc badge 361db773881415398ce05637f9f56bd6f2820c85 (Robert Brennan)
- fix "Chart.lock is out of sync with Chart.yaml" (#7119) e062146db3a9a9bec0e64f5db939416441b1af38 (海的澜色)
- fix(tests): mapfile is not available on MacOS cc33e394c7c464be1940a2f737a1f24887e4ca6f (Marc Khouzam)
- fix(cli): IsReachable check for "get values" bf4cc97bbe7ca994894a87df63fdf7da6ee0841a (Marc Khouzam)
- fix stack overflow error (#7114) 750b870aedd35b69b9ca1e1517635fa70367a309 (海的澜色)
- fix: ignore pax header files in chart validation 48704034a9f37a23eee192b32e15249b299e0767 (chloel)
- fix(plugin): Avoid crash on missing flag 32b4e2e5e998ee11559d132eae796f2b22fac0f7 (Marc Khouzam)
- chart_downloader: fix lint issue. 4c4328398ecc4f6eef07524f4bcddaca153b4570 (Andreas Stenius)
- fix(plugin): Avoid duplication of flag list 5179f8d698d30b243fd9aa646fac76224510b28b (Marc Khouzam)
- fix(plugin): Add missing -n known flag 6473234f43cbec7603124d684cb630dfdc4b1419 (Marc Khouzam)
- fix(lint): Remove requirement that directory name and chart name match 32ce016054648f20168a2d7f4ff4b954686e0689 (Scott Morgan)
- fix(lint): Remove requirement that directory name and chart name match 8a8463e08d8a52b59fd20739ec3aa98be5bf1177 (Scott Morgan)
- fix: change error message to contain correct field name 8889625af63a93d08909af0c2cfdbddbcd7204db (Daniel Strobusch)
- fix(get-helm-3): remove tiller checks, fixup version check c9da1eaae780488ba34c7bb66c5bff518c6c06ee (Matthew Fisher)
- fix(get): hard code DESIRED_VERSION when unset 3e77ca22c71e182860b0ef9508d229e25d8f4140 (Matthew Fisher)
- fix(wait): Adds support for waiting on v1 apiextensions for CRDs ecb55c1de7bcc0063b2cf956a0e2172fcd75bc59 (Taylor Thomas)
- fix(get): install Helm v2.16.1 06a5eb2272f26fcdb2bd5abf5abe45d7078b5e50 (Matthew Fisher)
- fix(reame): update links to docs a9b178758c6c3c3f36f6bbd7a1b4359efae27366 (flynnduism)
- fix(install): log the error when recording the release e91feed1a3c34ec15ff2bff4d07ee5e275a6d7b4 (Matthew Fisher)
- fix(pkg/downloader): resolve repo alias before checking digests on build 0987c6f7b91bffc360a8c604b9dfb87b845cc919 (Hang Park)
- fix(pkg/downloader): add failing test for build with repo alias 17553db485f6165c15aa17c6dfcc7589edb025ee (Hang Park)
- fix(strvals): port #3912, #4142, #4682, and #5151 to Helm 3 b30467c2e52ffebd0b4708ca318d34251ab5a692 (Matthew Fisher)
- fix(ci): pin golangci-lint to v1.21.0 4d1c11f05bf732bf914d5529493fc77d5134d1c9 (Matthew Fisher)
- fix(cli): helm list was ignoring some errors 30e8ed2f3df9e776b5a5937d92e8ff45c54f984f (Marc Khouzam)
- fix(tlsutil): accept only a CA certificate for validation aa6104e442ef8b574ae88efd8b5c41004437ac88 (Matthew Fisher)
- fix: stop discovery errors from halting chart rendering. (#6908) 865c46c014cdb7622f97ae287ee92fb8a280f3a9 (Matt Butcher)
- fix(cli): Sort output of helm env 3e09e2fa2831ab0b51678171b7934cf9e6b4f8a7 (Marc Khouzam)
- fix(show): restore comments from raw values bd1f4a443e95ea4eda88affad96577b63c0d6622 (Matthew Fisher)
- Correct spelling mistakes d683a431e241a37c40042ad168f04460e9306eaf (yuxiaobo)
- fix(cmd): Standardizes all output to use lower snake_case names 4226c45dfd7419874583a37b79124afdd55129ec (Taylor Thomas)
- fix(version): implement `helm version -c`, mark as hidden 444d006fe27bdea5ade0333fdb78c2141de2f175 (Matthew Fisher)
- fix(getter): set up TLS options during .Get() c9b127c3ee2fd6832c02c645600fc0caff7827c2 (Matthew Fisher)
- fix(chart): add JSON tags to chart object 668f51bfdf8171bfaf8d369752ff938ed630d655 (Matthew Fisher)
- fix(comp): Protect against user's aliases f16d3e295ca2dee5aeab0bd36c09400e74dd3f4d (Marc Khouzam)
- fix(cmd): Updates description for template validation flag 432fd9c110bf75de46cfc8db4748ad0a0fdc28fd (Taylor Thomas)
- fix(action): strip file extensions from name bf012282c846a1173f4ddc987756c2aa4dda9172 (Matthew Fisher)
- fix(kube): return error when object cannot be patched a505f910732f3a431fd44b52707760c39889ebcd (Matthew Fisher)
- fix(comp): helm plugin 'remove' is now 'uninstall' 1e58f484ff590d9f06e131226787eb55fb8f2d1f (Marc Khouzam)
- fix(version): lift "unreleased" status 1c64d8fb8164406e63bf91e263b11485d43a8324 (Matthew Fisher)
- Porting fix from commit f5986db184cf6d16dcd48760ac749a20236fb845 afda6b49408bad8f7a7a5faa9eeda016c8763400 (Lam Le)
- Fix import 41e70306b3464b99cf3afe4e23e85948fede3483 (Yagnesh Mistry)
- fix rename for helm dependency upgrade ceb6bcb318fa1f93ad2f67e3ba1cbbf1600fc154 (Yagnesh Mistry)

### 3.1.1

- Fix output of list action when it is failed 3fa62f4da11862c03742fa4306c8dacbaf9ded41 (Song Shukun)
- fix(kube): generate k8s native scheme only once 8d012c25ff46a64f34821e769f0cde1f0fc96a70 (Hidde Beydals)
- fix(kube): use non global Scheme to convert 742a46948b6665b8b916d7123e67b36787b853f3 (Hidde Beydals)
- fix(helm): improved logs 54524f92734961ca86a4e31a20672c843266c4f5 (Federico Bevione)
- fix(helm): Reworded logs for clarity 9791686136e84e2f7b78c7447fbb0469a3b2719e (Federico Bevione)
- fix(helm): Don't wait for service to be ready when external IP are set 30ebfaf20d36489513142ce060c6e8549e8b8c6b (Federico Bevione)
- Fix render error not being propogated af0960456ae56412575a5f356f2de24c97081164 (Martin Hickey)

### 3.1.2

- fix(install): correct append tls config. 7397096823f7d4ae4bf855a5fd8ad7cc1467fb27 (James McElwain)
- fix(install): use ca file for install (#7140) ecf50b376374441c117ad04af7f18c6886519f68 (James McElwain)
- fix(helm): add --skipCRDs flag to 'helm upgrade' When 'helm upgrade --install' is run, this will allow to skip installing CRDs Closes #7452 110336fc30ddb40e67a6c9555f142fcb2500d965 (akash-gautam)
- Fix dep build to be compatiable with Helm 2 when requirements use repo alias 2188551563f5bf52fafe85c2128dbf38ba0b8c8e (Song Shukun)
- Fixes verification output on pull command 47a79b58698f730ccbf31c176b43166c59260691 (Matt Farina)
- fixed dependencies processing in case of helm install or upgrade for disabled/enabled sub charts 2b932d5eddc63979456e3c3b0006765243403b75 (Florian Hopfensperger)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.1.2**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `helm/helm`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/helm.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
