---
id: VARIABLE-UPSTREAM_DNS_SERVERS
type: variable
title: upstream_dns_servers
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - upstream_dns_servers
tags:
  - dns
  - coredns
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Defines upstream DNS servers for cluster resolvers; default empty list."
relations: []
---

# upstream_dns_servers

## Summary
List of upstream DNS servers that the cluster DNS stack (CoreDNS / nodelocaldns) forwards external queries to. The default is an empty list `[]`, meaning no explicit upstream resolvers are injected by Kubespray and the platform's own resolver configuration is used. Operators set it to point cluster DNS at specific corporate or public resolvers.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

`upstream_dns_servers: []`

The default is unchanged across v2.29.0-v2.31.0 (only the surrounding line number shifts: line 135 in v2.29.0/v2.29.1/v2.31.0 and line 136 in v2.30.0). The value is an empty YAML list in every inspected tag.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Consumed by the DNS configuration logic (CoreDNS/nodelocaldns). Related variables: `dns_servers`, `nameservers`, `coredns_external_zones`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
