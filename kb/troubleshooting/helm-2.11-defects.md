---
id: TROUBLE-HELM_2_11_DEFECTS
type: troubleshooting
title: "helm 2.11: defects fixed in the 2.11 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.11.0 <2.12.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 2.11 known issues
  - helm 2.11 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 2.11 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 2.11: defects fixed in the 2.11 line

## Summary

**23 defects** the project fixed across **1 releases** of the 2.11 line, from 2.11.0 to
2.11.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.11.0

- fixed a bug where `helm lint` would fail when a `required` template value was not provided
- fixed an issue where tiller running locally wouldn't respect kubectl's auth provider plugins
- fixed a bug in `helm list` where only the first release in a given chunk from tiller was displayed
- fixed a regression where proxy environment variables were not respected
- fixed a bug where `helm dependency build` and `helm dependency update` did not respect a repository's credentials
- fix(helm): fix regression with TLS flags/environment variables not being parsed (#4657) 2e55dbe1fdb5fdb96b75ff144a339489417b146b (Matthew Fisher)
- Fix credentials not set for ResolveChartVersion default HTTP client (#4662) 19467a536a23c46d0a8d5df9136ebbcf4e43917e (Caleb Delnay)
- fix(helm): fix selector typo in service template for 'helm create' (#4663) 3946629409699a7f90997ee82bb90bb0066a4735 (Qiang Li)
- Fix race condition in `helm list` (#4620) 8d408876a059223c9a29d99efb35b3497a53504c (Matthew Fisher)
- Fix for checking helm version slice bounds out of range (#4609) 67b142ab0daeec1c3cd34b5813b9982c1afdf37d (Robert James Hernandez)
- Fix grammer for tests (#4599) c539454c9cddaa50f1de184062e172cea4932aa8 (Ian Chen)
- fix(release_server): handle the case when requested values is empty (#4604) 941b1f4d68b6cf3d299df880152d90227e1a441e (Matthew Fisher)
- Avoid importing k8s.io/kubernetes from pkg/helm (#4499) 37a731db798de00bf94837e207a8a418c76b6557 (Fabian Ruff)
- Set proxy for all connections, fixes #4326 (#4579) 2e9855b98ba0a04a4aa1576f3ed769b0dbd15c42 (Christian Köberl)
- fix(helm): Add --tiller-tls-hostname flag to 'helm init' 1b34a511d4ae38e43518e99a8250330515e3a93c (aswinkarthik)
- Fix typo in message.go 0b4e086e0572ae405a65af0a61c2dbe5a4ced2e5 (Jon Huhn)
- Fix helm create note for k8 label convention changes 7306b4c28eadcd06a9f090546d6edec8a0067ac0 (Martin Hickey)
- Fix typo in parser.go d92939119993174ae264dfec06db7cb1b07e37c9 (Jon Huhn)
- fix: link to custom resource definitions section f15d65845019f549679d06e18db9ec7ce7686922 (Alexey Volkov)
- fix(client): fix bug in list releases to append all releases 38eb73760b44f25b517f6f2f3c48cbb7dc047bb8 (Matt Tucker)
- fix(helm): fix(helm): add `--tls-hostname` flag to tls flags bd0686731c4d0bcf2bf1282f915bb20da3770c21 (fibonacci1729)
- fix(release_server): fix how we merge values 3e0de0dae9be9dd42386ab7e5a73abd9cc831204 (Michelle Noorali)
- Fixed error in docs for file access 1b955e63f7862c95c3e5033d67f2b2b6e2a11759 (Michael Huttner)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.11.0**, the newest release recorded here for this line.

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
