---
id: TROUBLE-CERT_MANAGER_1_5_DEFECTS
type: troubleshooting
title: "cert-manager 1.5: defects fixed in the 1.5 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.5.0 <1.6.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cert-manager 1.5 known issues
  - cert-manager 1.5 fixed in
  - is this cert-manager bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cert-manager
sources:
  - type: docs
    path: cert-manager/cert-manager release notes for the 1.5 line — bug-fix entries
    url: https://github.com/cert-manager/cert-manager/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cert-manager 1.5: defects fixed in the 1.5 line

## Summary

**12 defects** the project fixed across **6 releases** of the 1.5 line, from 1.5.0 to
1.5.5. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.5.0

- Fix a bug where failed Certificate Requests were not retried ([#4130](https://github.com/jetstack/cert-manager/pull/4130), [@irbekrm](https://github.com/irbekrm))
- Fix check for self-signed certificates in EncodeX509Chain which broke certs whose subject DN matched their issuer's subject DN ([#4237](https://github.com/jetstack/cert-manager/pull/4237), [@SgtCoDFish](https://github.com/SgtCoDFish))
- Fix handling of chains which don't have a root in ParseSingleCertificateChain, and improve handling in situations where that function is passed a single certificate. ([#4261](https://github.com/jetstack/cert-manager/pull/4261), [@SgtCoDFish](https://github.com/SgtCoDFish))
- Fixed a bug in the "gateway shim" controller that was causing the cert-manager controller to crash with a nil pointer exception when using the annotation "cert-manager.io/issuer" on a Gateway that had an empty `tls` block or with `certificateRef` left empty. ([#4293](https://github.com/jetstack/cert-manager/pull/4293), [@maelvls](https://github.com/maelvls))
- Fixed a goroutine leak that was causing the controller's memory usage to grow with time ([#4233](https://github.com/jetstack/cert-manager/pull/4233), [@maelvls](https://github.com/maelvls))
- Fixed a race condition introduced in v0.15.0 that would crash cert-manager for clusters with a large number of certificates. ([#4231](https://github.com/jetstack/cert-manager/pull/4231), [@maelvls](https://github.com/maelvls))

### 1.5.1

- Fix v1beta1 CRDs which were accidentally changed in cert-manager v1.5.0 ([#4355](https://github.com/jetstack/cert-manager/pull/4355), [@jetstack-bot](https://github.com/jetstack-bot))

### 1.5.2

- Fix regression in Ingress PathType introduced in v1.5.0 ([#4385](https://github.com/jetstack/cert-manager/pull/4385), [@jakexks](https://github.com/jakexks))
- Fixed the HTTP-01 solver creating ClusterIP instead of NodePort services by default. ([#4394](https://github.com/jetstack/cert-manager/pull/4394), [@jakexks](https://github.com/jakexks))

### 1.5.3

- Fixes renewal time issue for certs with skewed duration period. ([#4403](https://github.com/jetstack/cert-manager/pull/4403), @irbekrm). Thanks to @mfmbarros for help with debugging the issue!

### 1.5.4

- FIX: Prevent Vault Client from panicing when request to Vault health endpoint fails. ([#4476](https://github.com/jetstack/cert-manager/pull/4476), [@JoshVanL](https://github.com/JoshVanL))

### 1.5.5

- Fixed a regression where cert-manager was creating Ingresses using the field `ingressClassName` instead of the annotation `kubernetes.io/ingress.class`. More details about this regression are available [in the 1.7 release notes](https://cert-manager.io/next-docs/release-notes/release-notes-1.7/#ingress-class-semantics). ([#4783](https://github.com/jetstack/cert-manager/pull/4783), [@maelvls](https://github.com/maelvls))


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.5.5**, the newest release recorded here for this line.

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
