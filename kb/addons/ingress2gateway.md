---
id: CONCEPT-ADDON_INGRESS2GATEWAY
type: concept
title: "ingress2gateway — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: probable
aliases:
  - ingress2gateway
  - ingress to gateway api
tags:
  - addons
  - networking
  - gateway-api
  - migration
sources:
  - type: docs
    path: kubernetes-sigs/ingress2gateway
    url: https://github.com/kubernetes-sigs/ingress2gateway
    note: "CLI conversion tool Ingress→Gateway API; upstream ships no Helm chart"
relations:
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
  - type: see_also
    target: CONCEPT-ADDON_ENVOY_GATEWAY
---

# ingress2gateway — addon

## Summary

`ingress2gateway` is a **CLI conversion tool** (kubernetes-sigs) that translates Ingress and
provider-specific resources into Gateway API objects. It is **not a controller** and runs as
a one-shot. It is a common migration path off ingress-nginx toward Gateway API
([[CONCEPT-ADDON_ENVOY_GATEWAY]]).

## Context

- Class: upstream tool; catalog row in [[CONCEPT-ADDON_CATALOG]].
- **Chart caveat:** the inventory's chart **`0.0.6` could not be located** upstream —
  kubernetes-sigs ships **no Helm chart**, and 0.0.6 is not on Artifact Hub. It is likely a
  private/community wrapper (probably running the CLI as a Job). Confirm the exact source
  repo with whoever pinned it; `component_version`/behaviour here are **`probable`**.

## Implementation

- Upstream is a CLI/Job, not a long-running deployment; compatibility is governed by the
  **emitted Gateway API version**, not a server range.
- Reference upstream tool releases: v0.4.0 (2025-03), v0.5.0 (2026-01), v1.0.0 (2026-03),
  v1.2.0 (2026-07).

## Configuration

- Run against the target cluster's Ingress set; review the generated Gateway/HTTPRoute
  objects before applying — conversion is best-effort per provider.

## Compatibility

- **Kubernetes range:** driven by the Gateway API CRDs installed, not the tool
  (**unverified** for the 0.0.6 wrapper).
- **CVEs:** none found for kubernetes-sigs/ingress2gateway (it is cited as a migration path
  away from ingress-nginx CVEs, not itself a vulnerable runtime component).

## References

- kubernetes-sigs/ingress2gateway (above).
- Catalog: [[CONCEPT-ADDON_CATALOG]]; target gateway: [[CONCEPT-ADDON_ENVOY_GATEWAY]].
