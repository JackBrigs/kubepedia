---
id: TROUBLE-PROMETHEUS_TARGET_DOWN
type: troubleshooting
title: "Prometheus targets DOWN on a Kubespray cluster (control-plane / kubelet / etcd)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - prometheus target down
  - cannot scrape controller-manager scheduler
  - kubelet scrape 401 x509
  - etcd metrics down prometheus
  - servicemonitor no metrics
  - connection refused 127.0.0.1 metrics
tags:
  - troubleshooting
  - observability
  - prometheus
  - monitoring
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "hardening sets kube_controller_manager_bind_address / kube_scheduler_bind_address 127.0.0.1 (tag v2.31.0)"
relations:
  - type: see_also
    target: CONCEPT-OBSERVABILITY_STACK
  - type: see_also
    target: PRACTICE-CLUSTER_HARDENING
  - type: see_also
    target: TROUBLE-KUBELET_SERVING_CERT_TLS
---

# Prometheus targets DOWN on a Kubespray cluster (control-plane / kubelet / etcd)

## Summary

After deploying a monitoring stack on a Kubespray cluster, some targets show **DOWN** even
though the cluster is healthy. The usual culprits are **Kubespray-specific**:
controller-manager/scheduler bound to **`127.0.0.1`** (unreachable from a scraping pod on
another node), the **kubelet serving-cert** rejecting the scrape (`x509`), or **etcd
metrics** needing client certs. These aren't monitoring bugs — they're how a hardened
Kubespray control plane is wired.

## Problem

In Prometheus/VM, `up == 0` for `kube-controller-manager`, `kube-scheduler`, `kubelet`,
`etcd`, or `kube-proxy` targets; errors like `connection refused`,
`x509: certificate signed by unknown authority`, or `server returned HTTP 401`.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`.
- Relevant Kubespray wiring: with hardening,
  `kube_controller_manager_bind_address` / `kube_scheduler_bind_address` = **`127.0.0.1`**
  ([[PRACTICE-CLUSTER_HARDENING]]); the kubelet serves metrics over TLS with a
  (default) self-signed cert; etcd metrics are TLS-protected.

## Diagnostics

- **Which target + error:** the Prometheus `Targets` page shows the endpoint and the exact
  scrape error — match it below.
- **From a node/pod:** `curl -sk https://127.0.0.1:10257/metrics` (CM),
  `:10259` (scheduler) — reachable **locally** but not from another node confirms the
  bind-address issue.
- **kubelet:** `curl -sk https://<node>:10250/metrics/cadvisor` — `x509`/`401` shows the
  TLS/authz issue.

## Known Issues

- **CM / scheduler DOWN (`connection refused`)** — they're bound to `127.0.0.1`, so a
  Prometheus pod elsewhere can't reach them. Options: bind them to a routable address
  (`kube_controller_manager_bind_address` / `kube_scheduler_bind_address` = `0.0.0.0` or
  the node IP), or scrape via a node-local sidecar / hostNetwork. Weigh the security
  trade-off ([[PRACTICE-CLUSTER_HARDENING]] hardened them on purpose).
- **kubelet DOWN (`x509`)** — the scrape doesn't trust the self-signed kubelet serving
  cert. Use `insecureSkipVerify` on the ServiceMonitor/scrape, or enable rotated
  cluster-signed serving certs ([[TROUBLE-KUBELET_SERVING_CERT_TLS]]).
- **kubelet DOWN (`401`)** — the scrape needs a bearer token with `nodes/metrics` RBAC;
  the stack's ServiceAccount must have it (kube-prometheus-stack sets this up).
- **etcd DOWN** — etcd metrics require the etcd **client certs**; mount them into the scrape
  config and target the etcd metrics port (see the `etcd_metrics` run-tag).
- **No metrics at all from a ServiceMonitor** — label/namespace selector mismatch, or the
  Prometheus Operator not watching that namespace (`serviceMonitorSelector`).

**Gotchas:**

- Binding CM/scheduler to `0.0.0.0` **undoes a hardening control** — prefer scraping them
  from a node-local context if you must keep them on localhost.
- `kube-proxy` metrics bind is `kube_proxy_metrics_bind_address` — if it's `127.0.0.1` it
  has the same remote-scrape problem.

## References

- Kubespray CM/scheduler bind addresses (`v2.31.0`). Stack overview:
  [[CONCEPT-OBSERVABILITY_STACK]]; kubelet scrape TLS: [[TROUBLE-KUBELET_SERVING_CERT_TLS]];
  hardening: [[PRACTICE-CLUSTER_HARDENING]].
