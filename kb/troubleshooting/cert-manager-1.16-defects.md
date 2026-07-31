---
id: TROUBLE-CERT_MANAGER_1_16_DEFECTS
type: troubleshooting
title: "cert-manager 1.16: defects fixed in the 1.16 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.16.0 <1.17.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cert-manager 1.16 known issues
  - cert-manager 1.16 fixed in
  - is this cert-manager bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cert-manager
sources:
  - type: docs
    path: cert-manager/cert-manager release notes for the 1.16 line — bug-fix entries
    url: https://github.com/cert-manager/cert-manager/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cert-manager 1.16: defects fixed in the 1.16 line

## Summary

**9 defects** the project fixed across **4 releases** of the 1.16 line, from 1.16.0 to
1.16.4. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.16.0

- Venafi TPP issuer can now be used with a username & password combination with OAuth. Fixes #4653. Breaking: cert-manager will no longer use the API Key authentication method which was deprecated in 20.2 and since removed in 24.1 of TPP. ([#7084](https://github.com/cert-manager/cert-manager/pull/7084), [`@hawksight`](https://github.com/hawksight))
- BUGFIX: fix issue that caused Vault issuer to not retry signing when an error was encountered. ([#7105](https://github.com/cert-manager/cert-manager/pull/7105), [`@inteon`](https://github.com/inteon))
- Bump `grpc-go` to fix `GHSA-xr7q-jx4m-x55m` ([#7164](https://github.com/cert-manager/cert-manager/pull/7164), [`@SgtCoDFish`](https://github.com/SgtCoDFish))
- Fix Azure DNS causing panics whenever authentication error happens ([#7177](https://github.com/cert-manager/cert-manager/pull/7177), [`@eplightning`](https://github.com/eplightning))
- Fix incorrect indentation of `endpointAdditionalProperties` in the `PodMonitor` template of the Helm chart ([#7190](https://github.com/cert-manager/cert-manager/pull/7190), [`@wallrj`](https://github.com/wallrj))
- Fixes ACME HTTP01 challenge behavior when using Gateway API to prevent unbounded creation of HTTPRoute resources ([#7178](https://github.com/cert-manager/cert-manager/pull/7178), [`@miguelvr`](https://github.com/miguelvr))

### 1.16.1

- BUGFIX: A change in `v1.16.0` caused cert-manager's ACME ClusterIssuer to look in the wrong namespace for resources required for the issuance (e.g. credential Secrets). This is now fixed in `v1.16.1`. ([#7342](https://github.com/cert-manager/cert-manager/pull/7342), [`@inteon`](https://github.com/inteon))

### 1.16.3

- Fix the behaviour of `renewBeforePercentage` to comply with its spec (#7441, @cert-manager-bot)

### 1.16.4

- ❗ Fix issuing of certificates via DNS01 challenges on Cloudflare after a breaking change to the Cloudflare API (#7566, @LukeCarrier)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.16.4**, the newest release recorded here for this line.

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
