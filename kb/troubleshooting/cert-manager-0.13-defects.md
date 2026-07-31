---
id: TROUBLE-CERT_MANAGER_0_13_DEFECTS
type: troubleshooting
title: "cert-manager 0.13: defects fixed in the 0.13 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.13.0 <0.14.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cert-manager 0.13 known issues
  - cert-manager 0.13 fixed in
  - is this cert-manager bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cert-manager
sources:
  - type: docs
    path: cert-manager/cert-manager release notes for the 0.13 line — bug-fix entries
    url: https://github.com/cert-manager/cert-manager/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cert-manager 0.13: defects fixed in the 0.13 line

## Summary

**12 defects** the project fixed across **2 releases** of the 0.13 line, from 0.13.0 to
0.13.1. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.13.0

- Fix invalid service account name used in RBAC resources when manually specifying a service account name ([#2509](https://github.com/jetstack/cert-manager/pull/2509), [`@castlemilk`](https://github.com/castlemilk))
- fixed a bug that in certain cases could cause HTTP01 ingress `serviceName` fields to be incorrectly set ([#2460](https://github.com/jetstack/cert-manager/pull/2460), [`@greywolve`](https://github.com/greywolve))
- Fix bug causing ever-increasing CPU usage in webhook component ([#2467](https://github.com/jetstack/cert-manager/pull/2467), [`@munnerz`](https://github.com/munnerz))
- Fix bug causing temporary certificates to overwrite previously issued certificates when adding a new `dnsName` to an existing Certificate resource ([#2469](https://github.com/jetstack/cert-manager/pull/2469), [`@munnerz`](https://github.com/munnerz))
- Fix `certmanager_certificate_expiration_timestamp_seconds` metric recording ([#2416](https://github.com/jetstack/cert-manager/pull/2416), [`@munnerz`](https://github.com/munnerz))
- Fixes `ClusterIssuers` not finding the secret when the secret is in a different namespace than the certificate request using the Venafi issuer type ([#2520](https://github.com/jetstack/cert-manager/pull/2520), [`@mathianasj`](https://github.com/mathianasj))
- Fixes generation if invalid certificate name the the 52nd character in a domain name is a symbol. ([#2516](https://github.com/jetstack/cert-manager/pull/2516), [`@meyskens`](https://github.com/meyskens))
- Fix false-y values in helm chart to mitigate [`kubernetes/kubernetes#66450`](https://github.com/kubernetes/kubernetes/issues/66450) ([#2383](https://github.com/jetstack/cert-manager/pull/2383), [`@colek42`](https://github.com/colek42))

### 0.13.1

- Fix Venafi Cloud URL field being marked required ([#2583](https://github.com/jetstack/cert-manager/pull/2583), [@munnerz](https://github.com/munnerz))
- Fix cainjector.enabled=False override being ignored by the Helm Chart ([#2552](https://github.com/jetstack/cert-manager/pull/2552), [@gtaylor](https://github.com/gtaylor))
- Fix bug that could cause certificates to be incorrectly issued with an invalid public key ([#2543](https://github.com/jetstack/cert-manager/pull/2543), [@munnerz](https://github.com/munnerz))
- Fix GroupVersionKind set on OwnerReference of resources created by HTTP01 challenge solver, causing HTTP01 validations to fail on OpenShift 4.x ([#2554](https://github.com/jetstack/cert-manager/pull/2554), [@munnerz](https://github.com/munnerz))


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.13.1**, the newest release recorded here for this line.

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
