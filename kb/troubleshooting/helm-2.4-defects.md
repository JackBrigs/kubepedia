---
id: TROUBLE-HELM_2_4_DEFECTS
type: troubleshooting
title: "helm 2.4: defects fixed in the 2.4 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.4.0 <2.5.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 2.4 known issues
  - helm 2.4 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 2.4 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 2.4: defects fixed in the 2.4 line

## Summary

**23 defects** the project fixed across **3 releases** of the 2.4 line, from 2.4.0 to
2.4.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.4.0

- fix(releaseutil): remove newline on SplitManifests dcfbb2bd35b90cac6a25fa2a9bbd59150ff70abf (Michelle Noorali)
- fix(create): incorrect URL in default NOTES.txt f8b2c5eb571e46d99b88dab8498408b35f892f11 (Adnan Abdulhussein)
- fix(tiller): make new version check backwards compatible 9ae84c730f6b1b3e77f013138c1b6420a585c494 (Adam Reese)
- fix(*): handle unreleased versioning 2e819e014d78b83c15252571f7bcac75cd226ab7 (Adam Reese)
- fix(tiller): fix TOML panic 46035c35c418a18df7c62686196ac7d3ef54ac2f (Matt Butcher)
- fix(helm): fix style issues 3c55a0ee65804293c9f20d48108d5f4f273a35ba (Matt Butcher)
- fix(helm): return error when dependencies are missing 6246fa12a807e5c6ceb863f38dd6afa05ffc14fb (Matt Butcher)
- fix(tiller): update tls client auth policy d7240ff9430e31fa950e27fe5aa7a60edc3d99bf (fibonacci1729)
- Fix indent for defaultDeployment ce505f16e6671417135c23ebc9d28916ce8cea6c (Matthias Thubauville)
- fix(tiller): ignore empty YAML documents during delete 573a8a190c85e6bea538f4a739e16d5634c128b2 (Matt Butcher)
- fix(scripts): don't include plugins for generating docs 6bcd19d5191b223612b1cda5b73dab2fab66b978 (Adam Reese)
- fix(helm): fix nil pointer in requirements.go 19b111b1238d6aa770cb371dbf8b99492ae38d99 (Matt Butcher)
- fix(tiller): increase maximum size of gRPC message 26343023a3cff4ef4a484e9a04b80ed0fc6190c1 (Serguei Bezverkhi)
- fix(helm): correct import for apps api 7a141a10b3972a0761aab7b47d4d159bf7b59df0 (Adam Reese)
- fix(init): use ImagePullPolicy Always for canary installs 264ad3271ed01697c359bdfd1506c8cacf35721c (Adam Reese)
- Fixes hard-coded linux based file-separator 84fc5b776f6aadc5bcaecfdbf5e521dee4d45d72 (Sushil Kumar)
- fix(helm): remove duplicate commands 1a79c28f45f64967be118d0d684008dd7e493835 (Matt Butcher)

### 2.4.1

- fix(helm): reverted upgrade of imdario/mergo 201169a860ff5c560312596b55733bb7c1447ba7 (Rod Cloutier)

### 2.4.2

- fix(helm): add --devel flag to allow dev releases again 0b4c60b7d4ddf5ed75997efdbe974446554e2f0b (Matt Butcher)
- fix(lint): add KubeVersion and TillerVersion to linter 504f0f4d0a8786a9125ebd034a33469b428bc2c9 (Matt Butcher)
- fix(*): return non-zero exit code on test failure ddfd9a05aa91d38291fb18388f2a965404e46fcf (Michelle Noorali)
- Fixes messages for plugin remove option 61d01766985b7bc58649eb9b0f4f955524fa282c (Sushil Kumar)
- fix(tiller): Fixes bug with `--wait` and updated deployments 79c492b6aba9f018608d635530f00a17bf3539b8 (Taylor Thomas)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.4.2**, the newest release recorded here for this line.

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
