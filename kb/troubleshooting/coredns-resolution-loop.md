---
id: TROUBLE-COREDNS_RESOLUTION_LOOP
type: troubleshooting
title: "CoreDNS crashloop: 'Loop … detected'"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - coredns-resolution-loop
tags:
  - troubleshooting
  - operations
  - dns
sources:
  - type: docs
    url: https://coredns.io/plugins/loop/
    note: "CoreDNS loop plugin"
relations:
  - type: see_also
    target: COMPONENT-COREDNS
---

# CoreDNS crashloop: 'Loop … detected'

## Summary

CoreDNS pods crashloop with a `plugin/loop: Loop ... detected` message. This happens when CoreDNS forwards to an upstream that points back to CoreDNS — typically the host `/etc/resolv.conf` contains the cluster/local DNS.

## Problem

The `forward . /etc/resolv.conf` in the Corefile inherits the node's resolv.conf; if that resolv.conf points at a resolver that loops back (e.g. 127.0.0.1 systemd-resolved stub, or the nodelocaldns/cluster IP), CoreDNS detects a query loop and exits.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0` clusters. This is a general Kubernetes/component operational issue (not tied to one Kubespray version); the relevant tunables are noted in Known Issues.

## Diagnostics

```bash
kubectl -n kube-system logs -l k8s-app=kube-dns | grep -i loop
cat /etc/resolv.conf                 # on the node: does it point back to cluster/local DNS?
```

## Known Issues

Point the node's upstream resolv.conf at a real external resolver (`upstream_dns_servers` / `resolvconf_mode`, see TAG-RESOLVCONF), or configure CoreDNS `forward` to a real upstream. Do not let the resolver chain loop back to CoreDNS.

## References

- https://coredns.io/plugins/loop/ — CoreDNS loop plugin (verified behavior, 2026-07-16).
