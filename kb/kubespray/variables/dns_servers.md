---
id: VARIABLE-DNS_SERVERS
type: variable
title: dns_servers
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - dns_servers
tags:
  - dns
  - coredns
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Computed cluster DNS server list selected by dns_mode"
relations: []
---

# dns_servers

## Summary
Computed list of cluster DNS server IP addresses. Its value is selected from the `kube_dns_servers` mapping using the active `dns_mode` (`coredns`, `coredns_dual`, or `manual`), so the resulting addresses derive from `skydns_server` / `manual_dns_server`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

```yaml
dns_servers: "{{ kube_dns_servers[dns_mode] }}"
```

where `kube_dns_servers` maps `coredns: ["{{ skydns_server }}"]`, `coredns_dual: "{{ [skydns_server] + [skydns_server_secondary] }}"`, and `manual: ["{{ manual_dns_server }}"]`. Unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on `dns_mode`, `kube_dns_servers`, `skydns_server`, and `manual_dns_server`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
