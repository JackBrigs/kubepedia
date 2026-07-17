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

## References

- cert-manager supported releases (1.18 row), advisory GHSA-gx3x-vq4p-mhhv (above).
- Catalog: [[CONCEPT-ADDON_CATALOG]]; Kubespray sibling: [[COMPONENT-CERT_MANAGER]].
