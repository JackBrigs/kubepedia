---
id: TROUBLE-CERT_MANAGER_1_12_DEFECTS
type: troubleshooting
title: "cert-manager 1.12: defects fixed in the 1.12 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.12.0 <1.13.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cert-manager 1.12 known issues
  - cert-manager 1.12 fixed in
  - is this cert-manager bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cert-manager
sources:
  - type: docs
    path: cert-manager/cert-manager release notes for the 1.12 line — bug-fix entries
    url: https://github.com/cert-manager/cert-manager/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cert-manager 1.12: defects fixed in the 1.12 line

## Summary

**24 defects** the project fixed across **14 releases** of the 1.12 line, from 1.12.0 to
1.12.16. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.12.0

- [`cmctl` API check](https://cert-manager.io/docs/installation/verify/) is broken in v1.12.0 and v1.12.1. We suggest that you do not upgrade `cmctl` to this version. The fix was released in v1.12.2 (which has an additional issue, see below). See #6116 for context
- cainjector contains a memory leak in v1.12.0, v1.12.1 and v1.12.2 due to re-assignment of a log variable (see https://github.com/cert-manager/cert-manager/issues/6217). The fix was released in v1.12.3. See https://github.com/cert-manager/cert-manager/pull/6232 for further context
- Fix development environment and go vendoring on Linux arm64. ([#5810](https://github.com/cert-manager/cert-manager/pull/5810), [@SgtCoDFish](https://github.com/SgtCoDFish))
- Fix ordering of remote git tags when preparing integration tests ([#5910](https://github.com/cert-manager/cert-manager/pull/5910), [@SgtCoDFish](https://github.com/SgtCoDFish))
- The auto-retry mechanism added in VCert 4.23.0 and part of cert-manager 1.11.0 (#5674) has been found to be faulty. Until this issue is fixed upstream, we now use a patched version of VCert. This patch will slowdown the issuance of certificates by 9% in case of heavy load on TPP. We aim to release at an ulterior date a patch release of cert-manager to fix this slowdown. ([#5805](https://github.com/cert-manager/cert-manager/pull/5805), [@inteon](https://github.com/inteon))

### 1.12.1

- [`cmctl` API check](https://cert-manager.io/docs/installation/verify/) is broken in v1.12.0 and v1.12.1. We suggest that you do not upgrade `cmctl` to this version. The fix was released in v1.12.2 (which has an additional issue, see below). See #6116 for context
- cainjector contains a memory leak in v1.12.0, v1.12.1 and v1.12.2 due to re-assignment of a log variable (see https://github.com/cert-manager/cert-manager/issues/6217). The fix was released in v1.12.3. See https://github.com/cert-manager/cert-manager/pull/6232 for further context

### 1.12.2

- cainjector contains a memory leak in v1.12.0, v1.12.1 and v1.12.2 due to re-assignment of a log variable (see https://github.com/cert-manager/cert-manager/issues/6217). The fix was released in v1.12.3. See https://github.com/cert-manager/cert-manager/pull/6232 for further context
- BUGFIX: `cmctl check api --wait 0` exited without output; we now make sure we perform the API check at least once (#6116, @jetstack-bot)

### 1.12.3

- BUGFIX[cainjector]: 1-character bug was causing invalid log messages and a memory leak (#6235, @jetstack-bot)

### 1.12.4

- Fixes an issue where cert-manager would incorrectly reject two IP addresses as being unequal when they should have compared equal. This would be most noticeable when using an IPv6 address which doesn't match how Go's `net.IP.String()` function would have printed that address. (#6297, @SgtCoDFish)
- Use Go 1.20.7 to fix a security issue in Go's `crypto/tls` library. (#6318, @maelvls)

### 1.12.5

- BUGFIX: fix CertificateRequest name collision bug in StableCertificateRequestName feature. (#6359, @jetstack-bot)

### 1.12.6

- The Venafi issuer now properly resets the certificate and should no longer get stuck with `WebSDK CertRequest Module Requested Certificate` or `This certificate cannot be processed while it is in an error state. Fix any errors, and then click Retry.`. (#6401, @maelvls)

### 1.12.8

- If you misconfigure two Certificate resources to have the same target Secret resource, cert-manager will generate a MANY CertificateRequests, possibly causing high CPU usage and/ or high costs due to the large number of certificates issued (see https://github.com/cert-manager/cert-manager/pull/6406). This problem was resolved in v1.13.2 and other later versions, but the fix cannot be easily backported to v1.12.x. We recommend using v1.12.x with caution (avoid misconfigured Certificate resources) or upgrading to a newer version
- Fix CVE 2023 48795 by upgrading to golang.org/x/crypto@v0.17.0 (#6678, @wallrj)
- Fix GHSA-7ww5-4wqc-m92c by upgrading to `github.com/containerd/containerd@v1.7.12` (#6689, @wallrj)

### 1.12.9

- If you misconfigure two Certificate resources to have the same target Secret resource, cert-manager will generate a MANY CertificateRequests, possibly causing high CPU usage and/ or high costs due to the large number of certificates issued (see https://github.com/cert-manager/cert-manager/pull/6406). This problem was resolved in v1.13.2 and other later versions, but the fix cannot be easily backported to v1.12.x. We recommend using v1.12.x with caution (avoid misconfigured Certificate resources) or upgrading to a newer version
- BUGFIX: fix race condition due to registering and using global runtime.Scheme variables (#6833, @inteon)

### 1.12.10

- If you misconfigure two Certificate resources to have the same target Secret resource, cert-manager will generate a MANY CertificateRequests, possibly causing high CPU usage and/ or high costs due to the large number of certificates issued (see https://github.com/cert-manager/cert-manager/pull/6406). This problem was resolved in v1.13.2 and other later versions, but the fix cannot be easily backported to v1.12.x. We recommend using v1.12.x with caution (avoid misconfigured Certificate resources) or upgrading to a newer version

### 1.12.11

- Updated Go to 1.21.11 bringing in security fixes for archive/zip and net/netip. (#7077, @ThatsMrTalbot )

### 1.12.12

- BUGFIX: fix issue that caused Vault issuer to not retry signing when an error was encountered. (#7114, @cert-manager-bot)

### 1.12.14

- Set a maximum size for PEM inputs which cert-manager will accept to remove possibility of taking a long time to process an input (#7403, @SgtCoDFish)

### 1.12.16

- Fix issuing of certificates via DNS01 challenges on Cloudflare after a breaking change to the Cloudflare API (#7568, @SgtCoDFish + @LukeCarrier)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.12.16**, the newest release recorded here for this line.

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
