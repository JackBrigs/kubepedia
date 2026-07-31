---
id: TROUBLE-HELM_2_7_DEFECTS
type: troubleshooting
title: "helm 2.7: defects fixed in the 2.7 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.7.0 <2.8.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 2.7 known issues
  - helm 2.7 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 2.7 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 2.7: defects fixed in the 2.7 line

## Summary

**14 defects** the project fixed across **3 releases** of the 2.7 line, from 2.7.0 to
2.7.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.7.0

- fix circle not building tags f4f932fabd197f7e6d608c8672b33a483b4b76fa (Matthew Fisher)
- Fix a small typo in `yaml_techniques.md` bbad3c574eb03b8430df8f41921624d0cbc3dcc0 (Edward Medvedev)
- fix(tiller): Adds CRD ordering 29c3b5276f0290d21d43ef45ad0230e45b460b27 (Taylor Thomas)
- fix(semver): fixed edge cases that do not match prerelease b27b11a2806eb5134c92a09796850ec7100b1871 (Matt Farina)
- Fix #2937 - helm always appends /index.yaml at the end of URL (#2988) dad8c6f644b618983c7b6eca8146d736c73d04fd (Michal Cwienczek)
- fix(helm): invoking getterConstructor returns downstream error now a28e5dd2b30caad633834d132a61d754a0479676 (Nandor Kracser)
- fix(sorter): Adds missing unit test 333f8dd35493bff310fe27faf90103f4557ccc64 (Taylor Thomas)
- Avoid panics if test is failing a6872c124ac1c89b740f81200fb4bf9e2c71b34c (Maxim Ivanov)
- fix(deps): fix issues when running glide up b69d6ceca0bca9290efb9d1ca89c50cf337cbb08 (Matt Farina)

### 2.7.1

- fix(helm): update documentation to reflect $HOME env var change db76009b67dade70c65dfa08fb20f295b3671dad (Pietro Menna)
- fix(helm): home env not set on Windows 4f04c1cdb62e1559934fb973bf5951288c70bb92 (Pietro Menna)
- fix(tiller): upgrade last deployed release 0647a7b17a76cb0c89ed6bea1c063344ced098ed (Adam Reese)
- Fix for relative chart path support in index.yaml a97e4dba9470c69ecd4e943d743416e1863addd4 (Christian Jauvin)

### 2.7.2

- fix(helm): fix missing ssl params (#3152) e8e6ac5d7783808cc0bd1adad053bec339849647 (Matt Butcher)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.7.2**, the newest release recorded here for this line.

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
