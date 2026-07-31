---
id: TROUBLE-CERT_MANAGER_1_14_DEFECTS
type: troubleshooting
title: "cert-manager 1.14: defects fixed in the 1.14 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.14.0 <1.15.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cert-manager 1.14 known issues
  - cert-manager 1.14 fixed in
  - is this cert-manager bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cert-manager
sources:
  - type: docs
    path: cert-manager/cert-manager release notes for the 1.14 line — bug-fix entries
    url: https://github.com/cert-manager/cert-manager/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cert-manager 1.14: defects fixed in the 1.14 line

## Summary

**18 defects** the project fixed across **6 releases** of the 1.14 line, from 1.14.0 to
1.14.7. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.14.0

- During the release of `v1.14.0`, the Helm chart for this version was found to use the wrong OCI image for the `cainjector` Deployment, which caused the Helm installation to fail. In order to complete the release, the cert-manager team have manually updated the Helm chart for this version, which contains all the Helm chart fixes which are in `v1.14.1`
- New option `.spec.keystores.pkcs12.algorithms` to specify encryption and MAC algorithms for PKCS[#12](https://github.com/cert-manager/cert-manager/pull/12) keystores. Fixes issues [#5957](https://github.com/cert-manager/cert-manager/pull/5957) and [#6523](https://github.com/cert-manager/cert-manager/pull/6523). ([#6548](https://github.com/cert-manager/cert-manager/pull/6548), [@snorwin](https://github.com/snorwin))
- BUGFIX[helm]: Fix issue where webhook feature gates were only set if controller feature gates are set. ([#6380](https://github.com/cert-manager/cert-manager/pull/6380), [@asapekia](https://github.com/asapekia))
- Fix runaway bug caused by multiple Certificate resources that point to the same Secret resource. ([#6406](https://github.com/cert-manager/cert-manager/pull/6406), [@inteon](https://github.com/inteon))
- Fix(helm): templating of required value in controller and webhook ConfigMap resources ([#6435](https://github.com/cert-manager/cert-manager/pull/6435), [@ABWassim](https://github.com/ABWassim))
- Fixed a webhook validation error message when the key algorithm was invalid. ([#6571](https://github.com/cert-manager/cert-manager/pull/6571), [@pevidex](https://github.com/pevidex))
- Fixed error messaging when setting up vault issuer ([#6433](https://github.com/cert-manager/cert-manager/pull/6433), [@vinny](https://github.com/vinny-sabatini))
- The Venafi issuer now properly resets the certificate and should no longer get stuck with `WebSDK CertRequest Module Requested Certificate` or `This certificate cannot be processed while it is in an error state. Fix any errors, and then click Retry.`. ([#6398](https://github.com/cert-manager/cert-manager/pull/6398), [@maelvls](https://github.com/maelvls))
- Fix gosec G601: Implicit memory aliasing of items from a range statement ([#6551](https://github.com/cert-manager/cert-manager/pull/6551), [@wallrj](https://github.com/wallrj))
- Fix handling of serial numbers in literal certificate subjects. Previously a serial number could be specified in `subject.serialNumber` while using a literal certificate subject. This was a mistake and has been fixed. ([#6533](https://github.com/cert-manager/cert-manager/pull/6533), [@inteon](https://github.com/inteon))

### 1.14.1

- Fix broken cainjector image value in Helm chart ([#6693](https://github.com/cert-manager/cert-manager/pull/6693), [@SgtCoDFish](https://github.com/SgtCoDFish))
- Fix bug in cmctl namespace detection which prevented it being used as a startupapicheck image in namespaces other than cert-manager. ([#6706](https://github.com/cert-manager/cert-manager/pull/6706), [@inteon](https://github.com/inteon))
- Fix bug in cmctl which caused `cmctl experimental install` to panic. ([#6706](https://github.com/cert-manager/cert-manager/pull/6706), [@inteon](https://github.com/inteon))

### 1.14.2

- Logging-format json sometimes writes plaintext messages (see https://github.com/cert-manager/cert-manager/issues/6768). FIXED in v1.14.3
- Helm: Fix a bug in the logic that differentiates between 0 and an empty value. (#6729, @jetstack-bot)

### 1.14.3

- BUGFIX: Fixes issue with JSON-logging, where only a subset of the log messages were output as JSON. (#6781, @jetstack-bot)

### 1.14.6

- Updated Go to 1.21.11 bringing in security fixes for archive/zip and net/netip. (#7076, @ThatsMrTalbot)

### 1.14.7

- BUGFIX: fix issue that caused Vault issuer to not retry signing when an error was encountered. (#7113, @cert-manager-bot)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.14.7**, the newest release recorded here for this line.

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
