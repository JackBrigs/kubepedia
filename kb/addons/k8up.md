---
id: CONCEPT-ADDON_K8UP
type: concept
title: "K8up (restic backup operator) — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.22 <=1.35"
component_version: "2.12.0"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - k8up
  - k8up backup
  - restic operator
tags:
  - addons
  - storage
  - backup
  - restic
sources:
  - type: code
    path: k8up-4.8.4 chart tarball
    url: https://github.com/k8up-io/k8up/releases/download/k8up-4.8.4/k8up-4.8.4.tgz
    note: "chart 4.8.4, no kubeVersion/appVersion; operator image default v2.12.0"
  - type: docs
    path: k8up v2.12.0 release
    url: https://github.com/k8up-io/k8up/releases/tag/v2.12.0
    note: "labelSelector filtering; no breaking changes"
relations:
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
---

# K8up (restic backup operator) — addon

## Summary

K8up is a restic-based backup operator (`Backup`/`Schedule`/`Restore`/`Archive` CRDs). Chart
**4.8.4** deploys operator app **v2.12.0**. **Version note:** the chart declares no
`appVersion`; the operator image default in `values.yaml` is **v2.12.0**.

## Context

- Class: upstream addon; catalog row (+ `k8upcrd 0.1.0`) in [[CONCEPT-ADDON_CATALOG]].

## Implementation

- Chart 4.8.4 → operator **v2.12.0**. Chart `kubeVersion`: **none**. CRDs use
  `apiextensions.k8s.io/v1` → effectively K8s 1.22+.
- v2.12.0 adds PVC/preBackupPod filtering via `labelSelectors`, restic exclude/files-from via
  PVC annotations, and a `clusterName` label. No breaking changes declared.

## Configuration

- **The chart does NOT install CRDs** — `NOTES.txt` warns you must install/upgrade K8up CRDs
  separately (the primary upgrade gotcha; the `k8upcrd` chart in the inventory covers this).
- Provide a restic repository (S3/etc.) and encryption password secret.

## Compatibility

- **Kubernetes range:** upstream says 1.16+, but `apiextensions/v1` CRDs → effectively
  **1.22+**; no tested upper bound (1.29–1.35 **unverified** but expected).
- **Known issues:** forgetting the separate CRD install/upgrade; restic stale repo locks
  after interrupted jobs need manual unlock; prune/check jobs are resource-intensive.
- **CVEs:** none found for `k8up-io/k8up` at v2.12.0 (OSV empty).

## Upstream issues & upgrade notes (mined 2026-07-19)

**Future upgrade context** beyond pinned **2.12.0** (from upstream releases):
- **⚠ 2.15.0 breaking:** switched pod-exec streaming from **SPDY → websockets** (system-requirement change). **Upgrade note:** if application-aware backups fail after the upgrade, set **`INSECURE_ALLOW_PODEXEC_SPDY_FALLBACK`** on the operator.
- 2.16.0 bumps Restic to 0.19.0; 2.14.0 adds restore filtering by snapshot timestamp.

**Open upstream requests/bugs (as of 2026-07-19):** file include/exclude configuration (#317); PVC backups via **CSI snapshots/clones** for atomicity (#918); Helm-managed CRDs (#1050); S3 subpath/prefix support (#615).

## References

- k8up-4.8.4 chart tarball + v2.12.0 release notes (above).
- Catalog: [[CONCEPT-ADDON_CATALOG]].
