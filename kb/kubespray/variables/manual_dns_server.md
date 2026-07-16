---
id: VARIABLE-MANUAL_DNS_SERVER
type: variable
title: manual_dns_server
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - manual_dns_server
tags:
  - dns
  - networking
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Defines manual_dns_server default (empty string)"
relations: []
---

# manual_dns_server

## Summary
Optional manually specified upstream DNS server. Default is an empty string `""`, meaning no manual DNS server is configured unless the user overrides it.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as `manual_dns_server: ""`. The value is unchanged across v2.29.0–v2.31.0 (line 147, except 148 in v2.30.0).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Related to DNS/resolver configuration variables such as `dns_servers` and `cloud_resolver`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
