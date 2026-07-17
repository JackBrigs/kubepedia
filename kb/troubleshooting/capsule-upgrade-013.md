---
id: TROUBLE-CAPSULE_UPGRADE_013
type: troubleshooting
title: "Capsule 0.10→0.13 upgrade: webhooks/CRDs break"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.13.0 <=0.13.9"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - capsule webhook broke after upgrade
  - capsule crd not updated
  - capsule cert-manager required
  - capsule 0.13 upgrade
tags:
  - troubleshooting
  - capsule
  - multi-tenancy
  - upgrade
sources:
  - type: docs
    path: Capsule v0.13.0 release notes
    url: https://github.com/projectcapsule/capsule/releases/tag/v0.13.0
    note: "CRD lifecycle off the Helm hook; cert-manager default for webhook certs"
relations:
  - type: see_also
    target: CONCEPT-ADDON_CAPSULE
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
  - type: see_also
    target: TROUBLE-ADMISSION_WEBHOOK_BLOCKING
---

# Capsule 0.10→0.13 upgrade: webhooks/CRDs break

## Summary

Upgrading Capsule from the **0.10.x** line to **0.13.x** breaks the admission webhooks (no
certs) or leaves CRDs stale, because 0.13 moved CRD management off the Helm hook and defaults
webhook certs to **cert-manager**. Install cert-manager (or re-enable Capsule's TLS
controller) and let the chart manage CRDs.

## Problem

- Tenant operations fail: webhook `x509`/connection errors after the upgrade.
- New CRD fields/quota features missing; CRDs not updated.
- Everything tenant-related is blocked because the webhook is unreachable.

## Context

- Applies to Capsule **0.13.0–0.13.9** (owner spans 0.10.9→0.13.3 — [[CONCEPT-ADDON_CAPSULE]]).
  The `Tenant` CRD stays `capsule.clastix.io/v1beta2` (no apiVersion bump in this range).

## Diagnostics

- **Webhook certs default to cert-manager self-signed** — without cert-manager installed the
  webhooks have no certs. Install cert-manager, or re-enable Capsule's own TLS controller.
- **CRD lifecycle moved off the Helm CRD hook** (the hook couldn't deliver updates): 0.13
  manages CRDs via the chart (`crds.install=true`, new default). Pre-0.13 upgrades may need a
  manual/GitOps CRD apply first.
- 0.13 refactored GlobalTenantResources/TenantResources, added GlobalCustomQuotas/CustomQuotas
  and a `projectcapsule.dev/tenant` label, and migrated events `core/v1` → `events.k8s.io/v1`.

## Known Issues

- **CVE-2026-55636** (`namespace/finalize` typo) affects **0.13.0–0.13.5** — fixed **0.13.6**;
  upgrade past it. Webhook-unreachable blast radius: [[TROUBLE-ADMISSION_WEBHOOK_BLOCKING]].

## References

- Capsule v0.13.0 release notes (above); addon: [[CONCEPT-ADDON_CAPSULE]]; horizon:
  [[CONCEPT-UPGRADE_HORIZON]].
