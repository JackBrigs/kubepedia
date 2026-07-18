---
id: CONCEPT-TALOS_CLUSTER_API
type: concept
title: "Talos + Cluster API (CAPI) — CABPT, CACPPT, Sidero Metal providers"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "1.13.6"
verified_at: "2026-07-18"
confidence: verified
aliases:
  - talos cluster api
  - CABPT bootstrap provider talos
  - CACPPT control plane provider talos
  - sidero metal capi
  - talos capi providers
  - declarative talos clusters
tags:
  - talos
  - cluster-api
  - provisioning
sources:
  - type: docs
    path: public/talos/v1.13/getting-started/support-matrix.mdx
    url: https://github.com/siderolabs/docs/blob/main/public/talos/v1.13/getting-started/support-matrix.mdx
    note: "CABPT / CACPPT / Sidero provider min versions per Talos minor (siderolabs/docs @59a5195)"
relations:
  - type: see_also
    target: CONCEPT-TALOS_K8S_MATRIX
  - type: see_also
    target: CONCEPT-TALOS_OMNI
  - type: see_also
    target: CONCEPT-TALOS_PROVISIONING
---

# Talos + Cluster API (CAPI) — CABPT, CACPPT, Sidero Metal providers

## Summary

Talos clusters can be managed **declaratively via Cluster API (CAPI)**: you install three Talos-specific
providers into a CAPI management cluster and then declare Talos+Kubernetes clusters as CAPI resources.
The providers are **CABPT** (bootstrap), **CACPPT** (control-plane), and **Sidero Metal** (bare-metal
infrastructure). Their versions **must track the Talos minor** ([[CONCEPT-TALOS_K8S_MATRIX]]).

## Context

**The three providers:**

- **CABPT — Cluster API Bootstrap Provider Talos** (`siderolabs/cluster-api-bootstrap-provider-talos`):
  generates the Talos **machine bootstrap config** so a CAPI `Machine` comes up as a Talos node.
  Infra-agnostic.
- **CACPPT — Cluster API Control Plane Provider Talos**
  (`siderolabs/cluster-api-control-plane-provider-talos`): manages the Talos **control-plane** lifecycle
  (declarative HA control plane via `TalosControlPlane`). Infra-agnostic.
- **Sidero / Sidero Metal** (`sidero.dev`): the **bare-metal infrastructure** provider — turns physical
  servers (PXE-booted) into CAPI-managed Talos machines.

**Version pairing** (min provider versions per Talos minor — [[CONCEPT-TALOS_K8S_MATRIX]]):

| Talos | CABPT | CACPPT | Sidero |
|-------|-------|--------|--------|
| 1.13 | ≥ 0.6.12 | ≥ 0.5.13 | ≥ 0.6.13 |
| 1.12 | ≥ 0.6.11 | ≥ 0.5.12 | ≥ 0.6.12 |
| 1.11 | ≥ 0.6.8 | ≥ 0.5.9 | *(unverified)* |

**Model:** with the providers installed, a Talos cluster is a set of CAPI objects — `Cluster` + an
infra provider + `TalosControlPlane` (CACPPT) + `TalosConfig`/bootstrap (CABPT); the management cluster
reconciles them into running Talos+K8s clusters. Bootstrap/control-plane are infra-agnostic; **Sidero
Metal** is the bare-metal layer.

**Successor note.** In the modern Sidero Labs stack, **Omni's bare-metal infrastructure provider**
(`omni-infra-provider-bare-metal`) is positioned as the replacement for the manual Sidero-Metal model
for new bare-metal provisioning ([[CONCEPT-TALOS_OMNI]]); CAPI-via-Sidero remains a separately
versioned path. There is **no standalone CAPI walkthrough** in the current Talos docs — details beyond
provider identity/versions live in the external provider repos.

## References

- `siderolabs/docs` `public/talos/v1.13/getting-started/support-matrix.mdx` (@59a5195); provider repos
  `siderolabs/cluster-api-{bootstrap,control-plane}-provider-talos`, `sidero.dev`. Matrix
  [[CONCEPT-TALOS_K8S_MATRIX]]; Omni [[CONCEPT-TALOS_OMNI]]; provisioning [[CONCEPT-TALOS_PROVISIONING]].
