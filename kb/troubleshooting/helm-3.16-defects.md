---
id: TROUBLE-HELM_3_16_DEFECTS
type: troubleshooting
title: "helm 3.16: defects fixed in the 3.16 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.16.0 <3.17.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 3.16 known issues
  - helm 3.16 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 3.16 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 3.16: defects fixed in the 3.16 line

## Summary

**15 defects** the project fixed across **3 releases** of the 3.16 line, from 3.16.0 to
3.16.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.16.0

- fixed bug to now use burst limit setting for discovery
- Fix linting error for pr 12876 8a26add23ff165b56f012777bbef0059210e9391 (Scott Rigby)
- fix repository-cache flag help description from file to directory 84cbb2c59b6b3c29ed0127608731417d09f53221 (Maor Friedman)
- Fix race condition in TestInstallRelease_Wait_Interrupted test f69a2dd03e7ef7491fa7e770186a8c5ff78c77c6 (Alex Johnson)
- fix: update error handling in Configuration.Init method, add tests for the method 800c33a5aa1e676895e3c288a59f1dd6b6117469 (Suleiman Dibirov)
- fix(helm): Use burst limit setting for discovery 69362df367d6a4a620fde0d7833a805436e23506 (Evan Foster)
- fixed dependency_update_test.go 4d25dd3d8e403496065a130da92787f9fb175f0e (Suleiman Dibirov)
- fix(dependencyBuild): prevent race condition in concurrent helm dependency adeb4ca3d974936349f1980db3ac5599bac8611e (Suleiman Dibirov)
- fix: respect proxy envvars on helm install/upgrade b0603fb042c3299d16e9fdd861d3da5616e44d4a (Sidharth Menon)
- fix docs of DeployedAll 90df4fa4d1b4a98b1fb208b8f5fcec87dd54ccca (Daniel Strobusch)
- fix: wrong cli description bf4d6f290bce58388e38d4ec1b8be5621ed5623c (yyzxw)

### 3.16.2

- Grammar fixes 46e0a0f9e44b56b0d2fc81cc0e624534662b1df7 (Nathan Baulch)
- Fix typos a1bd541d17cd6d120635c1f65ada92edcd224517 (Nathan Baulch)

### 3.16.3

- fix: fix label name cfd07493f46efc9debd9cc1b02a0961186df7fdf (wangjingcun)
- fix(hooks): correct hooks delete order 19fe320ae87e8d1d4bc1952d9da8ea2fe435aa6e (Suleiman Dibirov)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.16.3**, the newest release recorded here for this line.

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
