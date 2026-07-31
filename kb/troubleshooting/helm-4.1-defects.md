---
id: TROUBLE-HELM_4_1_DEFECTS
type: troubleshooting
title: "helm 4.1: defects fixed in the 4.1 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=4.1.0 <4.2.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 4.1 known issues
  - helm 4.1 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 4.1 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 4.1: defects fixed in the 4.1 line

## Summary

**92 defects** the project fixed across **4 releases** of the 4.1 line, from 4.1.0 to
4.1.4. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 4.1.0

- Fixed bug where a plugin name could already be used by another command #31427
- Fixed bug where --server-side flag was not passed to install when using upgrade --install #31635
- Fixed bug where HELM_ environment variables were not passed to plugins. this fixes a regression which was blocking some getter plugins #31613
- Fixed bug where Helm test --logs failed with hook-delete-policy "hook-failed" or "hook-succeed" #31579
- Fixed regression where vendor-specific suffixes were stripped from .Capabilities.KubeVersion.GitVersion, breaking charts that detect managed Kubernetes platforms #31528
- Fixed a bug where helm uninstall with --keep-history did not suspend previous deployed releases #12564
- docs: fixed documentation about default wait strategy
- fix(release): fix test compilation error e751a70e84175212d9338738122d045aecb2ad89 (Evans Mungai)
- fix: typo in the function names 138f730aacf96d0d94535a1d5b29d6dd128a062e (Gergely Brautigam)
- fix: add default casess to switch statements 1c119bcaa6f68a73f27a21f9d7dba22c4baf4d7d (Brenden Ehlers)
- test(statuswait): fix Copilot code review suggestion for goroutine in tests d6b35cedeb0519b648941911298ebb08fa3b0edf (Mohsen Mottaghi)
- fix: use namespace-scoped watching to avoid cluster-wide LIST permissions 3dd54ed0b693e5e5805cceb535ed5167fa5ada25 (Mohsen Mottaghi)
- fix(doc): Update default wait strategy f92ae18977bfe4fad74c7cb0e8c7f7fc68d85306 (Deepak)
- Fix TestCliPluginExitCode 3c6557dcf57ef4feee0d4840d4095f1479a63b40 (tison)
- Fix `TestConcurrencyDownloadIndex` typo 592815ea2b020b354510685bfa61d252095baafb (George Jenkins)
- chore: fix some comments to improve readability 858cf315830dd4818297e00d8098e6f79422d306 (wangjingcun)
- fix(upgrade): pass --server-side flag to install when using upgrade --install 2dc581dc1c9c07e36dde9acc70bd86e23963662a (Evans Mungai)
- Fix govulncheck in CI bc9462f20fc9a948fe557c87c895c06d4c0ddc6a (Matt Farina)
- fix(cli): handle nil config in EnvSettings.Namespace() 8534663e730f7d32ac8777c3b41a7e6c6a94ab96 (Zadkiel AHARONIAN)
- fix(getter): pass settings environment variables 119341dca7fba0ae2987b4d0ffd41e9574e03a38 (Zadkiel AHARONIAN)
- fixes comment in install.go a109ac2f06d7cdca85c23567f3c545c726727904 (Stephanie Hohenberg)
- fixes tests after merge 2f598ffc850d9f83642da362a7be4121cf617275 (Stephanie Hohenberg)
- fixes lint issue bb9356e182a8abb0f806cd4866a317f273631862 (Stephanie Hohenberg)
- Fix linting issue 9f1c8a26f00ebbe2942064a06b49c275162d10ef (Benoit Tigeot)
- chore: fix typo in pkg/downloader/chart_downloader.go e71a29ce4ff045c8194625c0d804f789d121023e (megha1906)
- Fix kube client logging 936cd328ac59001f7a6716a3eb7e9075f3950f44 (Matt Farina)
- fix: prevent segmentation violation on empty yaml in multidoc 81d244ca21e232e5ebccd67040cdf7596b572e8b (Benoit Tigeot)
- fix: prevent reporting fallback on version when none specified 40e22dedb2d9fdb8c47376a2c3071b99ba056d9c (Benoit Tigeot)
- fix: add missing context to debug logs 2dc5864f447d0429f7101526a518529e9919b067 (shuv0id)
- fix: preserve vendor suffixes in KubeVersion.GitVersion ce273eea48c8e42323c648527bb8e0d0dbf6fd8c (Benoit Tigeot)
- fix b1a976073f11a972b3f5a6860bc5647a79268ef5 (George Jenkins)
- fix: Use server-side apply for object create during update 18616e6ce969cd7fbbd8a85d77557402839d59db (George Jenkins)
- fix: correct LDFLAGS path for default Kubernetes version b6a8c6521614f99d54752110a955b4f6fb5b8f5a (Benoit Tigeot)
- fix: improve plugin name validation err messages early via unmarshalling acf331a0057ee79246f6058fca02313be29506fa (Benoit Tigeot)
- fix: Make invalid name error message more similar and move tests 9e1e3d21c59820b39a05d950bf27027ba7ef1662 (Benoit Tigeot)
- fix: focus only on plugin name but give more info about what we get cf077ceb2758a63aa5f87410204d11c5f2ad3a7b (Benoit Tigeot)
- fix: improve plugin name validation error messages c04e18e45253f08d127a37c8328e7084e486c7cc (Benoit Tigeot)
- Fix syntax errors in the document faa0adcb3855a299596f68f7a18f3dd84ef9ed1a (Fish-pro)
- docs: Fix LFX Health Score badge URL in README.md 40856bf50cdaa6a178b1c8433c98c25004e44735 (Michael Crenshaw)
- Prevent surprising failure with SDK when timeout is not set 5f6fa437b2c2954092b6c3f8af5b83aef7dcb874 (Benoit Tigeot)
- Avoid confusion between `--wait` (watcher) and no --wait (hookOnly) 8535e9f4ab5c143fcbd429f45a0f15cf510a0cc0 (Benoit Tigeot)
- fix: do not run release workflow on forks d93ef03ee400292452dec97e88e821dc3188110e (Terry Howe)
- fix(rollback): `errors.Is` instead of string comp d158708fbfb08bc452d1733d9b8cc4c7dc9f8902 (Hidde Beydals)
- fix(uninstall): supersede deployed releases 2f1ecc7100868be90d302a299d707c70a7f45276 (Hidde Beydals)
- chore: fix typo of public field 0d6de28bf446b4d1b2cb71e0441e5c8ebc9e91c9 (tison)
- fix: Fix Helm v4 release distribtion/get-helm-3 script d5d1ea3f5527b4794c624e84c152f28fad860e10 (George Jenkins)
- fix test ae4af69b9dbd5ad01dc9621a90e5b08327a3499e (Artem Vdovin)
- fix: assign KUBECONFIG environment variable value to env.Kubeconfig b25fa862d5f7de6c20fa4b95ce5c85962669fd3b (LinPr)
- fix index concurrency 351bb78ee5a22cb0e68818a310d77d7240edc0b1 (Artem Vdovin)

