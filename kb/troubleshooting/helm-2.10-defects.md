---
id: TROUBLE-HELM_2_10_DEFECTS
type: troubleshooting
title: "helm 2.10: defects fixed in the 2.10 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.10.0 <2.11.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 2.10 known issues
  - helm 2.10 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 2.10 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 2.10: defects fixed in the 2.10 line

## Summary

**69 defects** the project fixed across **1 releases** of the 2.10 line, from 2.10.0 to
2.10.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.10.0

- Fixed a bug where `helm init -o` wouldn't display the service and secrets to be installed
- Fixed a bug where `helm install --dep-up` wouldn't deploy the updated dependencies
- Fixed a bug where `helm install --set foo=null` wouldn't coerce into a null type
- Fixed a bug where `helm install --set-string foo=null,bar=true` wouldn't coerce into string types
- Fixed a bug where `helm lint` wouldn't fail when Chart.yaml was missing
- Fixed a bug where `helm list` on a fresh cluster would show a stack trace
- Fixed a bug where `helm template -x` would error out due to pathing issues for Windows users
- Fixed a bug where `helm upgrade --force --dry-run` wouldn't obey `--dry-run`
- Fixed a bug where installing packaged charts from servers returning `application/x-tar` headers rather than `application/x-gzip` headers resulted in an error
- Fixed a regression where users needed to `--set` a bogus field for `--reuse-values` to work
- Fixed a regression where using Tiller with the [helm-local](https://github.com/adamreese/helm-local) plugin wouldn't support kubeconfig files with `auth-provider` authorization support
- Fixed the `--tiller-namespace` flag for helm plugins
- fix(helm): fix(helm): add `--tls-hostname` flag to tls flags df03a10a09b267329e6b662dadc002e46b2f50b6 (fibonacci1729)
- fix(release_server): fix how we merge values 39d41d09c6ab4937eca03d622891c536d47fe2f4 (Michelle Noorali)
- fix `helm template -x` pathing issues on Windows 1a1ea6383004e13c400070ec50e5003da69963e5 (Matthew Fisher)
- fix path output for Windows d8b46d840be34f2232cd72ee980b646ccdf8aa6c (Matthew Fisher)
- fix(helm): add --tls-hostname flag to tls-flags 7faf62a209e91bfae17522e4a63c750a3482f6f3 (fibonacci1729)
- fix(helm): return when listing with no releases or nil 6767f3cf08b30fda5f031cda7e2d0cb9d66a7bd8 (fibonacci1729)
- Fix(helm): fix the bug of the charts not deployed after downloaded in helm install --dep-up 4d579bbbdff7d9b7c6b380d256f29a5732147d22 (rocky)
- typo fix for template test 5d2140be384eaba7ed8bb0ff1bc2fb9be6284b4d (liyongxin)
- typo fix for lengh to length 63760b29377fde5e3d2ac9f3a3df97d133161858 (liyongxin)
- Typo fix: indentifies -> identifies b4cfb5f2f3efe957b1cb1b671ee33cfe18aeaf93 (ruicao)
- Fix incorrect timestamp when helm package 96a85a06ed48e618c53441cdc988680eb00f8e0c (mattjmcnaughton)
- Typo fix: retruns->returns 4d22b104b72cc1b6b024d047c423ba496ec05e0c (AdamDang)
- Fix test failure message e8b788dc4f3533934394e783cda94e65faf75918 (mattjmcnaughton)
- small typo fix 03d502c4313fdd516bf1ec4d5d9021accd377106 (Rob Salmond)
- Documentation: add syntax highlighting to code examples & fix spelling of kube primitives 4e29c7e2fd4ced670da320c7587cd8a9e7a895e2 (radbaron)
- Fix concurrency issues with helm install 53c8e9b67ed9482edd1c03146a55b73b014134b5 (mattjmcnaughton)
- Fix inaccurate comment in `tiller` 2b04523bafa1cc96eb92b64980f7672a399e3715 (mattjmcnaughton)
- fix charts doc: extra space in requirement condition 091dd84c71814fdeb8b67aaaf90179629f1f7f84 (Eric Zhang)
- Typo fix: mach->match 51f92b47877bcc36401dacc6b624eecff8a8931d (AdamDang)
- fix(kube): run schema validation on BuildUnstructured b831efdf5853dceb0249eaf441024d115b5cb633 (Adam Reese)
- Typo fix: usa helm->use helm ddb536aa7a9287a6bf45994f4430891d00c1f529 (AdamDang)
- Typo fix: evalutes->evaluates 07bebe6bff7885cafc800c063e52bf4669ed1c93 (AdamDang)
- Fix for - Downloader plugins not used when downloading new repo's index.yaml #3938 c2fa72ebcdc9a12381eec29b642374af75f5b45c (eyalbe4)
- fix(kube): output internal object table cefee4b749122bc38d019c2791faf79a4ab1376f (Adam Reese)
- Fix --tiller-namespace flag for plugins ed39f16ee57c094476ea61ef4983efcb501e7643 (Fabian Ruff)
- Avoid to call 'go' with empty -tags argument 6b2384f8b4dbc64e0452dfb60b987e94e8c21f00 (Julius Kammerl)
- Typo fix in plugins.md "that that"->"that" 28fb950588f64c4341886509a62d3b7670578e7a (AdamDang)
- fixed flag for tls ca cert option in the documentation b0eb40b2ca67146b7bb76e0197bfba0c83c5dd60 (Colin Dickson)
- fix(kube): get correct versioned object from info helper 6ffff5fea9febb3c2522a391a80cb09b838288a7 (Adam Reese)
- fix(kube): use correct object type in watch 31ddd707e8f832c2ac429aa09284e196f1664ec6 (Adam Reese)
- fix(pkg/strvals): evaluate "null" values 1850aeade9efe7edb960b130daa46c727ad98bab (Michelle Noorali)
- Correct the returned message in reset_test.go fac7caf5d266c33cc95d0413e73a9a4636e48317 (AdamDang)
- Correct the returned message 9f78c33c644cbf4599c30605470b752126573471 (AdamDang)
- Typo fix in functions_and_pipelines.md f291fdbb43730dbb266d7aeb146c40aa978a0c66 (AdamDang)
- fix(helm): resolve linter's warning on template command unit tests 75682ed5844400e5dcd24ec7532c0fa454defd4d (Arash Deshmeh)
- Fix some typo 4b09b0489b6ba1fbd413aaf599fe44e6697a1b1c (xianlubird)
- fix(helm): refactor tiller release install unit tests using chart and install request stubs c22492ff016ea85d7b05be013ecd4458b00b02ae (Arash Deshmeh)
- Typo fix 3f5e82c83207c7444f98cc65a73bf71a0babeb1d (Erik Sundell)
- fix(helm) refactor reset command unit tests to remove duplication in test code 826781a1a3ceddaf0abeced14bee867d86c96b4e (Arash Deshmeh)
- typo fix get->Get's ee9ef91df0ea72646ae0ea23497622bfd019a944 (AdamDang)
- fix(docs): Add the missing docs 85282ab864973cbbb85d97849c37be0432df7149 (Taylor Thomas)
- fix(package): Adds missing `set-string` flag and parameter b718b1c87038d44f2519f50d2df25454aad5f926 (Taylor Thomas)
- Fix some typos 138de17c64e6c01468f4e17ddff0231b34d3f683 (AdamDang)
- toYaml - Fixes #3470 - trailing \n issue 6cdf6cee56dcd90e3dca82950b15d46e6bb4587b (Erik Sundell)
- toYaml - Fixes #3410 - trailing \n issue 35132d141c54598e7dab23207acce7e6fb1dfa4a (Erik Sundell)
- Fixes typos introduced in #3540. Closes #3823 1e7915587f383a5e37f8506c9c1784bd37f43753 (Daryl Walleck)
- fix(pkg/tiller): reuseValues combines all prev val 9266731dc45aac2aa6a726e5a887ee1078aaf35f (Michelle Noorali)
- Typo fix helm->Helm 58ac6023653632afe1bb13d01ed5516fff3737f5 (AdamDang)
- Fix #3822 1d3ae54185e369477f42fb15d3a97f80c014c09c (Zack Williams)
- fix(helm) refactor release_testing unit tests to utilize runReleaseCases ea7c3fefc8cd79ac497965a7fca2aef390f82287 (Arash Deshmeh)
- Fix tiller deployment on RBAC clusters 1e03f1bce5eaab384c8ddabbf38b8f566d1c1d14 (John Koleszar)
- (fix) Handle caFile alone being set for repos 332dc83c46b1cb135bc42b7afa1c9b50629e0e15 (Morgan Parry)
- fix `helm get manifest` context deadline exceeded error 87c64e7987f348c0a99a4f6e12d6ec187723b7cc (Matthew Fisher)
- fix output leak from tiller release install test a43ddcc191f851e343075142a3b0f9a456e95be0 (Arash Deshmeh)
- Fixed SIGSEGV when running helm create with -p and no values.yaml file 99da9fb54817a00e0138a08ce0b0643b923e5b6e (Ali Rizwan)
- fix(helm): add service, secret manifests in `init -o` af80059b45804a3c9eb51b98f2bb8eded091d677 (ryane)
- fix(helm): fix importValues warnings from disabled charts fbe80437a499e6b5c7301588522b03dde593ce10 (Justin Scott)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.10.0**, the newest release recorded here for this line.

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
