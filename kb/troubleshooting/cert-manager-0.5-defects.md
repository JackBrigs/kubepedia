---
id: TROUBLE-CERT_MANAGER_0_5_DEFECTS
type: troubleshooting
title: "cert-manager 0.5: defects fixed in the 0.5 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.5.0 <0.6.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cert-manager 0.5 known issues
  - cert-manager 0.5 fixed in
  - is this cert-manager bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cert-manager
sources:
  - type: docs
    path: cert-manager/cert-manager release notes for the 0.5 line — bug-fix entries
    url: https://github.com/cert-manager/cert-manager/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cert-manager 0.5: defects fixed in the 0.5 line

## Summary

**9 defects** the project fixed across **3 releases** of the 0.5 line, from 0.5.0 to
0.5.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.5.0

- Fix issue that could cause Certificates to fail renewal (#800, @munnerz)
- [jjo] fix panic from acmedns.go constructor failure (#858, @jjo)
- Fix cloudflare provider failing on cleanup if no record is found (#849, @frankh)
- Fixed Route53 cleanup errors for already deleted records. (#746, @euank)
- Fix a race that could cause ACME orders to fail despite them being in a 'valid' state (#764, @munnerz)
- Fix cleanup of Google Cloud DNS hosted zone for dns-01 challenge records (#754, @kragniz)
- Fix issue causing existing Ingresses to not be cleaned up properly after HTTP01 challenges in some cases (#831, @munnerz)

### 0.5.1

- Fix concurrent map write race condition in ACME solver (#1033, @munnerz)

### 0.5.2

- Fix bug when cleaning up ingress resources after performing ACME HTTP01 validation (#1082, @munnerz)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.5.2**, the newest release recorded here for this line.

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
