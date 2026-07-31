---
id: TROUBLE-HELM_2_13_DEFECTS
type: troubleshooting
title: "helm 2.13: defects fixed in the 2.13 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.13.0 <2.14.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 2.13 known issues
  - helm 2.13 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 2.13 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 2.13: defects fixed in the 2.13 line

## Summary

**43 defects** the project fixed across **2 releases** of the 2.13 line, from 2.13.0 to
2.13.1. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.13.0

- fixed an issue where the output of `helm status` was unsorted
- fixed an issue where helm ignored build metadata with `helm fetch --version`
- fixed an issue where Tiller was improperly sorting unknown resource types and namespaces
- fixed an issue where `helm install --set someval=0` would treat the value `0` as a string
- fixed an issue where tiller would not respect `helm.io/resource-policy: keep` during an upgrade
- fixed a regression where `helm reset --force` would orphan the replicaset backing Tiller
- fixed a regression where `helm install --name` would not accept periods in the release name
- fix: helm display confused error message if version is empty (without quotes) (#5310) ccf1d7bc4b30a2c53f18d52bd5c2de36c75e42e4 (Alex)
- fix: helm fetch wrong version chart (#4850) f5986db184cf6d16dcd48760ac749a20236fb845 (liaoj)
- fix: Update gRPC to get better TLS connection handling (v2 minor release) (#5210) 70c509e77ee2acecc722c429bc78415b2c660616 (Matt Butcher)
- Fix function comment to consistent with its name (#5294) 9fb9850aca4afab0d38bcd73218098a145b4e7ac (lIuDuI)
- Fix function comment to consistent with its name 5767f13aaa5bfb513747b73f3c5d8cd4b0640684 (xichengliudui)
- Correct golint warning (#5287) bed4054c412f95d140c8c98b6387f40df7f3139e (Gábor Lipták)
- Fix issue #5273 for get script on armv7l (#5275) 6e26320befd19cc112f72d51e29230c26a191d9e (Alex Ellis)
- fix(helm): add descriptive error if dependency has blank "repository" (#5152) d8bdf484cc77e5e816b311d99609a2511c897eea (adshmh)
- fixed minor typo in doc (#5249) c2e8720c7258dbfbee7cd2ed73114160a937e8fd (Jecho)
- fix(helm): add test for repo update strict flag (#5183) 3953f0e884afd85a68ab4d8b4488cec735e2bc58 (adshmh)
- Fix: kind sorter incorrectly compares unknown and namespace (#5186) f5df47b1c855e02c66f57756af224bc9b1055b09 (Alexander Matyushentsev)
- Fix incorrect flow example and improve operator documentation (#4919) 7a70459ca1913fcffeb374eca4446c5f97427da9 (Alex Speaks)
- Fix: type conversion for zero values (#5151) 69c7ba320e041894c073f7f62a98075b72c6bfd8 (Flavian)
- Fix some spelling errors in comment (#5246) 9e18364fea6cc8a2cd97a2fa1b40650583b1eeff (JoeWrightss)
- Fix code syntax highlighting in docs (#5245) 251a6a2b580158b5dfb34e8b08b10071e6353c1a (Dean Coakley)
- fix(tiller): respect resource policy on upgrade (#5225) ab0ba3aa630f64e0fd46cdd6726645a7e3520db9 (James Ravn)
- Fixes #5046, zsh completion (#5072) 4c1edcf0492f7e6a315dbeced3c008e96a40bc47 (Peter Stalman)
- Fix codestyle and update docs 869efd59be7a960466055bc30966ebd572a4ee09 (Alexander Nesterenko)
- Fix some typos in comment (#5215) 197e68ec1f5cde7a78fc5053a798f939378f4158 (JoeWrightss)
- fix: ignore pax header "file"s in chart validation 05a365358f43a452e523d3f76b1107b6f4ff2aa7 (Geoff Baskwill)
- fix: use RFC 1123 subdomains for name verification (#5132) 581e6cdbb8e42753556ae48ccba8cef84c40f736 (Matthew Fisher)
- Fix delete.go file permission (#5194) 812b74aca5f14ea67b531a41687abfee8a6399a6 (Koichi Shiraishi)
- fix: perform extra validation on paths in tar archives (#5165) 5603fe8d3e6ca9347ea0c2a94b2b33a55f5134cd (Matt Butcher)
- Fix some spelling errors (#5114) e70bea6adb6825e4f0cce1917121e6e000bf9049 (JoeWrightss)
- fix minor build issue cbf9ad11be1153d72cade3212d708112af97eefe (Elad Iwanir)
- Revert "Fix for existing CRDs are deleted when crd-install hook is introduced (#4709)" (#5067) 29ab7a0a775ec7182be88a1b6daa9e65a472b46b (Matthew Fisher)
- Fix(helm): Use spaces in ingress template 89467a8bf154aa19ad41c6775dc4a4f7ce6dfc04 (Alex Humphreys)
- Fix some spelling error (#5032) e9a5465c661a7543d5a968f0020fc4729f95874f (JoeWrightss)
- fix(helm): Correct and improve resilence of template check in unit test (#5010) 146c61af3765417c4b0d95bbb1a4ad73d3c228c9 (Henry Nash)
- fix(helm): get rid of lint warning in pkg/storage (#5021) adce632c830b28ca5bf56e5a9df583a06cacef82 (Henry Nash)
- fix(helm): Print details for pod resource ede43a313dde2611ea63e89546af46854b4121d4 (Morten Torkildsen)
- fix(helm): Fix linebreaks when printing custom resources 5ac37fba9952e2df8a29c42500ee5746c3325c74 (Morten Torkildsen)
- fix(helm): add --render-subchart-notes flag to 'helm install' and 'helm upgrade' 1518f961af426bfb4ce8f4ef515c4d90b1a475fb (jgleonard)
- fix lint warning 61156e66565aaf5903efabcc5710846989a20f84 (Rajat Jindal)

### 2.13.1

- pkg/chartutil: fix SaveDir for nested templates directories 618447cbf203d147601b4b9bd7f8c37a5d39fbb4 (Joe Lanford)
- Fix #5046 compatible with MacOS (#5406) a6ccbdaa9e47d61111c88dae259a155bc1540f02 (Marc Khouzam)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.13.1**, the newest release recorded here for this line.

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
