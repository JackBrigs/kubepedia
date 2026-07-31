---
id: TROUBLE-CERT_MANAGER_1_0_DEFECTS
type: troubleshooting
title: "cert-manager 1.0: defects fixed in the 1.0 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.0.0 <1.1.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cert-manager 1.0 known issues
  - cert-manager 1.0 fixed in
  - is this cert-manager bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cert-manager
sources:
  - type: docs
    path: cert-manager/cert-manager release notes for the 1.0 line — bug-fix entries
    url: https://github.com/cert-manager/cert-manager/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cert-manager 1.0: defects fixed in the 1.0 line

## Summary

**12 defects** the project fixed across **5 releases** of the 1.0 line, from 1.0.0 to
1.0.4. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.0.0

- Fix bug of status certificate command where the matching CR gets overwritten ([#3117](https://github.com/jetstack/cert-manager/pull/3117), [@hzhou97](https://github.com/hzhou97))
- Fixes generation of ACME resources if the the 52nd character in a CR name is a symbol. ([#3232](https://github.com/jetstack/cert-manager/pull/3232), [@meyskens](https://github.com/meyskens))

### 1.0.1

- Fix conversion webhook when given v1beta1 requests ([#3243](https://github.com/jetstack/cert-manager/pull/3243), [@meyskens](https://github.com/meyskens), [@wallrj](https://github.com/wallrj))
- Revert de-duplication of cainjector leader-election to fix scenario where it crashes at startup due to broken webhook. ([#3255](https://github.com/jetstack/cert-manager/pull/3255), [@wallrj](https://github.com/wallrj))

### 1.0.2

- Fixes incorrect CSR validation when both "signing" and "digital signature" are set ([#3306](https://github.com/jetstack/cert-manager/pull/3306), @meyskens)

### 1.0.3

- Fix logic in patchDuplicateKeyUsage when signing and digital signature were set ([#3352](https://github.com/jetstack/cert-manager/pull/3352), [@meyskens](https://github.com/meyskens))
- Fixes incorrect CSR validation when both "signing" and "digital signature" are set ([#3306](https://github.com/jetstack/cert-manager/pull/3306), [@meyskens](https://github.com/meyskens))

### 1.0.4

- Fix a bug where the Venafi Issuer and ClusterIssuer did not set the Ready condition and message if there was an API connection or API authentication failure. The Ready condition will now always be set, including details of any errors during setup. ([#3389](https://github.com/jetstack/cert-manager/pull/3389), [@wallrj](https://github.com/wallrj))
- Fix a panic when changing the max concurrent challenges to a lower value ([#3418](https://github.com/jetstack/cert-manager/pull/3418), [@meyskens](https://github.com/meyskens))
- Fix bug in AWS route53 zone lookup that caused too many IAM requests ([#3375](https://github.com/jetstack/cert-manager/pull/3375), [@supriya-premkumar](https://github.com/supriya-premkumar))
- Fix logic in patchDuplicateKeyUsage when signing and digital signature were set ([#3352](https://github.com/jetstack/cert-manager/pull/3352), [@meyskens](https://github.com/meyskens))
- Fix nil pointer error in Cloud DNS when specific config was used. ([#3420](https://github.com/jetstack/cert-manager/pull/3420), [@meyskens](https://github.com/meyskens))


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.0.4**, the newest release recorded here for this line.

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
