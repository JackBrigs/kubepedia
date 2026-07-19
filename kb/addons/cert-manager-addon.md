---
id: CONCEPT-ADDON_CERT_MANAGER
type: concept
title: "cert-manager (addon v1.18.2) — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.33"
component_version: "1.18.2"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - cert-manager addon
  - cert-manager 1.18.2
tags:
  - addons
  - certificates
  - tls
  - security
sources:
  - type: docs
    path: cert-manager supported releases (1.18 row)
    url: https://cert-manager.io/docs/releases/
    note: "1.18 supports Kubernetes 1.29 → 1.33"
  - type: docs
    path: advisory GHSA-gx3x-vq4p-mhhv
    url: https://github.com/cert-manager/cert-manager/security/advisories/GHSA-gx3x-vq4p-mhhv
    note: "DoS via crafted DNS response; 1.18.0–1.18.4 affected, fixed 1.18.5"
relations:
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
  - type: see_also
    target: COMPONENT-CERT_MANAGER
---

# cert-manager (addon v1.18.2) — addon

## Summary

The owner's independent cert-manager install — **v1.18.2** — newer than the
Kubespray-managed [[COMPONENT-CERT_MANAGER]] (which pins 1.15.3). cert-manager 1.18 supports
Kubernetes **1.29 → 1.33**. **Security:** 1.18.2 is affected by a controller DoS CVE — move
to **1.18.5+**.

## Context

- Class: upstream addon; catalog row in [[CONCEPT-ADDON_CATALOG]] (overlaps the Kubespray
  cert-manager — different, newer version; don't conflate).

## Implementation

- Chart==app **v1.18.2** (cert-manager chart and app track together). Deploys the controller,
  webhook and cainjector plus CRDs.

## Configuration

- The **webhook** is a mutating/validating admission webhook — if it is unreachable,
  Certificate/Issuer operations (and dependent resources) fail
  ([[TROUBLE-ADMISSION_WEBHOOK_BLOCKING]]).
- CRDs are versioned with the release — apply/upgrade CRDs with the chart.

## Compatibility

- **Kubernetes range:** cert-manager **1.18 → K8s 1.29–1.33** (per the supported-releases
  page); 1.18 reached end-of-life **2026-03-10**, so it is out of upstream support — plan an
  upgrade to a supported minor.
- **CVE:** **GHSA-gx3x-vq4p-mhhv / GO-2026-4399** — cert-manager-controller DoS via a
  specially-crafted DNS response, affects **1.18.0–1.18.4** (so **1.18.2 is affected**), fixed
  **1.18.5** (and 1.19.3). Upgrade to 1.18.5+.

## Upstream issues & upgrade notes (mined 2026-07-19)

**Future upgrade context** beyond pinned **1.18.2** (from upstream releases):
- **1.20.0 breaking:** container **UID/GID changed 1000/0 → 65532/65532** (fix file-permission assumptions); `DefaultPrivateKeyRotationPolicyAlways` → GA.
- **1.21.0 breaking:** default `tokenrequest` RBAC removed from the Helm chart; Helm metrics values removed (`prometheus.servicemonitor.targetPort/path`, `podmonitor.path`).
- **⚠ Security (HIGH) GHSA-8rvj-mm4h-c258:** namespace users could create ACME `Challenge`/`Order` directly (privilege) — `create`/`patch`/`update` removed from the `cert-manager-edit` ClusterRole. Backported to **1.19.6 / 1.20.3**; the shipped 1.18.2 predates it.
- **1.20.0 (MODERATE):** controller panic (DoS) on unexpected DNS response order.

**Open upstream bugs (as of 2026-07-19):** DNS-01 propagation failures despite recursive NS (#5917); **leader-election defaults to `kube-system` → RBAC failure when installed elsewhere** (#6716); ACME `429` rate-limit not handled → permanent issuance failure (#5867); HTTP-01 solver pods don't inherit `imagePullSecrets` (#5959).

## Older-version CVEs & security history (mined 2026-07-19)

For clusters still on an **older** cert-manager (older Kubespray tags shipped lower versions):
- **CVE-2026-25518 / GHSA-gx3x-vq4p-mhhv** (Medium): malicious DNS-01 responses **panic the controller (DoS)** — affects **1.18.0–1.19.2**, fixed **1.18.5 / 1.19.3**.
- **GHSA-r4pg-vg54-wxx4** (Low): crafted PEM data causes **excessive CPU** (resource exhaustion) — affects **everything below 1.12.14 / 1.15.4 / 1.16.2**.
- **CVE-2026-62290 / GHSA-8rvj-mm4h-c258** (High, 1.18.0–1.20.2): direct ACME `Challenge`/`Order` creation bypasses Issuer DNS-01 policy and can disclose ClusterIssuer DNS creds — fixed **1.19.6 / 1.20.3**. Upgrade off any of these ranges.

## Guides & how-to (official)

- **Upgrade:** https://cert-manager.io/docs/installation/upgrade/ + per-version notes https://cert-manager.io/docs/releases/
- **Install (Helm):** https://cert-manager.io/docs/installation/helm/ ; **backup/restore:** https://cert-manager.io/docs/devops-tips/backup/
- **How to upgrade (key steps):** read the version-path release notes first; upgrade **one minor at a time** (latest patch); **CRDs** — if installed via `crds.enabled=true` Helm handles them, otherwise `kubectl apply` the new CRD manifest **before** the chart; **back up cert-manager resources first**.

## References

- cert-manager supported releases (1.18 row), advisory GHSA-gx3x-vq4p-mhhv (above).
- Catalog: [[CONCEPT-ADDON_CATALOG]]; Kubespray sibling: [[COMPONENT-CERT_MANAGER]].
