---
id: VARIABLE-CILIUM_L2ANNOUNCEMENTS
type: variable
title: cilium_l2announcements
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_l2announcements
tags:
  - cilium
  - loadbalancer
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Enables Cilium L2 announcements; default false"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_l2announcements

## Summary
Enables Cilium L2 announcements (`l2announcements.enabled`), used to advertise LoadBalancer/service IPs over L2 (ARP). Default: `false`.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml`:

```yaml
cilium_l2announcements: false
```

Consumed in `roles/network_plugin/cilium/templates/values.yaml.j2` (`l2announcements.enabled: {{ cilium_l2announcements | to_json }}`). Also present (uncommented, value `false`) in `inventory/sample/group_vars/k8s_cluster/k8s-net-cilium.yml`. The default `false` is unchanged across v2.29.0-v2.31.0 (only line numbers shift between tags).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variables: `cilium_loadbalancer_mode`, `cilium_loadbalancer_ip_pools`, `cilium_kube_proxy_replacement`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- roles/network_plugin/cilium/templates/values.yaml.j2
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
