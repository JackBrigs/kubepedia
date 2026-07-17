---
id: CONCEPT-OBSERVABILITY_STACK
type: concept
title: "Observability stack on a Kubespray cluster (Prometheus / VictoriaMetrics / Grafana)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - monitoring stack kubernetes
  - prometheus grafana alertmanager
  - kube-prometheus-stack
  - victoriametrics kubernetes
  - what to monitor kubernetes
  - node-exporter kube-state-metrics
tags:
  - observability
  - monitoring
  - prometheus
  - ecosystem
sources:
  - type: docs
    path: kube-prometheus-stack / VictoriaMetrics k8s-stack (Helm charts)
    url: https://github.com/prometheus-community/helm-charts
    note: "monitoring is not bundled by Kubespray; deployed via Helm (kube-prometheus-stack or VM stack)"
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "hardening sets CM/scheduler bind_address 127.0.0.1 — affects scraping (tag v2.31.0)"
relations:
  - type: see_also
    target: COMPONENT-METRICS_SERVER
  - type: see_also
    target: TROUBLE-KUBELET_SERVING_CERT_TLS
  - type: see_also
    target: PRACTICE-CLUSTER_HARDENING
---

# Observability stack on a Kubespray cluster (Prometheus / VictoriaMetrics / Grafana)

## Summary

Kubespray does **not** bundle a monitoring stack — you deploy it yourself. The two common
choices are **kube-prometheus-stack** (Prometheus + Alertmanager + Grafana +
kube-state-metrics + node-exporter) and the **VictoriaMetrics** stack (a drop-in
Prometheus-compatible TSDB with better compression/scale). Both scrape the same Kubernetes
targets; the integration work is the same. Note: **metrics-server ≠ monitoring** — it
only feeds HPA/`kubectl top`, not dashboards/alerts.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`. Deploy via Helm (`kube-prometheus-stack` or
  `victoria-metrics-k8s-stack`) — evidence tier is the upstream charts (`verified`).
- Kubespray provides the **cluster** and some metrics endpoints; the stack and its scrape
  config are yours.

## Implementation

**What to scrape (the standard Kubernetes targets):**

- **kube-apiserver** (`/metrics` on `6443`) — request rates, latency, error/APF metrics.
- **etcd** — `etcd_*` metrics; Kubespray exposes them (see the `etcd_metrics` run-tag).
  Critical for cluster health (slow-apply, db size, leader changes).
- **kubelet / cAdvisor** (`10250/metrics`, `/metrics/cadvisor`) — node & container
  resource usage.
- **node-exporter** — host metrics (CPU/mem/disk/network); deployed by the stack.
- **kube-state-metrics** — object state (deployments, pods, PVCs…); deployed by the stack.
- **CoreDNS / kube-proxy / Cilium** — each exposes Prometheus metrics
  (Cilium via `cilium_enable_hubble_metrics` / agent ports — [[CONCEPT-CILIUM_HUBBLE]]).

**Kubespray-specific integration gotchas:**

- **Hardening blocks control-plane scraping.** `PRACTICE-CLUSTER_HARDENING` sets
  `kube_controller_manager_bind_address` and `kube_scheduler_bind_address` to
  **`127.0.0.1`** — Prometheus on another node then can't scrape CM/scheduler `/metrics`.
  Bind them to a reachable address (or scrape locally) if you need those metrics
  ([[PRACTICE-CLUSTER_HARDENING]]).
- **kubelet scrape TLS.** Scraping the kubelet needs to trust its serving cert; the same
  self-signed-vs-rotated issue as metrics-server applies — use insecure-tls or the rotated
  serving cert ([[TROUBLE-KUBELET_SERVING_CERT_TLS]]).
- **etcd scrape** needs the etcd client certs (etcd metrics are TLS-protected); point the
  scrape at the etcd metrics port with the right certs.

## Compatibility

- **Prometheus vs VictoriaMetrics:** VM is Prometheus-remote-write/PromQL compatible and
  usually chosen for long retention / large clusters (less RAM, better compression);
  kube-prometheus-stack is the batteries-included default. Pick one — don't run both
  scraping the same targets.
- **CRDs / version:** the stack ships CRDs (ServiceMonitor/PodMonitor, VMServiceScrape…);
  keep the chart version aligned with your Kubernetes version.
- **Don't confuse layers:** `metrics-server` ([[COMPONENT-METRICS_SERVER]]) is for
  autoscaling; the observability stack is for dashboards/alerting/long-term metrics. They
  coexist.
- **Storage:** Prometheus/VM need a StorageClass for their PVs — ensure one exists
  ([[TROUBLE-PVC_PENDING_NO_STORAGECLASS]]).

## References

- kube-prometheus-stack / VictoriaMetrics k8s-stack charts; Kubespray CM/scheduler bind
  addresses (`v2.31.0`). Autoscaling metrics: [[COMPONENT-METRICS_SERVER]]; scrape TLS:
  [[TROUBLE-KUBELET_SERVING_CERT_TLS]]; hardening: [[PRACTICE-CLUSTER_HARDENING]].
