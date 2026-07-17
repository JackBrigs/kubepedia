---
id: CONCEPT-ADDON_VELERO
type: concept
title: "Velero (addon chart 11.4.0) — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "1.17.1"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - velero addon
  - velero 11.4.0
  - velero 1.17.1
tags:
  - addons
  - backup
  - dr
  - velero
sources:
  - type: code
    path: charts/velero/Chart.yaml
    url: https://raw.githubusercontent.com/vmware-tanzu/helm-charts/velero-11.4.0/charts/velero/Chart.yaml
    note: "kubeVersion >=1.16.0-0; appVersion 1.17.1"
  - type: docs
    path: Velero upgrade-to-1.17
    url: https://velero.io/docs/main/upgrade-to-1.17/
    note: "must be on 1.16.x first; CRD update required"
relations:
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
  - type: see_also
    target: CONCEPT-VELERO
---

# Velero (addon chart 11.4.0) — addon

## Summary

Velero backs up and restores cluster resources and PV data. The owner runs the community
chart **11.4.0** → Velero app **1.17.1** — an independent, newer install than any
Kubespray-managed Velero. Operational backup/restore guidance is in [[CONCEPT-VELERO]].

## Context

- Class: upstream addon; catalog row in [[CONCEPT-ADDON_CATALOG]].

## Implementation

- Chart→app: `velero-11.4.0` → Velero **1.17.1**. Chart `kubeVersion`: **`>=1.16.0-0`**.

## Configuration

- **Upgrade to 1.17 requires being on Velero 1.16.x first** (else do sequential upgrades),
  and a **CRD schema update**: `velero install --crds-only --dry-run -o yaml | kubectl apply
  -f -`. Update the Velero deployment, plugin and node-agent images **together**.
- Restic uploader is legacy — consider the optional `uploader-type` migration restic→kopia.

## Compatibility

- **Kubernetes range:** Velero 1.17 is expected-compatible through "1.18-latest"; explicitly
  **tested on 1.31.7, 1.32.3, 1.33.1, 1.34.0** — covers 1.29–1.35 as expected-compatible with
  explicit test coverage to 1.34.0.
- **Known issues (fixed in 1.17.1 = the prior failure modes):** fake completion notifications
  from repeated PodVolumeRestore updates (#9365); schedule controller queue build-up under
  blocking; VolumeSnapshot-field races in multi-threaded backups; backupPVC wrongly attaching
  to the source node (#9229).
- **CVEs:** none found directly affecting Velero app 1.17.1 (OSV empty). 2025 CVEs seen in
  searches (CVE-2025-1734, -61723, -64756) belong to Go stdlib / other packages in downstream
  FIPS/Wolfi rebuilds (`velero-fips`), not the Velero codebase.

## References

- `Chart.yaml`, upgrade-to-1.17 doc, v1.17.1 release notes (above).
- Catalog: [[CONCEPT-ADDON_CATALOG]]; backup hub: [[CONCEPT-VELERO]].
