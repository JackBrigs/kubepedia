---
id: TROUBLE-CERT_MANAGER_1_21_DEFECTS
type: troubleshooting
title: "cert-manager 1.21: defects fixed in the 1.21 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.21.0 <1.22.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cert-manager 1.21 known issues
  - cert-manager 1.21 fixed in
  - is this cert-manager bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cert-manager
sources:
  - type: docs
    path: cert-manager/cert-manager release notes for the 1.21 line — bug-fix entries
    url: https://github.com/cert-manager/cert-manager/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cert-manager 1.21: defects fixed in the 1.21 line

## Summary

**25 defects** the project fixed across **2 releases** of the 1.21 line, from 1.21.0 to
1.21.1. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.21.0

- **Controller crash-loops when a Certificate sets `renewal.policy: Disabled`**: the new Certificate renewal policies feature (#8258) causes a nil pointer dereference panic in the trigger controller whenever a Certificate's `spec.renewal.policy` is set to `Disabled` — `pki.RenewalTime()` returns `(nil, nil)` for that policy, but the caller unconditionally dereferences the result. This crashes the controller process (crash-loop) for any cluster with such a Certificate. **Workaround**: do not set `renewal.policy: Disabled` on any Certificate until this is fixed; remove the field (or set a different policy) from any Certificate that already has it, and restart the controller if it is currently crash-looping. See #9031 for details
- **Issuer/ClusterIssuer can get stuck at `Ready: False, Reason: InvalidSolver` and never self-correct**: new eager validation of ACME solver Secrets (#8255) means an Issuer/ClusterIssuer referencing a solver Secret (e.g. a DNS01 provider credential) that doesn't exist yet will correctly report `Ready: False`, but creating the missing Secret afterwards does not trigger re-reconciliation — the controller's Secret-watch logic was never updated to recognise solver Secrets. It will only recover on the next 10-hour informer resync, a change to the Issuer/ClusterIssuer's own spec, or a controller restart. **Workaround**: after creating the missing Secret, make a trivial edit to the Issuer/ClusterIssuer spec (or delete and recreate it) to force reconciliation. See cert-manager/cert-manager#9036 for details and a fix proposal
- **Integer overflow in `renewBeforePercentage`**: Certificates with durations longer than approximately 3 years were incorrectly rejected or assigned incorrect renewal times. (#8947)
- **Infinite re-issuance loop**: cert-manager no longer loops when an issuer returns an already-expired certificate. (#8610)
- **ACME transient network errors**: challenges no longer permanently fail on TLS handshake timeouts, DNS resolution failures, or context cancellation during nonce fetches and authorization waits. (#8760)
- **DNS-over-HTTPS response body cap**: response body reads are now bounded at 128 KB to prevent potential OOM. (#8803)
- **Vault path traversal**: the Vault issuer webhook now rejects `..` path segments, preventing `path.Join` from silently resolving relative segments. (#8930)
- **DNS issuer secrets validated before ready**: prevents silent misconfiguration. (#8255)
- Fix Venafi TPP issuer setup and signing regression on master: restore authentication of the vcert connector in the client constructor, which was removed in #8808. (#8843, @wallrj-cyberark)
- Fix a performance issue in the certificateRequestApproval webhook where CertificateRequests referencing a GroupKind whose CRD is not yet installed would trigger repeated API server discovery queries on every admission request. Negative results are now cached for 30 seconds. (#8651, @mateenali66)
- Fix webhook serving certificate not being renewed after system suspend. (#8464, @Peac36)
- Fixed a rare panic in the trigger controller when a Certificate is deleted from the informer cache while a reconcile is in progress (e.g. during namespace teardown). (#8962, @hjoshi123)
- Fixed an integer overflow in `renewBeforePercentage` calculations that caused Certificates with durations longer than approximately 3 years to be incorrectly rejected by validation or assigned incorrect renewal times. (#8947, @ThatsMrTalbot)
- Fixed duplicate `parentRef` bug when both issuer config and annotations are present. (#8619, @hjoshi123)
- Fixed infinite re-issuance loop when issuer returns an already expired certificate (#8610, @onurmicoogullari)
- Fixed local `e2e-setup-samplewebhook` installation to use the samplewebhook image repository and tag from the saved image tarball manifest. (#8821, @wallrj)
- Fixed potential OOM in DNS-over-HTTPS client by bounding response body read with io.LimitReader (128 KB cap). (#8803, @SebTardif)
- Fixed validation of timezone-prefixed renewal window cron specs without a schedule. (#8813, @immanuwell)
- Helm: Fix invalid YAML generated when both `webhook.config` and `webhook.volumes` are defined. (#8664, @jnohlgard)

### 1.21.1

- Avoid controller panic if a Certificate sets spec.renewal.policy=Disabled (#9038, @sklirg)
- Fix Issuer/ClusterIssuer stuck at Ready=False/InvalidSolver after a missing ACME DNS-01 solver Secret is created (#9083, @SebTardif)
- Fix log spam and dropped Secret informer events for non-cert-manager Secrets, caused by a generics regression introduced in 1.21.0. (#9037, @wallrj-cyberark)
- Fixed the commented Gateway API config example in the Helm chart values to use `gatewayAPI.enabled` instead of the invalid `gatewayAPI.enable`. (#9012, @mateenali66)
- Bump `github.com/google/cel-go` to v0.29.0 to fix a reported security vulnerability (#9072)
- Bump `go.opentelemetry.io/otel` to v1.44.0 to fix a reported security vulnerability (#9073)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.21.1**, the newest release recorded here for this line.

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
