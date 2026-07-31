---
id: TROUBLE-ARGO_CD_2_4_DEFECTS
type: troubleshooting
title: "argo-cd 2.4: defects fixed in the 2.4 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.4.0 <2.5.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - argo-cd 2.4 known issues
  - argo-cd 2.4 fixed in
  - is this argo-cd bug already fixed
tags:
  - troubleshooting
  - upgrade
  - argo-cd
sources:
  - type: docs
    path: argoproj/argo-cd release notes for the 2.4 line — bug-fix entries
    url: https://github.com/argoproj/argo-cd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# argo-cd 2.4: defects fixed in the 2.4 line

## Summary

**26 defects** the project fixed across **6 releases** of the 2.4 line, from 2.4.2 to
2.4.8. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.4.2

- fix: updated baseHRefRegex to perform lazy match (#9724)
- fix: updated config file permission requirements for windows (#9666)

### 2.4.3

- fix: respect OIDC providers' supported token signing algorithms (#9433) (#9761)
- fix websockets for terminal not working on subPath (#9795)
- fix: avoid closing and re-opening port of api server settings change (#9778)
- fix: [ArgoCD] Fixing webhook typo in case of error in GetManifests (#9671)
- fix: overrides should not appear in the manifest cache key (#9601)

### 2.4.4

- fix: missing path segments for git file generator (#9839)
- fix: make sure api server informer does not stop after setting change (#9842)
- fix: configurable CMP tar exclusions (#9675) (#9789)
- fix: prune any deleted refs before fetching (#9504)

### 2.4.5

- fix: webhook typo in case of error in GetManifests (#9671)

### 2.4.6

- fix: 'unexpected reserved bits' breaking web terminal (#9605) (#9895)
- fix: argocd login just hangs on 2.4.0 #9679 (#9935)
- fix: CMP manifest generation fails with ENHANCE_YOUR_CALM if over 40s (#9922)
- fix: NotAfter is not set when ValidFor is set (#9911)
- fix: add missing download CLI tool link for ppc64le, s390x (#9649)
- fix: Check tracking annotation for being self-referencing (#9791)
- fix: Make change of tracking method work at runtime (#9820)
- fix: argo-cd git submodule is using SSH auth instead of HTTPs (#3118) (#9821)

### 2.4.8

- feat: support application level extensions (#9923)
- feat: support multiple extensions per resource group/kind (#9834)
- fix: extensions is not loading for ConfigMap/Pods (#10010)
- fix: upgrade moment from 2.29.2 to 2.29.3 (#9330)
- fix: skip redirect url validation when it's the base href (#10058) (#10116)
- fix: Set HOST_ARCH for yarn build from platform (#10018)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.4.8**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `argoproj/argo-cd`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/argo-cd.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
