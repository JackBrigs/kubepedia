---
id: TROUBLE-HELM_2_3_DEFECTS
type: troubleshooting
title: "helm 2.3: defects fixed in the 2.3 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.3.0 <2.4.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 2.3 known issues
  - helm 2.3 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 2.3 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 2.3: defects fixed in the 2.3 line

## Summary

**42 defects** the project fixed across **2 releases** of the 2.3 line, from 2.3.0 to
2.3.1. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.3.0

- Patch releases will begin with Helm 2.3.1, focused on bug fixes and documentation changes
- fix (pkg/chartutil): correctly parse input values for ProcessRequirementsEnabled 8c720ee2c2804880491319b74fead9fa187a2bf1 (Justin Scott)
- fix(*): add missing proto for weight hook e4d39fd8c8fd5597611aaf22ead21cce6f538798 (Adam Reese)
- fix(glide.yaml): update SemVer to 1.2.3 8928a10071aa32d3bdbe4f5a9e7e91e7e8a4e035 (Matt Butcher)
- fix(helm): add 'skip-refresh' flag to 'helm init' ba6c55c987aa76b6c6f63cefdacaebbe037106a5 (Matt Butcher)
- fix(hooks): Change annotation from hookWeight to hook-weight b9ef8dbe563e6626c047d1cf91b1367ac7f087c2 (Jonathan Chauncey)
- Correct indention of YAML field in subchartB 75ea56641318bd8f47cce9f1687c69efeb3068f4 (Justin Scott)
- Fix codefences and nits in charts.md. Correct whitespace in charts. Add clarity to description of ImportValues requirements field. 3bf143f05223018eec79ca7ea9d91cf3fa559ec8 (Justin Scott)
- Fix identation of `helm dep` help text 5734c2162e6960b015b23a443421b77b10b817ad (David Wittman)
- Fixes TestInstallRelease_VerifyOptions & TestUpdateRelease_VerifyOptions a484d00e33039d91a42104060d5e59e623e1f9ae (Sushil Kumar)
- fix(helm): local path in requirements.yaml relative to working dir e6b79e138b1ec26c519b805fd9b100fe08128451 (Qin Wang)
- fix(helm): more quotation fixes b208258f5304f8beb748f23e9f43129bb6ea3362 (Anubhav Mishra)
- fix tests 6aeadb272d53872f41b48c4b7aed9e58fafe6c56 (Anubhav Mishra)
- fix(helm): fix comments and removed unwanted split 1cf197d69e824e2747d674b3e4e2e0c6708fbcfa (Anubhav Mishra)
- fix(tiller): now better formatting 73fd0e4557e6557121b573db51b731bc214966ce (Anubhav Mishra)
- fix(helm): using regexp to match whitespaces instead 837da9360edea2d53169b2199202ba7a8a10a298 (Anubhav Mishra)
- fix(tiller): adding kind to tiller client logs c17ce5f9c1bd5d32ccdd0e48f3607ffd41707f1e (Anubhav Mishra)
- fix(helm): manifests string parsing works for newlines in the manifests 611bba0f51770d9b6671183171505e68b801383d (Anubhav Mishra)
- fix(helm): Don't assume index.yaml is sorted f4486d485855f389e8244ea56cc3f0ebd43e1e49 (John Welsh)
- fix(helm): add --destination flag to 'helm package' a2ab1aaa09300186bd9d137e794c9b8a24313ff1 (Louis Taylor)
- fix(ci): disable gosimple 41f727761556c0b37a0794c9317ca9bf60f2f98f (Adam Reese)
- fix(tiller): fix helm status failure on missing resource 27c3ff595a6ec7aad28bba27a37cf782b83528d7 (Matt Butcher)
- fix(tiller): enforce release name length on uninstall d4061b5b608cb328dc62c37e52348d0bdbe8fcd0 (Adam Reese)
- fix(helm): remove max column width for repo list 3a5787335e1b9fab995bb9aad063c875ecde8df2 (Adam Reese)
- fix(tiller): Fixes problem with `--wait` on headless Services 185fb4f43c0f77664430d7946f2a42a7c468b238 (Taylor Thomas)
- Fix link for chart.md file 0499e3101789dd4795d7125fec478623b256190b (Eduardo Baitello)
- fix(docs): Updates hook documentation for `--wait` flag 6a319bd8f5c5bee3c81b0ec036ff5afa9057566a (Taylor Thomas)
- fix(helm): fix bug when helm update can't find release 1. d0c9bae9e92fbd2512d775fbaef8bfa52ef50da5 (Matt Butcher)
- Fix link to charts.md file 6ba9a14db0bff7981c6c23562b6fa33c592268a7 (Eduardo Baitello)
- fix checksum example 65a33d6ff0423d446090462068ae360a352fb338 (Fabian Ruff)
- Fix helm dep list reporting wrong status ee5dab9cb3eced74f5709cda6726794df4e152ae (Qin Wang)
- fix(tiller): Fixes `--wait` panic on upgrade 9afa04b71bfdea012898f0790a381e70bdd0c61b (Taylor Thomas)
- fix(helm): add message if release deleted successfully e0596ec4c3d1254ca7cb659ff39da1a127bb4c87 (Tao Zhou)
- fix(kube): fix wait and recreate 12db1f945f2ab229910b431eec0df235c1801331 (Adam Reese)
- fix(helm): resolve symlinks when loading chart edd4e561124d1d9620f510cf020b8227ff08e85e (Maxim Ivanov)
- fix(local-cluster): fix missing variable option 84e014026cedd5382e08cac9e95f6420874e7065 (Ladicle)
- fix(helm): fix broken cache paths in repositories 4829fad3a39c86f3062ca2cd839b718246b43f79 (Matt Butcher)

### 2.3.1

- fix(tiller): ignore empty YAML documents during delete db8b1f1418665153459c77a3a3d3ef6c47cb01b5 (Matt Butcher)
- fix(helm): fix nil pointer in requirements.go f3f4f0651c5dc5a58e5f8b656408bace3c74e4af (Matt Butcher)
- fix(tiller): increase maximum size of gRPC message ddf4e23280c4fcdbd00738cd8da1355f16b4b6da (Serguei Bezverkhi)
- Fixes hard-coded linux based file-separator 83d15d13a85861b3d3c7a5a8c80e46b38e237f59 (Sushil Kumar)
- fix(helm): remove duplicate commands 33bdcfdce7c3f5e1f8424f2dc7165f39ff03fb38 (Matt Butcher)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.3.1**, the newest release recorded here for this line.

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
