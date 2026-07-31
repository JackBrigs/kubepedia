---
id: TROUBLE-CERT_MANAGER_1_6_DEFECTS
type: troubleshooting
title: "cert-manager 1.6: defects fixed in the 1.6 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.6.0 <1.7.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cert-manager 1.6 known issues
  - cert-manager 1.6 fixed in
  - is this cert-manager bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cert-manager
sources:
  - type: docs
    path: cert-manager/cert-manager release notes for the 1.6 line — bug-fix entries
    url: https://github.com/cert-manager/cert-manager/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cert-manager 1.6: defects fixed in the 1.6 line

## Summary

**10 defects** the project fixed across **4 releases** of the 1.6 line, from 1.6.0 to
1.6.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.6.0

- FIX: Prevent Vault Client from panicing when request to Vault health endpoint fails. ([#4456](https://github.com/jetstack/cert-manager/pull/4456), [@JoshVanL](https://github.com/JoshVanL))
- Fix CRDs which were accidentally changed in cert-manager v1.5.0 ([#4353](https://github.com/jetstack/cert-manager/pull/4353), [@SgtCoDFish](https://github.com/SgtCoDFish))
- Fix regression in Ingress PathType introduced in v1.5.0 ([#4373](https://github.com/jetstack/cert-manager/pull/4373), [@jakexks](https://github.com/jakexks))
- Fixed the HTTP-01 solver creating ClusterIP instead of NodePort services by default. ([#4393](https://github.com/jetstack/cert-manager/pull/4393), [@jakexks](https://github.com/jakexks))
- Fixes renewal time issue for certs with skewed duration period. ([#4399](https://github.com/jetstack/cert-manager/pull/4399), [@irbekrm](https://github.com/irbekrm))
- Fix manually specified PKCS#10 CSR and X.509 Certificate version numbers (although these were ignored in practice) ([#4392](https://github.com/jetstack/cert-manager/pull/4392), [@SgtCoDFish](https://github.com/SgtCoDFish))

### 1.6.1

- Fixes an issue in `cmctl` that prevented displaying the Order resource with cert-manager 1.6 when running `cmctl status certificate`. ([#4572](https://github.com/jetstack/cert-manager/pull/4572), [@maelvls](https://github.com/maelvls))

### 1.6.2

- cert-manager now does one call to the ACME API instead of two when an Order fails. This fix is part of the effort towards mitigating [the high load](https://github.com/jetstack/cert-manager/issues/3298) that cert-manager deployments have on the Let's Encrypt API ([#4619](https://github.com/jetstack/cert-manager/pull/4619), [@irbekrm](https://github.com/irbekrm))

### 1.6.3

- Bumps the version of Go used to build the cert-manager binaries to 1.17.8, to fix a slew of CVEs (none of which were likely to be exploited) ([#4975](https://github.com/cert-manager/cert-manager/pull/4975), @vhosakot)
- Fixes an expired hardcoded certificate which broke unit tests ([#4977](https://github.com/cert-manager/cert-manager/pull/4977), @SgtCoDFish @jakexks)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.6.3**, the newest release recorded here for this line.

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
