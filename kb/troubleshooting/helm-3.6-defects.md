---
id: TROUBLE-HELM_3_6_DEFECTS
type: troubleshooting
title: "helm 3.6: defects fixed in the 3.6 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.6.0 <3.7.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 3.6 known issues
  - helm 3.6 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 3.6 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 3.6: defects fixed in the 3.6 line

## Summary

**27 defects** the project fixed across **4 releases** of the 3.6 line, from 3.6.0 to
3.6.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.6.0

- 3.6.1 will contain only bug fixes and is planned for release on July 14, 2021
- Fix capabilities changes leaking into other tests 0156ca61ca6999bcfb093d210a4ee597aece0edf (Thomas Dy)
- fix(ci) update ci to use main branch db2aa1a8d633756ec0814cf2f58889d8a767a9a1 (Adam Reese)
- Fix the example for --time-format flag 30f643ce6791b35afeff6b220afeb399cfee54cc (mert)
- fix(cmd): Show that flags can be used for zsh/fish 7b6dcfae98527c3ff7233fc16cbeac782dd82977 (Marc Khouzam)
- fix windows tests 4f1ab5a331d99370ff7bbd1f2004fe80878fbdaf (Christian)
- fix(test): Increase golangci-lint timeout 8d33624520375f5c7d60b15e9ff24a59232f336f (Marc Khouzam)
- fix(helm): get/get-helm-3 whitespace support in runAsRoot 784782013a11c5f1640fb454ec7b9ea0fbf2c389 (Michael Musenbrock)
- fix release sha256 24925c4ca384145706c59da8c5605177c4f0f31a (houfangdong)
- fix(*): Validate metadata semver and printable characters 657ce552cb6e582976c08cccc9605e42c242084e (Adam Reese)
- Fix-9253: Change the deprecated charts repo URL in release notes 64e2d596cf17688d4db1446c62255b07c755db64 (Jack Whitter-Jones)
- Fix `helm list --offset` cli help string f9200231813d1804038a602deb0f979ec60a56b8 (Krish)
- Fix dep build with OCI based charts 1135392b482f26f244c3c69f51511a1d82590eb7 (Matt Farina)
- Fix typo in comment fee2257e3493e9d06ca6caa4be7ef7660842cbdb (Guangwen Feng)
- fix(Makefile): rebuild the binary if go.mod has changed a58209dfa41d291c49dcb42b123b336c782356f3 (Adam Reese)
- fix(pkg/storage): If storage.Create fails to clean up recent release versions, return an error 00cf10d360de3fbe440789ee51662c2894e041ce (Daniel Lipovetsky)

### 3.6.1

- 3.6.2 will contain only bug fixes and is planned for release on July 14, 2021

### 3.6.2

- 3.6.3 will contain only bug fixes and is planned for release on July 14, 2021
- Fix the url being set by WithURL on the getters ee407bdf364942bcb8e8c665f82e15aa28009b71 (Matt Farina)

### 3.6.3

- 3.6.4 will contain only bug fixes and is planned for release on August 11, 2021
- fix(dep update): helm dep update is not respecting the "version" stipulated in the requirements fb31357e6b9f3f048d4d7ed57a00a7d942e86fd8 (cndoit18)
- fix(doc): fix kube client interface doc. (#9882) 29d4e1b9beec93d21f09c614b9ca3e770993ee2f (小龙同学)
- Fix the url being set by WithURL on the getters 473e83e303ca19403eb7cb5f110a001cf7adf632 (Matt Farina)
- fix(sql storage): Query() should return ErrReleaseNotFound immediately when no records are found f2d7ed8d8099dfd94478be40eed1a237bc2d8ef5 (Mike Ng)
- Fixed Test cbd2868ac2f73899dda1df9546d69ccd26230150 (Marcus Speight)
- Fail message is now the same as the required message. Fixed #8973 Helm function 'fail' should not fail when doing 'helm lint' bcee7a30fe97133ef4302354f06261abe1a8b917 (Marcus Speight)
- fix helm dep build/update doesn't inherit --insecure-skip-tls-verify from helm repo add 80402dc078908408fb724395177093f358ee7dae (yxxhero)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.6.3**, the newest release recorded here for this line.

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
