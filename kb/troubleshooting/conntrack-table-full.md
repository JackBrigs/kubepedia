---
id: TROUBLE-CONNTRACK_TABLE_FULL
type: troubleshooting
title: "nf_conntrack table full — dropped packets / intermittent timeouts"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - conntrack-table-full
tags:
  - troubleshooting
  - operations
  - networking
sources:
  - type: docs
    url: https://kubernetes.io/docs/reference/networking/virtual-ips/
    note: "kube-proxy/conntrack"
relations:
  - type: see_also
    target: VARIABLE-KUBE_PROXY_MODE
---

# nf_conntrack table full — dropped packets / intermittent timeouts

## Summary

Nodes log `nf_conntrack: table full, dropping packet` and services see intermittent connection timeouts/resets under load.

## Problem

Every tracked connection consumes a conntrack slot; high connection churn (many short-lived connections) can exhaust `nf_conntrack_max`. kube-proxy sizes this, but very busy nodes can still fill it.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0` clusters. This is a general Kubernetes/component operational issue (not tied to one Kubespray version); the relevant tunables are noted in Known Issues.

## Diagnostics

```bash
sysctl net.netfilter.nf_conntrack_count net.netfilter.nf_conntrack_max
dmesg | grep -i conntrack | tail
```

## Known Issues

Raise `nf_conntrack_max` (via kube-proxy conntrack settings or a sysctl in `additional_sysctl`), reduce connection churn (keep-alive/pooling), and check for connection leaks. With Cilium kube-proxy replacement the datapath differs (see PRACTICE-CILIUM_DIAGNOSTICS).

## References

- https://kubernetes.io/docs/reference/networking/virtual-ips/ — kube-proxy/conntrack (verified behavior, 2026-07-16).
