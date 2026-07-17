---
id: TROUBLE-CERT_MANAGER_CERTIFICATE_NOT_READY
type: troubleshooting
title: "cert-manager: Certificate stuck not-ready (ACME challenge)"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.15.0 <=1.21.0"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - certificate stuck not ready
  - acme challenge pending
  - cert-manager order pending
  - http01 dns01 challenge failing
tags:
  - troubleshooting
  - cert-manager
  - certificates
  - acme
sources:
  - type: docs
    path: cert-manager troubleshooting
    url: https://cert-manager.io/docs/troubleshooting/
    note: "Certificate→CertificateRequest→Order→Challenge chain"
relations:
  - type: see_also
    target: COMPONENT-CERT_MANAGER
  - type: see_also
    target: CONCEPT-ADDON_CERT_MANAGER
---

# cert-manager: Certificate stuck not-ready (ACME challenge)

## Summary

A `Certificate` stays `Ready: False` and no TLS secret appears. cert-manager processes a
chain — **Certificate → CertificateRequest → Order → Challenge** — and the block is almost
always at the **ACME challenge** (HTTP-01 reachability or DNS-01 propagation). Walk the chain
to the failing object.

## Problem

- `kubectl get certificate` shows `READY: False` for a long time.
- The referenced TLS secret is missing or empty; Ingress serves the default cert.

## Context

- Applies to cert-manager **1.15–1.21** (Kubespray 1.15.3 / addon 1.18.2 —
  [[COMPONENT-CERT_MANAGER]], [[CONCEPT-ADDON_CERT_MANAGER]]).

## Diagnostics

Follow the chain (each object's `status`/events explains the next):

1. `kubectl describe certificate <name>` → find the `CertificateRequest`.
2. `kubectl describe certificaterequest <name>` → find the `Order` (ACME).
3. `kubectl describe order <name>` → find the pending `Challenge`.
4. `kubectl describe challenge <name>` — the real error:
   - **HTTP-01:** the solver pod/Ingress path `/.well-known/acme-challenge/...` must be
     reachable from the internet on port 80 — check DNS A record, ingress class, firewall.
   - **DNS-01:** the `_acme-challenge` TXT record must propagate — check the DNS provider
     credentials/permissions and propagation time.
- **Issuer not ready:** `kubectl describe clusterissuer <name>` — ACME account
  registration/email/EAB problems block every certificate.
- **Rate limits:** Let's Encrypt limits duplicate/failed orders — repeated failures back off;
  use the **staging** issuer while debugging.

## Known Issues

- The **webhook** must be reachable or Certificate/Issuer admission fails
  ([[TROUBLE-ADMISSION_WEBHOOK_BLOCKING]]).
- Addon cert-manager **1.18.0–1.18.4** has a controller DoS CVE (fixed 1.18.5).

## References

- cert-manager troubleshooting docs (above); component: [[COMPONENT-CERT_MANAGER]]; addon:
  [[CONCEPT-ADDON_CERT_MANAGER]].
