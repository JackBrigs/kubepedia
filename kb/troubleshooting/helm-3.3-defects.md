---
id: TROUBLE-HELM_3_3_DEFECTS
type: troubleshooting
title: "helm 3.3: defects fixed in the 3.3 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.3.0 <3.4.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 3.3 known issues
  - helm 3.3 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 3.3 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 3.3: defects fixed in the 3.3 line

## Summary

**48 defects** the project fixed across **4 releases** of the 3.3 line, from 3.3.0 to
3.3.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.3.0

- Fix issue with install and upgrade running all hooks 8a4aeec08d67a7b84472007529e8097ec3742105 (Matt Farina)
- fix(template):Issue:helm template with --output-dir (#8156) ceff32d5f8aa173549426625b608137a47981447 (DongGang)
- fix(cmd): display warnings on stderr 863588ca69209153863f72327fe8c818c963904a (Matthew Fisher)
- Fix some go-lint warnings c6a00e63ef638c14be5560534c339484e35eb7ba (zouyu)
- Fix golint issue 7ec501155d082d2e2cc314d7fd03729b5873f21c (Guangwen Feng)
- fix template command use --show-only flags error in windows environment 4f136861d397ec37b18c92ceee8027333ba1bc24 (ShenXinkang)
- fix(chartutil): do not set helpers.tpl filetype for vim aa033196692ea9c4416fbb3859bebf05aded6bef (Adam Reese)
- fix(doc): generic description for --version/verify e09e8604e6160775890c154b1fb8b6683a8bbb6f (Marc Khouzam)
- Fix description is ignore when installed with upgrade 562767b04015546e53677bb3c8aa5cae12897fa3 (wawa0210)
- Fix crashing `helm chart list` with large list a0fd1d81f03aaabbd961f0bfd0dfd907493078c6 (Peter Engelbert)
- Fix issue with unhandled error on Stat f182ebc11c9ea7a5bf75e35d8e061f3ac68482fd (Matt Farina)
- Fix unit test 5600a2c82d236422e54b6089d5384dea44349900 (Martin Hickey)
- Fix repo cache setting 2ae83f276b60085c550fc81fb6e21b38146e2d9f (Martin Hickey)
- Add new line to fix code formatting in doc e6069769151b91c91a107bd4d79ca3a941658518 (Maksim Kochkin)
- fix(comp): Prepare plugin completion for Cobra 1.0 0366f9970f0ff5c0b61b02521d139445bfaeba8f (Marc Khouzam)
- chore(*): Fix formatting b18e7e201e55ba38fdecbcf81e4da512e55444b4 (Marc Khouzam)
- fix: upgrade using --force shoud not run patch logic (#8000) decab8ea2e6ea4b31560aff50abb2676a67ec8ba (小明同学)
- fix security mailing list address 2f39854d3f5da2f13cd749ccb08d61982cafef2f (Matthew Fisher)
- Fixes repo parsing 8cb9ab7095c885e1f8d9bea3a28229f58ba59a5e (Juned Memon)
- Fixes repo parsing b473f8adec7dab35614f0c20b0738a865830b443 (Juned Memon)
- docs: fix capitalization in a few help messages bc515991f8fb7c3294e7f7809778fd360751d5cb (Liu Ming)
- fix: removed strict template errors in linter (#8017) 08e546f169ff3d5694863f0766c3132da2f095b7 (Matt Butcher)
- fix: use correct regular expression for Kubernetes names (#8013) 524150c662f9c030d2caa9ad8f79d2ff9521c431 (Matt Butcher)
- Fix markdown table in helm command doc fb829c2c843df01ad1dd5ffd13c4e923be4ab9e9 (Lüchinger Dominic)
- Fix : Prints empty list in json/yaml is no repositories are present (#7949) cd50d0c3621ad91b3848f14b7ef3a8d6aa29d2c9 (Anshul Verma)
- fix: write index.yaml file atomically (#7954) 984d2ac7676874ae78a7617f7417513a7a9b5ef2 (Raphaël)
- fix(pkg/cli): ensure correct configuration from kubeconfig file 4a0dfbe53b2191e09a7034ce97e4caf84989d6db (Adam Reese)
- fix(cmd/env): make helm env command respect cli flags (#7978) 9ced0165aba1f0d90990396306d6f7e7a6725a91 (Adam Reese)
- fix(*): remove bom in utf files when loading chart files (#6081) 27ebfa8c561e758b60872b9bb081253036e559ff (Thomas FREYSS)
- fix(pkg/plugin): copy plugins directly to the data directory (#7962) 1cdd0a20488637c77d92e9a4844e89e8cefd578d (Adam Reese)
- fix linting error with lookup function (#7969) bb47286f09331271e88e6047c51fd6e0ea936506 (Matt Butcher)
- fix(helm): allow a previously failed release to be upgraded (#7653) 1911870958098b774973c6fe56bfdf4441f61596 (Matthew Morrissette)
- fix(pkg/kube): continue deleting objects when one fails bdf6f48704ed9e09d7fa636f025a3e2d344d42d4 (Adam Reese)
- fix: allow to rollback to previous version even if no deployed releases(#6978) cca68288063d235a4c32ef1ba822dd487317c8dc (liuming216448)
- fixed to mirror master f604105547dc260f4388792de44a6eb9d2a1353f (EItanya)
- fix test 2f534f97424ce4eaa3356e199e453e94bd65b4c6 (EItanya)
- Fix a typo "update" -> "updates" (#7346) 00769c4512c9c145eafb84f60e8a473de83b0209 (Hu Shuai)
- fix(cmd): Fixes logging on action conf init error (#6909) b7ff1e29327d33b6fe9b44b11d84c182d1adea45 (Jorge I. Gasca)

### 3.3.1

- Fix spelling in completion.go 249e5215cde0c3fa72e27eb7a30e8d55c9696144 (knrt10)
- Fix Quick Start Guide Link in README.md 800c627556938a0d632ef9d998dc1599f7ccc74c (Tero)
- fix test that modifies the wrong cache data fcb5e7789045cb7e3cad5a7319d56819c7105ceb (Matt Butcher)
- bufix: fix validateNumColons docs 53f68d8b64df51f87f70e0a9f28258bef18752a1 (bellkeyang)
- Fix typo ffc0aff3408e5c4b1973543e05f67e5aefe8ef59 (Martin Hickey)
- fix: Allow building in a path containing spaces 58f61d740ac5e97c66124bd5e69b7874d84cb971 (Chris Wells)

### 3.3.2

- fix(cmd/helm): add build tags for architecture 45d230fcc95c1c4d2e055b7451a988441f038509 (Adam Reese)
- fixed bug that caused helm create to not overwrite modified files 106f1fb45c93fe862ac86d9b774e2de8b1dd314c (Matt Butcher)
- fix: check mode bits on kubeconfig file 82398667dfe208407be9fe499ac96240aa8ce54b (Matt Butcher)

### 3.3.3

- fix: allow serverInfo field on index files 55e3ca022e40fe200fbc855938995f40b2a68ce0 (Matthew Fisher)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.3.3**, the newest release recorded here for this line.

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
