---
id: PRACTICE-MONITORING_BASELINE
type: best_practice
title: "Monitoring baseline — what to watch (Prometheus not bundled)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - what to monitor kubernetes
  - kubespray no prometheus bundled
  - control plane monitoring baseline
  - etcd apiserver metrics to watch
tags:
  - best-practice
  - monitoring
  - observability
  - kubespray
sources:
  - type: docs
    path: Kubernetes system metrics
    url: https://kubernetes.io/docs/reference/instrumentation/metrics/
    note: "apiserver/etcd/kubelet/scheduler metrics"
relations:
  - type: see_also
    target: CONCEPT-OBSERVABILITY_STACK
  - type: see_also
    target: TROUBLE-APISERVER_APF_429
  - type: see_also
    target: TROUBLE-ETCD_DB_SPACE_EXCEEDED
---

# Monitoring baseline — what to watch (Prometheus not bundled)

## Summary

**Kubespray does not bundle Prometheus/Grafana** — you bring your own stack (kube-prometheus,
VictoriaMetrics — [[CONCEPT-OBSERVABILITY_STACK]]). This is the **minimum signal set** to watch
so the failure modes elsewhere in this base are caught early instead of as outages.

## Context

- Applies to Kubespray **v2.29.0–v2.31.0** / Kubernetes **1.29–1.35**. Kubespray exposes an
  optional `prometheus_operator_crds`, but the actual monitoring stack is the operator's job.

## Implementation

Watch (with alerts) at least:

- **etcd (the #1 thing):** `etcd_disk_wal_fsync_duration_seconds` /
  `_backend_commit_duration_seconds` (p99 <10 ms), `etcd_server_has_leader`,
  `apiserver_storage_db_total_size_in_bytes` / DB size vs quota, leader changes
  ([[TROUBLE-ETCD_DB_SPACE_EXCEEDED]], [[TROUBLE-APISERVER_ETCD_LATENCY]]).
- **kube-apiserver:** request latency & error rate, **`apiserver_flowcontrol_rejected_requests_total`**
  (APF 429 — [[TROUBLE-APISERVER_APF_429]]), memory/OOM, `apiserver_admission_webhook_admission_duration_seconds`.
- **Nodes/kubelet:** node `Ready`, `NotReady` count, DiskPressure/MemoryPressure, kubelet
  `process_resident_memory_bytes` (leak — [[TROUBLE-KUBELET_MEMORY_OOM]]), PLEG relist duration.
- **Scheduler/controller-manager:** `scheduler_pending_pods`, leader-election flaps
  ([[TROUBLE-CONTROL_PLANE_LEADER_ELECTION]]).
- **Certs:** control-plane cert expiry (`kubeadm certs check-expiration` / a cert-expiry exporter)
  — [[TROUBLE-KUBEADM_CERT_RENEWAL]].
- **Capacity:** CPU/mem requests vs allocatable per node, PV usage, image/disk on nodes.

**Principles:** alert on **symptoms users feel** (API latency, pending pods, node NotReady) plus
the **leading indicators** above (etcd fsync, cert expiry, disk) so you act before the outage.
Scrape the control-plane component `/metrics` (they're on by default) and node-exporter.

## References

- Kubernetes metrics reference (above); stack: [[CONCEPT-OBSERVABILITY_STACK]]; APF:
  [[TROUBLE-APISERVER_APF_429]]; etcd: [[TROUBLE-ETCD_DB_SPACE_EXCEEDED]].
