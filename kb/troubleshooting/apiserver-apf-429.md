---
id: TROUBLE-APISERVER_APF_429
type: troubleshooting
title: "kube-apiserver: HTTP 429 from API Priority & Fairness (APF)"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - apiserver 429 too many requests
  - apf rejected requests
  - server is currently unable to handle the request
  - flowschema prioritylevelconfiguration
tags:
  - troubleshooting
  - apiserver
  - apf
  - control-plane
sources:
  - type: docs
    path: API Priority and Fairness
    url: https://kubernetes.io/docs/concepts/cluster-administration/flow-control/
    note: "FlowSchema → PriorityLevelConfiguration, seats, Reject/Queue"
relations:
  - type: see_also
    target: TROUBLE-APISERVER_MEMORY_LISTS
  - type: see_also
    target: CONCEPT-TROUBLESHOOTING_MAP
---

# kube-apiserver: HTTP 429 from API Priority & Fairness (APF)

## Summary

Clients get **HTTP 429** ("The server is currently unable to handle the request") even though
the apiserver process is up. **APF** (stable since 1.29) is rate-limiting them: one noisy client
or a batch of expensive LISTs fills a priority level's queue and excess requests are rejected.

## Problem

- `429` responses; `kubectl` retries with backoff. Response headers
  `X-Kubernetes-PF-FlowSchema-UID` / `X-Kubernetes-PF-PriorityLevel-UID` identify the mapping.
- Metrics: **`apiserver_flowcontrol_rejected_requests_total`** (per FlowSchema/PriorityLevel),
  `apiserver_flowcontrol_current_inqueue_requests`, `apiserver_flowcontrol_request_wait_duration_seconds`.

## Context

- Applies to Kubernetes **1.29–1.35** (APF stable). (The metric is
  `apiserver_flowcontrol_rejected_requests_total`, not `apf_rejected_requests_total`.)

## Diagnostics

- **How it works:** each request maps via a **FlowSchema** → **PriorityLevelConfiguration**,
  each level has concurrency "seats". Expensive **LISTs occupy multiple seats**; when a level's
  queue is full and `limitResponse.type: Reject`, excess requests get an immediate 429. One
  client can starve a level.
- **Find the offender:** use the rejected-requests metric labels + the PF response headers to
  identify the **user-agent**/FlowSchema being throttled.
- **Isolate it:** give the noisy client a **dedicated low-share** FlowSchema +
  PriorityLevelConfiguration (`assuredConcurrencyShares: 5`, `Reject`) so it can't starve
  system traffic; inspect `kubectl get flowschemas prioritylevelconfigurations`.
- **Add headroom:** raise `--max-requests-inflight` / `--max-mutating-requests-inflight` if the
  apiserver has CPU/mem to spare.

## Known Issues

- Latency inflation alone (slow etcd/admission) makes requests hold seats longer and can trip
  APF cluster-wide — fix the underlying latency ([[TROUBLE-APISERVER_ETCD_LATENCY]]).
- Expensive LISTs are both an APF and a memory problem — [[TROUBLE-APISERVER_MEMORY_LISTS]].

## References

- API Priority & Fairness docs (above). Related: [[TROUBLE-APISERVER_MEMORY_LISTS]],
  [[TROUBLE-APISERVER_ETCD_LATENCY]].
