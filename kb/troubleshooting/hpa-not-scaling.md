---
id: TROUBLE-HPA_NOT_SCALING
type: troubleshooting
title: "HorizontalPodAutoscaler not scaling (unknown / metrics unavailable)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - hpa not scaling
  - hpa unknown targets
  - metrics not available yet
  - FailedGetResourceMetric
  - missing request for cpu hpa
  - metrics api not available
tags:
  - troubleshooting
  - autoscaling
  - hpa
  - metrics
sources:
  - type: docs
    path: Kubernetes HorizontalPodAutoscaler
    url: https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/
    note: "HPA needs the metrics API and pod resource requests to compute utilization"
relations:
  - type: see_also
    target: TROUBLE-KUBELET_SERVING_CERT_TLS
  - type: see_also
    target: COMPONENT-METRICS_SERVER
  - type: see_also
    target: CONCEPT-TROUBLESHOOTING_MAP
---

# HorizontalPodAutoscaler not scaling (unknown / metrics unavailable)

## Summary

An HPA scales only if it can **read metrics** and **compute utilization**. When it shows
`TARGETS: <unknown>` or doesn't react to load, it's almost always: **metrics-server
missing/unhealthy** (no metrics API), the **kubelet serving cert** blocking scraping, or
the target pods have **no CPU/memory `requests`** (so % utilization is undefined).

## Problem

`kubectl get hpa` shows `TARGETS: <unknown>/50%` and `REPLICAS` not changing;
`kubectl describe hpa` shows `FailedGetResourceMetric` / `unable to get metrics` /
`missing request for cpu`.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`. CPU/memory HPAs use the **metrics.k8s.io** API
  served by **metrics-server** (`metrics_server_enabled`, off by default —
  [[COMPONENT-METRICS_SERVER]]).
- HPA utilization = usage ÷ **request**; without a request there's no denominator.

## Diagnostics

- **`kubectl describe hpa <name>`** — the Conditions/Events name the cause
  (`FailedGetResourceMetric`, `missing request for cpu`, `AbleToScale=False`).
- **Metrics API up?** `kubectl top pods` / `kubectl top nodes` — if these fail, the whole
  metrics pipeline is down, not just the HPA.
- **metrics-server health:** `kubectl -n kube-system get pods -l k8s-app=metrics-server`
  and its logs — `x509` there means it can't scrape the kubelet
  ([[TROUBLE-KUBELET_SERVING_CERT_TLS]]).
- **Requests set?** `kubectl get deploy <t> -o jsonpath='{..resources.requests}'` — a
  CPU/memory HPA needs the matching request on the pods.

## Known Issues

Map the cause to its fix:

- **metrics-server not installed** — enable it (`metrics_server_enabled: true`); no
  metrics API → every resource-metric HPA is `<unknown>`.
- **metrics-server can't scrape kubelet (`x509`)** — the classic Kubespray default: kubelet
  serving cert is self-signed and metrics-server needs `--kubelet-insecure-tls`
  (`metrics_server_kubelet_insecure_tls: true`, the default) or a rotated serving cert
  ([[TROUBLE-KUBELET_SERVING_CERT_TLS]]).
- **`missing request for cpu`/`memory`** — add `resources.requests` for the metric the HPA
  targets; utilization can't be computed without it.
- **Custom/external metrics** — `object`/`external` metric HPAs need a custom-metrics
  adapter (Prometheus Adapter, KEDA); metrics-server only serves CPU/memory.
- **Scaling but slow/flapping** — check `behavior` (stabilization windows) and the HPA sync
  period; brief `<unknown>` right after deploy (metrics not collected yet) is normal.

**Gotchas:**

- **`kubectl top` failing == HPA will fail** — fix the metrics pipeline first; the HPA is
  downstream.
- metrics-server serves **only** resource (CPU/memory) metrics — QPS/queue-length scaling
  needs a separate adapter, not metrics-server.
- A too-low `minReplicas`/`maxReplicas` or a maxed-out cluster (pods `Pending`,
  unschedulable) looks like "not scaling" but is a capacity problem
  ([[TROUBLE-POD_PENDING_UNSCHEDULABLE]]).

## References

- Kubernetes HPA task. metrics-server: [[COMPONENT-METRICS_SERVER]]; scrape TLS:
  [[TROUBLE-KUBELET_SERVING_CERT_TLS]]; capacity: [[TROUBLE-POD_PENDING_UNSCHEDULABLE]].
