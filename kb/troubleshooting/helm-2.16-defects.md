---
id: TROUBLE-HELM_2_16_DEFECTS
type: troubleshooting
title: "helm 2.16: defects fixed in the 2.16 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.16.0 <2.17.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 2.16 known issues
  - helm 2.16 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 2.16 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 2.16: defects fixed in the 2.16 line

## Summary

**45 defects** the project fixed across **9 releases** of the 2.16 line, from 2.16.0 to
2.16.12. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.16.0

- Fix url for bsd license 78242d1378cd6275f876639235f055f3e6b050bc (Brice Rising)
- Fix linting issues 42f12563e49da9d79d25616e0dbf48f0b0248304 (Brice Rising)
- Fix style issues 14f051ef50e26a7624b53d4610e693b37b7de275 (Brice Rising)
- Fix rename for helm dep upgrade c41037d9014efee44b0a9a3c79766e920609df19 (Brice Rising)
- Fix error when loading irregular files a4f46d7a38551d8dae01b19ce2d100ed3473c161 (Matt Farina)
- fix(wait): Removes ingress checks 93e4697f4a21f407fee2d27d1c0d0a60f6684aef (Taylor Thomas)
- fix(repo/search): fix helm repo search command to display proper versions 71fa47f576129e2e18092f1a71b989bfaef7f55b (Mateusz Szostok)
- fix silent lint ignore for non existing packaged charts 23926365a0654a0d12cd66022b0b54f67fdd79ef (Karuppiah Natarajan)
- fix(ci): only build Helm 2 off a tag 50b838f9d38696ec1feb5423821c97a5cb770841 (Matthew Fisher)
- fix(sympath): walk symbolic links one once 8489290300515730983eb88cb50fa1e950a9ab79 (Matthew Fisher)
- fix(cmd): acquire file lock on repository.lock 0a2d58457afc08dcdddc07db8bb67d3eaade1959 (Matthew Fisher)
- fix(kube): fix race condition 33bb88851d48bc80bf713a353db275edd5911adb (Matthew Fisher)

### 2.16.1

- fix(kube): Fixes missing API versions bbdfe5e7803a12bbdf97e94cd847859890cf4050 (Taylor Thomas)
- fix(kube): Fixes wait for jobs eec697424c7255a9689fe78c2c8e6d9004a68950 (Taylor Thomas)

### 2.16.4

- fix recursion count in templates 5e135cc465d4231d9bfe2c5a43fd2978ef527e83 (Matthew Fisher)
- fix(engine): allow limited recursion in templates 7ea3d725a32cdaec74ff73447d7175f5594be48a (Matthew Fisher)
- fix(requirements): refactor to use common codepath for table coalescing (#7047) 42941797f394d94800f17ea84566f0a838ec55dc (Fernando Antivero)
- Fix secure installation link in v2 (#6912) 0629eb6dc0aec96a0a044098bf801e37dc1f995a (Yury Fedorov)
- fix(tiller): improve handling of corrupted storage 0c99ca7b9dcb03fcf1d593c4549994a92dbfd1d8 (Cristian Klein)
- fix: backport #6901 to Helm 2 (#7196) 713ed84dcbce0abfe751a41dcf3e78655d6b93cd (Matt Butcher)

### 2.16.6

- Fix nul pointer error dd2e5695da88625b190e6b22e9542550ab503a47 (Matt Farina)
- fix: fixes for Go 1.14 (#7848) 288b521d5eda8a3bde7fef81a462bf7b22d2d873 (Matt Butcher)

### 2.16.7

- Fix issue with sorting pod lists 493cd340091e441ab6a84c3f0be220270c755467 (Matt Farina)
- fix: lint with strict passes for helm create (#7926) 0e32e6417b57ef72fd3bda0001b17db6f27040a8 (Matt Butcher)
- fix: fixes for Go 1.14 (#7848) 5f6269d00852c471b6f951e501d017a7eb2f95d6 (Matt Butcher)
- Fix nul pointer error 88e95b0d7c62ad91e2c910251797e80c4a1cd014 (Matt Farina)
- fix recursion count in templates 9d7b269499f83e19a49e9e5e8121edeae4da26c7 (Matthew Fisher)
- fix(engine): allow limited recursion in templates af3a02140697c7950aac12622ba2800b0277b64a (Matthew Fisher)
- fix(requirements): refactor to use common codepath for table coalescing (#7047) b7d2947d1010a5abf8f986886b3189d6e55b1d36 (Fernando Antivero)
- Fix secure installation link in v2 (#6912) dc2f5bcb33185dbe9691c19a36a7e085c65a83a7 (Yury Fedorov)
- fix(tiller): improve handling of corrupted storage 840e0e271d28584200d7d6304bad6cb5b993beac (Cristian Klein)
- fix: backport #6901 to Helm 2 (#7196) ab797325c6363afae3e238c17a7992a84c9802f4 (Matt Butcher)
- fix(kube): Fixes wait for jobs 77c973422c44bc3e6877400ba22aaa71ebdfa1e4 (Taylor Thomas)
- fix(kube): Fixes missing API versions e2894a18ee1d28341aedd5fc786aff4cc7f2c092 (Taylor Thomas)
- Fix url for bsd license 394ba588b9ecb0c23d86cf007dcf443b9684b1a2 (Brice Rising)
- Fix linting issues 16852f04d92b97de4599b60c2c6a540e950cb97e (Brice Rising)
- Fix style issues 3d15ec7125bff4a43f4da57225c88c086cbdf108 (Brice Rising)
- Fix rename for helm dep upgrade 94d87ef95db922c23ee9fff0a1808482635dcd6a (Brice Rising)

### 2.16.8

- fix(ci): use go 1.14 7606f0879c9eef980e652bd74842c6dcf1ee28a7 (Adam Reese)

### 2.16.10

- The Helm v2 bugfix window is now closed. Security fixes will still be accepted until November 13th, 2020
- fix: removed strict template errors from v2 linter f8d18c868c18e876080102c515d3a47e8198d9f4 (Jeff Knurek)
- fix(tiller): Avoid corrupting storage via a lock 5f66676300a134f467d7dc8cf714947eba04de12 (Cristian Klein)

### 2.16.11

- fix: use yaml annotations for yaml.v2 validation 077ffec4149aed43ba43942841473399afe4d3d1 (Matthew Fisher)
- backported fixes from helm3 6aab63765f99050b115f0aec3d6350c85e8da946 (Matt Butcher)

### 2.16.12

- Fix for issue 8761 47f0b88409e71fd9ca272abc7cd762a56a1c613e (Martin Hickey)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.16.12**, the newest release recorded here for this line.

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
