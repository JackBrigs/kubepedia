---
id: TROUBLE-KCM_ENDPOINTSLICE_CHURN
type: troubleshooting
title: "controller-manager: EndpointSlice churn / stale endpoints"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - endpointslice informer cache out of date
  - stale endpoints nxdomain
  - endpointslice rebalancing loop
  - endpoints notReadyAddresses stuck
tags:
  - troubleshooting
  - controller-manager
  - endpointslice
  - networking
sources:
  - type: docs
    path: EndpointSlice churn issue (1.30)
    url: https://github.com/kubernetes/kubernetes/issues/133474
    note: "informer cache out of date; rebalancing loop"
  - type: docs
    path: Endpoints controller stale (1.31)
    url: https://github.com/kubernetes/kubernetes/issues/127429
    note: "podEndpointsChanged ignores resync; notReadyAddresses"
relations:
  - type: see_also
    target: TROUBLE-SERVICE_NO_ENDPOINTS
  - type: see_also
    target: CONCEPT-TROUBLESHOOTING_MAP
---

# controller-manager: EndpointSlice churn / stale endpoints

## Summary

For large Services, the EndpointSlice/Endpoints controllers can **churn** — shuffling
endpoints between slices though pods are stable — leaving **stale endpoints** that cause
intermittent NXDOMAIN and stale kube-proxy rules.

## Problem

- Warning `EndpointSlice informer cache is out of date`; endpoints rebalanced between slices
  with no pod change; CoreDNS returns NXDOMAIN intermittently.
- Recovered pods stuck under `notReadyAddresses`; Endpoints controller logs `the object has been
  modified; please apply your changes to the latest version and try again`.

## Context

- Applies to Kubernetes **1.29–1.35**, worse for Services above the **100-endpoints-per-slice**
  threshold. Distinct from "no endpoints at all" ([[TROUBLE-SERVICE_NO_ENDPOINTS]]).

## Diagnostics

- **Rebalancing loop:** when a Service exceeds ~100 endpoints per slice, informer/event timing
  gaps trigger a slice-rebalancing loop and stale-cache comparisons (issue #133474). Reduce
  endpoints-per-Service pressure (split Services, use topology/`trafficDistribution` to limit
  fan-out); **restart kube-controller-manager** to reseed the informer caches.
- **Endpoints controller ignoring resync:** `podEndpointsChanged` ignored pod resync events, so
  recovered pods stayed in `notReadyAddresses` (issue #127429) — a kcm restart re-reconciles.
- **Downstream:** stale endpoints leave kube-proxy with stale rules and CoreDNS answering for
  gone pods — check both after the controller recovers.

## Known Issues

- This is load-sensitive — watch the `EndpointSlice informer cache is out of date` warning as an
  early signal under scale.

## References

- kcm issues #133474 (1.30) / #127429 (1.31) (above); no-endpoints case:
  [[TROUBLE-SERVICE_NO_ENDPOINTS]].
