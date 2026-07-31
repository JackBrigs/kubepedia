---
id: TROUBLE-CERT_MANAGER_1_20_DEFECTS
type: troubleshooting
title: "cert-manager 1.20: defects fixed in the 1.20 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.20.0 <1.21.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cert-manager 1.20 known issues
  - cert-manager 1.20 fixed in
  - is this cert-manager bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cert-manager
sources:
  - type: docs
    path: cert-manager/cert-manager release notes for the 1.20 line — bug-fix entries
    url: https://github.com/cert-manager/cert-manager/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cert-manager 1.20: defects fixed in the 1.20 line

## Summary

**10 defects** the project fixed across **4 releases** of the 1.20 line, from 1.20.0 to
1.20.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.20.0

- Fixed an issue where kind or group in the issuerRef of a Certificate was omitted, upgrading to 1.19.x incorrectly caused the certificate to be renewed (#8160, @inteon)
- Fix an issue where ACME challenge TXT records are not cleaned up when there are many resource records in CloudDNS. (#8456, @tkna)
- Fix unregulated retries with the DigitalOcean DNS-01 solver Add full detailed DNS-01 errors to the events attached to the Challenge, for easier debugging (#8221, @wallrj-cyberark)
- Fixed an infinite re-issuance loop that could occur when an issuer returns a certificate with a public key that doesn't match the CSR. The issuing controller now validates the certificate before storing it and fails with backoff on mismatch. (#8403, @calm329)
- Fixed an issue where HTTP-01 challenges failed when the Host header contains an IPv6 address. This means that users can now issue IP address certificates for IPv6 address subjects. (#8424, @SlashNephy)
- Fixed the HTTP-01 Gateway solver creating invalid HTTPRoutes by not setting spec.hostnames when the challenge DNSName is an IP address. (#8443, @alviss7)
- Security (MODERATE): Fix a potential panic in the cert-manager controller when a DNS response in an unexpected order was cached. If an attacker was able to modify DNS responses (or if they controlled the DNS server) it was possible to cause denial of service for the cert-manager controller. (#8469, @SgtCoDFish)

### 1.20.1

- Fixed duplicate `parentRef` bug when both issuer config and annotations are present. (#8658, @hjoshi123)

### 1.20.2

- Helm: Fix invalid YAML generated when both `webhook.config` and `webhook.volumes` are defined. (#8665, @cert-manager-bot)

### 1.20.3

- Bump go to 1.26.3, other deps to fix several govulncheck issues (#8789, @SgtCoDFish)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.20.3**, the newest release recorded here for this line.

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
