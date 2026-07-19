---
id: CONCEPT-ADDON_OLM
type: concept
title: "Operator Lifecycle Manager (OLM v0) — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "0.32.0"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - operator-lifecycle-manager
  - olm
  - olm 0.32.0
tags:
  - addons
  - operators
  - olm
sources:
  - type: docs
    path: OLM v0.32.0 release
    url: https://github.com/operator-framework/operator-lifecycle-manager/releases/tag/v0.32.0
    note: "operator-registry v1.55.0, K8s libs 0.32.x, NetworkPolicy support"
relations:
  - type: see_also
    target: TROUBLE-OLM_SUBSCRIPTION
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
---

# Operator Lifecycle Manager (OLM v0) — addon

## Summary

OLM v0 ("classic") manages the install/upgrade lifecycle of operators via
CatalogSource/Subscription/CSV. Release **v0.32.0**. Note: **0.32.0 is an OLM release
version, not a published Helm chart** — OLM v0 is normally installed via release manifests /
`operator-sdk olm install`, so the inventory's "chart 0.32.0" is the release, not a chart.

## Context

- Class: upstream addon (in-house packaging); catalog row in [[CONCEPT-ADDON_CATALOG]].
- OLM v0 is **legacy/maintenance** — its successor is **OLM v1** (operator-controller).

## Implementation

- OLM **0.32.0**; operator-registry **v1.55.0**; controller-runtime 0.20.1; K8s libs ~0.32.2.
- Installed from release manifests, not a versioned chart (the in-repo `deploy/chart` is a
  `0.0.0-dev` template).

## Configuration

- v0.32.0 adds **NetworkPolicy support for catalog sources** — may require network/RBAC
  adjustments on upgrade.
- `go-jose/v4` is pinned to mitigate transitive CVE-2025-27144.

## Compatibility

- **Kubernetes range:** not explicitly stated in the v0.32.0 notes (**unverified**); the K8s
  client/apiextensions deps at 0.32.x indicate alignment with **K8s 1.32-era** APIs. Assumed
  workable across 1.29–1.35.
- **Breaking changes:** none documented in v0.32.0; ecosystem-level, plan the eventual move
  to OLM v1.
- **CVEs:** none found in OLM itself (OSV empty); only transitive CVE-2025-27144, mitigated
  by the dependency pin.

## Upstream issues & upgrade notes (mined 2026-07-19)

**Future upgrade context** beyond pinned **0.32.0** (OLM v0, from upstream releases):
- **0.41.0:** Go bumped to resolve **CVE-2025-68121**; metrics moved to EndpointSlices.
- **0.42.0:** **blocks upgrades from 4.23 → 5.0**; fixes a nil-pointer in `sortUnpackJobs`; klog v1→v2.
- 0.43.0 improves **bundle-unpack failure handling** (relevant to the stuck-Subscription/CSV class in the troubleshooting doc).

## Older-version CVEs & security history (mined 2026-07-19)

OLM v0 publishes few code-specific CVEs; the notable older-version item is **CVE-2025-68121** (Go stdlib), pulled in by the **0.41.0** Go bump — older OLM images below 0.41 carry it and other transitive dependency CVEs. Practical action for older clusters: upgrade the OLM image to pick up the dependency fixes; the operator-registry/bundle-unpack path also hardened over 0.42–0.43.

## Guides & how-to (official)

- **Docs:** https://olm.operatorframework.io/docs/ ; **install/upgrade:** https://olm.operatorframework.io/docs/getting-started/
- **How to upgrade OLM v0:** apply the release manifests (`crds.yaml` then `olm.yaml`) for the target version, or `operator-sdk olm install --version <x>`; note **0.42 blocks 4.23→5.0 API upgrades**. (Operator installs themselves flow via Subscription/InstallPlan/CSV.)
## References

- OLM v0.32.0 release notes (above); OLM v1 successor (operator-controller).
- Catalog: [[CONCEPT-ADDON_CATALOG]].
