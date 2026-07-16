---
id: PRACTICE-CLUSTER_HEALTH_CHECKS
type: best_practice
title: Cluster health checks (day-2 runbook)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - health check
  - cluster status
  - is my cluster healthy
tags:
  - operations
  - diagnostics
  - troubleshooting
sources:
  - type: docs
    path: docs/operations
    url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0/docs/operations
    note: "operational context; commands are standard Kubernetes/etcd tooling"
relations:
  - type: see_also
    target: PRACTICE-ETCD_BACKUP_RESTORE
  - type: see_also
    target: PRACTICE-DNS_DEBUG
---

# Cluster health checks (day-2 runbook)

## Summary

A quick, safe, read-only sequence to assess the health of a Kubespray-deployed
cluster: nodes, control-plane, etcd, core add-ons (DNS, CNI). Run top to bottom;
each step is non-mutating.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0` clusters.
- Run from a control-plane node (has admin `kubeconfig`) or any host with
  `kubectl` and the admin config.

## Diagnostics

**Nodes and control plane:**

```bash
kubectl get nodes -o wide                     # all Ready? versions consistent?
kubectl get pods -n kube-system -o wide       # apiserver/controller/scheduler/etcd Running?
kubectl get --raw='/readyz?verbose'           # apiserver readiness detail
```

**Workload / events (expect no persistent failures):**

```bash
kubectl get pods -A | grep -vE 'Running|Completed'
kubectl get events -A --sort-by=.lastTimestamp | tail -30
```

**Core add-ons:**

```bash
kubectl -n kube-system get pods -l k8s-app=kube-dns          # CoreDNS
kubectl -n kube-system get ds nodelocaldns                   # NodeLocal DNS (see COMPONENT-NODELOCALDNS)
kubectl -n kube-system get pods -l k8s-app=cilium            # Cilium (if kube_network_plugin=cilium)
```

**Node-level (on a node, via SSH):**

```bash
systemctl status kubelet --no-pager           # kubelet up?
journalctl -u kubelet -n 50 --no-pager        # recent kubelet logs
crictl ps                                     # running containers (containerd)
```

## Implementation

Escalation by area:
- etcd unhealthy → [[PRACTICE-ETCD_BACKUP_RESTORE]] / [[COMPONENT-ETCD]].
- DNS failures → [[PRACTICE-DNS_DEBUG]].
- CNI/pod networking → [[PRACTICE-CILIUM_DIAGNOSTICS]].
- kubelet crashloop → check config/certs ([[PRACTICE-CERTIFICATE_EXPIRY]]).
- control-plane degraded beyond repair → [[PRACTICE-RECOVER_CONTROL_PLANE]].

## References

- Standard Kubernetes/kubelet/crictl tooling; Kubespray `docs/operations/`.
- Component detail: [[CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS]].
