---
id: TROUBLE-HELM_2_15_DEFECTS
type: troubleshooting
title: "helm 2.15: defects fixed in the 2.15 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.15.0 <2.16.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 2.15 known issues
  - helm 2.15 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 2.15 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 2.15: defects fixed in the 2.15 line

## Summary

**50 defects** the project fixed across **3 releases** of the 2.15 line, from 2.15.0 to
2.15.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.15.0

- fixed an issue where numbers were being parsed as floating point numbers (see https://github.com/helm/helm/pull/6010 for more context)
- fix(kube): fix race condition d6580a1c4aa5cd0f7e499c34f96439ed0994c6e5 (Matthew Fisher)
- fix(kube): watch events from a matching pod 9b9dcebea87f6a719f4d5ad6a08314612cf9c616 (Matthew Fisher)
- fix file mode,it should be octal expressed ecf9afbe06e07189b04cbf1a33fb8bbc288a3b64 (Guangming Wang)
- fix repo url being decoded while downloading repo index (#6060) 519ccac2949695ad54a8f8b159b353b998462e03 (Karuppiah Natarajan)
- fix style 91356c81ebf843fee5f1b2fddfba12ec4e1ecaee (Matthew Fisher)
- fix: return more information to the user 74653d3794617fab35976fea2e5e02269b7a6101 (Matthew Fisher)
- fix: use nonexistent rather than inexistent a31d4ad43e785412fa7e69613422d1e9fc0623ab (Matthew Fisher)
- fix(validate-license): update to work with newer versions of coreutils 935ee90d9ff3af9ffc22735c0d6c092c5050f3ef (Matthew Fisher)
- fix(generator): fixup package comment linting error caff38ffa1fa8595b445f37c327c01015ea6bb58 (Matthew Fisher)
- fix-up typo (#6501) 9d8a84ee3daa0870689ba24ca8bf6bb13a0d38ec (陈谭军)
- fix issue when dependency is URL b49f4269c5bdfee920b0d5fd7954513f5e17dad6 (Xiang Dai)
- fix BusyBox sed (#6327) 540fe23b692ab22b04e4718644cc654d694abc04 (Anton)
- fixes resetting os env after test run c839363f16447344f180b0318b09a571bb407882 (Ken Sipe)
- Fix the developer.md typo (#6203) aaf24e065851e96632997b4849c98721745a7a12 (kamal namdeo)
- Fix wrongly displayed markdown 74b6279f5fa2533fbc6e9462eaa9df2dad0bc9cc (Eduard Laur)
- fix some log typos in tlsutil_test.go e9ea2e0d1524b7de68feb3efb7a763d92a360f91 (AllenZMC)
- fix mis-spelling in manager.go 7b0a407ff7247aa41ad8efc6c4c1e0bd2cc2a046 (AllenZMC)
- fix wrong spells in hooks.go 53f1ab50e5ec38a33e7329c79a2ad61e747c4e18 (AllenZMC)
- fix word 'resoures' to 'resources 915d69a2c6a0026599f28c4857edff1c1f45bab9 (AllenZMC)
- fix word 'efault' to 'default' 6b5ab08a61d73980ca6f84ccdb3f6b996d950cae (AllenZMC)
- cleanup: log message typo fix 4117b38ae621a8061563417c4b125dfb8ff59b00 (dzzg)
- fix word 'potgres' to 'postgres' b788e3dce965e76368f8af66b93c6a21abf730a3 (AllenZMC)
- fix word `constrint` to `constraint` 6485fec30979357284ae989f29f223bf08b7034f (AllenZMC)
- fix: upgrade with CRD changes ae52477fbd1c9fd177a638a7954332772463b77f (Yusuke Kuoka)
- Fix subchart values not being deleted by setting value to nil in parent chart's values e53613db3f386b8728ac3d6038b9d13eba9caece (Stefan Deitmer)
- fix golint issues reported by make test 276bb9b1c8ee3c51064f768e8c0e2fb64c3fd5f2 (Tariq Ibrahim)
- Fixes per helpful feedback ce0ad06e941e12e335c5d083c145f830bf7f3083 (Bridget Kromhout)
- Fix broken link in docs/related.md 7247956b96d0f038195af41f1be9b7ce6002c662 (Pete Hodgson)
- Fix documentation to use existing chart in the stable repository 5a39ff90ad25647b75a9e5351dd73ed36fe958e5 (Nenad Merdanovic)
- Fixed failing tests for helm installer 70cd32c4cebac2af67f4da3934e141f0f0c00842 (Oleg Sidorov)
- fix(helm): Delete hooks should wait for resource to be removed from etcd before continuing cb2207c2fbddba7f0cabb626ecb7b02370ca9faa (Morten Torkildsen)
- fix: include glick.lock 3a5e9709ee502ea1ed106feeba51db6365d7d711 (Ace Eldeib)
- Fix nested null value overrides 5b9311d163654c2d3a7ee54742f6497a017a91ee (Adam Eijdenberg)
- (helm): Proper fix for #5046 0239cc4457463cfd6af1f61ec26aa35845dcb1c5 (Marc Khouzam)
- fix(helm): Disable schema validation for manifests ad886c5e36abd2b7cdc1d36b4a48ed638847a981 (Morten Torkildsen)
- fix the short descriptions of all helm commands 8fcc438b67de564a3dd9255ec9c1634229b764c0 (Tariq Ibrahim)
- fix(pkg/storage/driver): use shallowReleaseEqual() ae0d4b151b621a2f12a9b89e75a868349a6fc80f (Matthew Fisher)
- fix(completion): --flag=val breaks zsh completion 3e1ca6fe6e3e2add0518925c5273b650fcb64280 (Marc Khouzam)
- Fix plugin tar extract permissions 796f5eea85e47347709e024daeff5b3c3e7111f0 (Aaron Walker)
- fix(helm): Only validate new manifests 94adb5bbe01c554486630287fe722e9ee0d578f0 (Morten Torkildsen)
- fix(helm): improve error message for content outside base dir 720c28f4c517a72f71b294d35193825cbeeb7e53 (Arash Deshmeh)
- Fix for missing $root fdbbcab3b381c029ff0d586f8deeb5bdf06a2fd0 (Michel Belleau)
- fix(helm): fixed output leak from template command unit tests 9f4a9d206cd12b8ea57a59172dfa80a3b0c69586 (Arash Deshmeh)
- fix(helm): refactor lint unit tests to table-driven 764c3187e9d1e355513a064ffc8e151a1228b27f (Arash Deshmeh)
- fix(helm): allow lint to parse pre-release charts bfc0d76fff148865aa1e9d5ba28693da2947b4fe (Arash Deshmeh)
- fix(pkg/chartutil): conditions for alias and umrella charts (#3734) d80a96cf77ce40283006d3b7bad0ec5400d83acd (Christian Koeberl)
- fix(helm): fix unit tests of the history command to ensure the max option is covered. Add the required support to the fake client ff3dc9dd33f3a31b6bbc3681d2853c03cd57ebdf (Arash Deshmeh)

### 2.15.1

- fix(sympath): walk symbolic links one once cf1de4f8ba70eded310918a8af3a96bfe8e7683b (Matthew Fisher)

### 2.15.2

- Fix error when loading irregular files 8dce272473e5f2a7bf58ce79bb5c3691db54c96b (Matt Farina)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.15.2**, the newest release recorded here for this line.

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
