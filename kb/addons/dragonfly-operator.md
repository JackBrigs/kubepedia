---
id: CONCEPT-ADDON_DRAGONFLY
type: concept
title: "Dragonfly Operator — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "1.28.1"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - dragonfly
  - dragonfly-operator
  - dragonflydb
tags:
  - addons
  - data
  - cache
  - dragonfly
sources:
  - type: code
    path: charts/dragonfly-operator/Chart.yaml
    url: https://raw.githubusercontent.com/dragonflydb/dragonfly-operator/v1.1.11/charts/dragonfly-operator/Chart.yaml
    note: "no kubeVersion; operator v1.1.11"
  - type: code
    path: internal/resources/version.go
    url: https://raw.githubusercontent.com/dragonflydb/dragonfly-operator/v1.1.11/internal/resources/version.go
    note: "default datastore Dragonfly v1.28.1"
relations:
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
---

# Dragonfly Operator — addon

## Summary

The DragonflyDB operator (**v1.1.11**) manages Dragonfly (a Redis/Memcached-compatible
in-memory store) instances. It defaults the datastore to **Dragonfly v1.28.1** — which is
affected by **three CVEs**; override `spec.image` to ≥1.40 to clear them.

## Context

- Class: upstream addon; catalog row in [[CONCEPT-ADDON_CATALOG]] (local chart).

## Implementation

- Operator **v1.1.11** → default datastore **Dragonfly v1.28.1** (independent of the operator
  version; overridable via `spec.image`). Chart `kubeVersion`: **none** (docs mention a soft
  historical 1.19+ floor, not chart-enforced).

## Configuration

- **Pin `spec.image`** — on operator upgrade, pods without an explicit image roll to the
  operator's default datastore version (and into CVE exposure).
- Apply/upgrade CRDs before the controller (chart CRD alignment, PR #304).

## Compatibility

- **Kubernetes range:** no explicit tested upper bound for v1.1.11 (**unverified** but
  unconstrained across 1.29–1.35).
- **CVEs (default datastore v1.28.1 is affected by all three — override to ≥1.40):**
  CVE-2026-62357 / GHSA-cmmv-h748-v93x (`CMS.INITBYDIM` heap OOB write, <1.40);
  CVE-2026-54341 / GHSA-cwjr-j869-h8q9 (`RESTORE` crash, <1.39);
  CVE-2026-47206 / GHSA-h77h-c6hc-qc9h (RESP injection via Lua, <1.38.9). Operator: none found.
- **Known issues:** failover can cause data loss / non-zero downtime (#289, #275); master
  doesn't switch on node failure (#302, #250); replication reconcile stuck after OOMKill
  (#348).

## Upstream issues & upgrade notes (mined 2026-07-19)

**Future upgrade context** (Dragonfly **operator** releases; the pinned version tracks the DB, operator is on the 1.x line):
- **1.5.0:** adds a **replication-aware readiness gate to prevent data loss** on failover, PDB customization, and network policies restricting the admin port — worth enabling.
- 1.6.0: better replica management during rolling updates; snapshot-schedule handling.

**Open upstream bugs (as of 2026-07-19):** **master-failover handling** — clients aren't disconnected when a pod loses master, so they keep talking to a stale master (#238/#324); **NetworkPolicy blocks metrics scraping** from external pods (#495); no headless service for mesh integration (#225).

## Older-version CVEs & security history (mined 2026-07-19)

The Dragonfly DB GitHub advisories endpoint was not retrievable in this pass (rate-limited). Check the **Dragonfly project security page / releases** for version-specific CVEs before running an older image; historically the operator's data-loss risks (failover/readiness) have been the bigger operational concern than code CVEs — the **replication-aware readiness gate** (operator 1.5.0) is the key mitigation.

## References

- `Chart.yaml`, `version.go`, Dragonfly security advisories (above).
- Catalog: [[CONCEPT-ADDON_CATALOG]].
