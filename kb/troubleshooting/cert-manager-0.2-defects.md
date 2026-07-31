---
id: TROUBLE-CERT_MANAGER_0_2_DEFECTS
type: troubleshooting
title: "cert-manager 0.2: defects fixed in the 0.2 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.2.0 <0.3.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cert-manager 0.2 known issues
  - cert-manager 0.2 fixed in
  - is this cert-manager bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cert-manager
sources:
  - type: docs
    path: cert-manager/cert-manager release notes for the 0.2 line — bug-fix entries
    url: https://github.com/cert-manager/cert-manager/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cert-manager 0.2: defects fixed in the 0.2 line

## Summary

**11 defects** the project fixed across **5 releases** of the 0.2 line, from 0.2.0 to
0.2.5. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.2.0

- Fix checking for invalid data in issuer secrets (#170, @munnerz)
- Fix bug in ACME HTTP01 solver causing self-check to return true before paths have propagated (#166, @munnerz)
- Fix panic if the secret named in an ACME issuer exists but contains invalid data (or no data) (#165, @munnerz)
- Fix race condition in ACME HTTP01 solver when validating multiple domains (#155, @munnerz)

### 0.2.1

- Fix bugs when checking validity of certificate resources (#184, @munnerz)
- Fix a bug in checking certificate validity and improve validation of dnsNames and commonName (#183, @munnerz)

### 0.2.2

- Fix a bug that caused ACME certificates to not be automatically renewed (#215, @munnerz)

### 0.2.3

- Fix panic when ACME server returns an error other than HTTP Status Conflict during registration (#237, @munnerz)
- Fix a race condition in the package responsible for scheduling renewals (#218, @munnerz)
- Fix a bug in the ACME authorizer that would cause cert-manager to panic when certificate.spec.acme was not specified (#219, @munnerz)

### 0.2.5

- Fix bug that could cause excessive validation/issuance attempts for failing Certificate resources (#496, @munnerz)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.2.5**, the newest release recorded here for this line.

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
