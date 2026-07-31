---
id: TROUBLE-CERT_MANAGER_0_4_DEFECTS
type: troubleshooting
title: "cert-manager 0.4: defects fixed in the 0.4 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.4.0 <0.5.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cert-manager 0.4 known issues
  - cert-manager 0.4 fixed in
  - is this cert-manager bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cert-manager
sources:
  - type: docs
    path: cert-manager/cert-manager release notes for the 0.4 line — bug-fix entries
    url: https://github.com/cert-manager/cert-manager/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cert-manager 0.4: defects fixed in the 0.4 line

## Summary

**5 defects** the project fixed across **2 releases** of the 0.4 line, from 0.4.0 to
0.4.1. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.4.0

- Fix bugs affecting eTLD and CNAMEs during DNS zone resolution (#582, @ThatWasBrilliant)

### 0.4.1

- Fix issue that could cause Certificates to fail re-issuance if triggered before certificate expiry (#800, @munnerz)
- Fix a race that could cause ACME orders to fail despite them being in a 'valid' state (#764, @munnerz)
- Fixed Route53 cleanup errors for already deleted records. (#746, @euank)
- Fix cleanup of Google Cloud DNS hosted zone for dns-01 challenge records (#754, @kragniz)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.4.1**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `cert-manager/cert-manager`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/cert-manager.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
