---
id: TROUBLE-CERT_MANAGER_0_14_DEFECTS
type: troubleshooting
title: "cert-manager 0.14: defects fixed in the 0.14 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.14.0 <0.15.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cert-manager 0.14 known issues
  - cert-manager 0.14 fixed in
  - is this cert-manager bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cert-manager
sources:
  - type: docs
    path: cert-manager/cert-manager release notes for the 0.14 line — bug-fix entries
    url: https://github.com/cert-manager/cert-manager/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cert-manager 0.14: defects fixed in the 0.14 line

## Summary

**14 defects** the project fixed across **4 releases** of the 0.14 line, from 0.14.0 to
0.14.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.14.0

- Fix `GroupVersionKind` set on `OwnerReference` of resources created by HTTP01 challenge solver, causing HTTP01 validations to fail on OpenShift 4 ([#2546](https://github.com/jetstack/cert-manager/pull/2546), [`@munnerz`](https://github.com/munnerz))
- Fix Venafi Cloud URL field being marked required ([#2568](https://github.com/jetstack/cert-manager/pull/2568), [`@munnerz`](https://github.com/munnerz))
- Fix bug in ingress-shim causing Certificate resources to be rapidly updated if multiple `spec.tls[].hosts` entries refer to the same Secret name but a different set of hosts ([#2611](https://github.com/jetstack/cert-manager/pull/2611), [`@munnerz`](https://github.com/munnerz))
- Fix bug that could cause certificates to be incorrectly issued with an invalid public key ([#2539](https://github.com/jetstack/cert-manager/pull/2539), [`@munnerz`](https://github.com/munnerz))
- Fix `cainjector.enabled=False` override being ignored by the Helm Chart ([#2544](https://github.com/jetstack/cert-manager/pull/2544), [`@gtaylor`](https://github.com/gtaylor))

### 0.14.1

- Fix bug causing the experimental PKCS12 and JKS keystore feature to not work ([#2728](https://github.com/jetstack/cert-manager/pull/2728), [@munnerz](https://github.com/munnerz))
- Fix bug that could cause the `webhookbootstrap` controller to fail to Update webhook TLS resources in certain cases ([#2742](https://github.com/jetstack/cert-manager/pull/2742), [@munnerz](https://github.com/munnerz))
- Fix incorrect service name being used in the --webhook-dns-names flag ([#2735](https://github.com/jetstack/cert-manager/pull/2735), [@munnerz](https://github.com/munnerz))
- Fix issue causing cert-manager docker images to run as the root user instead of UID 1000 ([#2720](https://github.com/jetstack/cert-manager/pull/2720), [@munnerz](https://github.com/munnerz))
- Fix issue that could cause the ACME client to block for extended periods when the server responds with a long `retry-after` header, causing cert-manager to not process new orders or challenges. ([#2729](https://github.com/jetstack/cert-manager/pull/2729), [@JoshVanL](https://github.com/JoshVanL))

### 0.14.2

- Properly fix user ID used for Docker images in release targets ([#2774](https://github.com/jetstack/cert-manager/pull/2774), [@munnerz](https://github.com/munnerz))

### 0.14.3

- Fix bug in webhook based validation on Kubernetes API servers older than 1.15 ([#2860](https://github.com/jetstack/cert-manager/pull/2860), [@munnerz ](https://github.com/munnerz))
- Fix case where cert-manager.io/issuer doesn't set `Issuer` kind ([#2838](https://github.com/jetstack/cert-manager/pull/2838), [@meyskens](https://github.com/meyskens))
- Fix validatingwebhookconfiguration to use correct URL path and to suport v1alpha3 API objects. ([#2832](https://github.com/jetstack/cert-manager/pull/2832), [@wallrj ](https://github.com/wallrj ))


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.14.3**, the newest release recorded here for this line.

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
