---
id: VARIABLE-KUBE_DNS_SERVERS
type: variable
title: kube_dns_servers
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_dns_servers
tags:
  - dns
  - coredns
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Maps dns_mode to the list of cluster DNS server addresses"
relations: []
---

# kube_dns_servers

## Summary
A mapping from `dns_mode` to the list of cluster DNS server addresses. It is consumed by `dns_servers`, which is defined as `dns_servers: "{{ kube_dns_servers[dns_mode] }}"`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as a dictionary:

```
kube_dns_servers:
  coredns: ["{{ skydns_server }}"]
  coredns_dual: "{{ [skydns_server] + [skydns_server_secondary] }}"
  manual: ["{{ manual_dns_server }}"]
```

The structure and values are unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only line numbers within the file differ between tags).

## Compatibility
Available in Kubespray v2.29.0 through v2.31.0. Related: `dns_mode`, `dns_servers`, `skydns_server`, `skydns_server_secondary`, `manual_dns_server`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
