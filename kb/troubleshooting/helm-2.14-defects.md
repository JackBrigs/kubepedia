---
id: TROUBLE-HELM_2_14_DEFECTS
type: troubleshooting
title: "helm 2.14: defects fixed in the 2.14 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.14.0 <2.15.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 2.14 known issues
  - helm 2.14 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 2.14 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 2.14: defects fixed in the 2.14 line

## Summary

**43 defects** the project fixed across **4 releases** of the 2.14 line, from 2.14.0 to
2.14.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.14.0

- fixed an issue where Helm will print `ROLLING BACK` on all failed upgrades when atomic has not been set
- fixed an issue where CRDs installed through the `crd_install` hook might not be in the established state before the hook completed
- fixed an issue where the scaffold chart (`helm create`) would not install
- fixed an issue where `helm reset --force` hangs when Tiller pod is already removed
- fixed an issue where Helm completion in zsh was not compatible on MacOS
- fix(pkg/storage/driver): use shallowReleaseEqual() 05811b84a3f93603dd6c2fcfe57944dfa7ab7fd0 (Matthew Fisher)
- Fix formatting issue ee63d06192c7f8f90c8520d541defd32864e3977 (Elliot Maincourt)
- Fix typo e6d5fc933b81093050459397f011673ca83c508c (Jon Huhn)
- Fix missing link 51c99b125224093802def010a48d763ffab5b6df (Joshua Bussdieker)
- fix(helm): Regenerate go types from proto 072cd6af37bb9856aaabebe02b7489cd18a80293 (Morten Torkildsen)
- Fix scaffold chart label in helper template 470d92e126968478d4e7a0d96207f102d174d545 (Martin Hickey)
- Fix environment list in helm doc d082754b1ad9b93349e572cb6cee1a0e95dc49e5 (Martin Hickey)
- Reduce template code duplication. Fixes #5372 0270f2e2b5d75439d8c835969ec8d8d80bb55bcf (Luis Davim)
- Fix reset force which hangs Tiller pod removed 77185d31a95e5e66bb65a082ab0ed5cbf27a6192 (Martin Hickey)
- fix(helm): Fix manifest validation 32d7f1a3fc226c1745a58b51e318b7362bc7a0bf (Morten Torkildsen)
- Fix 'THE INCLUDE FUNCTION' in 'Developing Templates' output 2aa41559524f6d170a131eab251735b51fbc452c (Kenta Iso)
- Fixed default value for `helm.sh/chart` label e2a9bf29134297cacacf441c10ee6b1b2107ce5d (Sergey Kozlov)
- Fixed typos in docs/chart_best_practices 87e495c57d4585e6570cf2635644b97992ea5cd9 (Sergey Kozlov)
- Fixed a typo in docs 6cf433d719acbe165cf96000c935e11ad0147750 (Sergey Kozlov)
- fix(helm): Wait for CRDs to reach established state for crd_install hook b8e40a7c31faf094c950be40a0d08ce554bdc7dd (Morten Torkildsen)
- Fix description of helm dependency command 7990363d152dabf8de7b0d59d20d2f1d40733980 (Xiangxuan Liu)
- Fix `no RESOURCE with the name NAME found` 5ffe4ce5881449d31b9e14cb94d56dcf2453b0d7 (Timofey Kirillov)
- fix(script): remove check on release URL 65193adc10bc50edcf96499b5321c7aab46b796c (Arief Hidayat)
- fix(script): follow redirected URL of github latest release 7cb03fb5628f3decb9ab547c1f71ca6a21a31ee8 (Arief Hidayat)
- style: fix golint error in init.go for redundant err!=nil check 29795691edbc4ca28e8da28bb06700ae0d6d97d8 (tariqibrahim)
- fix(scripts): use a more precise method of grepping ab9cc982a0616e28d6e308d69033534cb7e62025 (Matthew Fisher)
- fix(tiller): fixed a typo in tiller and unit test 63ef73d4168980e650bc95c225f9be1b63b7b37c (Mikhail Kirpichev)
- Fix "helm init" parameters b480badd05ad01006363763c92b5394cdc5fc9c4 (Jens Frank)
- Fix debug printouts for zsh completion 4fec4b67661b7cc48b8ed1f1c5827a255c74db75 (Marc Khouzam)
- pkg/chartutil: fix SaveDir for nested templates directories a9c10fe104302f19e0eda5cec5b2ca314991cff0 (Joe Lanford)
- Fix #5046 compatible with MacOS (#5406) c94c00915f29fba5e816c277ff617babb3790cb1 (Marc Khouzam)
- Fix some typos (#5352) 63c970c5ce29b0971cdc6409d9c0e156321ea32a (Nguyen Quang Huy)
- Fix typos in various places (#5360) 268695813ba957821e53a784ac849aa3ca7f70a3 (tuanvcw)
- Fix many misspelling words (#5357) d9d2b3ae4812d756297ac89b8930eee61273c871 (Nguyen Hai Truong)
- trivial fix typo 2ca5d2ab9cf41a23a1d650ae2dc88a44344c898b (Nguyen Hai Truong)
- Correct misspelling of Helm d24ba97faeb39f692f74c87d183a723b4138ee52 (Nguyen Hai Truong)
- Fix wording in error message (#5322) 73a17eb59900348234ad7c4cba75a537dcef9708 (Miroslav Spousta)
- fix: helm display confused error message if version is empty (without quotes) (#5310) 9f964c11da1c1ae865aed2be87c1929f04683b82 (Alex)

### 2.14.1

- fix(helm): Disable schema validation for manifests 5270352a09c7e8b6e8c9593002a73535276507c0 (Morten Torkildsen)
- fix(helm): Only validate new manifests bf377c5ad5c05f0966ec5671b77ef8105c3c04dc (Morten Torkildsen)

### 2.14.2

- fix(helm): Delete hooks should wait for resource to be removed from etcd before continuing a8b13cc5ab6a7dbef0a58f5061bcc7c0c61598e7 (Morten Torkildsen)
- Fix nested null value overrides 85b4eef973d73ed9213b7ef76a404f2da7216dd3 (Adam Eijdenberg)

### 2.14.3

- fix: upgrade with CRD changes 0e7f3b6637f7af8fcfddb3d2941fcc7cbebb0085 (Yusuke Kuoka)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.14.3**, the newest release recorded here for this line.

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
