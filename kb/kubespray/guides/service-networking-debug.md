---
id: PRACTICE-SERVICE_NETWORKING_DEBUG
type: best_practice
title: Service networking and kube-proxy debugging
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - service not reachable
  - kube-proxy debug
  - clusterip unreachable
tags:
  - operations
  - networking
  - diagnostics
sources:
  - type: docs
    path: docs/advanced/dns-stack.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/advanced/dns-stack.md
    note: "networking context; commands are standard Kubernetes tooling"
relations:
  - type: see_also
    target: VARIABLE-KUBE_PROXY_MODE
  - type: see_also
    target: PRACTICE-CILIUM_DIAGNOSTICS
---

# Service networking and kube-proxy debugging

## Summary

When a `ClusterIP`/`NodePort` service is unreachable, the fault is usually in
Endpoints (no backing pods), kube-proxy programming ([[VARIABLE-KUBE_PROXY_MODE]],
default `ipvs`), or the CNI datapath. This runbook isolates the layer.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`. Default kube-proxy mode is `ipvs`;
  with Cilium kube-proxy replacement enabled, service LB is in eBPF instead
  ([[VARIABLE-CILIUM_KUBE_PROXY_REPLACEMENT]]).

## Diagnostics

```bash
# does the service have endpoints?
kubectl get svc <svc> -o wide
kubectl get endpointslices -l kubernetes.io/service-name=<svc>
# (empty endpoints = selector/pod problem, not networking)

# from a pod, test the ClusterIP and DNS
kubectl run nettest --image=nicolaka/netshoot --restart=Never --rm -it -- \
  sh -c 'curl -sS http://<clusterip>:<port> ; nslookup <svc>.<ns>.svc.cluster.local'
```

kube-proxy programming (ipvs default):

```bash
kubectl -n kube-system get pods -l k8s-app=kube-proxy -o wide
kubectl -n kube-system logs -l k8s-app=kube-proxy --tail=40
# on a node:
ipvsadm -Ln | grep -A3 <clusterip>          # ipvs rules present?  (mode=ipvs)
iptables -t nat -L KUBE-SERVICES -n | grep <clusterip>   # (mode=iptables)
```

## Implementation

Localize:
- **No endpoints** → service selector vs pod labels; pods not Ready.
- **Endpoints present, ClusterIP dead** → kube-proxy not programming: check the
  kube-proxy pods/logs and mode ([[VARIABLE-KUBE_PROXY_MODE]]); for `ipvs`,
  confirm the IPVS kernel modules are loaded.
- **With Cilium kube-proxy replacement** → check `cilium service list`
  ([[PRACTICE-CILIUM_DIAGNOSTICS]]); make sure kube-proxy is consistently removed.
- **Cross-node only** → CNI/datapath ([[PRACTICE-CILIUM_DIAGNOSTICS]]).
- **NodePort external** → also check host firewall.

## References

- Standard Kubernetes service/kube-proxy debugging; Kubespray `docs/`.
