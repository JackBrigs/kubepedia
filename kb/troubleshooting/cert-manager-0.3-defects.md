---
id: TROUBLE-CERT_MANAGER_0_3_DEFECTS
type: troubleshooting
title: "cert-manager 0.3: defects fixed in the 0.3 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.3.0 <0.4.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cert-manager 0.3 known issues
  - cert-manager 0.3 fixed in
  - is this cert-manager bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cert-manager
sources:
  - type: docs
    path: cert-manager/cert-manager release notes for the 0.3 line — bug-fix entries
    url: https://github.com/cert-manager/cert-manager/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cert-manager 0.3: defects fixed in the 0.3 line

## Summary

**10 defects** the project fixed across **3 releases** of the 0.3 line, from 0.3.0 to
0.3.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.3.0

- Fix panic when ACME server returns an error other than HTTP Status Conflict during registration (#237, @munnerz)
- Fix a race condition in the package responsible for scheduling renewals (#218, @munnerz)
- Fix a bug that caused ACME certificates to not be automatically renewed (#215, @munnerz)
- Fix a bug in checking certificate validity and improve validation of dnsNames and commonName (#183, @munnerz)
- Fix bugs when checking validity of certificate resources (#184, @munnerz)

### 0.3.1

- Fix a bug that could cause ACME Issuers to re-check Account validation status every few seconds (#662, @munnerz)
- Fix bug that could cause ACME Certificates to not be renewed near renewal time (#674, @munnerz)
- vault: fix panic when vault is sealed or uninitialized (#587, @vdesjardins)

### 0.3.2

- Fix panic when a Certificate specifies a DNS01 provider that is not present on the Issuer resource (#708, @munnerz)
- Fix bug that could cause changes to Ingress resources when using ingress-shim to not be properly propagated to their respective Certificate resources (#686, @kragniz)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.3.2**, the newest release recorded here for this line.

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
