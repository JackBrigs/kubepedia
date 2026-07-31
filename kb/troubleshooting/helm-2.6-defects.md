---
id: TROUBLE-HELM_2_6_DEFECTS
type: troubleshooting
title: "helm 2.6: defects fixed in the 2.6 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.6.0 <2.7.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 2.6 known issues
  - helm 2.6 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 2.6 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 2.6: defects fixed in the 2.6 line

## Summary

**28 defects** the project fixed across **3 releases** of the 2.6 line, from 2.6.0 to
2.6.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.6.0

- Fix Typo in Contributing Guidelines 6de79b7ea8d5769c6aad4ffb34cc98a5603fc7b5 (Malepati Bala Siva Sai Akhil)
- Fix the default NOTES.txt bbf2d6b7e8b9208e5246f134eb881de65b455116 (Maxime Guyot)
- fix(helm): pass os.stdin when executing a plugin (#2740) e61ee5c54e1d24e791f516cb61059fc910befd1b (Maciej Strzelecki)
- Fix link 1c3d9b892e3ec7496e9bac53274d3a01396136c8 (Miouge1)
- fix spelling error 3ee74217d162a21ced3df5c6b901b520ed64a4d4 (jiaweizhou)
- fix(pkg/strvals): use rune literal instead of ASCII a5dc546726e664db822104cb612fb74a4a134df0 (Sam Leavens)
- fix(pkg/strvals): preserve leading zeros in vals 609e72b357c8be43c3ec5f2d148f2188233ef0b1 (Sam Leavens)
- docs(fix): fixed misspelled word 97893afc620fb454c880df1cdef35f7430f5f7a5 (gardlt)
- fix(pkg/chartutil): Fix test, improve message cf09e344d186b6292fed5ddc5c2aeea1350ed199 (Sam Leavens)
- fix(tiller): remove locking system from storage and rely on backend controls fa68a6e1db81cbc113c3b289c81ab5d0600ec4a3 (Justin Scott)
- fix(helm): fix flag parsing once and for all a29e610938b1a4f59ea2c038d0d23193d54bb2f9 (Adam Reese)
- fix(dep): Fixes out of date dependency info 564ba7ba7ccc5aaf074222d8dec1c0f5091ca2f2 (Taylor Thomas)
- fix(helm): fix `helm get` subcommands b671888ff4442cadaa47bd46d37eb1ff5639181c (Matt Butcher)
- fix(helm): support HELM_HOME during plugin loading 876cbc205c8d3a158a65db903b256596df2523e5 (Adam Reese)
- fix(tests): fix sorting hooks test flake 9325d136d4ee619a3d8fc1cd22c91585f31b67fa (Adam Reese)
- fix(helm): load home from flags during runtime dd952e61f0922a5baad2d2e39107913fdaf4ec5a (Adam Reese)
- fix(docs): run docs generator 057c747c1fcca755ea4dfc4c61ac50905acccffc (Adam Reese)
- fix(semver): Prerelease number comparison issues 453e79ffc51c89c193d513a26eece343753e56c1 (Matt Farina)
- Fix a bug causing 'helm depndency update' to delete required charts 04a7e241e67630e2019e6a58f373f6490829dc9c (Alon Lavi)
- fix scripts/get runAsRoot CMD var building 974c4b67c7a9241887ca223d978f47052b29e575 (Tony Fahrion)
- Fix broken tests due to "server-side" text change. b704947d54cbbe10c54e247f85fcfa5fb79d6065 (Justin Scott)
- Correct punctuation and capitalization for user facing strings. af4c243ee377ca1b52a55f5b5292bba33b25cf31 (Justin Scott)
- Fixed helm test sample. c19bba17c530453e02c5fd85012092643103f676 (William Denniss)
- Fix markdown syntax in doc 963aca1d7843f9894cc8a7010050634ca84f2485 (Yuvi Panda)

### 2.6.1

- Fix(helm): Fix the bug of dependency update deleting subcharts 165818e39102e84c7dcb76e72db5670fc16b7a42 (Adam Reese)

### 2.6.2

- fix(deps): fix issues when running glide up be3ae4ea91b2960be98c07e8f73754e67e87963c (Matt Farina)
- fix(helm): Fix the bug in helm dependency update -verify 7ed614d06d1f6b6ad243c04f9e36ae79ed8f74f0 (@rocky-nupt)
- fix(helm):Fix dependency aliaes not working 5f1defd07255b98760be568cc380ab0b4e90db18 (@llsheldon)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.6.2**, the newest release recorded here for this line.

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
