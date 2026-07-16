---
id: VARIABLE-COREDNS_K8S_EXTERNAL_ZONE
type: variable
title: coredns_k8s_external_zone
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - coredns_k8s_external_zone
tags:
  - coredns
  - dns
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "DNS zone served by the CoreDNS k8s_external plugin; default k8s_external.local"
relations: []
---

# coredns_k8s_external_zone

## Summary
Defines the DNS zone name handled by the CoreDNS `k8s_external` plugin, used to
expose Services of type LoadBalancer / with external IPs under an external
domain. Default value is `k8s_external.local`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

```yaml
coredns_k8s_external_zone: k8s_external.local
```

The same default is mirrored in the sample inventory at
`inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml`. The value is
unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the line number
shifts between tags).

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Relevant only when the CoreDNS
`k8s_external` plugin is enabled.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
