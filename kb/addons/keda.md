---
id: CONCEPT-ADDON_KEDA
type: concept
title: "KEDA (event-driven autoscaling) — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.30 <=1.32"
component_version: "2.17.2"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - keda
  - event driven autoscaling
  - keda 2.17.2
tags:
  - addons
  - autoscaling
  - keda
sources:
  - type: code
    path: keda/Chart.yaml
    url: https://raw.githubusercontent.com/kedacore/charts/v2.17.2/keda/Chart.yaml
    note: "kubeVersion >=v1.23.0-0; appVersion 2.17.2"
  - type: docs
    path: KEDA 2.17 cluster support
    url: https://keda.sh/docs/2.17/operate/cluster/
    note: "tested K8s v1.30–v1.32 (N-2 policy)"
  - type: docs
    path: advisory GHSA-c4p6-qg4m-9jmr
    url: https://github.com/kedacore/keda/security/advisories/GHSA-c4p6-qg4m-9jmr
    note: "CVE-2025-68476, fixed 2.17.3"
relations:
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
  - type: see_also
    target: TROUBLE-HPA_NOT_SCALING
---

# KEDA (event-driven autoscaling) — addon

## Summary

KEDA scales workloads on external event sources (queues, metrics, cron) by driving an HPA.
Chart/app **2.17.2**, officially tested on Kubernetes **v1.30–v1.32** (N-2 policy).
**Security:** 2.17.2 is affected by a Vault-credential path-traversal CVE — upgrade to
**2.17.3+**.

## Context

- Class: upstream addon; catalog row in [[CONCEPT-ADDON_CATALOG]]. It sits on top of the HPA
  machinery — HPA troubleshooting still applies ([[TROUBLE-HPA_NOT_SCALING]]).

## Implementation

- Chart→app: `keda` v2.17.2 → KEDA core 2.17.2.
- Chart `kubeVersion`: **`>=v1.23.0-0`** (looser than the tested range).

## Configuration

- Define `ScaledObject`/`ScaledJob` + `TriggerAuthentication`; misconfigured scalers or
  auth are the common "not scaling" cause.
- KEDA follows an **N-2 Kubernetes support policy** — running beyond the tested 1.30–1.32
  window is unsupported.

## Compatibility

- **Kubernetes range:** tested **v1.30–v1.32**. Within 1.29–1.35 only that band is covered;
  1.29 and 1.33–1.35 are outside the 2.17 tested set.
- **CVE (2.17.2 affected):** **CVE-2025-68476 / GHSA-c4p6-qg4m-9jmr** — arbitrary file read
  via insufficient path validation in HashiCorp Vault ServiceAccount credential handling
  (High, ~CVSS 8.2), affects KEDA <2.17.3, **fixed 2.17.3**. Also GHSA-w92x-gx4w-j5f2 (CI
  supply-chain, not runtime). Upgrade to 2.17.3+.

## References

- `Chart.yaml`, KEDA 2.17 cluster docs, advisory GHSA-c4p6-qg4m-9jmr (above).
- Catalog: [[CONCEPT-ADDON_CATALOG]]; HPA: [[TROUBLE-HPA_NOT_SCALING]].
