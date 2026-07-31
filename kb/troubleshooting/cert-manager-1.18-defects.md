---
id: TROUBLE-CERT_MANAGER_1_18_DEFECTS
type: troubleshooting
title: "cert-manager 1.18: defects fixed in the 1.18 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.18.0 <1.19.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cert-manager 1.18 known issues
  - cert-manager 1.18 fixed in
  - is this cert-manager bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cert-manager
sources:
  - type: docs
    path: cert-manager/cert-manager release notes for the 1.18 line — bug-fix entries
    url: https://github.com/cert-manager/cert-manager/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cert-manager 1.18: defects fixed in the 1.18 line

## Summary

**9 defects** the project fixed across **3 releases** of the 1.18 line, from 1.18.0 to
1.18.5. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.18.0

- Fix AWS Route53 error detection for not-found errors during deletion of DNS records. (#7690, @wallrj)
- Fix behavior when running with `--namespace=<namespace>`: limit the scope of cert-manager to a single namespace and disable cluster-scoped controllers. (#7678, @tsaarni)
- Fix handling of certificates with IP addresses in the `commonName` field; IP addresses are no longer added to the DNS `subjectAlternativeName` list and are instead added to the `ipAddresses` field as expected. (#7081, @johnjcool)
- Fix issuing of certificates via DNS01 challenges on Cloudflare after a breaking change to the Cloudflare API (#7549, @LukeCarrier)
- Fixed the `certmanager_certificate_renewal_timestamp_seconds` metric help text indicating that the metric is relative to expiration time, rather than Unix epoch time. (#7609, @solidDoWant)

### 1.18.1

- ACME: Increased challenge authorization timeout to 2 minutes to fix `error waiting for authorization`. ([`#7801`](https://github.com/cert-manager/cert-manager/pull/7801), @hjoshi123)

### 1.18.5

- Fixed an infinite re-issuance loop that could occur when an issuer returns a certificate with a public key that doesn't match the CSR. The issuing controller now validates the certificate before storing it and fails with backoff on mismatch. (#8414, @cert-manager-bot)
- Fixed an issue where HTTP-01 challenges failed when the Host header contains an IPv6 address. This means that users can now issue IP address certificates for IPv6 address subjects. (#8437, @cert-manager-bot)
- Security (MODERATE): Fix a potential panic in the cert-manager controller when a DNS response in an unexpected order was cached. If an attacker was able to modify DNS responses (or if they controlled the DNS server) it was possible to cause denial of service for the cert-manager controller. (#8467, @SgtCoDFish)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.18.5**, the newest release recorded here for this line.

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
