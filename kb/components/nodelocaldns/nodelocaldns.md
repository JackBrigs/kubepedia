---
id: COMPONENT-NODELOCALDNS
type: component
title: NodeLocal DNS (nodelocaldns)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: "1.25.0"
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - nodelocaldns
  - node-local dns
tags:
  - dns
  - nodelocaldns
  - addons
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    lines: "281,282"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "nodelocaldns_version: 1.25.0; image registry.k8s.io/dns/k8s-dns-node-cache"
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    lines: "138,140"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "enable_nodelocaldns: true; nodelocaldns_ip: 169.254.25.10"
relations:
  - type: see_also
    target: COMPONENT-COREDNS
  - type: see_also
    target: VARIABLE-DNS_MODE
---

# NodeLocal DNS (nodelocaldns)

## Summary

NodeLocal DNS runs a DNS cache (`k8s-dns-node-cache`) as a DaemonSet on every
node, improving DNS latency and reliability by serving queries locally and
forwarding to cluster DNS ([[COMPONENT-COREDNS]]). It is **enabled by default**
(`enable_nodelocaldns: true`) and pinned to version `1.25.0` across
`v2.29.0`–`v2.31.0`.

## Context

- Covers Kubespray `v2.29.0`–`v2.31.0`.
- Listens on the link-local address `nodelocaldns_ip: 169.254.25.10`.
- Sits in front of CoreDNS; the DNS mode is governed by [[VARIABLE-DNS_MODE]].

## Implementation

The version is a literal
(`roles/kubespray_defaults/defaults/main/download.yml`):

```yaml
nodelocaldns_version: "1.25.0"
nodelocaldns_image_repo: "{{ kube_image_repo }}/dns/k8s-dns-node-cache"  # registry.k8s.io/dns/k8s-dns-node-cache
```

Enabled in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
enable_nodelocaldns: true
nodelocaldns_ip: 169.254.25.10
```

The version does not change across the indexed tags.

## Configuration

- Enablement: `enable_nodelocaldns` (default `true`).
- Version: `nodelocaldns_version` (literal `1.25.0`).
- Image: `registry.k8s.io/dns/k8s-dns-node-cache:{{ nodelocaldns_version }}`.
- Local listen IP: `nodelocaldns_ip` (`169.254.25.10`).

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: NodeLocal DNS `1.25.0`, enabled by default.
- Works with `dns_mode: coredns` / `coredns_dual`.

## References

- `roles/kubespray_defaults/defaults/main/download.yml:281,282`.
- `roles/kubespray_defaults/defaults/main/main.yml:138,140`.
- Tags: v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`.
