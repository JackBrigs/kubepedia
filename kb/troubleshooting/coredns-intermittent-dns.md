---
id: TROUBLE-COREDNS_INTERMITTENT_DNS
type: troubleshooting
title: "CoreDNS: intermittent/slow DNS resolution in pods"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.11.0 <=1.14.6"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - intermittent dns failures kubernetes
  - coredns slow resolution
  - dns 5 second timeout
  - coredns SERVFAIL loop
tags:
  - troubleshooting
  - coredns
  - dns
  - networking
sources:
  - type: docs
    path: Kubernetes DNS debugging
    url: https://kubernetes.io/docs/tasks/administer-cluster/dns-debugging-resolution/
    note: "resolver, ndots, CoreDNS Corefile checks"
relations:
  - type: see_also
    target: COMPONENT-COREDNS
  - type: see_also
    target: COMPONENT-NODELOCALDNS
  - type: see_also
    target: TROUBLE-DNS_EXTERNAL_RESOLUTION
---

# CoreDNS: intermittent/slow DNS resolution in pods

## Summary

Pods see **intermittent** DNS failures or ~5-second lookup delays. The classic causes are the
**conntrack race** on UDP (mitigated by node-local DNS), `ndots:5` search-domain amplification,
and CoreDNS overload or a bad `Corefile`. Confirm with in-pod queries, then address the layer.

## Problem

- Occasional `SERVFAIL`/timeouts; app retries succeed.
- ~5s latency on some external lookups.
- CoreDNS pods high CPU or `CrashLoopBackOff`.

## Context

- Applies to CoreDNS **1.11–1.14.6** (base ≤1.12.4 — [[COMPONENT-COREDNS]]).

## Diagnostics

1. From a pod: `nslookup kubernetes.default` and an external name; compare against querying a
   CoreDNS pod IP directly to localize.
2. **Conntrack race (5s timeouts):** parallel A/AAAA UDP lookups can hit a kernel conntrack
   race → deploy **node-local DNS** ([[COMPONENT-NODELOCALDNS]]) which uses TCP upstream and
   sidesteps it. Kubespray ships it as an option.
3. **`ndots:5` amplification:** unqualified external names get tried against every search
   domain first → many failed queries. Use FQDNs (trailing dot) or tune `ndots` for
   external-heavy workloads.
4. **CoreDNS health/scale:** check `kubectl -n kube-system logs` for plugin errors; a
   `loop` plugin detection crash means the upstream resolver points back at CoreDNS (fix the
   node `/etc/resolv.conf`). Scale replicas / check `cache` and `forward` config in the
   Corefile.
5. **Upstream resolution issues** (external names only) are a separate class —
   [[TROUBLE-DNS_EXTERNAL_RESOLUTION]].

## Known Issues

- On `systemd-resolved` nodes the upstream may be a stub (`127.0.0.53`) — ensure the real
  upstream nameservers are used, not just the stub.

## References

- Kubernetes DNS debugging (above); component: [[COMPONENT-COREDNS]]; node-local:
  [[COMPONENT-NODELOCALDNS]]; external resolution: [[TROUBLE-DNS_EXTERNAL_RESOLUTION]].
