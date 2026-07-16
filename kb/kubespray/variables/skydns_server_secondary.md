---
id: VARIABLE-SKYDNS_SERVER_SECONDARY
type: variable
title: skydns_server_secondary
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - skydns_server_secondary
tags:
  - dns
  - networking
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Computed secondary in-cluster DNS server address derived from the service subnet"
relations: []
---

# skydns_server_secondary

## Summary
Computed address of the secondary in-cluster DNS service. It is derived from the
first Kubernetes service subnet by taking the 4th host address of that network
(`kube_service_subnets` -> net -> host index 4). Used when a secondary DNS
server is configured for the cluster.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as a computed
expression:

```yaml
skydns_server_secondary: "{{ kube_service_subnets.split(',') | first | ansible.utils.ipaddr('net') | ansible.utils.ipaddr(4) | ansible.utils.ipaddr('address') }}"
```

The same expression is also present in the sample inventory at
`inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml`. The expression is
unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the surrounding
line numbers differ).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on `kube_service_subnets`. Related to
`skydns_server` (primary DNS address).

## References
- roles/kubespray_defaults/defaults/main/main.yml
- inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
