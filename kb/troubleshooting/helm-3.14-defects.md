---
id: TROUBLE-HELM_3_14_DEFECTS
type: troubleshooting
title: "helm 3.14: defects fixed in the 3.14 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.14.0 <3.15.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 3.14 known issues
  - helm 3.14 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 3.14 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 3.14: defects fixed in the 3.14 line

## Summary

**14 defects** the project fixed across **5 releases** of the 3.14 line, from 3.14.0 to
3.14.4. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.14.0

- 3.14.1 will contain only bug fixes and will be on February 14, 2024
- Fix issues when verify generation readiness was merged c042264a9d1dd5d584684e105aa1ab0e38d96f20 (Matt Farina)
- fix test to use the default code's k8sVersionMinor 6e5332e79b01eb37f902a3569b1e7b80a8d86dd8 (Joe Julian)
- FIX Default ServiceAccount yaml 828763e0d841fbe513f7f28e22d23fd103f97753 (Lars Zimmermann)
- fix(registry): address anonymous pull issue fe4c01f6241a8de566a6fc94cb6d1e5b5eb273d6 (Hidde Beydals)
- fix(registry): unswallow error da3c666a8223376e091e362856ebf0759e16fcd6 (Hidde Beydals)
- Fix missing run statement on release action 21ea847ff25960f6f3a5fdbeb1bf002a5cf8fd95 (Ian Zink)
- fix: pass 'passCredentialsAll' as env-var to getter fa067ec16c576dcf7ea20974baa152dca5121a9c (Mathias Neerup)
- fix post install hook deletion due to before-hook-creation policy fa025fc28be80ff30ef0b2d7475aaee13a8bdaaf (zak905)

### 3.14.1

- 3.14.2 will contain only bug fixes and be released on March 13, 2024

### 3.14.2

- 3.14.3 will contain only bug fixes and be released on March 13, 2024

### 3.14.3

- 3.14.4 will contain only bug fixes and be released on April 10, 2024
- Fix: Ignore alias validation error for index load d6acc0027dca47dec40ccdd66febd0c8bcf4813f (George Jenkins)

### 3.14.4

- fix: reinstall previously uninstalled chart with --keep-history 5a11c768386dab08ff026fb1001e592ab0a033f8 (Alex Petrov)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.14.4**, the newest release recorded here for this line.

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
