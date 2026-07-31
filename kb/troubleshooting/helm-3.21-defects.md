---
id: TROUBLE-HELM_3_21_DEFECTS
type: troubleshooting
title: "helm 3.21: defects fixed in the 3.21 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.21.0 <3.22.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 3.21 known issues
  - helm 3.21 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 3.21 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 3.21: defects fixed in the 3.21 line

## Summary

**13 defects** the project fixed across **4 releases** of the 3.21 line, from 3.21.0 to
3.21.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.21.0

- fix: upgrade opentelemetry packages to patch CVEs 13d5fc4ae0e7222e1af8796ff4fa467b52208471 (Terry Howe)
- fix: Chart dot-name path bug 2552884e3bc1b763c3901c5ea7240b59ef6791f1 (George Jenkins)
- fix: pin codeql-action/upload-sarif to commit SHA in scorecards workflow ec05dd5f0481c2de3a41a554adf3c52a6a2a9bb6 (Terry Howe)
- fix pulling charts from OCI indices e629995c5d65ec2d5095ecd6d094bf85d02b3266 (Pedro Tôrres)
- Fix import 97affe067aa1e39fe6552c0d46de749f02063183 (Evans Mungai)
- Fix lint warning d409df87ff6c2cbe17cc465b93ce646003b71d28 (Evans Mungai)
- fix(values): preserve nil values when chart default is empty map b13743c8d4ef5488f40148af1d6ccd35ee9b97e3 (Evans Mungai)

### 3.21.1

- Fixed nil pointer panic that could happen with helm template in ClientOnly flows. Now correctly returns a template error https://github.com/helm/helm/pull/31920
- fix(action): avoid nil REST client getter panic when installing CRDs c56dd0095fd76da5d7b30ecdf506103e7f26745e (sergiochan)
- fix(registry): keep credentials on plain-HTTP fallback with oras-go v2.6.1 702529f90a0021e4d9df4880d6589198ec0e05f7 (Terry Howe)
- fix(deps): bump golang.org/x/net to v0.55.0 to address GO-2026-5026 bad6cd478f5b3f3c96b795f4d6a010f04a89624f (Terry Howe)

### 3.21.2

- fixes b52e27609b4420d206c1874ce9b0c75e271665e7 (Matheus Pimenta)

### 3.21.3

- fix: drop containerd v1 dep to resolve govulncheck CVEs 037733e7d51b08e30a0233bd546c345ab3ea3bba (Benoit Tigeot)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.21.3**, the newest release recorded here for this line.

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
