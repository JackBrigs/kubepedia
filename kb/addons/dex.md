---
id: CONCEPT-ADDON_DEX
type: concept
title: "Dex (OIDC provider) — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "2.42.0"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - dex
  - dexidp
  - oidc provider
  - dex 0.23.0
tags:
  - addons
  - identity
  - oidc
  - sso
sources:
  - type: code
    path: charts/dex/Chart.yaml
    url: https://raw.githubusercontent.com/dexidp/helm-charts/dex-0.23.0/charts/dex/Chart.yaml
    note: "kubeVersion >=1.14.0-0; appVersion v2.42.0"
  - type: docs
    path: dex v2.42.0 release
    url: https://github.com/dexidp/dex/releases/tag/v2.42.0
    note: "Go 1.24 bump, SAML/LDAP fixes, offline session change"
relations:
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
---

# Dex (OIDC provider) — addon

## Summary

Dex is a federated OIDC/OAuth2 identity provider deployed via the `dexidp` Helm chart
**0.23.0**, shipping app **v2.42.0**. It brokers upstream identity (LDAP, SAML, GitHub,
etc.) into OIDC for cluster and app SSO. Chart 0.23.0 is bundled by several other addons in
this platform (envoy-xds-controller, kubernetes-dashboard flows) — check for version drift.

## Context

- Class: upstream addon; catalog row in [[CONCEPT-ADDON_CATALOG]].
- Frequently co-deployed as a sidecar identity layer (the inventory ships dex `0.22.1`
  alongside `exc`), so more than one Dex version may run — keep issuer/config consistent.

## Implementation

- Chart→app: `dex-0.23.0` → dex **v2.42.0**, image `ghcr.io/dexidp/dex:v2.42.0`.
- Chart `kubeVersion`: **`>=1.14.0-0`** (floor only; 1.29–1.35 all satisfy).
- 2.42.0 bumped Go 1.22.5→**1.24.0** and refreshed x/crypto, x/net, gRPC, etcd — a large
  dependency turn; re-verify TLS/gRPC behaviour after upgrade. Behavioural: offline sessions
  are now created even when the approval screen is skipped; SAML nil-pointer panic fixed;
  LDAP `DialURL` scheme fixed.

## Configuration

- Chart 0.23.0 changed image templating for dynamic image/digest — re-check any
  registry/tag overrides on upgrade.
- Ensure the OIDC `issuer` URL is stable and TLS-terminated correctly; Dex's TLS handling
  regressed in 2.37.0 and was fixed from 2.38.0 (so 2.42.0 is patched — GHSA-gr79-9v6v-gc9r).

## Compatibility

- **Kubernetes range:** no explicit upstream matrix (**unverified**); only the chart floor
  `>=1.14`. No K8s API deprecation affects the chart manifests across 1.29–1.35.
- **CVEs:** image scanners flag transitive **CVE-2024-45338** (`golang.org/x/net/html`) in
  the 2.42.0 image, which can fail CI image gates; there is no dex-application-level CVE
  unique to 2.42.0 in GHSA/OSV. Older dex CVEs (CVE-2020-26290/-27847, CVE-2022-39222) are
  already fixed — scanner hits on those are false positives.

## Upstream issues & upgrade notes (mined 2026-07-19)

**Future upgrade context** beyond pinned **2.42.0** (from upstream releases):
- **⚠ 2.45.0 breaking:** bundles **gomplate v5.0.0** (its own breaking changes), and **`ContinueOnConnectorFailure` is now enabled by default** (a behavior change — a failing connector no longer blocks startup). Adds **PKCE** support and a Vault signer for JWTs.
- **Security:** gomplate carries CVE-2025-68121 / CVE-2026-25934 (gomplate is optional — avoid it if unused).
- **Maintenance signal:** Dex maintenance is thin (public calls for maintainers) — factor into reliance.

**Open upstream requests (as of 2026-07-19):** no **end-session/logout (RP-initiated logout) endpoint** forwarding to upstream (#1697); no built-in **MFA/2FA** (#352); arbitrary custom claims (#1182).

## Older-version CVEs & security history (mined 2026-07-19)

Older Dex exposure is dominated by **bundled gomplate** (CVE-2025-68121, CVE-2026-25934 — optional, avoid if unused) and base-image/Go-stdlib CVEs in old images. Dex has had occasional OIDC-handling advisories historically — verify an old pin against the Dex security advisories. Upgrading also brings PKCE (2.45.0) and the connector-failure default change.

## References

- `Chart.yaml` + dex v2.42.0 release (above); TLS advisory GHSA-gr79-9v6v-gc9r.
- Catalog: [[CONCEPT-ADDON_CATALOG]].
