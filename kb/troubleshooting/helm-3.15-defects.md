---
id: TROUBLE-HELM_3_15_DEFECTS
type: troubleshooting
title: "helm 3.15: defects fixed in the 3.15 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.15.0 <3.16.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 3.15 known issues
  - helm 3.15 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 3.15 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 3.15: defects fixed in the 3.15 line

## Summary

**15 defects** the project fixed across **3 releases** of the 3.15 line, from 3.15.0 to
3.15.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.15.0

- Fix namespace on kubeconfig error 214fb6eff393f1c17890d45e9eaee86f6b37ea17 (Calvin Krist)
- Update testdata PKI with keys that have validity until 3393 (Fixes #12880) 1b75d48189c2484cb5904f7996933d8d85315adb (Dirk Müller)
- Some fixes 764557c470533fa57aad99f865c9ff75a64d4163 (Matt Farina)
- Fix: Ignore alias validation error for index load 68294fdae0deba2464805067228790e025207ebd (George Jenkins)
- validation fix 8e6a5149d2e2e3beffa51d53048b2fed90d8c529 (Matt Farina)
- Fix grammatical error c25736c894ed1058c75b68fca0094c8fd953e131 (Matt Carr)
- fix: reinstall previously uninstalled chart with --keep-history 9e198fa89d3c798dec1012bb4dff7107e22700d7 (Alex Petrov)

### 3.15.2

- 3.15.3 will contain only bug fixes and be released on July 10, 2024
- fix: wrong cli description 1a500d5625419a524fdae4b33de351cc4f58ec35 (yyzxw)
- fix docs of DeployedAll b3640f196a2cf77136ab01295bffe76fa184991d (Daniel Strobusch)

### 3.15.3

- 3.15.4 will contain only bug fixes and be released on August 14, 2024
- fix(helm): Use burst limit setting for discovery 3bb50bbbdd9c946ba9989fbe4fb4104766302a64 (Evan Foster)
- fixed dependency_update_test.go f440d3b19ed772502b85ade33f7ee6bf4a35c85c (Suleiman Dibirov)
- fix(dependencyBuild): prevent race condition in concurrent helm dependency f262d80d30bd7c13f2ffe9719d23035adcbc7ede (Suleiman Dibirov)
- fix: respect proxy envvars on helm install/upgrade 7413819bb9c481707efa58b111ff0b85829b79f9 (Sidharth Menon)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.15.3**, the newest release recorded here for this line.

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
