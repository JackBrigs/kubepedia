---
id: CONCEPT-ADDON_VECTOR_OPERATOR
type: concept
title: "vector-operator (kaasops) — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.28 <=1.31"
component_version: "0.3.3"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - vector-operator
  - kaasops vector
  - vector logs operator
tags:
  - addons
  - observability
  - logging
  - vector
sources:
  - type: code
    path: helm/charts/vector-operator/Chart.yaml
    url: https://raw.githubusercontent.com/kaasops/vector-operator/v0.3.3/helm/charts/vector-operator/Chart.yaml
    note: "chart 0.7.2 published from git tag v0.3.3; no kubeVersion"
  - type: code
    path: go.mod
    url: https://raw.githubusercontent.com/kaasops/vector-operator/v0.3.3/go.mod
    note: "k8s.io/api v0.31.0, controller-runtime v0.19.0, Go 1.22"
relations:
  - type: see_also
    target: TROUBLE-VECTOR_OPERATOR
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
---

# vector-operator (kaasops) — addon

## Summary

The kaasops **vector-operator**, chart **0.7.2** → operator app **v0.3.3**, manages Vector
log pipelines via CRDs. It does **not** ship a fixed Vector version — the managed Vector
image is user-supplied through the CRD.

## Context

- Class: upstream addon; catalog row in [[CONCEPT-ADDON_CATALOG]].
- **Version-mapping caveat:** chart 0.7.2 = operator **v0.3.3** (published from that git
  tag), not a bundled Vector version.

## Implementation

- Chart→app: `vector-operator` chart 0.7.2 → operator **v0.3.3**. Operator image tag is
  pinned to `Chart.AppVersion` unless overridden.
- Chart `kubeVersion`: **none** (field absent).
- v0.3.3 is a single bugfix: propagate `volumes`/`volumeMounts` to the configcheck pod
  (PR #203). Dual-stack, a configcheck memory-leak fix and buffered event channels arrived
  only in operator **v0.4.0 / chart 0.8.0** — NOT in 0.7.2.

## Configuration

- Supply the Vector image explicitly in the CRD (e.g. `timberio/vector:<ver>-distroless`);
  the chart ships only a commented example.
- Ensure any `volumes`/`volumeMounts` needed by config validation are set — the exact defect
  fixed in v0.3.3 was configcheck pods missing them.

## Compatibility

- **Kubernetes range:** no upstream matrix (**unverified**). Indicator: operator builds
  against `k8s.io/api v0.31.0` / controller-runtime v0.19.0, which validates against K8s
  **1.28–1.31** — treat that as the practical tested band; higher minors (1.32–1.35) are
  unverified.
- **CVEs:** none found (OSV empty for `github.com/kaasops/vector-operator`).

## Upstream issues & upgrade notes (mined 2026-07-19)

**Future upgrade context** beyond pinned **0.3.3** (from upstream releases): actively maintained (releases every 1–2 months); latest **0.4.1**. **0.4.0** adds **dual-stack** support and a testing framework; **no breaking changes** in the 0.3→0.4 line. Newer versions may widen the older 1.28–1.31 K8s window — verify before adopting on 1.32+.

## Older-version CVEs & security history (mined 2026-07-19)

The kaasops vector-operator is a small project with no notable CVE record; older-version exposure is the **user-supplied Vector image** (Vector's own CVEs) and base images. Since the Vector version is set via the CRD, patch **Vector** independently of the operator; the operator itself is low-CVE-surface.

## Guides & how-to (official)

- **Docs/repo:** https://github.com/kaasops/vector-operator (see `docs/`, quick-start)
- **How to upgrade:** `helm upgrade` the chart; CRDs backward-compatible 0.3→0.4 (no breaking). The **Vector image is user-supplied via the CRD** — upgrade Vector independently of the operator.
## References

- `Chart.yaml`, `go.mod`, release v0.3.3 / PR #203 (above).
- Catalog: [[CONCEPT-ADDON_CATALOG]].
