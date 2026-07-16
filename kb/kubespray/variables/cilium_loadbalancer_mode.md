---
id: VARIABLE-CILIUM_LOADBALANCER_MODE
type: variable
title: cilium_loadbalancer_mode
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_loadbalancer_mode
tags:
  - cilium
  - loadbalancer
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Cilium load-balancer datapath mode; default snat"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_loadbalancer_mode

## Summary
Selects Cilium's load-balancer datapath mode (`loadBalancer.mode`). Default: `snat`. The sample inventory shows this as a commented override.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml`:

```yaml
cilium_loadbalancer_mode: snat
```

Consumed in `roles/network_plugin/cilium/templates/values.yaml.j2` (`loadBalancer.mode: {{ cilium_loadbalancer_mode }}`). Exposed (commented) in `inventory/sample/group_vars/k8s_cluster/k8s-net-cilium.yml` as `# cilium_loadbalancer_mode: snat`. The default `snat` is unchanged across v2.29.0-v2.31.0 (only line numbers shift between tags).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variables: `cilium_loadbalancer_ip_pools`, `cilium_l2announcements`, `cilium_kube_proxy_replacement`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- roles/network_plugin/cilium/templates/values.yaml.j2
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
