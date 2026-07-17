---
id: CONCEPT-ADDON_SPEGEL
type: concept
title: "Spegel (P2P registry mirror) — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "0.0.1"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - spegel
  - registry mirror
  - p2p image mirror
tags:
  - addons
  - registry
  - containerd
  - spegel
sources:
  - type: code
    path: charts/spegel/Chart.yaml
    url: https://raw.githubusercontent.com/spegel-org/spegel/v0.0.1/charts/spegel/Chart.yaml
    note: "no kubeVersion; chart==app v0.0.1 (lockstep)"
  - type: docs
    path: spegel getting-started
    url: https://spegel.dev/docs/getting-started/
    note: "containerd requirements (certs.d, discard_unpacked_layers=false)"
relations:
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
---

# Spegel (P2P registry mirror) — addon

## Summary

Spegel is a stateless peer-to-peer OCI **registry mirror** for containerd — nodes pull images
from each other, reducing registry load and speeding pulls. Chart/app **v0.0.1** (chart and
app are lock-stepped; v0.0.1 is the first release / CI placeholder — current upstream is
0.7.x). It gates on **containerd**, not the Kubernetes version.

## Context

- Class: upstream addon; catalog row in [[CONCEPT-ADDON_CATALOG]] (in-house packaging).

## Implementation

- Chart==app **v0.0.1**. Chart `kubeVersion`: **none**. Runs across 1.29–1.35 if the
  containerd requirements are met.

## Configuration

- **containerd requirements:** `config_path = "/etc/containerd/certs.d"` must be set;
  `discard_unpacked_layers = false` is required; a containerd restart is needed (Spegel does
  not write the config itself). On GKE, containerd config must be applied manually.

## Compatibility

- **Kubernetes range:** unconstrained by K8s (gates on containerd) — works across 1.29–1.35
  with a compatible containerd.
- **containerd version:** current Spegel dropped containerd 1.7/2.0 support (effectively
  needs **containerd 2.1+**, PR #1168) — but the pinned **v0.0.1** predates that and targets
  older containerd; verify against the actual deployed image.
- **Known issues:** mirrors not used on **EKS 1.34 + containerd 2.1** (transfer service
  bypasses `hosts.toml`, #1272); GKE manual config; requires `certs.d` +
  `discard_unpacked_layers=false` set manually.
- **CVEs:** none found (OSV clean for spegel-org/spegel and legacy xenitab/spegel).

## References

- `Chart.yaml` (v0.0.1), spegel getting-started, PR #1168, issue #1272 (above).
- Catalog: [[CONCEPT-ADDON_CATALOG]].
