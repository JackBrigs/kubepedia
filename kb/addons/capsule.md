---
id: CONCEPT-ADDON_CAPSULE
type: concept
title: "Capsule + capsule-proxy (multi-tenancy) — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "0.13.3"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - capsule
  - capsule-proxy
  - capsule-system
  - multi-tenancy operator
tags:
  - addons
  - multi-tenancy
  - capsule
sources:
  - type: docs
    path: Capsule v0.13.0 release notes
    url: https://github.com/projectcapsule/capsule/releases/tag/v0.13.0
    note: "CRD-lifecycle, cert-manager default, quota refactor"
  - type: docs
    path: capsule installation/support policy
    url: https://projectcapsule.dev/docs/operating/setup/installation/
    note: "supported: latest K8s minor only"
  - type: docs
    path: advisory CVE-2026-55636
    url: https://github.com/projectcapsule/capsule/security/advisories
    note: "GHSA-gwxr-7h77-7777, affects 0.13.0–0.13.5, fixed 0.13.6"
relations:
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
---

# Capsule + capsule-proxy (multi-tenancy) — addon

## Summary

Capsule (CNCF Sandbox) provides self-service multi-tenancy via a `Tenant` CRD; `capsule-proxy`
lets tenant users list/watch cluster-scoped resources they own. The inventory spans **capsule
0.10.9 → 0.13.3** and **capsule-proxy 0.9.13 → 0.13.4** (now version-aligned). The 0.10 → 0.13
jump carries real operational changes.

## Context

- Class: upstream addon; `capsule-system` row in [[CONCEPT-ADDON_CATALOG]]. Capsule and
  capsule-proxy are **version-paired** (capsule chart 0.13.3 bundles capsule-proxy 0.13.3).

## Implementation

- App: capsule **0.13.3** (`ghcr.io/projectcapsule/capsule:v0.13.3`), capsule-proxy **0.13.4**.
- Chart `kubeVersion`: **none**. The `Tenant` CRD was already `capsule.clastix.io/v1beta2`
  before 0.10 — **no v1beta1→v1beta2 bump** in this range.

## Configuration

- **CRD lifecycle moved off the Helm CRD hook (0.13):** CRDs are now managed by the chart
  (`crds.install=true`, new default) because the legacy hook could not deliver CRD updates.
  Pre-0.13 upgrades need manual/GitOps CRD application.
- **Webhook certs default to cert-manager** self-signed — without cert-manager you must
  re-enable Capsule's own TLS controller or the webhooks break.
- 0.13 refactored GlobalTenantResources/TenantResources and added a new quota system
  (GlobalCustomQuotas/CustomQuotas), a new `projectcapsule.dev/tenant` label, and migrated
  events `core/v1` → `events.k8s.io/v1`. Intermediate: 0.11 made tenant owners optional; 0.12
  added a TenantOwner CRD.

## Compatibility

- **Kubernetes range:** upstream policy is "**latest minor only**" (historical min v1.16+);
  the chart declares no `kubeVersion`, so an exact floor is **unverified**. Treat as tracking
  current minors across 1.29–1.35.
- **CVE (0.13.3 affected):** **CVE-2026-55636 / GHSA-gwxr-7h77-7777** — a `namespace/finalize`
  typo, Moderate, affects **0.13.0–0.13.5** (incl. 0.13.3), fixed **0.13.6**. capsule-proxy's
  older advisories (empty-token auth bypass GHSA-fpvw-6m5v-hqfp, etc.) predate the 0.13.x line.

## Upstream issues & upgrade notes (mined 2026-07-19)

**Future upgrade context** beyond pinned **0.13.3** (from upstream releases):
- **Security (0.13.7 / 0.13.8):** multiple advisories — **regex-validation bypass**, forbidden label/annotation enforcement gaps, hostname/NodeMetadata regex validation, and an **incomplete fix for CVE-2026-22872**. Move to **0.13.8+** for the tenant-isolation hardening.
- **0.13.9 requires Kubernetes v1.35+** — watch the K8s floor when upgrading Capsule.

## Older-version CVEs & security history (mined 2026-07-19)

For clusters on an **older** Capsule, the tenant-isolation fixes landed in **0.13.7 / 0.13.8** (see the upgrade section): **regex-validation bypass**, forbidden label/annotation enforcement gaps, hostname/NodeMetadata regex validation, and an **incomplete fix for CVE-2026-22872**. Anything **below 0.13.7** has weaker tenant-boundary enforcement — a real concern for a multi-tenancy operator. Move to **0.13.8+**.

## Guides & how-to (official)

- **Docs/upgrade:** https://projectcapsule.dev/docs/ (install + upgrade) ; **Artifact Hub chart:** capsule
- **How to upgrade:** `helm upgrade projectcapsule/capsule`; review the chart README's major-changes notes per version; ensure **Kubernetes ≥1.35** for recent releases. Move to **≥0.13.8** for the tenant-isolation security fixes.
## References

- v0.13.0 release notes, installation/support policy, security advisories (above);
  upgrade issue projectcapsule/capsule#438.
- Catalog: [[CONCEPT-ADDON_CATALOG]].
