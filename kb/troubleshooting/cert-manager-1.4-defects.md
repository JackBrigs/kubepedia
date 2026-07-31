---
id: TROUBLE-CERT_MANAGER_1_4_DEFECTS
type: troubleshooting
title: "cert-manager 1.4: defects fixed in the 1.4 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.4.0 <1.5.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cert-manager 1.4 known issues
  - cert-manager 1.4 fixed in
  - is this cert-manager bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cert-manager
sources:
  - type: docs
    path: cert-manager/cert-manager release notes for the 1.4 line — bug-fix entries
    url: https://github.com/cert-manager/cert-manager/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cert-manager 1.4: defects fixed in the 1.4 line

## Summary

**10 defects** the project fixed across **4 releases** of the 1.4 line, from 1.4.0 to
1.4.4. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.4.0

- Fix incorrect `PublicKeysEqual` comparison function for public keys and improve doc comments on related functions ([#3914](https://github.com/jetstack/cert-manager/pull/3914), [@SgtCoDFish](https://github.com/SgtCoDFish))
- Fixes a bug where the default cert renewal duration (30d) was clashing with the duration of certs issued by Vault PKI. All Certificates are now renewed 2/3 through the duration unless custom renew period specified by setting spec.renewBefore on the Certificate. ([#4092](https://github.com/jetstack/cert-manager/pull/4092), [@irbekrm](https://github.com/irbekrm))
- Fixes an issue where an ACME `Certificate` with a long name (52 characters or more) does not get renewed due to non-unique `Order` names being generated. ([#3866](https://github.com/jetstack/cert-manager/pull/3866), [@jandersen-plaid](https://github.com/jandersen-plaid))
- Fixes stuck Orders in case of a misbehaving ACME server ([#3805](https://github.com/jetstack/cert-manager/pull/3805), [@irbekrm](https://github.com/irbekrm))
- Panic when failing to register schemes during initialization for pkg/webhook/server Various static analysis fixes across many files including removing unused or redundant code ([#4037](https://github.com/jetstack/cert-manager/pull/4037), [@SgtCoDFish](https://github.com/SgtCoDFish))

### 1.4.1

- Fix check for self-signed certificates in EncodeX509Chain which broke certs whose subject DN matched their issuer's subject DN ([#4238](https://github.com/jetstack/cert-manager/pull/4238), [@SgtCoDFish](https://github.com/SgtCoDFish))

### 1.4.2

- Fix handling of chains which don't have a root in ParseSingleCertificateChain, and improve handling in situations where that function is passed a single certificate. ([#4272](https://github.com/jetstack/cert-manager/pull/4272), [@jetstack-bot](https://github.com/jetstack-bot))
- Fixed a goroutine leak that was causing the controller's memory usage to grow with time ([#4278](https://github.com/jetstack/cert-manager/pull/4278), [@SgtCoDFish](https://github.com/SgtCoDFish))
- Fixed a race condition introduced in v0.15.0 that would crash cert-manager for clusters with a large number of certificates. ([#4275](https://github.com/jetstack/cert-manager/pull/4275), [@jetstack-bot](https://github.com/jetstack-bot))

### 1.4.4

- Fixes renewal time issue for certs with skewed duration period. ([#4403](https://github.com/jetstack/cert-manager/pull/4403), @irbekrm). Thanks to @mfmbarros for help with debugging the issue!


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.4.4**, the newest release recorded here for this line.

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
