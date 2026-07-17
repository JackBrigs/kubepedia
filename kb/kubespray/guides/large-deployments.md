---
id: PRACTICE-LARGE_DEPLOYMENTS
type: best_practice
title: Tuning Kubespray for Large Deployments
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - large scale kubespray
tags:
  - scaling
  - performance
  - tuning
sources:
  - type: docs
    path: docs/operations/large-deployments.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/operations/large-deployments.md
    note: "Recommended Ansible, download, DNS, resource, reliability, and etcd configuration changes for large clusters"
relations:
  - type: see_also
    target: TROUBLE-INOTIFY_FILE_LIMITS
  - type: see_also
    target: PRACTICE-GRACEFUL_UPGRADE
---

# Tuning Kubespray for Large Deployments

## Summary
When deploying a large-scale Kubernetes cluster with Kubespray, several defaults should be overridden to keep the run reliable and to reduce load on the delegate node. Key levers are Ansible parallelism (`forks`, `timeout`), download once/localhost behavior, retry staggering, DNS and component resource limits, node-monitoring/eviction timeouts, network prefix sizing, and a dedicated etcd events cluster.

## Context
Applies to large clusters (the doc uses a 200-node example). Involves Ansible runtime settings, the download role, the DNS applications, per-role resource defaults, kube-controller-manager / kube-apiserver reliability parameters, network CIDR variables, and the etcd/Calico setup. Many of these variables live in roles' defaults and follow a `foo_*` naming convention.

## Implementation
Recommended changes for large deployments:

- Ansible parallelism: tune `forks` and `timeout` to fit the node count. Example for 200 nodes: run with `--forks=50`, `--timeout=600`, and set `retry_stagger: 60`.
- Registry: override container image repo vars (`foo_image_repo`) to point at an intranet registry.
- Downloads: override `download_run_once: true` and/or `download_localhost: true` (see docs/advanced/downloads.md). Adjust the global `retry_stagger` var so retried push/download operations put a sane load on the delegate (the first control plane node).
- DNS tuning: adjust `dns_replicas`, `dns_cpu_limit`, `dns_cpu_requests`, `dns_memory_limit`, `dns_memory_requests`. Limits must always be >= requests.
- Resource tuning: set per-component `foo_memory_limit`, `foo_memory_requests`, `foo_cpu_limit`, `foo_cpu_requests` in roles' defaults. Note: K8s 'Mi' memory units are submitted as 'M' and cpu 'm' is dropped when applied to `docker run`, because docker does not understand K8s units.
- Reliability: tune `kubelet_status_update_frequency`; and for cluster-level reliability `kube_controller_node_monitor_grace_period`, `kube_controller_node_monitor_period`, `kube_apiserver_pod_eviction_not_ready_timeout_seconds`, `kube_apiserver_pod_eviction_unreachable_timeout_seconds` (see docs/advanced/kubernetes-reliability.md).
- Network sizing: tune `kube_network_node_prefix`, `kube_service_addresses`, and `kube_pods_subnet` to accommodate the node/pod scale.
- Calico/Canal: add `calico_rr` (route reflector) nodes so nodes recover from host/network interruption much faster.
- etcd: override `etcd_events_cluster_setup: true` to store events in a separate dedicated etcd instance.
- Inventory: consult the Getting Started inventory guidance for building a large-scale Ansible inventory.

## References
- docs/operations/large-deployments.md (tag v2.31.0 1c9add4)
