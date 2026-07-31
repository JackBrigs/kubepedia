---
id: TROUBLE-LOCAL_PATH_PROVISIONER_0_0_DEFECTS
type: troubleshooting
title: "local-path-provisioner 0.0: defects fixed in the 0.0 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.0.0 <0.1.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - local-path-provisioner 0.0 known issues
  - local-path-provisioner 0.0 fixed in
  - is this local-path-provisioner bug already fixed
tags:
  - troubleshooting
  - upgrade
  - local-path-provisioner
sources:
  - type: docs
    path: rancher/local-path-provisioner release notes for the 0.0 line — bug-fix entries
    url: https://github.com/rancher/local-path-provisioner/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# local-path-provisioner 0.0: defects fixed in the 0.0 line

## Summary

**30 defects** the project fixed across **11 releases** of the 0.0 line, from 0.0.22 to
0.0.36. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.0.22

- Fix a typo on README.md(https://github.com/rancher/local-path-provisioner/pull/226)
- Correct directory naming for helm chart (https://github.com/rancher/local-path-provisioner/pull/231)

### 0.0.23

- FIX: imagePullSecrets setting error @tgfree7 (1804059)
- Fix depreciated kubectl instruction in README @kate-goldenring (4768915)

### 0.0.24

- Fix sharedFilesystemPath not being available in helm deployment by @meln5674 in https://github.com/rancher/local-path-provisioner/pull/275
- fix quota example by @liupeng0518 in https://github.com/rancher/local-path-provisioner/pull/278

### 0.0.26

- [Fix helper Pod that always runs in privileged mode](https://github.com/rancher/local-path-provisioner/pull/370)
- [Fix CVEs issues by updating go version and packages](https://github.com/rancher/local-path-provisioner/pull/369)

### 0.0.27

- Fix duplicate labels by @runningman84 in https://github.com/rancher/local-path-provisioner/pull/393
- Fix: Chart.yaml file is missing on helm install by @jamshidi799 in https://github.com/rancher/local-path-provisioner/pull/388
- chart: fix pathPattern by @derekbit in https://github.com/rancher/local-path-provisioner/pull/409

### 0.0.28

- fix(ci): allow to read docker hub secret by @mantissahz in https://github.com/rancher/local-path-provisioner/pull/412

### 0.0.31

- Update dependencies by @harsimranmaan in https://github.com/rancher/local-path-provisioner/pull/472 Fix CVE issues

### 0.0.32

- fix: helm install command by @antonengelhardt in https://github.com/rancher/local-path-provisioner/pull/468
- fix: multiple paths is not true random (fix #342) by @tulequ in https://github.com/rancher/local-path-provisioner/pull/496
- fix: do not override nodeName, if exists by @BohdanTkachenko in https://github.com/rancher/local-path-provisioner/pull/499
- Fix helper pod tolerations by @sbocinec in https://github.com/rancher/local-path-provisioner/pull/486
- fix: rename workflows by @derekbit in https://github.com/rancher/local-path-provisioner/pull/512
- fix: fix chart tag by @derekbit in https://github.com/rancher/local-path-provisioner/pull/514
- fix: fix Invalid Semantic Version by @derekbit in https://github.com/rancher/local-path-provisioner/pull/515

### 0.0.33

- fix: don't try to clean up pvs on nodes that are gone by @marcusramberg in https://github.com/rancher/local-path-provisioner/pull/480
- fix(chart): correct ServiceAccount namespace in ClusterRoleBinding by @J3m3 in https://github.com/rancher/local-path-provisioner/pull/528
- fix: give clusterrole update on pvc by @marcusramberg in https://github.com/rancher/local-path-provisioner/pull/530
- fix: prohibit the reference path in pathPattern by @mantissahz in https://github.com/rancher/local-path-provisioner/pull/542
- fix: podDisruptionBudget renders correctly in all cases by @jcpunk in https://github.com/rancher/local-path-provisioner/pull/540

### 0.0.34

- fix: mitigate the impact of enforcing a pathPattern prefix by @mantissahz in https://github.com/rancher/local-path-provisioner/pull/547
- fix: read allowUnsafePathPattern from storageclass annotations by @derekbit in https://github.com/rancher/local-path-provisioner/pull/548

### 0.0.36

- fix: qualify image references to avoid short-name resolution and Docker Hub rate limits by @bejaratommy in https://github.com/rancher/local-path-provisioner/pull/573
- fix: add helper pod template validation by @derekbit in https://github.com/rancher/local-path-provisioner/pull/576
- fix: relax helper pod template validation by @derekbit in https://github.com/rancher/local-path-provisioner/pull/577


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.0.36**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `rancher/local-path-provisioner`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/local-path-provisioner.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
