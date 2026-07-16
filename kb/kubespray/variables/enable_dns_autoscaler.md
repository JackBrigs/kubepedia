---
id: VARIABLE-ENABLE_DNS_AUTOSCALER
type: variable
title: enable_dns_autoscaler
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - enable_dns_autoscaler
tags:
  - dns
  - coredns
  - autoscaler
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Enables the cluster-proportional DNS autoscaler; default true"
relations: []
---

# enable_dns_autoscaler

## Summary
Toggles deployment of the cluster-proportional DNS autoscaler that scales the number of CoreDNS replicas based on cluster size. Default is `true`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:
```yaml
enable_dns_autoscaler: true
```
The default value `true` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the line number varies).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related to the CoreDNS deployment and DNS scaling variables.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
