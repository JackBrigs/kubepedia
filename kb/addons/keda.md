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

## Upstream issues & upgrade notes (mined 2026-07-19)

**Future upgrade context** beyond the shipped **2.17.2** — breaking changes to plan for if/when the
pin moves (from upstream releases):

- **⚠ 2.20.0 silent-breakage (critical):** KEDA Events **moved to the `events.k8s.io` API group** —
  **grant the operator `create`/`patch` on events *before* upgrading**, or event emission breaks.
- **2.18.0 breaking:** CPU/Memory scaler `type` **removed** → use `metricType`; IBM MQ `tls` **removed**
  → use `unsafeSsl`; Prometheus webhook `prommetrics` deprecations removed.
- **2.19.0 breaking:** **NATS Streaming Server** scaler support removed.
- **2.20.0 breaking:** GCP PubSub `subscriptionSize` removed; Huawei Cloudeye `minMetricValue` removed;
  InfluxDB `authToken` in triggerMetadata removed; IBM MQ `tls` code removed.
- **Security:** CVE-2025-68476 fixed in **2.17.3** (and 2.18.3) — the shipped 2.17.2 is affected.
- **Fixed-in-newer bugs of note:** paused-replicas annotation races / `nil` panic (2.18.2); concurrent
  map race causing panics on simultaneous triggers (2.20.1).

**Open upstream bugs (as of 2026-07-19)** — live, unpinned; relevant while on 2.17.x:

- **metrics adapter TCP-connection leak** (#3387) — the metric server accumulates unclosed TCP
  connections until it hits system limits (watch fd usage on the operator).
- **paused annotation not honored** — a `ScaledObject` created with the `paused` annotation reverts to
  paused after resume (#6421); cron-scaled objects can't be un-suspended (#4044).
- **Secrets Store CSI timing** (#2315) — KEDA won't scale if the referenced Secret doesn't exist yet
  (created lazily by the CSI driver).
- **Kafka scaler:** unsynchronized shared CertPool causes panics / spurious x509 failures (#7910);
  invalid negative metrics on GKE (#5730).

## Older-version CVEs & security history (mined 2026-07-19)

For clusters on an **older** KEDA: the shipped **2.17.2 is affected by CVE-2025-68476** (Vault-credential path-traversal arbitrary-file-read, High ~CVSS 8.2, all <2.17.3), fixed **2.17.3 / 2.18.3** — upgrade off 2.17.2 and any earlier 2.17.x. Also GHSA-w92x-gx4w-j5f2 (CI supply-chain, non-runtime). Older KEDA carries the metrics-adapter and scaler bugs later fixed (paused-annotation races 2.18.2, concurrent-map panic 2.20.1).

## References

- `Chart.yaml`, KEDA 2.17 cluster docs, advisory GHSA-c4p6-qg4m-9jmr (above); upstream releases
  2.17.3–2.20.1 and open `kedacore/keda` issues (mined 2026-07-19).
- Catalog: [[CONCEPT-ADDON_CATALOG]]; HPA: [[TROUBLE-HPA_NOT_SCALING]]; scaling issues:
  [[TROUBLE-KEDA_SCALEDOBJECT_NOT_SCALING]].
