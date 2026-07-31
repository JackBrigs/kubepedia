---
id: TROUBLE-CERT_MANAGER_1_1_DEFECTS
type: troubleshooting
title: "cert-manager 1.1: defects fixed in the 1.1 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.1.0 <1.2.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cert-manager 1.1 known issues
  - cert-manager 1.1 fixed in
  - is this cert-manager bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cert-manager
sources:
  - type: docs
    path: cert-manager/cert-manager release notes for the 1.1 line — bug-fix entries
    url: https://github.com/cert-manager/cert-manager/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cert-manager 1.1: defects fixed in the 1.1 line

## Summary

**8 defects** the project fixed across **2 releases** of the 1.1 line, from 1.1.0 to
1.1.1. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.1.0

- Fix a panic when changing the max concurrent challenges to a lower value ([#3399](https://github.com/jetstack/cert-manager/pull/3399), [@meyskens](https://github.com/meyskens))
- Fix bug in AWS route53 zone lookup that caused too many IAM requests ([#3354](https://github.com/jetstack/cert-manager/pull/3354), [@supriya-premkumar](https://github.com/supriya-premkumar))
- Fix conversion webhook when given v1beta1 requests ([#3242](https://github.com/jetstack/cert-manager/pull/3242), [@meyskens](https://github.com/meyskens))
- Fix logic in patchDuplicateKeyUsage when signing and digital signature were set ([#3343](https://github.com/jetstack/cert-manager/pull/3343), [@meyskens](https://github.com/meyskens))
- Fix nil pointer error in Cloud DNS when specific config was used. ([#3417](https://github.com/jetstack/cert-manager/pull/3417), [@meyskens](https://github.com/meyskens))
- Fixes incorrect CSR validation when both "signing" and "digital signature" are set ([#3279](https://github.com/jetstack/cert-manager/pull/3279), [@meyskens](https://github.com/meyskens))
- Revert de-duplication of cainjector leader-election to fix scenario where it crashes at startup due to broken webhook. ([#3254](https://github.com/jetstack/cert-manager/pull/3254), [@wallrj](https://github.com/wallrj))

### 1.1.1

- Fix Helm chart type conversion bug ([#3647](https://github.com/jetstack/cert-manager/pull/3647), [@irbekrm](https://github.com/irbekrm))


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.1.1**, the newest release recorded here for this line.

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
