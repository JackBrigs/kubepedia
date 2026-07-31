---
id: TROUBLE-CERT_MANAGER_1_15_DEFECTS
type: troubleshooting
title: "cert-manager 1.15: defects fixed in the 1.15 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.15.0 <1.16.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cert-manager 1.15 known issues
  - cert-manager 1.15 fixed in
  - is this cert-manager bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cert-manager
sources:
  - type: docs
    path: cert-manager/cert-manager release notes for the 1.15 line — bug-fix entries
    url: https://github.com/cert-manager/cert-manager/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cert-manager 1.15: defects fixed in the 1.15 line

## Summary

**12 defects** the project fixed across **3 releases** of the 1.15 line, from 1.15.0 to
1.15.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.15.0

- Add hint to validation error message to help users of external issuers more easily fix the issue if they specify a Kind but forget the Group (#6913, @SgtCoDFish)
- BUGFIX: Fixes issue with JSON-logging, where only a subset of the log messages were output as JSON. (#6779, @inteon)
- Fix backwards incompatible removal of default prometheus Service resource. (#6699, @inteon)
- Fix broken cainjector image value in Helm chart (#6692, @SgtCoDFish)
- Helm: Fix a bug in the logic that differentiates between 0 and an empty value. (#6713, @inteon)
- Fix ACME issuer being stuck waiting for DNS propagation when using Azure DNS with multiple instances issuing for the same FQDN (#6351, @eplightning)
- Fix cainjector ConfigMap not mounted in the cainjector deployment. (#7055, @inteon)

### 1.15.1

- BUGFIX: fix issue that caused Vault issuer to not retry signing when an error was encountered. (#7111, @inteon)

### 1.15.2

- Bump `grpc-go` to fix `GHSA-xr7q-jx4m-x55m` ([#7167](https://github.com/cert-manager/cert-manager/pull/7167), [`@SgtCoDFish`](https://github.com/SgtCoDFish))
- Fix Azure DNS causing panics whenever authentication error happens ([#7188](https://github.com/cert-manager/cert-manager/pull/7188), [`@cert-manager-bot`](https://github.com/cert-manager-bot))
- Fix incorrect value and indentation of `endpointAdditionalProperties` in the `PodMonitor` template of the Helm chart ([#7191](https://github.com/cert-manager/cert-manager/pull/7191), [`@inteon`](https://github.com/inteon))
- Fixes ACME HTTP01 challenge behavior when using Gateway API to prevent unbounded creation of `HTTPRoute` resources ([#7186](https://github.com/cert-manager/cert-manager/pull/7186), [`@cert-manager-bot`](https://github.com/cert-manager-bot))


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.15.2**, the newest release recorded here for this line.

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
