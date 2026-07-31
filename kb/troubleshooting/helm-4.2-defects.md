---
id: TROUBLE-HELM_4_2_DEFECTS
type: troubleshooting
title: "helm 4.2: defects fixed in the 4.2 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=4.2.0 <4.3.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 4.2 known issues
  - helm 4.2 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 4.2 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 4.2: defects fixed in the 4.2 line

## Summary

**71 defects** the project fixed across **3 releases** of the 4.2 line, from 4.2.0 to
4.2.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 4.2.0

- fix: add -extldflags -static to dist target to match build-cross f60ab7c31c81a73b8e0aade5aff41bfc01c08820 (Terry Howe)
- fix: address goreleaser build issues flagged in review c075022ce16489f5f7afd45a37b679cf58fa36ea (Terry Howe)
- fix: pass VERSION as GORELEASER_CURRENT_TAG to preserve v-prefix in archive names 04885dd905b6f8a823733dbc9b9f5cb2843a975f (Terry Howe)
- fix: disable goreleaser checksums.txt and restrict zip to windows only 93103ce66cb6374d9d7b552802f53b21ea2c2dd1 (Terry Howe)
- fix: use index for optional env var in version_template e49a1dc16eee526928d8928b8d96c01ee513ebd9 (Terry Howe)
- fix: canary build file names eaa09100b9b18175d878b1e114cbe9df2a3f70c2 (Terry Howe)
- Fix archive name 5a75279c1a017a60b97bd44986288af7399c6ff8 (Terry Howe)
- fix goreleaser archive 37284a9211972f7f41a2acc3c3313517596dd4b0 (Terry Howe)
- fix artifact directory a9659b07e3eec20ab5b964fddae05f51f478f704 (Terry Howe)
- fix: adds topLevel permissions to improve openSSF scores 277d9702555532d13426119d31c70fffb389d589 (Gagan H R)
- fix(templating): hooks conflicting with templates in post-renderers (#32049) 8f56f24d638612a46f3e23265d06338c1f93bccb (Matheus Pimenta)
- fix(templating): SplitManifests must preserve line endings for downstream YAML parsers (#31952) 265c5eb530a36ec651e79ecf4d37ba2f098b7e59 (Matheus Pimenta)
- fix(values): do not copy chart-default nils into coalesced values 00638773d1366dc962c785de3d297cf0279b9a0d (Johannes Lohmer)
- fix(templating): fix wrong YAML separator parsing for post-renderers (#31941) a27f1add79c6c02459413dbb60f8438d8051cf06 (Matheus Pimenta)
- fix: add debug logging to HTTP getter for helm pull c26be60d81e5cb6a147d6088477cf86fd5aaf1f0 (Cairon)
- fix: unnecessary-format lint issues from merge 087736b66e97393ccaa0bdf1e5df13dcc9d88340 (George Jenkins)
- fix: Plugin missing provenance bypass 586eb57338d848e65686a3a9616e2776e87cfd1e (George Jenkins)
- Minor nit: fix import instructions to comply with canonical import paths de58531ca7ff557342acaa2c906082e58521ef47 (Anmol Virdi)
- fix(action): return correct error variable in prepareUpgrade 8ef2d45934ba1b9ca341818f1157112fcf7cdf1d (Rhys McNeill)
- fix(kube): clarify server-side apply patch errors f257c95c783f5595e36cb5a7dcc862cc1f6266b5 (abhay1999)
- fix: pin codeql-action/upload-sarif to commit SHA in scorecards workflow 7025480397d8b6b7fd8cdb5e083dc37b62dbd3d8 (Terry Howe)
- fix(kube): remove legacy import comments from test files e64d628a139fab8c876a1d2f4c2928096b286bed (Terry Howe)
- fix: Plugin version path traversal 36dcc27ca3c0cd6d0d08713b03dca82f43d7c5f9 (George Jenkins)
- fix: Chart dot-name path bug 60184996e5332d26e0b6390cefbf86776829dc46 (George Jenkins)
- fix: insert newline after doc separators glued to content by template trimming af94abf976ce69dd635aaf086a0bb4b17bd95bc1 (Matheus Pimenta)
- fix: bump go.opentelemetry.io/otel/sdk to v1.40.0 for GO-2026-4394 b550ce90946b3b47cecd290fc5d0eee637ddb531 (Terry Howe)
- fix: bump fluxcd/cli-utils to v0.37.2-flux.1 1dfa77ed8ba6f9e26542064248bc9eab40c1a662 (Terry Howe)
- fix: enable nolinlint linter 5b6c6bbfc7ca9850c69d3823ca1e21b445e75c0d (Matthieu MOREL)
- fix: correct import comment in statuswait.go from v3 to v4 c59c140ce07ce973f16fe50c0c5e991e1d6308a6 (rohansood10)
- fix: handle OCI digest algorithm prefix in chart downloader (#31601) ee018608f6fbf381fac1bae9759164a65c6a0b1f (Evans Mungai)
- fix(pkg): errorlint linter 259f76a849391e6ff60a9a2e95ce7310d958c602 (Matthieu MOREL)
- fix(internal): errorlint linter 025418291a7911441e7962895ba4bc24b72b55b3 (Matthieu MOREL)
- fix(pkg): errorlint linter 6d1490ed1ea5968235087658d03bb440e4014a36 (Matthieu MOREL)
- fix(pkg): errorlint linter 4d0ae7f33a09093f8f52d02b952e3822c87b8c5f (Matthieu MOREL)
- fix(internal): errorlint linter abecafa0f507a69888877b9ddb714095714b64c8 (Matthieu MOREL)
- fix(pkg): errorlint linter 4330bdea0409f428e75145f15532bfa0e2bc945c (Matthieu MOREL)
- fix(pkg): errorlint linter c8989d984ff69e8ad21b27d6ac6193dd3150b1a7 (Matthieu MOREL)
- fix(cmd): errorlint linter edbd705bd034246700cc0998016caa303cff42dc (Matthieu MOREL)
- fix(downloader): safely handle concurrent file writes on Windows 76eb37c01aaece271343039f44d7803017dd5c81 (Orgad Shaneh)
- fix(install): check nil for restClientGetter and fix tests 9817a68618245370e98e09d7f06c7cc1cefe8a62 (Manuel Alonso)
- fix pulling charts from OCI indices d983696e354a9e0605cbb3034937dc84af42995c (Pedro Tôrres)
- fix(template): deprecate unused --hide-notes and --render-subchart-notes flags 6d5f56fa6e7c8e4462d80895fcce87b926e4b8ce (Scott Rigby)
- fix(copystructure): handle nil elements in slice copying e3829ebbbb833e159926c6193e474eb9d067ef75 (Philipp Born)
- bugfix(storage): fix storage not getting logger from driver a8eb5278478c940c615741312ca9f4fec0d84c1a (Matheus Pimenta)
- fix(test): fix tests and check nil for restclient 0f949a92c149cf11e5bb19caf4d19d05567be6eb (Manuel Alonso)
- fix(test): merge fix correctly 561410ae1d09c2aa289ff8d8cad5b7fa979cd135 (Manuel Alonso Gonzalez)
- Fix import b8937ad1922bca47be8bbf8e6274608ebc34a778 (Evans Mungai)
- Fix rollback for missing resources 374aeb4b4e0463f72e3a0175138ed4bf7e87a156 (Feruzjon Muyassarov)
- fix(install): add more tests and check nil file data 00f0a48a7dae379c2b6bd0dea43984d42b27a494 (Manuel Alonso)
- fix(test): no check empty resources 0357e8d0f7eab074252ca49e1ca3aded834a001d (Manuel Alonso)
- fix(install): check lenght and file nil, add tests 52235cc0bf7d0c8faf17c7dc8cddd77f93434aea (Manuel Alonso)
- fix(action): crd resources can be empty 268593bf2e9769ef4b75328b33dfb4195e6e9e5a (Manuel Alonso)
- fix: casing issue fixed 170911459bc4f2b5efea7e549e09bd45c7578cc4 (Mujib Ahasan)
- fix: error handled correctly 94860626ce9c83a9227b5bce02a5c03a050816ac (Mujib Ahasan)
- fix: doc string added 12e8b715aa0732b613c3a9896fa6af29b3201536 (Mujib Ahasan)
- fix(values): preserve nil values when chart default is empty map 292fe702193e8ba9ce4c8ffffdd90cdfa761501c (Evans Mungai)
- fixed: --dry-run=server now respect generateName 2820ebe8c97b7d7b8a447375b74c9cb3741a4ffa (Mujib Ahasan)

### 4.2.1

- Fixed data race detected by -race flag when concurrent goroutines (upgrade + rollback, install + uninstall) both call GetWaiterWithOptions on the same FailingKubeClient instance #31925
- Fixed helm command success messages writing to stderr instead of stdout. Now correctly outputing to stdout #32056
- Fixed Helm 4 emitting "unable to find exact version" when using version range constraints #31757
- Fixed a race condition in WaitForDelete where the status observer canceled the watch too early, causing intermittent failures when running a full test suite #32081
- Fixed SDK errors by upgrading dependencies: cli-utils 1.2.1, controller-runtime 0.24.1 and k8s 1.36.1 #32128
- fix: protect FailingKubeClient.RecordedWaitOptions from data race (#31925) d591a19b953bd9cfdf7d9ddd83c2f4ffdaeafb29 (Terry Howe)
- fix: route registry client output to stdout instead of stderr (#32056) 2a9fcae29280472edec988c6bf0528e4ae79b33a (Terry Howe)
- fix(version): avoid false range detection on prerelease x/X eabfae560459d1ffe1f7a3268d5441238e9f84b2 (Benoit Tigeot)
- fix(version): version range || can has no space e3fd51f331e14fb4056951540d2f2ffde81b405c (Benoit Tigeot)
- fix: prevent warning when using version range constraints a33e23939a85ac60eb9a6bee818f2c5459fda576 (Benoit Tigeot)
- fix(kube): always propagate context.Canceled in WaitForDelete fa06d4455724afe22bbe00af7925549a82d95e6c (Terry Howe)
- fix(kube): prevent spurious early exit in WaitForDelete during informer sync 360d4835df0fb8bd7cbde4cad0cbc79de01a6e93 (Terry Howe)
- fix(upstream): upgrade to cli-utils 1.2.1, controller-runtime 0.24.1 and k8s 1.36.1 57a4803bd4953d8ef9d51d927f492ecaaf5df9db (Matheus Pimenta)

### 4.2.2

- Revert: Fixed a race condition in WaitForDelete where the status observer canceled the watch too early, causing intermittent failures when running a full test suite #32214


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **4.2.2**, the newest release recorded here for this line.

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
