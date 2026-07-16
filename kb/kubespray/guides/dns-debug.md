---
id: PRACTICE-DNS_DEBUG
type: best_practice
title: Cluster DNS debugging (CoreDNS / NodeLocal DNS)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - dns not resolving
  - coredns debug
  - nodelocaldns debug
tags:
  - operations
  - dns
  - diagnostics
sources:
  - type: docs
    path: docs/advanced/dns-stack.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/advanced/dns-stack.md
    note: "DNS stack; commands are standard Kubernetes tooling"
relations:
  - type: see_also
    target: COMPONENT-COREDNS
  - type: see_also
    target: COMPONENT-NODELOCALDNS
  - type: see_also
    target: VARIABLE-DNS_MODE
---

# Cluster DNS debugging (CoreDNS / NodeLocal DNS)

## Summary

DNS resolution failures inside pods usually trace to CoreDNS
([[COMPONENT-COREDNS]]), the NodeLocal DNS cache ([[COMPONENT-NODELOCALDNS]], on
`169.254.25.10` by default), or the pod's `resolv.conf`/`ndots`. This runbook
localizes the layer.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`; default `dns_mode: coredns` with
  NodeLocal DNS enabled ([[VARIABLE-DNS_MODE]]).

## Diagnostics

```bash
# CoreDNS and NodeLocal DNS pods healthy?
kubectl -n kube-system get pods -l k8s-app=kube-dns -o wide
kubectl -n kube-system get pods -l k8s-app=nodelocaldns -o wide
kubectl -n kube-system logs -l k8s-app=kube-dns --tail=50

# resolve from a throwaway pod
kubectl run dnstest --image=busybox:1.36 --restart=Never --rm -it -- \
  nslookup kubernetes.default.svc.cluster.local

# check the pod resolv.conf (ndots, nameserver = nodelocaldns IP or CoreDNS SVC)
kubectl run dnstest --image=busybox:1.36 --restart=Never --rm -it -- cat /etc/resolv.conf
```

On a node, check the NodeLocal DNS listener:

```bash
ip addr | grep 169.254.25.10           # link-local IP present?
```

## Implementation

Common failure patterns:
- **CoreDNS CrashLoop / OOM** → check logs and the Corefile ConfigMap; upstream
  loop (`plugin/loop`) if host resolv.conf points back to cluster DNS.
- **NodeLocal DNS not answering** → the `169.254.25.10` iptables/interface setup
  is missing on the node; re-run the node/dns tasks.
- **Intermittent failures / slow lookups** → `ndots:5` causes extra queries;
  consider fewer search domains. NodeLocal DNS specifically mitigates this.
- **Wrong upstream** → `upstream_dns_servers` / host `resolv.conf`
  (see [[TAG-RESOLVCONF]]).

## References

- `docs/advanced/dns-stack.md`; standard Kubernetes DNS debugging.
- Components: [[COMPONENT-COREDNS]], [[COMPONENT-NODELOCALDNS]].
