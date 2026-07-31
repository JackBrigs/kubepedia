---
id: TROUBLE-CERT_MANAGER_0_9_DEFECTS
type: troubleshooting
title: "cert-manager 0.9: defects fixed in the 0.9 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.9.0 <0.10.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cert-manager 0.9 known issues
  - cert-manager 0.9 fixed in
  - is this cert-manager bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cert-manager
sources:
  - type: docs
    path: cert-manager/cert-manager release notes for the 0.9 line — bug-fix entries
    url: https://github.com/cert-manager/cert-manager/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cert-manager 0.9: defects fixed in the 0.9 line

## Summary

**11 defects** the project fixed across **2 releases** of the 0.9 line, from 0.9.0 to
0.9.1. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.9.0

- Fix bug causing ECDSA certificates to be issued using 2048-bit RSA private keys ([#1757](https://github.com/jetstack/cert-manager/pull/1757), [@munnerz](https://github.com/munnerz))
- Fix bug with auto-generated Order names being longer than 63 characters ([#1765](https://github.com/jetstack/cert-manager/pull/1765), [@cheukwing](https://github.com/cheukwing))
- Fix a panic when a misconfigured Issuer is used for HTTP01 challenge solving ([#1758](https://github.com/jetstack/cert-manager/pull/1758), [@munnerz](https://github.com/munnerz))
- Fix a bug where the logic to select a solver would always return the last solver and may return the wrong kind of solver for the challenge that it returned. ([#1717](https://github.com/jetstack/cert-manager/pull/1717), [@dobesv](https://github.com/dobesv))
- Fix indentation on ACME setup examples ([#1785](https://github.com/jetstack/cert-manager/pull/1785), [@lachlancooper](https://github.com/lachlancooper))
- Fix a the logic to select the most specific solver from an issuer if multiple matched ([#1715](https://github.com/jetstack/cert-manager/pull/1715), [@dobesv](https://github.com/dobesv))
- Fix issue causing challenge controller to attempt to list Secrets across all namespaces even when --namespace is specified ([#1849](https://github.com/jetstack/cert-manager/pull/1849), [@munnerz](https://github.com/munnerz))
- Fix issue with private managed-zone being picked in CloudDNS ([#1704](https://github.com/jetstack/cert-manager/pull/1704), [@cheukwing](https://github.com/cheukwing))
- Fix incorrect handling of `issuewild` tag when verifying CAA ([#1777](https://github.com/jetstack/cert-manager/pull/1777), [@cheukwing](https://github.com/cheukwing))

### 0.9.1

- Fix concurrent map write panic in certificates controller ([#1980](https://github.com/jetstack/cert-manager/pull/1980), [@munnerz](https://github.com/munnerz))
- Fix panic when an ACME Order fails ([#1965](https://github.com/jetstack/cert-manager/pull/1965), [@munnerz](https://github.com/munnerz))


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.9.1**, the newest release recorded here for this line.

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
