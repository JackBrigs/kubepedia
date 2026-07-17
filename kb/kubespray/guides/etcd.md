---
id: PRACTICE-ETCD
type: best_practice
title: etcd deployment types and metrics exposition in Kubespray
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - etcd deployment
tags:
  - etcd
  - metrics
sources:
  - type: docs
    path: docs/operations/etcd.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/operations/etcd.md
    note: "etcd deployment methods and Prometheus metrics exposition"
relations:
  - type: see_also
    target: CONCEPT-ETCD_3_6_CHANGES
  - type: see_also
    target: PRACTICE-ETCD_BACKUP_RESTORE
---

# etcd deployment types and metrics exposition in Kubespray

## Summary
Kubespray can deploy etcd in three ways selected via `etcd_deployment_type`: `host` (default, systemd service), `docker` (containers, only with `container_manager: docker`), and `kubeadm` (experimental static pod on control plane hosts, new deployments only). The doc also covers exposing etcd metrics on a separate HTTP port and wiring them into kube-prometheus-stack.

## Context
Applies when configuring how etcd runs and how its metrics are scraped. The main variable is `etcd_deployment_type`; metrics variables are `etcd_metrics_port`, `etcd_metrics_service_labels`, and `etcd_listen_metrics_urls`. All are set in the inventory (group_vars).

## Implementation
Deployment method — set `etcd_deployment_type`:
- `host` (default): etcd installed as a systemd service.
- `docker`: installs docker on etcd group members and runs etcd in containers; only usable when `container_manager` is set to `docker`.
- `kubeadm`: experimental, new deployments only; deploys etcd as a static pod on control plane hosts.

Metrics on a separate HTTP port:
```yaml
etcd_metrics_port: 2381
```

Create an `etcd-metrics` service and endpoints in the `kube-system` namespace by defining labels:
```yaml
etcd_metrics_service_labels:
  k8s-app: etcd
  app.kubernetes.io/managed-by: Kubespray
  app: kube-prometheus-stack-kube-etcd
  release: kube-prometheus-stack
```
The `app` and `release` labels let kube-prometheus-stack scrape the metrics when installed with release name `kube-prometheus-stack` and Helm values `kubeEtcd.service.enabled: false`. Adjust the `release` label if your Helm release name differs.

Fully override the metrics URLs:
```yaml
etcd_listen_metrics_urls: "http://0.0.0.0:2381"
```
If exposing metrics on specific node IPs in `etcd_listen_metrics_urls`, configure kube-prometheus-stack to scrape those endpoints directly via `kubeEtcd.enabled: true` and an explicit `endpoints:` list of the node IPs.

## References
- docs/operations/etcd.md (tag v2.31.0 1c9add4)
