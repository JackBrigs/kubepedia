---
id: TROUBLE-WEBHOOK_CERT_MANAGER_ORDERING
type: troubleshooting
title: "Admission webhooks fail when cert-manager isn't ready first (ordering)"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - webhook x509 after install
  - cert-manager ordering webhooks
  - operator webhook no certs
  - install order cert-manager first
tags:
  - troubleshooting
  - cross-component
  - webhooks
  - cert-manager
sources:
  - type: docs
    path: cert-manager webhook concepts
    url: https://cert-manager.io/docs/concepts/webhook/
    note: "many operators use cert-manager to issue webhook TLS"
relations:
  - type: see_also
    target: TROUBLE-ADMISSION_WEBHOOK_BLOCKING
  - type: see_also
    target: CONCEPT-ADDON_CERT_MANAGER
  - type: see_also
    target: CONCEPT-ADDON_CAPSULE
---

# Admission webhooks fail when cert-manager isn't ready first (ordering)

## Summary

A **cross-component** failure: many operators default to **cert-manager** to issue their
admission-webhook TLS (Capsule, OpenTelemetry Operator, vault-secrets-webhook, and others). If
cert-manager isn't installed/ready **before** them, their webhooks come up with no certs and
`x509`/connection errors block the resources they gate — sometimes cluster-wide.

## Problem

- Right after a bulk install/bootstrap, tenant/CR operations fail with webhook `x509` or
  "connection refused" errors.
- An operator's own CRs can't be created because its webhook has no serving cert.
- Removing cert-manager (or a cert-manager outage) breaks multiple unrelated operators at once.

## Context

- Affects any component whose webhook certs come from cert-manager:
  [[CONCEPT-ADDON_CAPSULE]] (0.13 defaults to cert-manager), the OpenTelemetry Operator
  ([[CONCEPT-ADDON_OTEL_OPERATOR]]) which **requires** cert-manager, vault-secrets-webhook
  ([[CONCEPT-ADDON_VAULT_SECRETS_WEBHOOK]]), and cert-manager's own webhook
  ([[CONCEPT-ADDON_CERT_MANAGER]]).

## Diagnostics

- **Install/bootstrap order:** cert-manager (controller + webhook **Ready**, CRDs present)
  must be up **before** operators that depend on it. In GitOps, express this dependency (sync
  waves / health checks), don't apply everything at once.
- **Certificate/Issuer health:** if the operator's webhook `Certificate` isn't `Ready`, its
  `ValidatingWebhookConfiguration`/`MutatingWebhookConfiguration` `caBundle` is empty → every
  gated request fails. Fix the underlying Certificate ([[TROUBLE-CERT_MANAGER_CERTIFICATE_NOT_READY]]).
- **Alternative cert mode:** some operators can self-sign their webhook certs instead of using
  cert-manager — enable that mode if you don't run cert-manager.
- **Blast radius:** scope `namespaceSelector`/`failurePolicy` so a webhook outage doesn't block
  the whole cluster ([[TROUBLE-ADMISSION_WEBHOOK_BLOCKING]]).

## Known Issues

- A cert-manager **upgrade** that briefly restarts the webhook can flap dependent operators —
  upgrade cert-manager in a low-traffic window.
- Capsule 0.13 moved webhook certs to cert-manager by default; without it, re-enable Capsule's
  own TLS controller ([[TROUBLE-CAPSULE_UPGRADE_013]]).

## References

- cert-manager webhook concepts (above); webhook blast radius:
  [[TROUBLE-ADMISSION_WEBHOOK_BLOCKING]]; cert chain:
  [[TROUBLE-CERT_MANAGER_CERTIFICATE_NOT_READY]].
