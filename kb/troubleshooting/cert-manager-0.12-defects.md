---
id: TROUBLE-CERT_MANAGER_0_12_DEFECTS
type: troubleshooting
title: "cert-manager 0.12: defects fixed in the 0.12 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.12.0 <0.13.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cert-manager 0.12 known issues
  - cert-manager 0.12 fixed in
  - is this cert-manager bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cert-manager
sources:
  - type: docs
    path: cert-manager/cert-manager release notes for the 0.12 line — bug-fix entries
    url: https://github.com/cert-manager/cert-manager/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cert-manager 0.12: defects fixed in the 0.12 line

## Summary

**8 defects** the project fixed across **1 releases** of the 0.12 line, from 0.12.0 to
0.12.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.12.0

- Fixes issues with Pod Security Policies that prevented pods from running when Pod Security Policy is enabled in Kubernetes ([#2234](https://github.com/jetstack/cert-manager/pull/2234), [@sam-cogan](https://github.com/sam-cogan))
- Fix issue causing certificates not to be issued when running with `OwnerReferencesPermissionEnforcement` admission controller enabled ([#2325](https://github.com/jetstack/cert-manager/pull/2325), [@CoaxVex](https://github.com/CoaxVex))
- Fix bug causing SIGTERM and SIGINT signals to not be respected whilst the controller is performing leader election ([#2236](https://github.com/jetstack/cert-manager/pull/2236), [@munnerz](https://github.com/munnerz))
- Fix setting ownerReference on Challenge resources created by Orders controller ([#2324](https://github.com/jetstack/cert-manager/pull/2324), [@CoaxVex](https://github.com/CoaxVex))
- Allow clouddns resolvers to be validated correctly without `serviceAccountSecretRef` to allow ambient permissions to be used. ([#2250](https://github.com/jetstack/cert-manager/pull/2250), [@baelish](https://github.com/baelish))
- Add missing apiVersion to Chart.yaml ([#2270](https://github.com/jetstack/cert-manager/pull/2270), [@yurrriq](https://github.com/yurrriq))
- Perform API resource validation of the 'status' subresource on cert-manager resources ([#2283](https://github.com/jetstack/cert-manager/pull/2283), [@munnerz](https://github.com/munnerz))
- Fix outdated documentation for solver configuration in Issuers and ClusterIssuers ([#2210](https://github.com/jetstack/cert-manager/pull/2210), [@nickbp](https://github.com/nickbp))


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.12.0**, the newest release recorded here for this line.

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
