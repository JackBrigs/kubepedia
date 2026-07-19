---
id: CONCEPT-ADDON_HEADLAMP
type: concept
title: "Headlamp (Kubernetes UI) — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "0.43.0"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - headlamp
  - kubernetes ui headlamp
tags:
  - addons
  - dashboard
  - ui
sources:
  - type: code
    path: charts/headlamp/Chart.yaml
    url: https://raw.githubusercontent.com/kubernetes-sigs/headlamp/headlamp-helm-0.43.0/charts/headlamp/Chart.yaml
    note: "no kubeVersion; appVersion 0.43.0 (chart tag headlamp-helm-0.43.0)"
relations:
  - type: see_also
    target: TROUBLE-HEADLAMP
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
---

# Headlamp (Kubernetes UI) — addon

## Summary

Headlamp is a CNCF (kubernetes-sigs) web UI for clusters, deployed via chart **0.43.0**
(app 0.43.0). A modern, actively-maintained alternative to the retired kubernetes-dashboard
([[CONCEPT-ADDON_KUBERNETES_DASHBOARD]]).

## Context

- Class: upstream addon; catalog row in [[CONCEPT-ADDON_CATALOG]].
- The correct chart tag is `headlamp-helm-0.43.0` (not `headlamp-0.43.0`).

## Implementation

- Chart→app: `0.43.0` (appVersion matches chart).
- Chart `kubeVersion`: **none** (field absent).

## Configuration

- ServiceAccount-token creation differs on K8s 1.24+ (tokens are no longer auto-created) —
  a procedural note, not a support-range limit.

## Compatibility

- **Kubernetes range:** install docs state no min/max K8s version (**unverified** matrix);
  works across 1.29–1.35.
- **Breaking changes:** none flagged for 0.43.0 (**unverified** beyond release notes).
- **CVEs:** none affecting 0.43.0. Advisory GHSA-34rf-485x-g5h7 (command injection) is in the
  macOS **desktop** build's `codeSign.js` 0.31.0 (patched 0.31.1) — does not affect the
  in-cluster chart 0.43.0.

## References

- `Chart.yaml` (headlamp-helm-0.43.0); advisory GHSA-34rf-485x-g5h7.
- Catalog: [[CONCEPT-ADDON_CATALOG]]; sibling UI: [[CONCEPT-ADDON_KUBERNETES_DASHBOARD]].
