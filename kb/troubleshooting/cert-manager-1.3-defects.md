---
id: TROUBLE-CERT_MANAGER_1_3_DEFECTS
type: troubleshooting
title: "cert-manager 1.3: defects fixed in the 1.3 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.3.0 <1.4.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cert-manager 1.3 known issues
  - cert-manager 1.3 fixed in
  - is this cert-manager bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cert-manager
sources:
  - type: docs
    path: cert-manager/cert-manager release notes for the 1.3 line — bug-fix entries
    url: https://github.com/cert-manager/cert-manager/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cert-manager 1.3: defects fixed in the 1.3 line

## Summary

**9 defects** the project fixed across **3 releases** of the 1.3 line, from 1.3.0 to
1.3.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.3.0

- Correct permissions on edit aggregate role ([#3697](https://github.com/jetstack/cert-manager/pull/3697), [@yann-soubeyrand](https://github.com/yann-soubeyrand))
- Fix a bug that prevented the immediate re-issuance of a failing certificate: even when the user edited the certificate to fix an incorrect field, no certificate request would get created. Editing a failed certificate now properly re-issues immediately. ([#3444](https://github.com/jetstack/cert-manager/pull/3444), [@maelvls](https://github.com/maelvls))
- Fixed approle login when namespaces were used in HashiCorp Vault Fixed incorrectly failing health check that was caused when the Vault token did not have sufficient permission to call /sys/- endpoints ([#3582](https://github.com/jetstack/cert-manager/pull/3582), [@lalitadithya](https://github.com/lalitadithya))
- Fixes Helm upgrade bug ([#3647](https://github.com/jetstack/cert-manager/pull/3647), [@irbekrm](https://github.com/irbekrm))
- Fixes multiple Certificate Requests issue - see #3603 ([#3665](https://github.com/jetstack/cert-manager/pull/3665), [@irbekrm](https://github.com/irbekrm))

### 1.3.1

- Fixes an upgrade issue with Helm. People upgrading from cert-manager v1.2 should now be able to upgrade with no error. ([#3886](https://github.com/jetstack/cert-manager/pull/3886), [@irbekrm](https://github.com/irbekrm))
- Fixes a regression that was introduced in v1.3. Before v1.3, a CertificateRequest that would fail would have the condition `Ready=False` added to it. After v1.3, the `Ready=False` was not set anymore due to the addition of the [Approval API](https://cert-manager.io/docs/concepts/certificaterequest/#approval). ([#3892](https://github.com/jetstack/cert-manager/pull/3892), [@JoshVanL](https://github.com/JoshVanL))

### 1.3.2

- Fixed a goroutine leak that was causing the controller's memory usage to grow with time ([#4279](https://github.com/jetstack/cert-manager/pull/4279), [@SgtCoDFish](https://github.com/SgtCoDFish))
- Fixed a race condition introduced in v0.15.0 that would crash cert-manager for clusters with a large number of certificates. ([#4280](https://github.com/jetstack/cert-manager/pull/4280), [@jetstack-bot](https://github.com/jetstack-bot))


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.3.2**, the newest release recorded here for this line.

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