### 4.1.1

- fix: fine-grained context options for waiting #31735
- fix: kstatus do not wait forever on failed resources #31730
- fix: Revert "Consider GroupVersionKind when matching resources" #31772
- fix: handle nil elements in slice copying #31751
- fix(copystructure): handle nil elements in slice copying 261387a112bd91edca6511d34de23f7cc5ce9f8b (Philipp Born)

### 4.1.3

- Fixed a bug where --dry-run=server was not respecting generateName #31563
- Fixed a bug where empty CRD resources caused a crash. Now it prints an error #31578
- Fixed a bug where OCI references with tag+digest failed with "invalid byte" error #31601
- Fixed a bug where user-provided nil value was not preserved when chart has an empty map or no default for a key #31644
- Fixed a regression since Helm 3.18.0 where Pulling charts from OCI repositories that use an index to store both Container Images and Helm Charts under the same tag failed #31776
- Fixed a Helm 4 regression where gotemplate white space trimming directly after YAML doc separators, when present after postrendering, caused YAML file corruption #31868
- Fixed a bug where `FailedStatus` is treated as a terminal state, causing upgrades to fail prematurely when cluster autoscalers needed time to provision nodes, or when pods were being deleted during rolling updates #31897
- Fixed broken backwards compatibility for deprecated `--atomic` flag on install command #31901
- SDK: Fixed a Windows 'Access Deined' error if multiple processes try to download the same chart version concurrently #31128
- SDK: Fixed a bug where users did not receive any logs from the waiter, causing confusion as several minutes could pass with no user feedback #31717
- SDK: Fixed a bug where server-side apply defaults did not always match the CLI defaults #31732
- SDK: Fixed a Go import issue when downstream tooling attempted to vendor helm.sh/helm/v4/pkg/kube #31852
- Fix import d47cb2b7efaa26090510f4c2289127f40451062e (Evans Mungai)
- Fix lint warning f7cec12e23fe800495814432da4368b54c6d4552 (Evans Mungai)
- fix(values): preserve nil values when chart default is empty map 8c5fe4ef9781c714dc121288a4d499e62cc10bf8 (Evans Mungai)
- fix: bump go.opentelemetry.io/otel/sdk to v1.40.0 for GO-2026-4394 5b26d4f1f99091262fef50ed51133e7ae8e3b011 (Terry Howe)
- fix: bump fluxcd/cli-utils to v0.37.2-flux.1 360c1315ba2d468fcff77193f52764c6ad912c90 (Terry Howe)
- fix: insert newline after doc separators glued to content by template trimming b868e6a7cce696744d3f0c87e3f6bba6a779aff3 (Matheus Pimenta)
- fix: correct import comment in statuswait.go from v3 to v4 dbfbea91e34220911481f82fc6831284d954959a (rohansood10)
- fix pulling charts from OCI indices 2fe6b106e6d515b6792d53aff517489ae97387be (Pedro Tôrres)
- fix: handle OCI digest algorithm prefix in chart downloader (#31601) e3e2d01ef45c6e4179d0536ea4a475f18fa23846 (Evans Mungai)
- fix(install): check nil for restClientGetter and fix tests c15e7114dc0a0f24e0fda65dff83e7a18e264f60 (Manuel Alonso)
- fix(test): fix tests and check nil for restclient 4b896ca82fa827760086998d6521965e0ace059f (Manuel Alonso)
- fix(test): merge fix correctly 3fc79399c8af02b6704c10cba14be2ced9497cb2 (Manuel Alonso Gonzalez)
- fix(install): add more tests and check nil file data 6017d2b470b07a4f55efd2c55ac0745203ddcd0b (Manuel Alonso)
- fix(test): no check empty resources f451967ab5a5a9b1a26deb699bd1a1f4f2ba6b1e (Manuel Alonso)
- fix(install): check lenght and file nil, add tests fdadff59eb8c3552de76c7647a9c787c248cdbd2 (Manuel Alonso)
- fix(action): crd resources can be empty 10d606726560f1e813617c050c7b9cfbb8b0cb26 (Manuel Alonso)
- fix: casing issue fixed 0fec40f9b61a1dc5799e67bd4fb4ea4321cdd836 (Mujib Ahasan)
- fix: error handled correctly 263749874cb21ba31ebca17fe6c19fb3d0379417 (Mujib Ahasan)
- fix: doc string added 961d7d7cd6b39ccc3a63bce7bba505b94a9be384 (Mujib Ahasan)
- fixed: --dry-run=server now respect generateName f289d1605c9f02c843dd1b5dd03221fdb980f28e (Mujib Ahasan)
- fix(downloader): safely handle concurrent file writes on Windows bfac7393e4cc8b22a36fb015264d10ddb30e03da (Orgad Shaneh)

### 4.1.4

- 4.1.5 and 3.20.3 are the next patch (bug fix) releases and will be on April 8, 2026
- fix: Plugin missing provenance bypass 05fa37973dc9e42b76e1d2883494c87174b6074f (George Jenkins)
- fix: Chart dot-name path bug 4e7994d4467182f535b6797c94b5b0e994a91436 (George Jenkins)
- fix: Plugin version path traversal 36c8539e99bc42d7aef9b87d136254662d04f027 (George Jenkins)
- fix: pin codeql-action/upload-sarif to commit SHA in scorecards workflow c61e0860ec797330a4c26a78dde7020cdc6743b1 (Terry Howe)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **4.1.4**, the newest release recorded here for this line.

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
