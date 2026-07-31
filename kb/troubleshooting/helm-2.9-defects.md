---
id: TROUBLE-HELM_2_9_DEFECTS
type: troubleshooting
title: "helm 2.9: defects fixed in the 2.9 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.9.0 <2.10.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 2.9 known issues
  - helm 2.9 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 2.9 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 2.9: defects fixed in the 2.9 line

## Summary

**73 defects** the project fixed across **2 releases** of the 2.9 line, from 2.9.0 to
2.9.1. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.9.0

- Fix for - Downloader plugins not used when downloading new repo's index.yaml #3938 26f4405fdf9d7334fc8ae966aae8f880e2b1b9a4 (eyalbe4)
- fix(kube): output internal object table 4c14bc4f342786a949d256c5b7dbe4335bb329bb (Adam Reese)
- fix(pkg/tiller): reuseValues combines all prev val 4dd21780bb6debf2eccfef2c37bdcb52bf649abd (Michelle Noorali)
- fix(kube): get correct versioned object from info helper f91c62f888e0a8f764fda8d7e3c2abf98abf1081 (Adam Reese)
- fix(kube): use correct object type in watch 561e034ada08d9ab707227756a62a4da47cee10d (Adam Reese)
- toYaml - Fixes #3410 - trailing \n issue 9d81cc097119a88b072ebddc31db9ad941c1da44 (Erik Sundell)
- toYaml - Fixes #3470 - trailing \n issue 1dc32f78491856085b88217a1686936a8bb6ef5c (Erik Sundell)
- fix `helm get manifest` context deadline exceeded error 73324d5ec971359c2a6fa4011d619232dc1e34f5 (Matthew Fisher)
- Fix tiller deployment on RBAC clusters 992effc1cd8870ab9061ec5d56847bf25e818af3 (John Koleszar)
- fix(helm): fix output leak from unit tests of helm create command e0056a9e41d5432192ee4d103a72e36ba9aeec36 (Arash Deshmeh)
- fix 'eveything' -> 'everything' (#3754) 0ba75b6652aec058c51fc1152988e01403496318 (muhongwei)
- fix 'mulitenant'->'multitenant' (#3755) 75387fe3183a724684b2bea29c2a0023e7a9a354 (muhongwei)
- Fix several golint warnings (#3756) 1a55161a53345816d724e1df9664f789113e1328 (adshmh)
- fixed typo + moved into Helm Included section 6abbee0d44f2890ad76cb5f2bd09a79a540a63d9 (James Strachan)
- fix Syntax error bddb6591d46ce176e87668ed458da54fa0da5eaf (fqsghostcloud)
- Fix HTML parsing when setting TAG with wget 908addd6fc778515fc0b2ed54a5050149554b961 (Ferenc-)
- Fixed typo 08f450404b1a7711d12efcdbfc47abafdd42bcda (Andrii Soldatenko)
- fix(helm): fix helm history unit tests 34b6d12ebe0824cae6fc9ebb1b14d3c8fd822a92 (Adam Reese)
- fix(helm): refactor tests on helm dependency list command to remove duplication 74bf7584a0333e817bca52b80e56e189cb1ed98c (Arash Deshmeh)
- fix(helm): remove duplication in tests of repo-add command b66c10df10a4039adc26ae21edb649b7a2a5f630 (Arash Deshmeh)
- fixed an issue in versioning.mk (#3653) a53f93c8ee28ad6b5ac043382b63e483a1f70e55 (John Rowley)
- fix windows path issues on `helm template -x` 6de9ebccbca7dd085f5d8857f1715c20075ed40e (Matthew Fisher)
- fix(helm): refactor search command tests to remove duplication 1e4770248c9f263ee2fd54516a93a28cd2fd6670 (Arash Deshmeh)
- fix(helm): search command returns error on index search failures (specifically on regular expression errors) 4b145622a268a3aca5643c149da5a3172df03dd4 (Arash Deshmeh)
- Fixed referencing the wrong env variable if SHA sum doesn't match. 08a92b23d1defbb03a3f6580f3ce9b3dcb935c76 (Michal Zerola)
- Fix link to github issues bb932f77022b55d3090506cb0a02d4431c52eaf2 (Stuart Leeks)
- fix(helm): refactor helm version command tests to remove duplication 23b570fabdb2907a6cc2887a4885cc9086cc7ad3 (Arash Deshmeh)
- fix(helm) refactor helm status command tests to use releaseCase struct and the corresponding function runReleaseCases. Fixes #3659 e25df2ae76e3c772ee6ae86e2eaf5be3be72cca9 (Arash Deshmeh)
- fix(helm): remove duplicate code from cmd/helm/history_test.go. Closes #3649 cdd9a85676edc2f126486ff7ccb5b14093744857 (Arash Deshmeh)
- fix typo in docs and fake 92972b0353430344c7dc1b9f7abc152f08bdc4f2 (Rajat Jindal)
- fix protoc 250d25fdceaf5546f29228f3711cedd8d6776fcd (Matthew Fisher)
- fix helm init --wait a66a39a171fa453f6515cbe23d7d2715cba9cc81 (Matthew Fisher)
- fix(helm): remove duplicate test code from cmd/helm/list_test. Closes #3637 75ccc353eb12884ebf2f8c653cee7730cc397f67 (Arash Deshmeh)
- fix kubeVersion example 01b404b68e4be94fe7776fc51cd65c155308a5fa (Matthew Fisher)
- Fixed bad link to Issues page 3058644f364f5fbce596aac1fc0edd718b504f5b (bryangunn)
- fix(helm): fix the bug in test code 'cmd/helm/init_test.go' and 'cmd/helm/repo_update_test.go' that leave behind temporary helm home directories during build. With this fix, the build process no longer leaves behind 'helm_home-*' temp directories. da989dc275a92fd48343263baf99231b310ce9ac (Arash Deshmeh)
- fix(helm): Don't crash in search if upper case chars are encountered. d8489901224c8279b724c84c0f17df67a9d5aaf2 (Morgan Parry)
- Add --replicas option for HA fixes #2334 2f252e95242849123fa7826748cbfd050fde870c (Yaroslav Molochko)
- fix(circle): fix download link to download.docker.com 286c902572a209d1a827b32ce794c721fcf21e44 (Matthew Fisher)
- fix(tiller): Supersede multiple deployments (#3539) 5f1a21bc321b326f3fab87b71bdc12bcd7125441 (Johnny Bergström)
- fix(plugins): support installing plugins by relative path (#3568) fa611fe2853f3393c7c2d902b8dabc72c88d63df (Adam Reese)
- fix(plugins): support newer git (#3571) c314e2e2f1a3ef1d54daea24c66bed215c9be152 (Adam Reese)
- Fix link to Slack 64b7d060baa92150f8a45cdff644a6cadc34ddb5 (Mauricio Scheffer)
- Fix minor typo df041c4b19d4007256123bfba57c56355086c934 (Radu Matei)
- fix(helm): fix the bug in tests under cmd/helm that leaves behind temporary directories named "repo-test-*" during build. 55cc23cb0168d527ba60de359e38c5717cf2577d (Arash Deshmeh)
- fix(helm): fix the bug in test code under pkg/tiller that leaks output to stdout during build 5b25eef9e260f2658914c5b9de27d8f69efcc2a3 (Arash Deshmeh)
- fix(helm): fix the output leak to stdout during build by tests under pkg/releasetesting, by redirecting output from mock clients. 4fcf69bc5287f6ca6090655ef8b8bb8087d6fa8a (Arash Deshmeh)
- Fix typo fbe17d277e5e4260edea47c9ede97dadab78be7c (Frederik Carlier)
- Fix linting bug with charts containing more than one hyphen abd33764e8738e9d46b6ec9dc5d7f73f1eeee675 (Liam White)
- fix(helm): fix the implicit dependency of TestSetAppVersion test on previous tests, due to helm home, by explicitly creating a temporary helm directory for the test. c78af5483c895fc4ccc204c350ed47b5da48fc17 (Arash Deshmeh)
- fix(helm): fix the bug in test code 'cmd/helm/create_test.go' that leaves behind temp directories during build a9ba3aa89777d651b4515b53f7cae98637447503 (Arash Deshmeh)
- fix occurences typo in charts.md 50cba63c5c3054f10d09b493b010ac4ee82441ae (Yann Coleu)
- fix a typo in client 76a40fc573120cca95042a0385dc97701b98c228 (yank1)
- docs: Fix FromJson comment a59d2125123d9d829e99823e1f969309841fefd8 (Thibaut Rousseau)
- Fix bash example ffc76861fe2e97ec63f36575bb2b3898a8b3a11d (Jonathan Hall)
- Grammar fixes and clarifications 0d12288e46fb21f57cf8974c8b9df0c80a4c529a (Jonathan Hall)
- fix(helm): update helm reset --force tip for clarity 084a2bb945ef2c6fcb3a97cb3ee00210a2f0fe5d (Justin Scott)
- fix(helm): fix the build-time golint warning on 'cmd/helm/install.go' 244b1b152865c3f7d86f38a16d4dc9ce2a574bd2 (Arash Deshmeh)
- fix(grpc): Fixes issue where message sending limited to 4mb 614cd9dfe7413a3b8624311bebaf8e8229b05e3f (Matt Farina)
- fix(api-machinery): Fixes patching for unstructured objects e6137ff05fd6d6e736a108cf91f5752e8669b268 (Matt Farina)
- Fix subchart2 example tag 782b394e9799e875649219295e6ace6bd54ec39a (Jonas Fonseca)
- fix doc spell check f953b2be2d4440228056af93912d91897f528faf (lihuangzym)
- Fix 'getSelectorFromObject' ea520afd3e4d0eb3637a10b7443ca83bcaf340e8 (Reinhard Nägele)
- Fix typo 3c66183cb51eea000ad7120ba68b9b7e4fef26f8 (Bin Liu)
- Fix type 1e0906ed67c08f754cc28c7047eea228cb76e373 (Bin Liu)
- fix helm init --upgrade logic 4947e5aaf8a5354cfada9816e837420ff7a75ca7 (Matthew Fisher)
- fix RELEASE_BRANCH_NAME 4763cca8cb49e6166475d19442ad379067531bdf (Matthew Fisher)
- change child-parent title & links to fix links d77a60a4621479b0d8c42cdafebfdcf69b1b10e0 (jonathan.striebel)
- docs: fixed incorrect clone path in developer docs 03f35cdd32fbfc41ab49a0c1106ee0e9cbf6d520 (scriptonist)
- fix link to image 9fcd6be4ffbc032396d7cb0d71c8f551a51aa277 (Matthew Fisher)
- Fix pod recreation 3d05da010980fd93258d4f10ff4d0dbabe53dba2 (Reinhard Nägele)

### 2.9.1

- Revert "toYaml - Fix #3470 and #3410's trailing \n issues" a00bcc297914fe2f9e7eadab45ea34d1d99f8e87 (Matthew Fisher)
- Revert "Fix tiller deployment on RBAC clusters" c6e7f0335bc083aa298127c5e4d72a28a6822f3f (Matthew Fisher)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.9.1**, the newest release recorded here for this line.

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
