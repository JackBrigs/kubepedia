---
id: TROUBLE-CERT_MANAGER_1_17_DEFECTS
type: troubleshooting
title: "cert-manager 1.17: defects fixed in the 1.17 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.17.0 <1.18.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cert-manager 1.17 known issues
  - cert-manager 1.17 fixed in
  - is this cert-manager bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cert-manager
sources:
  - type: docs
    path: cert-manager/cert-manager release notes for the 1.17 line — bug-fix entries
    url: https://github.com/cert-manager/cert-manager/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cert-manager 1.17: defects fixed in the 1.17 line

## Summary

**7 defects** the project fixed across **3 releases** of the 1.17 line, from 1.17.0 to
1.17.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.17.0

- BUGFIX: A change in v1.16.0 caused cert-manager's ACME ClusterIssuer to look in the wrong namespace for resources required for the issuance (eg. credential Secrets). This is now fixed in v1.16.1+ and v1.17.0+ (#7339, @inteon)
- Fix ACME HTTP-01 solver for IPv6 endpoints (#7391, @Peac36)
- Fix the behavior of `renewBeforePercentage` to comply with its spec (#7421, @adam-sroka)
- The issuer will now more quickly retry when its linked Secret is updated to fix an issue that caused a high back-off timeout. (#7455, @inteon)

### 1.17.1

- ❗ Fix issuing of certificates via DNS01 challenges on Cloudflare after a breaking change to the Cloudflare API (#7565, @LukeCarrier)

### 1.17.3

- Bump Go to 1.23.10 to fix GO-2025-3749, GO-2025-3750, and GO-2025-3751 (#7799, @wallrj)
- ACME: Increased challenge authorization timeout to 2 minutes to fix error `waiting for authorization` (#7798, @hjoshi123)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.17.3**, the newest release recorded here for this line.

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
