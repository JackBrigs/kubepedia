---
id: TROUBLE-CERT_MANAGER_1_11_DEFECTS
type: troubleshooting
title: "cert-manager 1.11: defects fixed in the 1.11 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.11.0 <1.12.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cert-manager 1.11 known issues
  - cert-manager 1.11 fixed in
  - is this cert-manager bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cert-manager
sources:
  - type: docs
    path: cert-manager/cert-manager release notes for the 1.11 line — bug-fix entries
    url: https://github.com/cert-manager/cert-manager/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cert-manager 1.11: defects fixed in the 1.11 line

## Summary

**11 defects** the project fixed across **4 releases** of the 1.11 line, from 1.11.0 to
1.11.5. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.11.0

- Fixed a bug in AzureDNS resolver that led to early reconciliations in misconfigured Workload Identity-enabled setups (when Federated Identity Credential is not linked with a controller's k8s service account) (#5663, @weisdd)
- `vcert` was upgraded to `v4.23.0`, fixing two bugs in cert-manager. The first bug was preventing the Venafi issuer from renewing certificates when using TPP has been fixed. You should no longer see your certificates getting stuck with `WebSDK CertRequest Module Requested Certificate` or `This certificate cannot be processed while it is in an error state. Fix any errors, and then click Retry.`. The second bug that was fixed prevented the use of `algorithm: Ed25519` in Certificate resources with VaaS. (#5674, @maelvls)
- Bug fix: When using feature gates with the helm chart, enable feature gate flags on webhook as well as controller (#5584, @lvyanru8200)
- Fix `golang.org/x/text` vulnerability (#5562, @SgtCoDFish)
- Fixes a bug that caused the Vault issuer to omit the Vault namespace in requests to the Vault API. (#5591, @wallrj)
- Fix cainjector's --namespace flag. Users who want to prevent cainjector from reading all Secrets and Certificates in all namespaces (i.e to prevent excessive memory consumption) can now scope it to a single namespace using the --namespace flag. A cainjector that is only used as part of cert-manager installation only needs access to the cert-manager installation namespace. (#5694, @irbekrm)
- Fixes a bug where cert-manager controller was caching all Secrets twice (#5691, @irbekrm)

### 1.11.1

- Bump helm and other dependencies to fix CVEs, along with upgrading go and base images (#5815, @SgtCoDFish)
- The auto-retry mechanism added in VCert 4.23.0 and part of cert-manager 1.11.0 (#5674) has been found to be faulty. Until this issue is fixed upstream, we now use a patched version of VCert. This patch will slowdown the issuance of certificates by 9% in case of heavy load on TPP. We aim to release at an ulterior date a patch release of cert-manager to fix this slowdown. (#5819, @maelvls)

### 1.11.4

- Resolved docker/docker trivy CVE alert (#6164, @inteon)

### 1.11.5

- Use Go 1.19.9 to fix a security issue in Go's `crypto/tls` library. (#6317, @maelvls)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.11.5**, the newest release recorded here for this line.

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
