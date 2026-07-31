---
id: TROUBLE-HELM_3_7_DEFECTS
type: troubleshooting
title: "helm 3.7: defects fixed in the 3.7 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.7.0 <3.8.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 3.7 known issues
  - helm 3.7 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 3.7 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 3.7: defects fixed in the 3.7 line

## Summary

**35 defects** the project fixed across **3 releases** of the 3.7 line, from 3.7.0 to
3.7.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.7.0

- fix tarFromLocalDir saving file dependencies in dest path eeac83883cb4014fe60267ec6373570374ce770b (Matthew Fisher)
- Fix HELM_DRIVER docs for sql option bc1fefa9f33f14521c44e08768c9f9bac3681907 (Ed Carrel)
- Fix encoded path for 'helm dependency build' 58018d121098992121071e83b576700cd4f273e1 (Mathieu Parent)
- Fix SIGSEGV when job.Spec.Completions is nil 249d1b5fb98541f5fb89ab11019b6060d6b169f1 (lsowen)
- fix: refactor downloadAll 4b23d0a25b15f990e5de9bc2e1e8cbd80de9243c (Matthew Fisher)
- [fix concern] implement test 2131f4cba830dc2910990b629ba12f40de8edd3c (André Schröder)
- [fix concern] use io.ReadAll instead of ioutil.ReadAll 6515ea84e2c20e844fd015ca8a973953c87285bd (André Schröder)
- fix(engine): parse fail messages with newlines 79df3926f623e040ae50dd6d84a0bbd985c591af (Cory Snider)
- fix HELM PLUGINS behavior another_way 90fa4c962a16ea0d62f0f9b835760e98ecc33630 (yxxhero)
- Resolve PR comments 4bc901c95f3589b6d6b4b3bc0843347334cd0f68 (Stephane Moser)
- fix(typo): fix typo of storage doc 2deb641efd1af421d4afd28f2ae75a4b10b0870f (longkai)
- fix(tests): Remove unnecessary test 6a3daaa7aa5b89a150042cadcbe869b477bb62a1 (Marc Khouzam)
- fix(ci-lint): increase timeout for golangci-lint d1da9e757e140268068d32c051ccd88013138096 (Adam Reese)
- fix(doc): fix kube client interface doc. (#9882) cf0c6fed519d48101cd69ce01a355125215ee46f (小龙同学)
- Fix the url being set by WithURL on the getters 4e2e4084edc0fa1e21d6a9a83b3ffdc8c1ec5e01 (Matt Farina)
- resolve golint errors 8f60ee76a5b78b406d3f9f304e671ce581c1b8d5 (Josh Dolitsky)
- Fix coalesce globals to prevent subchart globals to leak upstream 3b68afc1c820d456e8281a6e6911af59c4b661c8 (Giacomo Margaria)
- fix(dep update): helm dep update is not respecting the "version" stipulated in the requirements 402c7f1a52eb93dbd78710c8afd6291fd8b0c4c7 (cndoit18)
- fix v2 install script, hardcode to v2.17.0 74c41179755120516f0f4f16d8dbe0510f2a6eed (Cameron Motevasselani)
- fix helm dep build/update doesn't inherit --insecure-skip-tls-verify from helm repo add f735a240b6fc483b74e324202dad414ee419225e (yxxhero)
- Fixed Test 7a663a56c24f4dd05375a4ece81e6107eb1b0d78 (Marcus Speight)
- [FIX]error string should not be capitalized 89f2f84a0241422d3c430e2e67c3e4e21fbf4eb8 (Scaat Feng) [FIX]comment should start with whitespace 9020c95fb139944a99632ad5154a4fd5d89032d1 (Scaat Feng)
- [FIX]comment should start with whitespace f1f2e6ff4c4d65d14b1caa809be4257919047049 (Scaat Feng)
- [FIX]comment should start with whitespace 1852694a65a1d64496af06492833b3182032bec6 (Scaat Feng)
- [FIX]error string should not be capitalized 14f6bde04a062da4e5491fdfd9e42263e127534b (Scaat Feng)
- [COMMENT]fix comment 0de89685d428b8af7f1188711f256e7c12703e64 (Scaat Feng)
- [FIX]'rest' collides with imported package name b6bd8d7363cf6ffeb7178526e7284603a6bb4495 (Scaat Feng)
- [FIX]receiver names are different 5c14eec3a39fb2f2cabdd616e9638f15a0946934 (Scaat Feng)
- Fail message is now the same as the required message. Fixed #8973 Helm function 'fail' should not fail when doing 'helm lint' 7a0739a863d36371ed7e57ac5205926c7e574a24 (Marcus Speight)
- fix(sql storage): Query() should return ErrReleaseNotFound immediately when no records are found b86105aebc535541b8a40aefdfc443d434d06106 (Mike Ng)

### 3.7.1

- 3.6.4 will contain only bug fixes and is planned for release on November 10, 2021
- docs: fix typo Charts.yaml 2aacc5f07a67d207f14f28f84c63a7e85dfd4ec7 (Alexey Igrychev)
- Fix default registry config path of oci protocol provider 57ecc256a0225ba396da4aed00b08853bd90b6c9 (Kai Takac)

### 3.7.2

- Fix memory leak in upgrade action 95c03eecdb87feae2ba5d5651225ef6f53d6892a (Jerome Küttner)
- Fix specifying of Kubernetes version from build scripts bb7f8b2b4092f4040247525ab406f62babc174c5 (Matt Farina)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.7.2**, the newest release recorded here for this line.

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
