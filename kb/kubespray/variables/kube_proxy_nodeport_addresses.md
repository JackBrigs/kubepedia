---
id: VARIABLE-KUBE_PROXY_NODEPORT_ADDRESSES
type: variable
title: kube_proxy_nodeport_addresses
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_proxy_nodeport_addresses
tags:
  - kube-proxy
  - nodeport
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    note: "Defines kube_proxy_nodeport_addresses as a computed list from kube_proxy_nodeport_addresses_cidr, default []"
relations: []
---

# kube_proxy_nodeport_addresses

## Summary
Sets the kube-proxy `nodePortAddresses` — the CIDR ranges on which kube-proxy accepts NodePort traffic. Computed: if `kube_proxy_nodeport_addresses_cidr` is defined it becomes `[<cidr>]`, otherwise `[]` (all addresses).

## Implementation
Defined identically in three places — `roles/kubernetes/control-plane/defaults/main/kube-proxy.yml` (primary), `roles/kubespray_defaults/defaults/main/main.yml`, and the sample inventory `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml`:

```yaml
kube_proxy_nodeport_addresses: >-
  {%- if kube_proxy_nodeport_addresses_cidr is defined -%}
  [{{ kube_proxy_nodeport_addresses_cidr }}]
  {%- else -%}
  []
  {%- endif -%}
```

The computed expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Applies to Kubespray v2.29.0–v2.31.0. Feeds the kube-proxy `KubeProxyConfiguration`. Driven by the optional `kube_proxy_nodeport_addresses_cidr` variable.

## References
- roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
- roles/kubespray_defaults/defaults/main/main.yml
- inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
