---
id: TROUBLE-CERT_MANAGER_1_13_DEFECTS
type: troubleshooting
title: "cert-manager 1.13: defects fixed in the 1.13 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.13.0 <1.14.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cert-manager 1.13 known issues
  - cert-manager 1.13 fixed in
  - is this cert-manager bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cert-manager
sources:
  - type: docs
    path: cert-manager/cert-manager release notes for the 1.13 line — bug-fix entries
    url: https://github.com/cert-manager/cert-manager/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cert-manager 1.13: defects fixed in the 1.13 line

## Summary

**13 defects** the project fixed across **6 releases** of the 1.13 line, from 1.13.0 to
1.13.5. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.13.0

- Fix CloudDNS issuers stuck in propagation check, when multiple instances are issuing for the same FQDN (#6088, @cypres)
- Fix indentation of Webhook NetworkPolicy matchLabels in helm chart. (#6220, @ubergesundheit)
- Fixed Cloudflare DNS01 challenge provider race condition when validating multiple domains (#6191, @Richardds)
- Fixes a bug where webhook was pulling in controller's feature gates. *⚠️ ⚠️ BREAKING ⚠️ ⚠️** : If you deploy cert-manager using helm and have `.featureGates` value set, the features defined there will no longer be passed to cert-manager webhook, only to cert-manager controller. Use `webhook.featureGates` field instead to define features to be enabled on webhook. *⚠️Potentially breaking**: If you were, for some reason, passing cert-manager controller's features to webhook's `--feature-gates` flag, this will now break (unless the webhook actually has a feature by that name). (#6093, @irbekrm)
- Fixes an issue where cert-manager would incorrectly reject two IP addresses as being unequal when they should have compared equal. This would be most noticeable when using an IPv6 address which doesn't match how Go's `net.IP.String()` function would have printed that address. (#6293, @SgtCoDFish)

### 1.13.1

- BUGFIX: fix CertificateRequest name collision bug in StableCertificateRequestName feature. (#6358, @jetstack-bot)

### 1.13.2

- BUGFIX[helm]: Fix issue where webhook feature gates were only set if controller feature gates are set. (#6381, @asapekia)
- Fix runaway bug caused by multiple Certificate resources that point to the same Secret resource. (#6425, @inteon)
- The Venafi issuer now properly resets the certificate and should no longer get stuck with `WebSDK CertRequest Module Requested Certificate` or `This certificate cannot be processed while it is in an error state. Fix any errors, and then click Retry.`. (#6402, @maelvls)

### 1.13.3

- Upgrade Go modules: `otel`, `docker`, and `jose` to fix CVE alerts. See https://github.com/advisories/GHSA-8pgv-569h-w5rw, https://github.com/advisories/GHSA-jq35-85cj-fj4p, and https://github.com/advisories/GHSA-2c7c-3mj9-8fqh. ([#6514](https://github.com/cert-manager/cert-manager/pull/6514), [@inteon](https://github.com/inteon))

### 1.13.4

- Fix CVE 2023 48795 by upgrading to golang.org/x/crypto@v0.17.0 (#6675, @wallrj)
- Fix GHSA-7ww5-4wqc-m92c by upgrading to `github.com/containerd/containerd@v1.7.12` (#6684, @wallrj)

### 1.13.5

- BUGFIX: fix race condition due to registering and using global runtime.Scheme variables (#6832, @inteon)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.13.5**, the newest release recorded here for this line.

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
