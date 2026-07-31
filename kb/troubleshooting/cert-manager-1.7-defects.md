---
id: TROUBLE-CERT_MANAGER_1_7_DEFECTS
type: troubleshooting
title: "cert-manager 1.7: defects fixed in the 1.7 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.7.0 <1.8.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cert-manager 1.7 known issues
  - cert-manager 1.7 fixed in
  - is this cert-manager bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cert-manager
sources:
  - type: docs
    path: cert-manager/cert-manager release notes for the 1.7 line — bug-fix entries
    url: https://github.com/cert-manager/cert-manager/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cert-manager 1.7: defects fixed in the 1.7 line

## Summary

**9 defects** the project fixed across **3 releases** of the 1.7 line, from 1.7.0 to
1.7.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.7.0

- Fix unexpected exit when multiple DNS providers are passed to `RunWebhookServer` (#4702, @devholic)
- Fixed a bug in the way the Helm chart handles service annotations on the controller and webhook services. (#4329, @jwenz723)
- Fixed a bug that can cause `cmctl version` to erroneously display the wrong webhook pod versions when older failed pods are present. (#4615, @johnwchadwick)
- Fixes a bug where a previous failed CertificateRequest was picked up during the next issuance. Thanks to @MattiasGees for raising the issue and help with debugging! (#4688, @irbekrm)
- Fixes an issue in `cmctl` that prevented displaying the Order resource with cert-manager 1.6 when running `cmctl status certificate`. (#4569, @maelvls)
- The `cmctl experimental install` command now uses the cert-manager namespace. This fixes a bug which was introduced in release 1.6 that caused cert-manager to be installed in the default namespace. (#4763, @wallrj)

### 1.7.1

- Fix: The alpha feature Certificate's `additionalOutputFormats` is now correctly validated at admission time, and no longer _only_ validated if the `privateKey` field of the Certificate is set. The Webhook component now contains a separate feature set. `AdditionalCertificateOutputFormats` feature gate (disabled by default) has been added to the webhook. This gate is required to be enabled on both the controller and webhook components in order to make use of the Certificate's `additionalOutputFormat` feature. (#4816, @JoshVanL)

### 1.7.2

- Bumps the version of Go used to build the cert-manager binaries to 1.17.8, to fix a slew of CVEs (none of which were likely to be exploited) ([#4976 ](https://github.com/cert-manager/cert-manager/pull/4976), @vhosakot)
- Fixes an expired hardcoded certificate which broke unit tests ([#4978](https://github.com/cert-manager/cert-manager/pull/4978), @SgtCoDFish @jakexks)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.7.2**, the newest release recorded here for this line.

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
