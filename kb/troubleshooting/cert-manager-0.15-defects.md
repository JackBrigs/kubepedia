---
id: TROUBLE-CERT_MANAGER_0_15_DEFECTS
type: troubleshooting
title: "cert-manager 0.15: defects fixed in the 0.15 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.15.0 <0.16.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cert-manager 0.15 known issues
  - cert-manager 0.15 fixed in
  - is this cert-manager bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cert-manager
sources:
  - type: docs
    path: cert-manager/cert-manager release notes for the 0.15 line — bug-fix entries
    url: https://github.com/cert-manager/cert-manager/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cert-manager 0.15: defects fixed in the 0.15 line

## Summary

**12 defects** the project fixed across **2 releases** of the 0.15 line, from 0.15.0 to
0.15.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.15.0

- Fix bug causing the experimental PKCS12 and JKS keystore feature to not work ([#2723](https://github.com/jetstack/cert-manager/pull/2723), [@munnerz](https://github.com/munnerz))
- Fix bug in webhook based validation on Kubernetes API servers older than 1.15 ([#2851](https://github.com/jetstack/cert-manager/pull/2851), [@munnerz](https://github.com/munnerz))
- Fix bug that could cause ACME Orders that contain already valid Authorizations to not be completed ([#2869](https://github.com/jetstack/cert-manager/pull/2869), [@munnerz](https://github.com/munnerz))
- Fix bug that could cause the `webhookbootstrap` controller to fail to Update webhook TLS resources in certain cases ([#2739](https://github.com/jetstack/cert-manager/pull/2739), [@munnerz](https://github.com/munnerz))
- Fix build system issue causing docker images to use user ID 0 (root) instead of '1000' as before ([#2708](https://github.com/jetstack/cert-manager/pull/2708), [@munnerz](https://github.com/munnerz))
- Fix case where cert-manager.io/issuer doesn't set `Issuer` kind ([#2837](https://github.com/jetstack/cert-manager/pull/2837), [@meyskens](https://github.com/meyskens))
- Fix incorrect service name being used in the --webhook-dns-names flag ([#2733](https://github.com/jetstack/cert-manager/pull/2733), [@munnerz](https://github.com/munnerz))
- Fix issuing causing CRDs to added to the static manifests twice ([#2790](https://github.com/jetstack/cert-manager/pull/2790), [@munnerz](https://github.com/munnerz))
- Fix validatingwebhookconfiguration to use correct URL path and to suport v1alpha3 API objects. ([#2831](https://github.com/jetstack/cert-manager/pull/2831), [@wallrj](https://github.com/wallrj))
- Properly fix user ID used for Docker images in release targets ([#2771](https://github.com/jetstack/cert-manager/pull/2771), [@munnerz](https://github.com/munnerz))
- Webhook: add `--tls-min-version` to allow configuring the minimum allowed TLS version and fix default ciphers list. ([#2769](https://github.com/jetstack/cert-manager/pull/2769), [@munnerz](https://github.com/munnerz))

### 0.15.2

- Fix entrypoint being inside a shell in UBI images ([cert-manager-olm#12](https://github.com/jetstack/cert-manager-olm/pull/12), [@meyskens](https://github.com/meyskens))


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.15.2**, the newest release recorded here for this line.

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
