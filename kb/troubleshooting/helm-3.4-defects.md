---
id: TROUBLE-HELM_3_4_DEFECTS
type: troubleshooting
title: "helm 3.4: defects fixed in the 3.4 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.4.0 <3.5.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 3.4 known issues
  - helm 3.4 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 3.4 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 3.4: defects fixed in the 3.4 line

## Summary

**43 defects** the project fixed across **3 releases** of the 3.4 line, from 3.4.0 to
3.4.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.4.0

- 3.4.1 will contain only bug fixes. It will be released on November 11, 2020
- Fix wrong function's name in comment a167b3fc8719db19e87280bc134a24801808272e (zouyu)
- fix example time format b17cf19a2eab5664375c8578531940cafe4aa035 (Abhilash Gnan)
- fix ls command example 78177de664942452485aee890ddf07fa1cf4e420 (Abhilash Gnan)
- fix: allow serverInfo field on index files f19acbdc94578194d19a6758f01cd8eed85b792e (Matthew Fisher)
- fix(cmd/helm): add build tags for architecture 45d230fcc95c1c4d2e055b7451a988441f038509 (Adam Reese)
- fixed bug that caused helm create to not overwrite modified files 106f1fb45c93fe862ac86d9b774e2de8b1dd314c (Matt Butcher)
- fix: if not .Values.autoscaling.enabled indent b4bb73d8ceeb4abf70c1a2e57d4779b5bfd6a82e (Thulio Ferraz Assis)
- fix: check mode bits on kubeconfig file 82398667dfe208407be9fe499ac96240aa8ce54b (Matt Butcher)
- fix incorrect wildcard expand d1c8561be6e6b08bbf425dc79631149100a1e0db (Li Zhijian)
- fix(comp): Disable file comp for output formats 459dcd7f728b38ec44c72d79192ee93d6964d53d (Marc Khouzam)
- fix: with .Values.podAnnotations indent template 6766017d388cbc21636f6b1deb9ab931a4617259 (Thulio Ferraz Assis)
- Fixed a variable name collision caused by two PR merges (#8681) 04fb35814f64122c0aa08165f6fdb7b67c216558 (Matt Butcher)
- Fix/8467 linter failing (#8496) 70d03e5cefa8f42727e29db310f78aeae4d65bb0 (Matt Butcher)
- fix name length check on lint (#8543) 96d9ab9663b69cbd85444ca5232d8283017eeeea (Matt Butcher)
- Fix spelling in completion.go 45b084b25504a1e19592684f964f43b57792875a (knrt10)
- pkg/*: Small linting fixes 4abcdc40efb9ad455ed99bc73c8ee716fe89123d (Manuel Rüger)
- Correct checksum file links 8a545d6ca7e40ae412c53f5dc683ecc8a8ecdb96 (Ma Xinjian)
- Fix Quick Start Guide Link in README.md 5421c7e99526af9683491fe5e069ed001fb5fd58 (Tero)
- Fix linting issues 09172b468a7c8278c566880c26efd1078e43e5c8 (Dmitry Chepurovskiy)
- fix test that modifies the wrong cache data 131510aa94faaa66ea4b3c3b7e4156206902ffc5 (Matt Butcher)
- bufix: fix validateNumColons docs fbc32aea3d43853f94768e4bc7bc4045fe9fb749 (bellkeyang)
- Fix issue with install and upgrade running all hooks 44212f83dc9c893d962fe48648320e7b7b66950c (Matt Farina)
- fix watch error due to elb/proxy timeout 4faeedd98b03e5af7733317a84e77ebff28c55f7 (Rajat Jindal)
- Avoid hardcoded container port in default notes d141593d834f99822c08b9f3ca768258483afbf1 (She Jiayu)
- fix(sdk): Polish the downloader/manager package error return (#8491) ffc3d42f87f8334684f12372bbdda8147702a12d (Holder)
- fix insecure-skip-tls-verify flag does't work on helm install, Keep FindChartInRepoURL and FindChartInAuthRepoURL functions signatures intact. 52295490fd7a22c05058ad6eab794ccd4fdf3193 (yxxhero)
- fix: Allow building in a path containing spaces 9a13385022b0976a704c24c8d11e7b0f3561b931 (Chris Wells)
- fix(create): update the hook name of test-connection pod 9777925a2ae1e98a3e7ec3923d0b56b7199c7806 (Dong Gang)
- fix(helm): Update test during pending install 0d70c63396083f868963797632715f06c9b90ca9 (Cristian Klein)
- fix(helm): Added test for concurrent upgrades 20fb7bac4e9001751a0b04c71006b4bb506378cf (Cristian Klein)
- fix(helm): Avoid corrupting storage via a lock 9a4f4ec64b8092d2ba3d7493001837df4737e36c (Cristian Klein)
- fix the code style error 1dfe66aa85bf09cd1f09271c2810c5deb9f22454 (Dong Gang)
- fix(kube): use logger instead of fmt.Printf 8217aba4a6cf04bac538ba2178603ec1378dbaef (Hidde Beydals)
- fix windows build failure caused by #8431 7ba8343b8d0edc1a3de96ee15003b072c7e72627 (Jack Weldon)
- fix conflict d58a984878ea290e04a135ef037b75e13b7b8df5 (zwwhdls)
- fix another extreme case 4532485fd03a8cb56186c93ffeba285431073429 (zwwhdls)
- fix #6116 5396df2e282c61ffb1fc8fa65240c36a0216055f (zwwhdls)

### 3.4.1

- 3.4.2 will contain only bug fixes and be released on December 9, 2020
- Fix that the invalid version number of the helm package command will escape b266b571ce971574ac07e4513cdce05e2db0a8be (wawa0210)
- Fix the lint error message for valid names 1f6fd5df26514907d1ac2014f44ca399cdf0b8fc (Martin Hickey)
- Fixes Error: could not find protocol handler for e1858f78359af4948a94628fa318e44cd2e1aaa0 (Matt Farina)

### 3.4.2

- fix: ingress path issue 3ba833f5ad97c157a3a27b9985d6f0c660db901e (Salim Salaues)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.4.2**, the newest release recorded here for this line.

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
