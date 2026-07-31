---
id: TROUBLE-CERT_MANAGER_1_19_DEFECTS
type: troubleshooting
title: "cert-manager 1.19: defects fixed in the 1.19 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.19.0 <1.20.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cert-manager 1.19 known issues
  - cert-manager 1.19 fixed in
  - is this cert-manager bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cert-manager
sources:
  - type: docs
    path: cert-manager/cert-manager release notes for the 1.19 line — bug-fix entries
    url: https://github.com/cert-manager/cert-manager/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cert-manager 1.19: defects fixed in the 1.19 line

## Summary

**7 defects** the project fixed across **4 releases** of the 1.19 line, from 1.19.0 to
1.19.6. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.19.0

- ACME: Increased challenge authorization timeout to 2 minutes to fix `error waiting for authorization` (#7796, @hjoshi123)
- Helm: Fix naming template of `tokenrequest` RoleBinding resource to improve consistency (#7761, @lunarwhite)

### 1.19.1

- Bump Go to 1.25.3 to fix a backwards incompatible change to the validation of DNS names in X.509 SAN fields which prevented the use of DNS names with a trailing dot (#8177, @wallrj-cyberark)

### 1.19.3

- Fixed an infinite re-issuance loop that could occur when an issuer returns a certificate with a public key that doesn't match the CSR. The issuing controller now validates the certificate before storing it and fails with backoff on mismatch. (#8415, @cert-manager-bot)
- Fixed an issue where HTTP-01 challenges failed when the Host header contained an IPv6 address. This means that users can now issue IP address certificates for IPv6 address subjects. (#8436, @cert-manager-bot)
- Security (MODERATE): Fix a potential panic in the cert-manager controller when a DNS response in an unexpected order was cached. If an attacker was able to modify DNS responses (or if they controlled the DNS server) it was possible to cause denial of service for the cert-manager controller. (#8468, @SgtCoDFish)

### 1.19.6

- Upgrade Go to 1.25.10 to fix reported vulnerabilities, along with other dependency bumps ([#8788](https://github.com/cert-manager/cert-manager/pull/8788), [@SgtCoDFish](https://github.com/SgtCoDFish))


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.19.6**, the newest release recorded here for this line.

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
